# Типи даних та обмеження

У SQL існує різноманіття типів даних і обмежень (constraints), які забезпечують цілісність даних і контроль над їх форматом. Розглянемо основні типи даних, а також особливості обмежень PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, і пояснимо такі поняття, як DECIMAL.

## 1. Основні типи даних

### 1.1. Числові типи
  - `INT` / `INTEGER` – цілі числа. Використовується для зберігання числових значень без дробової частини.
  - `FLOAT` / `REAL` – числа з плаваючою комою. Використовуються для зберігання значень з дробовою частиною.
  - `DECIMAL(p, s)` / `NUMERIC(p, s)` – точні числа з фіксованою кількістю десяткових знаків. Використовується для фінансових даних, щоб уникнути проблем з округленням.
    
      p – загальна кількість цифр (precision).
    
      s – кількість цифр після коми (scale).
    
      Наприклад, DECIMAL(10, 2) може зберігати число з 10 цифрами, з яких 2 цифри знаходяться після коми, наприклад, 12345678.90.

### 1.2. Текстові типи
  - `CHAR(n)` – рядок з фіксованою довжиною n. Якщо довжина значення менша за n, прогалини додаються автоматично.
  - `VARCHAR(n)` – рядок зі змінною довжиною, максимальною довжиною n.
  - `TEXT` – текст довільної довжини. Використовується для великих обсягів текстових даних (приміток, описів).

### 1.3. Дата та час
  - `DATE` – зберігає лише дату (YYYY-MM-DD).
  - `TIME` – зберігає час (HH:MM).
  - `DATETIME` – зберігає дату і час одночасно (YYYY-MM-DD HH:MM).
  - `TIMESTAMP` – зберігає дату і час у вигляді UNIX-часу, корисний для відстеження часу створення або модифікації запису.

### 1.4. Логічні типи
  - `BOOLEAN` – зберігає логічні значення TRUE або FALSE. У деяких базах даних зберігається як 0 для FALSE і 1 для TRUE.

## 2. Обмеження (Constraints)
Обмеження забезпечують правила для даних у таблицях, підвищуючи їх цілісність і унікальність.

- `PRIMARY KEY` – унікальний ідентифікатор записів у таблиці. Значення в стовпці або комбінації стовпців з PRIMARY KEY має бути унікальним і не може бути NULL.

  ```sql
  CREATE TABLE users (
      user_id INT PRIMARY KEY,
      username VARCHAR(50) NOT NULL
  );
  ```

- `FOREIGN KEY` – посилання на PRIMARY KEY іншої таблиці. Забезпечує зв'язок між двома таблицями.

  ```sql
  CREATE TABLE orders (
      order_id INT PRIMARY KEY,
      user_id INT,
      FOREIGN KEY (user_id) REFERENCES users(user_id)
  );
  ```

- `NOT NULL` – обмеження, яке забороняє пусті значення (NULL) у стовпці.

  ```sql
  CREATE TABLE employees (
      employee_id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL
  );
  ```

- `UNIQUE` – обмеження, що забезпечує унікальність значень у стовпці. На відміну від PRIMARY KEY, UNIQUE допускає NULL.

  ```sql
  CREATE TABLE products (
      product_id INT PRIMARY KEY,
      serial_number VARCHAR(100) UNIQUE
  );
  ```

- `DEFAULT` – задає значення за замовчуванням для стовпця, якщо воно не вказано під час вставки.

  ```sql
  CREATE TABLE accounts (
      account_id INT PRIMARY KEY,
      status VARCHAR(10) DEFAULT 'active'
  );
  ```

- `CHECK` – обмеження, що визначає умови, яким мають відповідати значення стовпця.

  ```sql
  CREATE TABLE employees (
      employee_id INT PRIMARY KEY,
      age INT CHECK (age >= 18)
  );
  ```

### 3. Особливості та приклади
- `DECIMAL`: Використовується для фінансових або точних даних, наприклад, зберігання цін. На відміну від FLOAT, значення зберігаються точно, що запобігає помилкам округлення.

  ```sql
  CREATE TABLE transactions (
      transaction_id INT PRIMARY KEY,
      amount DECIMAL(10, 2) NOT NULL
  );
  ```

- `PRIMARY KEY` з `AUTO_INCREMENT` (MySQL): значення збільшується автоматично для кожного нового запису, що зручно для унікальних ідентифікаторів.

  ```sql
  CREATE TABLE customers (
      customer_id INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(50) NOT NULL
  );
  ```

- `FOREIGN KEY` з `ON DELETE` та `ON UPDATE`: визначають поведінку, якщо запис з PRIMARY KEY, на який посилається FOREIGN KEY, видаляється або оновлюється.

  ```sql
  CREATE TABLE orders (
      order_id INT PRIMARY KEY,
      customer_id INT,
      FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
  );
  ```

  - `ON DELETE CASCADE`: видаляє записи, які посилаються на видалений запис з основної таблиці.
  - `ON UPDATE CASCADE`: автоматично оновлює значення зовнішнього ключа, якщо основне значення було змінено.
