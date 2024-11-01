# Типи даних в TypeScript

TypeScript, як типізована надбудова JavaScript, пропонує широкий вибір типів даних і засобів, що допомагають створювати структурований та безпечний код. Давайте розглянемо основні типи даних, інтерфейси, класи та інші корисні концепції в TypeScript.

## 1. Типи даних в TypeScript
TypeScript підтримує стандартні типи JavaScript, додаючи статичну типізацію, що дає можливість уникнути багатьох помилок.

- `number`: Цілі числа та числа з плаваючою комою.

  ```typescript
  let age: number = 30;
  ```

- `string`: Рядки.

  ```typescript
  let name: string = "John";
  ```

- `boolean`: Логічні значення true або false.

  ```typescript
  let isActive: boolean = true;
  ```

- `array`: Масиви, які можуть містити лише елементи певного типу.

  ```
  typescript
  let numbers: number[] = [1, 2, 3];
  let fruits: Array<string> = ["apple", "banana"];
  ```

- `tuple`: Кортежі, де кожен елемент має визначений тип.

  ```typescript
  let user: [string, number] = ["Alice", 25];
  ```

- `enum`: Перелічуваний тип, що дозволяє визначити набір іменованих значень.

  ```typescript
  enum Color {
      Red,
      Green,
      Blue
  }
  let c: Color = Color.Green;
  ```

- `any`: Тип, що може містити будь-яке значення. Використовується, коли точно невідомий тип змінної.

  ```typescript
  let variable: any = "hello";
  variable = 42;
  ```

- `void`: Використовується для функцій, які не повертають значення.

  ```typescript
  function logMessage(message: string): void {
      console.log(message);
  }
  ```

- `null` та `undefined`: Спеціальні типи для null і undefined. В строгому режимі вони не можуть бути значенням інших типів, якщо це не дозволено явно.

- `never`: Використовується для функцій, які ніколи не повертають значення (наприклад, функції, що кидають помилки або зациклюються).

  ```typescript
  function throwError(errorMsg: string): never {
      throw new Error(errorMsg);
  }
  ```

## 2. Інтерфейси
Інтерфейси визначають структуру об’єктів і дозволяють типізувати об’єктні дані. Вони є декларативною конструкцією для опису формату даних.

- Базовий інтерфейс:

  ```typescript
  interface User {
      name: string;
      age: number;
  }
  
  let user: User = {
      name: "Alice",
      age: 30
  };
  ```

- Необов’язкові властивості: За допомогою ? можна визначити необов’язкові властивості.

  ```typescript
  interface Product {
      name: string;
      price?: number; // price може бути відсутньою
  }
  ``` 
- readonly: Модифікатор, що робить властивість лише для читання.

  ```typescript
  interface Book {
      readonly title: string;
      author: string;
  }
  ```

- Інтерфейси для функцій: Інтерфейс може використовуватися для опису типів функцій.

  ```typescript
  interface Calculate {
      (x: number, y: number): number;
  }
  
  const add: Calculate = (x, y) => x + y;
  ```

- Наслідування інтерфейсів: Інтерфейси можуть наслідувати один одного, що дозволяє створювати більш гнучкі структури.

  ```typescript
  interface Animal {
      name: string;
  }
  
  interface Dog extends Animal {
      breed: string;
  }
  ```

## 3. Класи
Класи в TypeScript базуються на класах ECMAScript, але з додатковими можливостями, такими як статична типізація, модифікатори доступу і декоратори.

- Основний синтаксис класу:

  ```typescript
  class Person {
      name: string;
      age: number;
  
      constructor(name: string, age: number) {
          this.name = name;
          this.age = age;
      }
  
      greet(): void {
          console.log(`Hello, my name is ${this.name}`);
      }
  }
  
  let person = new Person("John", 30);
  person.greet();
  ```

- Модифікатори доступу:

  - public (за замовчуванням) — властивість чи метод доступні будь-де.
  - private — властивість чи метод доступні лише всередині класу.
  - protected — доступні всередині класу та його підкласів.

  ```typescript
  class Animal {
      public name: string;
      private type: string;
      protected age: number;
  
      constructor(name: string, type: string, age: number) {
          this.name = name;
          this.type = type;
          this.age = age;
      }
  }
  ```
  
- Наслідування класів: Класи можуть наслідувати інші класи, використовуючи extends.

  ```typescript
  class Dog extends Animal {
      breed: string;
  
      constructor(name: string, type: string, age: number, breed: string) {
          super(name, type, age);
          this.breed = breed;
      }
  }
  ```
  
- Гетери та сетери: Використовуються для контролю доступу до властивостей.

  ```typescript
  class Rectangle {
      private _width: number;
      private _height: number;
  
      constructor(width: number, height: number) {
          this._width = width;
          this._height = height;
      }
  
      get area(): number {
          return this._width * this._height;
      }
  
      set width(width: number) {
          this._width = width;
      }
  }
  ```
  
- Статичні властивості та методи: Статичні елементи належать класу, а не його екземплярам.

  ```typescript
  class MathUtil {
      static pi: number = 3.14159;
  
      static calculateCircumference(diameter: number): number {
          return this.pi * diameter;
      }
  }

  let circumference = MathUtil.calculateCircumference(10);
  ```

## 4. Дженерики
Дженерики дозволяють створювати багаторазові компоненти, які можуть працювати з різними типами.

- Основний приклад використання дженериків:

  ```typescript
  function identity<T>(value: T): T {
      return value;
  }
  
  let num = identity<number>(10);
  let str = identity<string>("hello");
  ```

- Дженерики в класах: Дженерики можуть використовуватися для створення універсальних класів.

  ```typescript
  class Box<T> {
      contents: T;
  
      constructor(contents: T) {
          this.contents = contents;
      }
  
      getContents(): T {
          return this.contents;
      }
  }
  
  let box = new Box<string>("toys");
  ```

## 5. Перетин типів (Intersection Types) та об’єднання типів (Union Types)
Перетин типів дозволяє об’єднати декілька типів в один.

  ```typescript
  interface A {
      a: string;
  }
  
  interface B {
      b: number;
  }
  
  type C = A & B;
  
  let example: C = { a: "hello", b: 42 };
  ```

Об’єднання типів дозволяє змінній мати кілька типів.

  ```typescript
  let value: string | number;
  value = "hello";
  value = 100;
  ```

## 6. Декоратори
Декоратори — це спеціальні функції, які використовуються для додавання метаданих до класів, методів або властивостей. Вони часто застосовуються в Angular для визначення компонентів, служб та ін.

- Приклад декоратора класу:

  ```typescript
  function logClass(constructor: Function) {
      console.log("Class created:", constructor.name);
  }
  
  @logClass
  class MyClass {
      constructor() {}
  }
  ```

TypeScript забезпечує сильну типізацію та розширює можливості JavaScript, що значно полегшує розробку великих і складних застосунків. Інтерфейси, класи, дженерики та модифікатори доступу дозволяють забезпечити кращу структурованість і зрозумілість коду, що робить TypeScript ефективним інструментом для сучасної розробки.
