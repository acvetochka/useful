# Структура Backend проекту

Практичний шаблон, як створити повну структуру бекенду з нуля, щоб проєкт був зрозумілий, масштабований і не перетворився на хаос.

> на прикладі Node.js + Express, бо це один із найзручніших варіантів для старту. 

## 1. Що зазвичай має бути в бекенді

Повноцінний бекенд зазвичай містить:

- запуск сервера
- роутери
- контролери
- сервіси з бізнес-логікою
- моделі / схеми даних
- роботу з базою даних
- middleware
- валідацію
- авторизацію / аутентифікацію
- конфігурацію через .env
- логування
- обробку помилок
- тести
- документацію API

## 2. Рекомендована структура папок
```
backend/
├── src/
│   ├── app.js
│   ├── server.js
│   │
│   ├── config/
│   │   ├── db.js
│   │   ├── env.js
│   │   └── swagger.js
│   │
│   ├── routes/
│   │   ├── index.js
│   │   ├── authRoutes.js
│   │   └── userRoutes.js
│   │
│   ├── controllers/
│   │   ├── authController.js
│   │   └── userController.js
│   │
│   ├── services/
│   │   ├── authService.js
│   │   └── userService.js
│   │
│   ├── models/
│   │   └── User.js
│   │
│   ├── middlewares/
│   │   ├── authMiddleware.js
│   │   ├── errorHandler.js
│   │   └── validateBody.js
│   │
│   ├── validators/
│   │   ├── authSchemas.js
│   │   └── userSchemas.js
│   │
│   ├── utils/
│   │   ├── HttpError.js
│   │   ├── ctrlWrapper.js
│   │   └── sendEmail.js
│   │
│   ├── constants/
│   │   └── index.js
│   │
│   └── docs/
│       └── openapi.yaml
│
├── tests/
│   ├── auth.test.js
│   └── user.test.js
│
├── .env
├── .env.example
├── .gitignore
├── package.json
└── README.md
```

## 3. Для чого потрібна кожна папка
`src/server.js`

Точка входу. Тут запускається сервер.

`src/app.js`

Тут створюється express() і підключаються middleware, роутери, обробка помилок.

`config/`

Усе, що стосується конфігурації:
- підключення до БД
- зчитування змінних середовища
- swagger/openapi

`routes/`

Опис маршрутів:
- POST /auth/register
- POST /auth/login
- GET /users/me

`controllers/`

Приймають request/response, викликають сервіси, повертають відповідь.

`services/`

Бізнес-логіка:
- реєстрація
- логін
- хешування пароля
- перевірка токена
- оновлення користувача

`models/`

Схеми або моделі бази даних.

`middlewares/`

Проміжні обробники:
- перевірка токена
- валідація body
- глобальна обробка помилок

`validators/`

Joi / Zod / Yup схеми для перевірки даних.

`utils/`

Допоміжні функції, які використовуються в різних місцях.

`tests/`

Тести API або окремих модулів.

## 4. Як це створити крок за кроком
- Крок 1. Створити проєкт
  ```bash
  mkdir backend
  cd backend
  ```
- Крок 2. Встановити основні пакети

  ```bash
  npm install express cors dotenv morgan
  npm install mongoose bcrypt jsonwebtoken joi
  npm install nodemon --save-dev
  ```

Якщо ти працюєш з `PostgreSQL`, тоді замість mongoose будуть інші пакети, наприклад `pg` або `sequelize/prisma`.

## 5. Створити базову структуру папок

У Bash:
```bash
mkdir -p src/{config,routes,controllers,services,models,middlewares,validators,utils,constants,docs}
mkdir tests
touch src/app.js src/server.js
touch src/config/db.js src/config/env.js
touch src/routes/index.js src/routes/authRoutes.js src/routes/userRoutes.js
touch src/controllers/authController.js src/controllers/userController.js
touch src/services/authService.js src/services/userService.js
touch src/models/User.js
touch src/middlewares/authMiddleware.js src/middlewares/errorHandler.js src/middlewares/validateBody.js
touch src/validators/authSchemas.js src/validators/userSchemas.js
touch src/utils/HttpError.js src/utils/ctrlWrapper.js
touch .env .env.example .gitignore README.md
```
На Windows Git Bash це теж має працювати.

## 6. Базові файли
src/server.js
```js
const app = require('./app');
const { connectDB } = require('./config/db');

const PORT = process.env.PORT || 3000;

const start = async () => {
  try {
    await connectDB();
    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });
  } catch (error) {
    console.error('Failed to start server:', error.message);
    process.exit(1);
  }
};

start();
```
src/app.js
```js
const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const routes = require('./routes');
const errorHandler = require('./middlewares/errorHandler');

const app = express();

app.use(cors());
app.use(morgan('dev'));
app.use(express.json());

app.use('/api', routes);

app.use((req, res) => {
  res.status(404).json({ message: 'Route not found' });
});

app.use(errorHandler);

module.exports = app;
```
src/config/db.js
```js
const mongoose = require('mongoose');

const connectDB = async () => {
  const dbUri = process.env.DB_URI;

  if (!dbUri) {
    throw new Error('DB_URI is not defined');
  }

  await mongoose.connect(dbUri);
  console.log('Database connected');
};

module.exports = { connectDB };
```
src/routes/index.js
```js
const express = require('express');
const authRoutes = require('./authRoutes');
const userRoutes = require('./userRoutes');

const router = express.Router();

router.use('/auth', authRoutes);
router.use('/users', userRoutes);

module.exports = router;
```

## 7. Приклад модуля користувача
src/models/User.js
```js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema(
  {
    email: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model('User', userSchema);
```

src/services/authService.js
```js
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const HttpError = require('../utils/HttpError');

const registerUser = async ({ email, password, name }) => {
  const existingUser = await User.findOne({ email });

  if (existingUser) {
    throw HttpError(409, 'Email already in use');
  }

  const hashedPassword = await bcrypt.hash(password, 10);

  const user = await User.create({
    email,
    password: hashedPassword,
    name,
  });

  return {
    id: user._id,
    email: user.email,
    name: user.name,
  };
};

const loginUser = async ({ email, password }) => {
  const user = await User.findOne({ email });

  if (!user) {
    throw HttpError(401, 'Email or password is invalid');
  }

  const isPasswordCorrect = await bcrypt.compare(password, user.password);

  if (!isPasswordCorrect) {
    throw HttpError(401, 'Email or password is invalid');
  }

  const token = jwt.sign(
    { id: user._id },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );

  return {
    token,
    user: {
      id: user._id,
      email: user.email,
      name: user.name,
    },
  };
};

module.exports = {
  registerUser,
  loginUser,
};
```

src/controllers/authController.js
```js
const authService = require('../services/authService');

const register = async (req, res) => {
  const result = await authService.registerUser(req.body);
  res.status(201).json(result);
};

const login = async (req, res) => {
  const result = await authService.loginUser(req.body);
  res.status(200).json(result);
};

module.exports = {
  register,
  login,
};
src/routes/authRoutes.js
const express = require('express');
const ctrl = require('../controllers/authController');
const validateBody = require('../middlewares/validateBody');
const { registerSchema, loginSchema } = require('../validators/authSchemas');
const ctrlWrapper = require('../utils/ctrlWrapper');

const router = express.Router();

router.post('/register', validateBody(registerSchema), ctrlWrapper(ctrl.register));
router.post('/login', validateBody(loginSchema), ctrlWrapper(ctrl.login));

module.exports = router;
```

src/validators/authSchemas.js
```js
const Joi = require('joi');

const registerSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(6).required(),
  name: Joi.string().min(2).required(),
});

const loginSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().required(),
});

module.exports = {
  registerSchema,
  loginSchema,
};
```

## 8. Middleware для валідації та помилок
src/middlewares/validateBody.js
```js
const HttpError = require('../utils/HttpError');

const validateBody = (schema) => {
  return (req, res, next) => {
    const { error } = schema.validate(req.body);

    if (error) {
      return next(HttpError(400, error.message));
    }

    next();
  };
};

module.exports = validateBody;
```

src/middlewares/errorHandler.js
```js
const errorHandler = (err, req, res, next) => {
  const status = err.status || 500;
  const message = err.message || 'Server error';

  res.status(status).json({
    message,
  });
};

module.exports = errorHandler;
```

src/utils/HttpError.js
```js
const HttpError = (status, message) => {
  const error = new Error(message);
  error.status = status;
  return error;
};

module.exports = HttpError;
```

src/utils/ctrlWrapper.js
```
const ctrlWrapper = (ctrl) => {
  return async (req, res, next) => {
    try {
      await ctrl(req, res, next);
    } catch (error) {
      next(error);
    }
  };
};

module.exports = ctrlWrapper;
```

## 9. .env
```env
PORT=3000
DB_URI=mongodb://127.0.0.1:27017/mydb
JWT_SECRET=supersecretkey
```
.env.example
```env
PORT=
DB_URI=
JWT_SECRET=
```

## 10. package.json scripts
```json
"scripts": {
  "start": "node src/server.js",
  "dev": "nodemon src/server.js"
}
```

## 11. Як правильно будувати логіку

Хороший принцип:
- route → тільки шлях і middleware
- controller → прийняв запит, викликав service, віддав response
- service → уся основна логіка
- model → структура даних
- middleware → повторно використовувана перевірка

Тобто не варто пхати всю логіку прямо в роут.

## 12. Що ще додати в “повний” бекенд

Для більш серйозного проєкту ще бажано мати:

**Авторизацію**
- JWT
- refresh token
- ролі admin/user

**Безпеку**
- helmet
- rate limit
- sanitize input
- CORS config

**Логування**
- morgan для HTTP
- окремий logger для помилок

**Документацію**
- Swagger / OpenAPI

**Тести**
- Jest + Supertest

**Роботу з файлами**
- multer
- хмарне сховище

**Фонові задачі**
- cron jobs
- черги, якщо треба email/обробка зображень

## 13.  Більш професійна структура по модулях

Коли проєкт росте, зручніше групувати не по типах файлів, а по фічах:
```
src/
├── modules/
│   ├── auth/
│   │   ├── auth.controller.js
│   │   ├── auth.service.js
│   │   ├── auth.routes.js
│   │   └── auth.schemas.js
│   │
│   └── users/
│       ├── user.controller.js
│       ├── user.service.js
│       ├── user.routes.js
│       └── user.schemas.js
│
├── middlewares/
├── models/
├── utils/
├── config/
├── app.js
└── server.js
```

Це часто кращий варіант для середніх і великих проєктів.

## 14. Мінімальний порядок створення бекенду

Щоб не заплутатись, роби так:
- створити проєкт і встановити залежності
- створити server.js і app.js
- підключити БД
- зробити одну сутність, наприклад users
- додати модель
- додати routes → controller → service
- додати валідацію
- додати обробку помилок
- додати auth
- додати документацію і тести

## 15. Типова помилка новачків

Найчастіше проблеми виникають, коли:
- уся логіка лежить у роуті
- немає розділення controller/service
- немає централізованої обробки помилок
- змінні з .env читаються хаотично
- немає окремого шару для валідації
- структура папок росте без системи

## 16. Найкращий стартовий варіант

Для невеликого або середнього проєкту я б радив таку структуру:
```
src/
├── app.js
├── server.js
├── config/
├── routes/
├── controllers/
├── services/
├── models/
├── middlewares/
├── validators/
└── utils/
```
Це простіше за “enterprise”-архітектуру, але вже достатньо правильно.

## 17. Якщо хочеш зовсім готовий каркас

Ось короткий шаблон логіки для кожної нової сутності:

Для products ти створюєш:
- routes/productRoutes.js
- controllers/productController.js
- services/productService.js
- models/Product.js
- validators/productSchemas.js

І далі:

- `route` приймає шлях
- `controller` викликає service
- `service` працює з model
- `validator` перевіряє body

## 18. Висновок

Повна структура бекенду — це не просто набір папок, а розділення відповідальностей:

- routes — куди йде запит
- controllers — що відповісти
- services — що треба зробити
- models — як зберігаються дані
- middlewares — загальні перевірки
- validators — правильність даних
- config — налаштування
- utils — допоміжні речі