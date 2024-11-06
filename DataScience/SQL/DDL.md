# Data Definition Language (DDL)
DDL включає оператори для визначення структури бази даних і її об’єктів, таких як таблиці, індекси та схеми. Ось основні команди DDL:

## 1. Основні оператори DDL
- `CREATE` – створення нових об'єктів у базі даних, таких як таблиці, індекси та схеми.

  - `CREATE TABLE` – створення нової таблиці.

    ```sql
    CREATE TABLE table_name (
        column1 datatype CONSTRAINT,
        column2 datatype CONSTRAINT,
        ...
    );
    ```
    Наприклад:
    
    ```sql
    CREATE TABLE employees (
        id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        salary DECIMAL(10, 2)
    );
    ```

  - `CREATE INDEX` – створення індексу для прискорення доступу до даних.

    ```sql
    CREATE INDEX index_name ON table_name (column);
    ```

  - `CREATE VIEW` – створення віртуальної таблиці на основі результату запиту.
  
    ```sql
    CREATE VIEW view_name AS
    SELECT column1, column2 FROM table_name WHERE condition;
    ```
  
- `ALTER` – модифікація існуючих об'єктів у базі даних.

  - `ALTER TABLE` – зміна структури таблиці (додавання, видалення чи модифікація колонок).
  
    ```sql
    ALTER TABLE table_name
    ADD column_name datatype;
    ```
  
  - Видалення колонки:
    
    ```sql
    ALTER TABLE table_name
    DROP COLUMN column_name;
    ```
    
  - Зміна типу даних колонки:
  
    ```sql
    ALTER TABLE table_name
    MODIFY column_name new_datatype;
    ```
    
- `DROP` – видалення об'єктів з бази даних.

  - `DROP TABLE` – видалення таблиці разом з усіма її даними.
  
    ```sql
    DROP TABLE table_name;
    ```

  - `DROP INDEX` – видалення індексу.
  
    ```sql
    DROP INDEX index_name ON table_name;
    ```
  
  - `DROP VIEW` – видалення представлення (view).
  
    ```sql
    DROP VIEW view_name;
    ```

- `TRUNCATE` – швидке видалення всіх записів у таблиці, не зберігаючи журнал транзакцій.

  ```sql
  TRUNCATE TABLE table_name;
  ```
  
  Примітка: TRUNCATE працює швидше за DELETE, але не можна відкотити видалення, оскільки це DDL-операція.

## 2. Тонкощі та особливості DDL
- TRANSACTION Control: DDL-команди автоматично фіксують транзакцію, що означає, що їх не можна відкотити через ROLLBACK.
- Безпечне використання DROP: Після видалення таблиці з допомогою DROP відновити дані не можна. З обережністю використовуйте цю команду в продакшн-базах.
- Використання ALTER TABLE: Зміна структури великих таблиць може займати багато часу та вимагати блокування таблиці, що може вплинути на доступ до даних для інших користувачів.
- Індекси та продуктивність: Індекси покращують швидкість вибірки, але можуть впливати на продуктивність вставок і оновлень.
