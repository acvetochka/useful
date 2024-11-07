# Підключення до баз даних

## 1. Підключення до бази даних SQLite в Python
SQLite — це легка вбудована реляційна система управління базами даних, яка не вимагає окремого сервера для роботи. У Python для роботи з SQLite використовується вбудований модуль sqlite3.

Основні кроки:
- Імпорт бібліотеки:

  ```python
  import sqlite3
  ```

- Створення підключення: Для підключення до бази даних SQLite використовується функція sqlite3.connect(), де вказується шлях до бази даних.

  ```python
  conn = sqlite3.connect('path_to_db.db')  # для існуючої бази
  ```

- Виконання SQL запитів: Після підключення можна виконувати SQL запити:

  ```python
  cursor = conn.cursor()  # створення курсора для виконання запитів
  cursor.execute("SELECT * FROM table_name")  # виконуємо запит
  rows = cursor.fetchall()  # отримуємо всі результати
  ```

- Закриття підключення: Не забудьте закрити підключення після завершення роботи:

  ```python
  conn.close()
  ```

Використання в Jupyter:

В Jupyter можна використовувати магію клітин для роботи з SQLite:

  ```python
  %sql sqlite:///path_to_db.db
  ```

## 2. Підключення до IBM Db2 за допомогою Python
IBM Db2 — це потужна реляційна система баз даних. Для підключення до IBM Db2 через Python використовують бібліотеку ibm_db.

Основні кроки:

- Інсталяція бібліотеки: Для підключення потрібно встановити бібліотеку ibm_db.

  ```bash
  pip install ibm_db
  ```

- Підключення до бази даних: Для встановлення підключення потрібно вказати параметри підключення (ім’я хоста, база даних, користувач, пароль):

  ```python
  import ibm_db
  conn = ibm_db.connect("DATABASE=YOUR_DB;HOSTNAME=your_host;PORT=50000;UID=your_user;PWD=your_password;", "", "")
  ```

- Виконання запитів: Після встановлення з’єднання можна виконувати запити:

  ```python
  sql = "SELECT * FROM table_name"
  stmt = ibm_db.exec_immediate(conn, sql)
  result = ibm_db.fetch_assoc(stmt)
  while result:
      print(result)
      result = ibm_db.fetch_assoc(stmt)
  ```

- Закриття з’єднання: Не забудьте закрити з’єднання:

  ```python
  ibm_db.close(conn)
  ```

## 3. Підключення до бази даних через Pandas
Pandas має вбудовану підтримку для підключення до різних баз даних за допомогою функції read_sql(). Підключення через Pandas дозволяє безпосередньо імпортувати дані з бази даних в DataFrame.

- Підключення до SQLite:
  ```python
  import pandas as pd
  import sqlite3
  
  # Підключення до SQLite
  conn = sqlite3.connect('path_to_db.db')
  
  # Виконання запиту та збереження результатів в DataFrame
  df = pd.read_sql("SELECT * FROM table_name", conn)
  ```

- Підключення до PostgreSQL:
  
  Для роботи з PostgreSQL через Pandas необхідно мати бібліотеку psycopg2:

  ```bash
  pip install psycopg2
  ```

  Підключення до PostgreSQL:

  ```python
  import pandas as pd
  import psycopg2
  
  # Підключення до PostgreSQL
  conn = psycopg2.connect("dbname=test user=postgres password=secret")
  
  # Виконання запиту та збереження результатів в DataFrame
  df = pd.read_sql("SELECT * FROM table_name", conn)
  ```

## 4. Підключення до бази даних через Jupyter (SQL magic)
Jupyter дозволяє інтегрувати SQL запити безпосередньо в блокноти за допомогою магії клітин. Для цього використовуються спеціальні магічні команди %sql (для однорядкових запитів) або %%sql (для багаторядкових запитів).

Встановлення SQL magic:

- Інсталяція бібліотеки ipython-sql:

```bash
pip install ipython-sql
```

- Імпорт бібліотеки і підключення до бази даних: В Jupyter необхідно завантажити магію SQL:

```python
%load_ext sql
```

- Підключення до бази даних:
  - Для SQLite:

    ```python
    %sql sqlite:///path_to_db.db
    ```

  - Для PostgreSQL:
  
    ```python
    %sql postgresql://user:password@localhost/dbname
    ```

- Виконання запитів:
  - Для простих запитів:

    ```python
    %sql SELECT * FROM table_name
    ```
  - Для багаторядкових запитів:
  
     ```python
      %%sql
      SELECT * FROM table_name
      WHERE condition = 'value'
     ```
   
## 5. Підключення до MySQL через Python
Для підключення до MySQL через Python використовується бібліотека mysql-connector-python.

Основні кроки:

- Інсталяція бібліотеки:

  ```bash
  pip install mysql-connector-python
  ```

- Підключення до MySQL:

  ```python
  import mysql.connector
  
  conn = mysql.connector.connect(
      host="localhost",
      user="your_user",
      password="your_password",
      database="your_database"
  )
  ```

- Виконання запитів:

  ```python
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM table_name")
  rows = cursor.fetchall()
  for row in rows:
      print(row)
  ```

- Закриття з’єднання:

  ```python
  conn.close()
  ```

## 6. Підключення до MongoDB через Python
MongoDB — це документо-орієнтована база даних. Для підключення до MongoDB в Python використовується бібліотека pymongo.

Основні кроки:

- Інсталяція бібліотеки:

  ```bash
  pip install pymongo
  ```

- Підключення до MongoDB:

  ```python
  from pymongo import MongoClient
  
  client = MongoClient("mongodb://localhost:27017/")
  db = client['your_database']
  collection = db['your_collection']
  ```

- Виконання запитів:

  ```python
  data = collection.find({"field": "value"})
  for record in data:
      print(record)
  ```
