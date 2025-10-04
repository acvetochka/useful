# Database migration from SQLite to PostgreSQL

## 🧭 Крок 1. Встанови PostgreSQL на сервері

Підключися до свого сервера:
```shell
ssh root@<твоя-IP-адреса>
```


І виконай:
```shell
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

Перевір, чи запущений PostgreSQL:
```shell
sudo systemctl status postgresql
```


(Щоб вийти з перегляду статусу — натисни `q`.)

## 🧩 Крок 2. Створи базу даних і користувача

Запусти термінал PostgreSQL:
```shell
sudo -u postgres psql
```

Тепер у консолі psql введи ці команди:
```sql
-- 1️⃣ Створити базу
CREATE DATABASE strapi_db;

-- 2️⃣ Створити користувача
CREATE USER strapi_user WITH PASSWORD 'superpassword';

-- 3️⃣ Надати права користувачу
GRANT ALL PRIVILEGES ON DATABASE strapi_db TO strapi_user;

-- 4️⃣ Вийти з PostgreSQL
\q
```

🔐 Заміни `superpassword` на свій власний надійний пароль.

## ⚙️ Крок 3. Встанови драйвер PostgreSQL у Strapi

Перейди у свою директорію Strapi:
```
cd /var/www/strapi-backend
```

І встанови залежність:
```
npm install pg
```

## 📁 Крок 4. Онови файл .env

Відкрий або створи файл .env у корені проєкту:
```
nano .env
```

Впиши туди:
```
# Strapi basic
HOST=0.0.0.0
PORT=1337
APP_KEYS=someRandomKey1,someRandomKey2
API_TOKEN_SALT=sometokenSalt
ADMIN_JWT_SECRET=someJWTsecret

# PostgreSQL Database
DATABASE_CLIENT=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=strapi_db
DATABASE_USERNAME=strapi_user
DATABASE_PASSWORD=superpassword
DATABASE_SSL=false
```

❗ Важливо: заміни значення `DATABASE_PASSWORD` і ключі на свої власні.

Збережи файл:
`Ctrl + O → Enter → Ctrl + X`

## 🛠️ Крок 5. Зміни конфіг Strapi для PostgreSQL

Відкрий файл:
`./config/database.ts` або `./config/database.js` (залежно від твоєї структури).

Заміні вміст на цей:
```js
export default ({ env }) => ({
  connection: {
    client: 'postgres',
    connection: {
      host: env('DATABASE_HOST', 'localhost'),
      port: env.int('DATABASE_PORT', 5432),
      database: env('DATABASE_NAME', 'strapi_db'),
      user: env('DATABASE_USERNAME', 'strapi_user'),
      password: env('DATABASE_PASSWORD', 'superpassword'),
      ssl: env.bool('DATABASE_SSL', false),
    },
  },
});
```

## 🧹 Крок 6. Очисти старі збірки (SQLite)
```shell
rm -rf .tmp node_modules package-lock.json
npm install
```

## 🚀 Крок 7. Запусти Strapi
```
npm run develop
```

Після запуску Strapi створить усі таблиці в PostgreSQL.
Вперше ти знову побачиш сторінку реєстрації адміністратора (бо це нова база).

## 📦 Крок 8. (Додатково) — Міграція старих даних (якщо потрібно)

SQLite → PostgreSQL напряму не переноситься,
але можна експортувати дані вручну:

- Локально (де стара база) — зайди в .tmp/data.db

- Відкрий її через DB Browser for SQLite

- Експортуй таблиці в .csv

- У Strapi на сервері (де PostgreSQL) — імпортуй ці .csv у відповідні таблиці.
