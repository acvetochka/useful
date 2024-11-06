# Оператори SQL
SQL (Structured Query Language) – це мова для управління даними в реляційних базах даних. Вона надає можливість створювати, модифікувати та запитувати дані в структурованих таблицях.

## Зміст 

+ [Категорії операторів SQL](#категорії-операторів-sql) 
+ [1. Оператори для вибірки даних](#1-оператори-для-вибірки-даних) - SELECT, DISTINCT, WHERE
+ [2. Оператори для сортування](#2-оператори-для-сортування) - ORDER BY
+ [3. Оператори для агрегації даних](#3-оператори-для-агрегації-даних) - COUNT, SUM, AVG, MIN і MAX
+ [4. Групування результатів](#4-групування-результатів) - GROUP BY, HAVING
+ [5. З’єднання таблиць (JOIN)](#5-зєднання-таблиць-join) - INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN
+ [6. Оператори підзапитів](#6-оператори-підзапитів) - EXISTS, IN
+ [7. Оператори зміни даних](#7-оператори-зміни-даних) - INSERT INTO, UPDATE, DELETE
+ [8. Спеціальні оператори](#8-спеціальні-оператори) - LIKE, BETWEEN, IS NULL, IS NOT NULL
+ [9. Об’єднання результатів](#9-обєднання-результатів) - UNION, UNION ALL
+ [10. Оператори для роботи з рядками](#10-оператори-для-роботи-з-рядками) - CONCAT, LENGTH / CHAR_LENGTH, UPPER / LOWER, SUBSTRING / SUBSTR, TRIM, REPLACE, POSITION / INSTR, LEFT / RIGHT, LPAD / RPAD, FORMAT
+ [11. Оператори для об'єднання множин](#11-оператори-для-обєднання-множин) - INTERSECT, EXCEPT / MINUS
+ [12. Оператори для умов у запитах](#12-оператори-для-умов-у-запитах) - CASE, COALESCE, NULLIF
+ [13. Інші корисні оператори](#13-інші-корисні-оператори) - IS DISTINCT FROM, ROW_NUMBER()
+ [14. Оператори керування доступом - DCL (Data Control Language)](#14-оператори-керування-доступом---dcl-data-control-language) - GRANT, REVOKE
+ [15. Оператори для роботи з транзакціями - TCL (Transaction Control Language)](#15-оператори-для-роботи-з-транзакціями---tcl-transaction-control-language)- BEGIN TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT, ROLLBACK TO SAVEPOINT, SET TRANSACTION, LOCK TABLE
+ [Інші особливості SQL](#інші-особливості-sql)
+ [Тонкощі роботи з SQL](#тонкощі-роботи-з-sql)



## Категорії операторів SQL
В SQL існує п'ять основних видів операторів, кожен із яких має свої функції та призначення для роботи з базами даних:

- `DDL` (Data Definition Language) – мова визначення даних

  Відповідає за структуру бази даних, створення, зміну та видалення об’єктів (таблиць, індексів, схем тощо).

  Основні команди:
  - CREATE (створення таблиць, індексів, представлень, схем),
  - ALTER (зміна структури об'єктів),
  - DROP (видалення об'єктів),
  - TRUNCATE (видалення всіх записів таблиці),
  - RENAME (перейменування об'єктів).
 
  [Докладніше  про оператори DDL](https://github.com/acvetochka/useful/blob/main/DataScience/SQL/DDL.md)
  
- `DML` (Data Manipulation Language) – мова маніпулювання даними

  Використовується для роботи з даними всередині таблиць: вставка, оновлення, видалення, вибірка даних.

  Основні команди:
  - SELECT (вибірка даних),
  - INSERT (додавання нових записів),
  - UPDATE (оновлення існуючих записів),
  - DELETE (видалення записів).
 
    Докладніше з цими операторами можете ознайомитись нижче, де використовується інша класифікація.
 
- `TCL` (Transaction Control Language) – мова керування транзакціями

  Використовується для управління транзакціями та контролю над цілісністю даних при виконанні змін у базі.

  Основні команди:
  - BEGIN (початок транзакції, підтримується не у всіх СУБД),
  - COMMIT (фіксація змін у базі),
  - ROLLBACK (відкат змін),
  - SAVEPOINT (встановлення проміжної точки в транзакції),
  - ROLLBACK TO SAVEPOINT (відкат до проміжної точки).
 
  [Докладніше про оператори TCL](#15-оператори-для-роботи-з-транзакціями---tcl-transaction-control-language)

- `DCL` (Data Control Language) – мова контролю доступу

  Використовується для управління правами доступу до об'єктів бази даних.

  Основні команди:
  - GRANT (надання прав доступу),
  - REVOKE (відкликання прав доступу).
 
  [Докладніше  про оператори DCL](#14-оператори-керування-доступом---dcl-data-control-language)

- `DQL` (Data Query Language) – мова запитів даних

  У деяких класифікаціях виділяється окремо, проте зазвичай вважається частиною DML.

  Основна команда:
  - SELECT – вибірка даних із бази даних. Це фактично єдина команда, яка часто розглядається як частина DQL, хоча її також відносять до DML.

  [Повернутися до змісту](#зміст)

## 1. Оператори для вибірки даних
- `SELECT` – вибір даних із таблиці.
  
  ```sql
  SELECT column1, column2 FROM table_name;
  ```

- `DISTINCT` – унікальні значення в колонці.
  ```sql
  SELECT DISTINCT column1 FROM table_name;
  ```
- `WHERE` – фільтрація даних за умовами.

  ```sql
  SELECT * FROM table_name WHERE condition;
  ```

  [Повернутися до змісту](#зміст)

## 2. Оператори для сортування

- `ORDER BY` – сортування результатів.

  ```sql
  SELECT * FROM table_name ORDER BY column1 ASC|DESC;
  ```

## 3. Оператори для агрегації даних
- `COUNT` – кількість записів.
  ```sql
  SELECT COUNT(column) FROM table_name;
  ```

- `SUM` – сума значень.
  ```sql
  SELECT SUM(column) FROM table_name;
  ```

- `AVG` – середнє значення.
  ```sql
  SELECT AVG(column) FROM table_name;
  ```

- `MIN` і `MAX` – мінімальне та максимальне значення.
  ```sql
  SELECT MIN(column), MAX(column) FROM table_name;
  ```

   [Повернутися до змісту](#зміст)

## 4. Групування результатів
- `GROUP BY` – групування записів за колонкою.
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
  ```

- `HAVING` – умови для груп.
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 1;
  ```

   [Повернутися до змісту](#зміст)
  
## 5. З’єднання таблиць (JOIN)
- `INNER JOIN` – повертає записи з обох таблиць, що мають спільні значення.
  ```sql
  SELECT columns FROM table1 INNER JOIN table2 ON table1.id = table2.id;
  ```

- `LEFT JOIN` – повертає всі записи з лівої таблиці й відповідні записи з правої.
  ```sql
  SELECT columns FROM table1 LEFT JOIN table2 ON table1.id = table2.id;
  ```

- `RIGHT JOIN` – повертає всі записи з правої таблиці та відповідні записи з лівої.
  ```sql
  SELECT columns FROM table1 RIGHT JOIN table2 ON table1.id = table2.id;
  ```

- `FULL JOIN` – повертає всі записи, якщо є співпадіння з обох сторін.
  ```sql
  SELECT columns FROM table1 FULL OUTER JOIN table2 ON table1.id = table2.id;
  ```

   [Повернутися до змісту](#зміст)


## 6. Оператори підзапитів
- `EXISTS` – перевіряє, чи повертає підзапит будь-який результат.
  ```sql
  SELECT * FROM table1 WHERE EXISTS (SELECT * FROM table2 WHERE condition);
  ```

- `IN` – перевірка наявності значення в множині результатів.
  ```sql
  SELECT * FROM table_name WHERE column IN (SELECT column FROM table_name2);
  ```

   [Повернутися до змісту](#зміст)


## 7. Оператори зміни даних
- `INSERT INTO` – додавання записів.
  ```sql
  INSERT INTO table_name (column1, column2) VALUES (value1, value2);
  ```

- `UPDATE` – оновлення записів.
  ```sql
  UPDATE table_name SET column1 = value1 WHERE condition;
  ```

- `DELETE` – видалення записів.
  ```sql
  DELETE FROM table_name WHERE condition;
  ```

  [Повернутися до змісту](#зміст)


## 8. Спеціальні оператори
- `LIKE` – пошук за шаблоном (% і _ для масок).
  ```sql
  SELECT * FROM table_name WHERE column LIKE 'pattern%';
  ```

- `BETWEEN` – перевірка діапазону значень.
  ```sql
  SELECT * FROM table_name WHERE column BETWEEN value1 AND value2;
  ```

- `IS NULL` і `IS NOT NULL` – перевірка на відсутність значень.
  ```sql
  SELECT * FROM table_name WHERE column IS NULL;
  ```

  [Повернутися до змісту](#зміст)


## 9. Об’єднання результатів
- `UNION` – об’єднання результатів двох запитів.
  ```sql
  SELECT column FROM table1 UNION SELECT column FROM table2;
  ```

- `UNION ALL` – повертає всі записи, включаючи дублікати.
  ```sql
  SELECT column FROM table1 UNION ALL SELECT column FROM table2;
  ```

   [Повернутися до змісту](#зміст)


## 10. Оператори для роботи з рядками

- `CONCAT` - oб’єднує два або більше рядків в один

  ```sql
  SELECT CONCAT(first_name, ' ', last_name) AS full_name 
  FROM employees;

  -- Поверне значення full_name для кожного запису, поєднуючи first_name та last_name з пробілом між ними.
  ```

- `LENGTH` / `CHAR_LENGTH` - Повертає довжину рядка в символах.
  ```sql
  SELECT name, LENGTH(name) AS name_length 
  FROM products;
  
  -- Поверне назву продукту та його довжину (кількість символів) у полі name_length
  ```
  
- `UPPER` / `LOWER` - Перетворює рядок на верхній (UPPER) або нижній (LOWER) регістр.
  ```sql
  SELECT LOWER(email) AS lowercase_email 
  FROM users;
  
  -- Поверне значення email у нижньому регістрі для кожного користувача.
  ```
  
- `SUBSTRING` / `SUBSTR` - Витягує частину рядка, починаючи з вказаної позиції.
  ```sql
  SELECT SUBSTRING(description, 1, 10) AS short_desc 
  FROM items;
  
  -- Витягує перші 10 символів з description для кожного запису та повертає їх у полі short_desc.
  ```

- `TRIM` - Видаляє пробіли або інші символи з початку, кінця або обох сторін рядка.
  ```sql
  SELECT TRIM('   some text   ') AS trimmed_text;
  
  -- Повертає some text без пробілів на початку і в кінці.
  ```
  
- `REPLACE` - Замінює частину рядка на інший рядок.
  ```sql
  SELECT REPLACE(email, '@example.com', '@domain.com') AS updated_email 
  FROM users;
  
  -- Замість @example.com у полі email буде підставлено @domain.com.
  ```

- `POSITION` / `INSTR` - Знаходить позицію підрядка в рядку.
  ```sql
  SELECT POSITION('apple' IN description) AS position_in_desc 
  FROM products;
  
  -- Поверне позицію, на якій вперше зустрічається apple в description.
  ```

- `LEFT` / `RIGHT` - Витягує частину рядка з лівого (LEFT) або правого (RIGHT) боку.
  ```sql
  SELECT LEFT(name, 5) AS name_start 
  FROM clients;
  
  -- Поверне перші 5 символів з name.
  ```

- `LPAD` / `RPAD` - Додає заданий символ зліва або справа до рядка, поки він не досягне вказаної довжини.
  ```sql
  SELECT LPAD(order_id, 10, '0') AS padded_order_id 
  FROM orders;
  
  -- Додає 0 зліва до рядка order_id, щоб загальна довжина була 10 символів.
  ```

- `FORMAT` - Форматує числове значення як рядок.
  ```sql
  SELECT FORMAT(12345.6789, 2) AS formatted_number;
  
  -- Повертає 12345.68 як відформатоване значення з двома десятковими знаками.
  ```

   [Повернутися до змісту](#зміст)


##  11. Оператори для об'єднання множин
- `INTERSECT` – повертає спільні рядки, які є в обох множинах результатів двох запитів. Доступний у деяких СУБД (не підтримується, наприклад, у MySQL).

  ```sql
  SELECT column FROM table1
  INTERSECT
  SELECT column FROM table2;
  ```

- `EXCEPT` / `MINUS` – повертає рядки, які є в першому запиті, але відсутні в другому. (В MySQL теж не підтримується, а в Oracle використовується MINUS).

  ```sql
  SELECT column FROM table1
  EXCEPT
  SELECT column FROM table2;
  ```

   [Повернутися до змісту](#зміст)


## 12. Оператори для умов у запитах
- `CASE` – оператор умовного вибору, який працює подібно до оператора if-else.

  ```sql
  SELECT product_id,
         CASE
             WHEN quantity > 100 THEN 'High Stock'
             WHEN quantity > 0 THEN 'Low Stock'
             ELSE 'Out of Stock'
         END AS stock_status
  FROM products;
  ```

- `COALESCE` – повертає перше не NULL значення серед заданих аргументів.

  ```sql
  SELECT COALESCE(column1, column2, 'default_value') AS result FROM table_name;
  ```

- `NULLIF` – порівнює два значення, повертає NULL, якщо вони рівні, інакше повертає перше значення.

  ```sql
  SELECT NULLIF(column1, column2) AS result FROM table_name;
  ```

   [Повернутися до змісту](#зміст)


## 13. Інші корисні оператори
- `IS DISTINCT FROM` – порівнює значення, враховуючи NULL, що дозволяє визначити, чи відрізняються два значення (навіть якщо одне з них NULL).

  ```sql
  SELECT * FROM table_name WHERE column1 IS DISTINCT FROM column2;
  ```
  
- `ROW_NUMBER()` – функція, яка генерує послідовний номер для кожного рядка в межах визначеного набору результатів.


  ```sql
  SELECT column, ROW_NUMBER() OVER (ORDER BY column) AS row_num FROM table_name
  ```

   [Повернутися до змісту](#зміст)


## 14. Оператори керування доступом - DCL (Data Control Language)
- `GRANT` – надає права користувачам на певні операції (SELECT, INSERT тощо) або об'єкти (таблиці, бази даних).

  ```sql
  GRANT SELECT, INSERT ON table_name TO user_name;
  ```

- `REVOKE` – відкликає права доступу, раніше надані користувачеві.

  ```sql
  REVOKE INSERT ON table_name FROM user_name;
  ```

   [Повернутися до змісту](#зміст)


## 15. Оператори для роботи з транзакціями - TCL (Transaction Control Language) 

- `BEGIN TRANSACTION` – початок транзакції.
  ```sql
  BEGIN TRANSACTION;
  ```

- `COMMIT` – підтвердження змін.
  ```sql
  COMMIT;
  ```

- `ROLLBACK` – скасування змін.
  ```sql
  ROLLBACK;
  ```
  
- `SAVEPOINT` – встановлює проміжну точку в транзакції, щоб можна було зробити частковий відкат до цієї точки без скасування всієї транзакції.

  ```sql
  SAVEPOINT savepoint_name;
  ```

- `ROLLBACK TO SAVEPOINT` – відкочує транзакцію до певного SAVEPOINT.

  ```sql
  ROLLBACK TO SAVEPOINT savepoint_name;
  ```

- `SET TRANSACTION` – задає параметри для поточної транзакції, наприклад, рівень ізоляції (рівні ізоляції керують тим, як транзакції бачать незавершені зміни інших транзакцій).

  ```sql
  SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
  ```

- `LOCK TABLE` – встановлює блокування на таблицю для управління паралельними транзакціями, запобігаючи одночасному доступу до неї.

  ```sql
  LOCK TABLE table_name IN ACCESS EXCLUSIVE MODE;
  ```

   [Повернутися до змісту](#зміст)

  
## Інші особливості SQL
- Індекси – для оптимізації пошуку.
  ```sql
  CREATE INDEX index_name ON table_name (column);
  ```

- Права доступу – контроль прав користувачів.
  ```sql
  GRANT SELECT, INSERT ON table_name TO user;
  REVOKE SELECT ON table_name FROM user;
  ```

   [Повернутися до змісту](#зміст)


## Тонкощі роботи з SQL
- `HAVING` проти `WHERE`: HAVING використовується для фільтрації результатів після групування, тоді як WHERE – перед групуванням.
- Вкладені запити: дозволяють виконувати складні запити, проте можуть впливати на продуктивність.
- Індекси: значно покращують швидкість запитів, але можуть сповільнити операції вставки та оновлення.
- Оператор `EXISTS`: ефективний для перевірки існування записів, особливо в підзапитах.

 [Повернутися до змісту](#зміст)

