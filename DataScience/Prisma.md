У Prisma є 3 головні речі:

## 1️⃣ schema.prisma

Це опис структури БД.

Наприклад:
```sql
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
```
Тут ти описуєш таблиці.

## 2️⃣ migrations

Це історія змін структури БД.

Коли хтось змінює schema:
```
model User {
  id    Int @id @default(autoincrement())
  email String @unique
  name  String?
  age   Int?
}
```
то запускають:
```
npx prisma migrate dev
```
Prisma:

 - 1️⃣ створює SQL
 - 2️⃣ створює папку міграції
 - 3️⃣ застосовує її до БД

## 3️⃣ Prisma Client

Це згенерована бібліотека для роботи з БД.

Приклад використання:
```javascript
const users = await prisma.user.findMany()
```
Він генерується командою:
```bash
npx prisma generate
```
Файли з'являються тут:
```
node_modules/.prisma
```
Саме тому іноді треба видаляти `.prisma` і генерувати заново.

## 4️⃣ Як редагуються таблиці

Правильний workflow:

- 1️⃣ редагуєш schema.prisma
  ```
  model User {
    id Int @id @default(autoincrement())
    email String
    age Int?
  }
  ```
- 2️⃣ запускаєш
  ```
  npx prisma migrate dev
  ```

Prisma:

- створить нову міграцію
- змінить базу
- згенерує client

## 5️⃣ Що робити коли ти просто підключилась до проекту

Тобі зазвичай потрібно:
```bash
npm install
npx prisma generate
npx prisma migrate dev
```
або іноді:
```
npx prisma migrate deploy
```
(це залежить від проєкту)

