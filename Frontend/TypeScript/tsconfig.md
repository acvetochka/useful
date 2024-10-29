# tsconfig.json

tsconfig.json є конфігураційним файлом для компілятора TypeScript, який дозволяє налаштувати всі необхідні параметри компіляції, що дає гнучкість у налаштуванні проекту. Ось детальніше про основні та додаткові властивості цього файлу.

## Основні властивості tsconfig.json
### 1. compilerOptions
Цей розділ визначає різноманітні параметри компіляції.

- `target`: Стандарт ECMAScript, який використовується для компіляції (напр. ES5, ES6/ES2015, ES2020).

  ```json
  "target": "ES6"
  ```

- `module`: Формат модулів (commonjs, esnext, amd, system).

  ```json
  "module": "commonjs"
  ```

- `lib`: Масив бібліотек, які включатимуться під час компіляції. Дозволяє працювати з API відповідних специфікацій, як-от DOM, ES2015.

  ```json
  "lib": ["ES6", "DOM"]
  ```

- `allowJs`: Дозволяє компілювати .js файли поряд із .ts файлами.

  ```json
  "allowJs": true
  ```

- `checkJs`: Дозволяє перевіряти типи в .js файлах.

  ```json
  "checkJs": true
  ```

- `outDir`: Вказує директорію для збереження скомпільованих файлів.

  ```json
  "outDir": "./dist"
  ```

- `rootDir`: Вказує кореневу директорію вихідних файлів.

  ```json
  "rootDir": "./src"
  ```

- `strict`: Включає всі строгі правила компілятора (описані нижче).

  ```json
  "strict": true
  ```

- `strictNullChecks`: Дозволяє уникати присвоєння null чи undefined змінним, де цього не передбачено.

  ```json
  "strictNullChecks": true
  ```

- `strictPropertyInitialization`: Вимагає ініціалізації всіх властивостей класів.

  ```json
  "strictPropertyInitialization": true
  ```

- `noImplicitAny`: Забороняє використання неявного типу any.

  ```json
  "noImplicitAny": true
  ```

- `noImplicitThis`: Забороняє використання this без явного визначення типу.

  ```json
  "noImplicitThis": true
  ```

- `esModuleInterop`: Забезпечує сумісність з ES-модулями (import з CommonJS).

  ```json
  "esModuleInterop": true
  ```

- `forceConsistentCasingInFileNames`: Вимагає використання однакового регістру для файлів у всьому проекті.

  ```json
  "forceConsistentCasingInFileNames": true
  ```

- `noEmit`: Забороняє створення скомпільованих файлів, корисно для перевірки коду.

  ```json
  "noEmit": true
  ```

- `declaration`: Створює файли декларацій (.d.ts).

  ```json
  "declaration": true
  ```

- `sourceMap`: Створює .map файли для відлагодження.

  ```json
  "sourceMap": true
  ```

- `resolveJsonModule`: Дозволяє імпорт .json файлів.

  ```json
  "resolveJsonModule": true
  ```

- `jsx`: Налаштування для JSX у проектах React (preserve, react, react-jsx).

  ```json
  "jsx": "react"
  ```

### 2. include, exclude та files
- `include`: Вказує файли або директорії, які необхідно включити до компіляції.

  ```json
  "include": ["src/**/*.ts"]
  ```

- `exclude`: Вказує файли або директорії, які необхідно виключити з компіляції.

  ```json
  "exclude": ["node_modules", "dist"]
  ```
  
- `files`: Конкретний перелік файлів для компіляції (рідше використовується, коли потрібно чітко визначити файли).

  ```json
  "files": ["src/index.ts"]
  ```

### 3. Інші корисні налаштування
- `paths та baseUrl`: Дозволяють налаштувати псевдоніми шляхів для зручнішого імпорту модулів.

  ```json
  "baseUrl": "./",
  "paths": {
      "@app/*": ["src/app/*"]
  }
  ```

- `typeRoots`: Вказує директорії для пошуку типів (корисно для кастомних типів або кастомних дефініцій).

  ```json
  "typeRoots": ["./node_modules/@types", "./types"]
  ```

- `types`: Явно вказує, які дефініції типів слід включати.

  ```json
  "types": ["node", "jest"]
  ```

- `emitDecoratorMetadata`: Створює метадані для декораторів (часто використовується з Angular).

  ```json
  "emitDecoratorMetadata": true
  ```

- `experimentalDecorators`: Дозволяє використовувати декоратори.

  ```json
  "experimentalDecorators": true
  ```

- `skipLibCheck`: Пропускає перевірку типів у файлах .d.ts, що прискорює компіляцію.

  ```json
  "skipLibCheck": true
  ```

- `incremental`: Зберігає інформацію про компіляцію для прискорення повторних компіляцій.

  ```json
  "incremental": true
  ```

- `composite`: Вказує, що проєкт є залежним і може збиратись у певній послідовності. Потрібен для монорепозиторіїв.

  ```json
  "composite": true
  ```

### Приклад конфігураційного файлу tsconfig.json
Ось приклад файлу tsconfig.json з основними параметрами:

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs",
    "lib": ["ES6", "DOM"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "noImplicitAny": true,
    "skipLibCheck": true,
    "incremental": true,
    "jsx": "react",
    "sourceMap": true,
    "declaration": true,
    "paths": {
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"]
    }
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

Ця конфігурація дозволить оптимізувати компіляцію TypeScript, чітко визначаючи правила для кожного аспекту, від типів і модулів до директорій, які потрібно включити або виключити.
