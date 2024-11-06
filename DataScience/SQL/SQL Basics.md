# Основи SQL
SQL (Structured Query Language) – це мова для управління даними в реляційних базах даних. Вона надає можливість створювати, модифікувати та запитувати дані в структурованих таблицях.

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

## 4. Групування результатів
- `GROUP BY` – групування записів за колонкою.
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
  ```

- `HAVING` – умови для груп.
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 1;
  ```

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

## 6. Оператори підзапитів
- `EXISTS` – перевіряє, чи повертає підзапит будь-який результат.
  ```sql
  SELECT * FROM table1 WHERE EXISTS (SELECT * FROM table2 WHERE condition);
  ```

- `IN` – перевірка наявності значення в множині результатів.
  ```sql
  SELECT * FROM table_name WHERE column IN (SELECT column FROM table_name2);
  ```

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

## 8. Оператори для роботи з транзакціями
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

## 9. Спеціальні оператори
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

## 10. Об’єднання результатів
- `UNION` – об’єднання результатів двох запитів.
  ```sql
  SELECT column FROM table1 UNION SELECT column FROM table2;
  ```

- `UNION ALL` – повертає всі записи, включаючи дублікати.
  ```sql
  SELECT column FROM table1 UNION ALL SELECT column FROM table2;
  ```

## 11. Інші особливості SQL
- Індекси – для оптимізації пошуку.
  ```sql
  CREATE INDEX index_name ON table_name (column);
  ```

- Права доступу – контроль прав користувачів.
  ```sql
  GRANT SELECT, INSERT ON table_name TO user;
  REVOKE SELECT ON table_name FROM user;
  ```

## Тонкощі роботи з SQL
- `HAVING` проти `WHERE`: HAVING використовується для фільтрації результатів після групування, тоді як WHERE – перед групуванням.
- Вкладені запити: дозволяють виконувати складні запити, проте можуть впливати на продуктивність.
- Індекси: значно покращують швидкість запитів, але можуть сповільнити операції вставки та оновлення.
- Оператор `EXISTS`: ефективний для перевірки існування записів, особливо в підзапитах.
