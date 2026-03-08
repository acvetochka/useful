# Prisma + PostgreSQL + PostGIS

для Prisma + PostgreSQL + PostGIS структура й логіка трохи інші, ніж у “звичайному” Express + Mongo, бо тут є окремий шар:

- Prisma schema — опис моделей
- міграції — SQL-історія змін БД
- Prisma Client — згенерований JS/TS-клієнт для запитів
- PostgreSQL — сама база
- PostGIS — розширення PostgreSQL для геоданих і геозапитів

Головна ідея така: ти не пишеш більшість SQL руками щодня, а описуєш структуру в schema.prisma, Prisma генерує клієнт і міграції, а для PostGIS-частини часто додаються кастомні SQL-міграції або raw SQL, бо Prisma досі не має повної нативної підтримки PostGIS-типів; Prisma прямо пише, що custom types з extension можуть відображатися як Unsupported, а для PostGIS радить обхід через raw SQL / extensions-підхід.

Як це працює концептуально

У тебе є 4 рівні:
- Код бекенду — `routes` / `controllers` / `services`
- `Prisma Client` — API для звернення до БД з коду
- `PostgreSQL` — зберігає таблиці, індекси, constraints
- `PostGIS` — додає типи `geometry` / `geography`, просторові функції, індекси та оператори через extension PostgreSQL. PostgreSQL офіційно пояснює, що extension встановлюється через `CREATE EXTENSION`, а objects extension стають частиною поточної бази.

Тобто потік такий:
- ти змінюєш `schema.prisma`
- запускаєш `prisma migrate dev`
- Prisma створює SQL-міграцію
- міграція застосовується до PostgreSQL
- Prisma оновлює `_prisma_migrations`
- Prisma Client генерується заново під нову схему
- бекенд вже працює з новими моделями через `prisma.<model>`...

## 1. Рекомендована структура проєкту

Для бекенду на Node.js + Express + Prisma + PostgreSQL + PostGIS я б радив таку структуру:
```
backend/
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   │   ├── 20260306110000_init/
│   │   │   └── migration.sql
│   │   ├── 20260306113000_add_locations/
│   │   │   └── migration.sql
│   │   └── ...
│   └── seed.ts
│
├── src/
│   ├── app.ts
│   ├── server.ts
│   │
│   ├── config/
│   │   ├── env.ts
│   │   └── prisma.ts
│   │
│   ├── modules/
│   │   ├── auth/
│   │   │   ├── auth.controller.ts
│   │   │   ├── auth.service.ts
│   │   │   ├── auth.routes.ts
│   │   │   └── auth.validation.ts
│   │   │
│   │   ├── users/
│   │   │   ├── users.controller.ts
│   │   │   ├── users.service.ts
│   │   │   ├── users.routes.ts
│   │   │   └── users.validation.ts
│   │   │
│   │   └── locations/
│   │       ├── locations.controller.ts
│   │       ├── locations.service.ts
│   │       ├── locations.routes.ts
│   │       └── locations.validation.ts
│   │
│   ├── middlewares/
│   │   ├── auth.middleware.ts
│   │   ├── error.middleware.ts
│   │   └── validate.middleware.ts
│   │
│   ├── lib/
│   │   ├── prisma.ts
│   │   └── logger.ts
│   │
│   ├── utils/
│   │   ├── http-error.ts
│   │   └── ctrl-wrapper.ts
│   │
│   └── types/
│       └── express.d.ts
│
├── tests/
│   ├── auth.test.ts
│   └── locations.test.ts
│
├── .env
├── .env.example
├── package.json
├── tsconfig.json
└── README.md
```

## 2. Які файли тут обов’язкові

Мінімально потрібні ось ці:

У корені
- package.json
- .env
- .env.example

У prisma/
- schema.prisma
- migrations/ — якщо ти використовуєш Prisma Migrate
- seed.ts — не обов’язковий технічно, але дуже бажаний

У src/
- server.ts
- app.ts
- файл з Prisma client, наприклад src/lib/prisma.ts

## 3. Обов’язкова роль кожного ключового файлу
`prisma/schema.prisma`

Це головний файл Prisma, де описуються:
- datasource
- generator
- моделі таблиць
- relations
- індекси
- іноді multi-schema налаштування

Приклад:
```prisa
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(uuid())
  email     String   @unique
  password  String
  name      String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  locations Location[]
}

model Location {
  id        String   @id @default(uuid())
  title     String
  latitude  Decimal? @db.Decimal(9, 6)
  longitude Decimal? @db.Decimal(9, 6)
  userId    String
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  createdAt DateTime @default(now())

  @@index([userId])
}
```

Prisma schema визначає структуру, а `prisma migrate` на її основі створює SQL-міграції. `db push`, навпаки, синхронізує схему без збереження історії міграцій.

***

`prisma/migrations/.../migration.sql`

Це реальний SQL, який Prisma згенерувала або який ти вручну відредагувала.

Наприклад, для PostGIS там може бути:
```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```

Prisma офіційно рекомендує для PostgreSQL extensions використовувати customized migrations, коли фіча не має прямого представлення в Prisma Schema.
***

`src/lib/prisma.ts`

Єдине місце, де створюється PrismaClient:
```ts
import { PrismaClient } from '@prisma/client';

export const prisma = new PrismaClient();
```
У більших проєктах сюди ще додають логування, singleton для dev-режиму, перехоплення shutdown тощо.
***

`src/server.ts`

Запускає HTTP-сервер.

***
`src/app.ts`

Підключає middleware, роутери, error handler.

## 4. Як створюється база даних з Prisma

Є два основні сценарії:

### Варіант A — правильний для реального проєкту: `migrate`

Ти:

1. описуєш моделі в schema.prisma
2. запускаєш:
  ```bash
  npx prisma migrate dev --name init
  ```
3. Prisma:
- порівнює schema і поточну БД
- генерує SQL-міграцію
- застосовує її до dev-бази
- оновлює _prisma_migrations
- генерує Prisma Client

Це найкращий варіант, бо в тебе є історія змін.

***

### Варіант B — швидкий для прототипу: `db push`
```bash
npx prisma db push
```

Це просто “проштовхує” поточну схему в БД без створення історії міграцій. Prisma CLI прямо вказує, що db push підходить для прототипування й випадків, коли versioned migrations не потрібні.

Для серйозного бекенду краще:
- dev/prod → migrate
- дуже ранній прототип → db push

## 5. Як база даних змінюється далі

Коли треба змінити таблицю:

Було
  ```prisma
  model User {
    id    String @id @default(uuid())
    email String @unique
  }
  ```
Стало
  ```prisma
  model User {
    id        String   @id @default(uuid())
    email     String   @unique
    name      String?
    createdAt DateTime @default(now())
  }
  ```

Тоді запускаєш:
```bash
npx prisma migrate dev --name add_user_name
```
Prisma створить нову папку в `prisma/migrations`/ і SQL на кшталт:
```sql
ALTER TABLE "User" ADD COLUMN "name" TEXT;
ALTER TABLE "User" ADD COLUMN "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
```
Потім код уже може працювати з новими полями через оновлений Prisma Client. Prisma Migrate зберігає історію міграцій як SQL-файли й застосовує їх у потрібному порядку.

## 6. Як працює PostGIS у цій схемі

**PostGIS** — це extension у PostgreSQL, а не окрема база. Воно додає:
- типи `geometry`, `geography`
- просторові функції
- spatial indexes
- оператори для геозапитів. PostgreSQL документує, що extensions встановлюються командою `CREATE EXTENSION`, а оновлюються через `ALTER EXTENSION ... UPDATE`.

Приклад увімкнення

У SQL-міграції:
```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```
Це треба виконати в конкретній базі, бо extension інсталюється на рівні бази, а не всього сервера як абстрактної схеми даних.

## 7. Важливий момент: Prisma і PostGIS

Ось ключова практична річ:

Prisma добре працює з PostgreSQL, але PostGIS-типи підтримуються не повністю нативно. Prisma docs прямо кажуть:
- custom extension types можуть бути `Unsupported(...)`
- для них часто потрібен raw SQL
- для PostGIS пропонуються workarounds через raw SQL / client extensions / customized migrations.

Тому є 2 нормальні підходи.
***

### Підхід 1 — зберігати координати як `latitude/longitude`

Найпростіший і найзручніший для більшості CRUD-проєктів:
```prisma
model Place {
  id        String   @id @default(uuid())
  name      String
  latitude  Decimal  @db.Decimal(9, 6)
  longitude Decimal  @db.Decimal(9, 6)
}
```
Плюси:
- Prisma повністю керує моделлю
- простий CRUD
- легко фільтрувати
- менше болю

Мінус:
- складні геооперації треба рахувати окремо або raw SQL

Це хороший варіант, якщо тобі треба:
- просто зберігати точки
- показувати на мапі
- шукати “приблизно поруч”

***
### Підхід 2 — справжній PostGIS `geometry/geography`

Коли потрібні:
- distance queries
- polygon containment
- nearest neighbors
- spatial indexes
- intersections, buffers, ST_DWithin, ST_Distance, ST_Intersects тощо

Тоді колонка створюється через SQL, а в Prisma часто позначається як `Unsupported`.

Наприклад:
```prisma
model Place {
  id       String @id @default(uuid())
  name     String
  location Unsupported("geometry(Point, 4326)")?

  @@index([location], map: "place_location_gist")
}
```

Але на практиці індекси і типи тут часто зручніше доробляти прямо в SQL-міграції, бо unsupported database features Prisma радить покривати нативним SQL.

## 8. Як виглядає міграція для PostGIS

Приклад реального підходу:
***
### Крок 1 — створити звичайну міграцію
```bash
npx prisma migrate dev --name add_places
```
***
### Крок 2 — відредагувати `migration.sql`

Наприклад так:
```sql
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE "Place" (
  "id" TEXT NOT NULL,
  "name" TEXT NOT NULL,
  "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "Place_pkey" PRIMARY KEY ("id")
);

ALTER TABLE "Place"
ADD COLUMN "location" geometry(Point, 4326);

CREATE INDEX "Place_location_gist"
ON "Place"
USING GIST ("location");
```

Оце якраз той випадок, коли Prisma schema не описує все ідеально, а частина живе в SQL-міграції. Prisma documentation окремо описує customized migrations для таких сценаріїв.

## 9. Як робити запити до PostGIS

Оскільки Prisma Client не покриває всі геофункції, для просторових речей зазвичай використовують:
- `prisma.$queryRaw`
- `prisma.$executeRaw`

Наприклад пошук точок у радіусі:
```ts
const places = await prisma.$queryRaw`
  SELECT id, name
  FROM "Place"
  WHERE ST_DWithin(
    location::geography,
    ST_SetSRID(ST_MakePoint(${lng}, ${lat}), 4326)::geography,
    ${radiusMeters}
  )
`;
```
Або вставка точки:
```ts
await prisma.$executeRaw`
  INSERT INTO "Place" ("id", "name", "location")
  VALUES (${id}, ${name}, ST_SetSRID(ST_MakePoint(${lng}, ${lat}), 4326))
`;
```
Prisma docs для unsupported / extension features і SafeQL прямо рекомендують raw SQL як робочий шлях для PostGIS-подібних фіч.

## 10. Яка структура модуля з геоданими найкраща

```bash
src/modules/places/
├── places.controller.ts
├── places.service.ts
├── places.routes.ts
├── places.validation.ts
└── places.repository.ts
```
І саме для PostGIS корисно додати ще `repository`, бо:

- `service` — бізнес-логіка
- `repository` — SQL / Prisma-запити

Тобто:

`places.service.ts`
```ts
import { placesRepository } from './places.repository';

export const createPlace = async (dto) => {
  return placesRepository.create(dto);
};

export const findNearbyPlaces = async (lat: number, lng: number, radius: number) => {
  return placesRepository.findNearby(lat, lng, radius);
};
```
`places.repository.ts`
```ts
import { prisma } from '../../lib/prisma';

export const placesRepository = {
  async findNearby(lat: number, lng: number, radius: number) {
    return prisma.$queryRaw`
      SELECT id, name
      FROM "Place"
      WHERE ST_DWithin(
        location::geography,
        ST_SetSRID(ST_MakePoint(${lng}, ${lat}), 4326)::geography,
        ${radius}
      )
    `;
  },
};
```
Для звичайних таблиць `repository` не завжди обов’язковий, але для Prisma + raw SQL + PostGIS це дуже зручно.

## 11. Як виглядає повсякденний цикл роботи
**Створення з нуля**
1. створюєш PostgreSQL базу
2. ставиш PostGIS на сервер/контейнер
3. створюєш Prisma проєкт
4. пишеш schema.prisma
5. створюєш першу міграцію
6. додаєш CREATE EXTENSION postgis
7. запускаєш міграцію
8. Prisma генерує client
9. пишеш сервіси та роутери
***

**Додавання нової таблиці**
1. змінюєш schema.prisma
2. npx prisma migrate dev --name add_xxx
3. якщо треба PostGIS-тип — правиш migration.sql
4. запускаєш і перевіряєш
5. оновлюєш service/controller
***

**Протягом розробки**
- схема змінюється через Prisma schema
- складні геоштуки — через SQL
- читання/запис простих полів — через Prisma Client
- геозапити — через raw SQL

## 12. Які файли Prisma зазвичай є в проєкті

Ось стандартний Prisma-блок:
```bash
prisma/
├── schema.prisma
├── migrations/
└── seed.ts
```

`schema.prisma`

Опис моделей.

`migrations/`

Історія змін БД. Для production це дуже важливо.

`seed.ts`

Початкові дані:
- admin user
- roles
- тестові place/location записи
- довідники

## 13. Приклад schema.prisma для реального проєкту
```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(uuid())
  email     String   @unique
  password  String
  name      String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  places    Place[]
}

model Place {
  id          String   @id @default(uuid())
  title       String
  description String?
  latitude    Decimal? @db.Decimal(9, 6)
  longitude   Decimal? @db.Decimal(9, 6)
  userId      String
  user        User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  createdAt   DateTime @default(now())

  @@index([userId])
}
```

Це безпечніший старт. А вже коли реально потрібні spatial queries — додаєш PostGIS-колонку окремою SQL-міграцією.

## 14. Як краще починати: з координат чи одразу з geometry

**Якщо проєкт на старті**

Почни з:
- latitude
- longitude

**Якщо точно потрібні геозапити**

Додавай:
- PostGIS extension
- geometry/geography
- GiST index
- raw SQL

Бо Prisma + PostGIS — це сильна комбінація, але не така “пряма”, як Prisma + звичайні текстові/числові поля. Це випливає і з Prisma docs про unsupported/custom extension types.

## 15. Як виглядає генерація Prisma Client

Після зміни схеми Prisma генерує клієнт командою:
```bash
npx prisma generate
```
У багатьох випадках `prisma migrate dev` уже запускає генерацію автоматично під час workflow міграції. Це частина типового Prisma Migrate потоку.

Потім у коді:
```ts
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const users = await prisma.user.findMany();
```

## 16. Як виглядає зміна структури в production

Для production логіка така:
1. локально міняєш schema.prisma
2. створюєш міграцію
3. комітиш schema.prisma + prisma/migrations/...
4. на сервері запускаєш:
    ```bash
    npx prisma migrate deploy
    ```
Prisma розділяє dev- та prod-workflow: у dev зазвичай `migrate dev`, у production — застосування вже готових міграцій без генерації нової історії “на місці”. Це описано в Prisma Migrate workflows для development and production.

## 17. Що обов’язково тримати під контролем версій

У Git треба комітити:
- `prisma/schema.prisma`
- `prisma/migrations/`
- `seed.ts`
- код модулів

Не треба комітити:
- `.env`
- generated artifacts, якщо вони генеруються автоматично у збірці

## 18. Хороший практичний шаблон для такого стеку

```bash
backend/
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   └── seed.ts
├── src/
│   ├── app.ts
│   ├── server.ts
│   ├── lib/prisma.ts
│   ├── config/env.ts
│   ├── middlewares/
│   ├── modules/
│   │   ├── auth/
│   │   ├── users/
│   │   └── places/
│   └── utils/
├── tests/
├── package.json
├── tsconfig.json
├── .env
└── README.md
```

## 19. Найважливіше, що треба запам’ятати
Prisma відповідає за:
- models
- relations
- migrations
- generated client

PostgreSQL відповідає за:
- реальні таблиці
- constraints
- indexes
- транзакції

PostGIS відповідає за:
- геотипи
- геофункції
- spatial indexes
- distance/intersection queries

А твій бекенд відповідає за:
- API
- auth
- validation
- business logic
- виклик Prisma Client і raw SQL

## 20. Практична порада для старту

Для більшості реальних проєктів:
1. Prisma + PostgreSQL без geometry
2. зберігай latitude/longitude
3. побудуй весь CRUD
4. тільки коли реально потрібні:
   - пошук у радіусі
   - nearest points
   - polygon intersection  
  тоді додай PostGIS-колонку і raw SQL

Так простіше розробляти й підтримувати.

## 21.  Висновок

У стеку Prisma + PostgreSQL + PostGIS проєкт зазвичай має дві архітектури одночасно:
- Node backend architecture: routes / controllers / services / middlewares
- database architecture: schema.prisma / migrations / generated Prisma Client / кастомний SQL для PostGIS

Найважливіше:
- `schema.prisma` — джерело правди для більшості таблиць
- `migrations/` — історія змін
- PostGIS — часто через `CREATE EXTENSION` і SQL-міграції
- складні геозапити — через `prisma.$queryRaw`