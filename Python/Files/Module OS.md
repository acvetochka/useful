# Module OS

Модуль os в Python надає інтерфейси для роботи з операційною системою, дозволяючи виконувати різноманітні дії з файлами, каталогами та іншими системними операціями.

## 
1. [Імпорт модуля os](https://github.com/acvetochka/useful/blob/main/Python/Files/Module%20OS.md#1-%D1%96%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8F-os)
2. [Основні функції модуля os](https://github.com/acvetochka/useful/blob/main/Python/Files/Module%20OS.md#2-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8F-os)

   2.1. [Робота з файлами та каталогами](https://github.com/acvetochka/useful/blob/main/Python/Files/Module%20OS.md#21-%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%B0-%D0%B7-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0%D0%BC%D0%B8-%D1%82%D0%B0-%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%D0%B0%D0%BC%D0%B8)
   
   2.2. [Отримання інформації про файли](https://github.com/acvetochka/useful/blob/main/Python/Files/Module%20OS.md#22-%D0%BE%D1%82%D1%80%D0%B8%D0%BC%D0%B0%D0%BD%D0%BD%D1%8F-%D1%96%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D1%96%D1%97-%D0%BF%D1%80%D0%BE-%D1%84%D0%B0%D0%B9%D0%BB%D0%B8)
   
   2.3. [Навігація по файловій системі]()
   
   2.4. [Запуск зовнішніх команд]()
   
   2.5. [Маніпуляція змінними середовища]()
   
3. [Приклади використання]()

   3.1. [Отримати список всіх файлів у директорії]()
   
   3.2. [Створення нового каталогу та запис файлу в нього]()
   
   3.3. [Отримання абсолютного шляху до файлу]()
   
   3.4. [Перевірка існування та видалення файлу]()
   
## 1. Імпорт модуля os
Для використання функцій модуля спочатку потрібно його імпортувати:

```python
import os
```
## 2. Основні функції модуля os
### 2.1. Робота з файлами та каталогами
Створення, перейменування, видалення файлів і директорій:

- os.mkdir(path) — створює новий каталог за вказаним шляхом.
```python
os.mkdir("new_directory")  # Створює каталог "new_directory"
```
- os.rename(src, dst) — перейменовує файл або каталог.
```python
os.rename("old_name.txt", "new_name.txt")  # Перейменовує файл
```
- os.remove(path) — видаляє файл.
```python
os.remove("file.txt")  # Видаляє файл "file.txt"
```
- os.rmdir(path) — видаляє порожній каталог.
```python
os.rmdir("empty_directory")  # Видаляє порожній каталог
```
- os.listdir(path) — повертає список файлів та директорій у вказаній директорії.
```python
files = os.listdir(".")  # Список файлів в поточному каталозі
```
Перевірка існування файлів та директорій:

- os.path.exists(path) — перевіряє, чи існує файл або каталог.
```python
if os.path.exists("file.txt"):
    print("Файл існує")
```
- os.path.isfile(path) — перевіряє, чи є шлях файлом.
```python
if os.path.isfile("file.txt"):
    print("Це файл")
```
- os.path.isdir(path) — перевіряє, чи є шлях директорією.
```python
if os.path.isdir("my_folder"):
    print("Це каталог")
```
### 2.2. Отримання інформації про файли
- os.path.getsize(path) — повертає розмір файлу в байтах.
```python
size = os.path.getsize("file.txt")
print(f"Розмір файлу: {size} байтів")
```
- os.path.abspath(path) — повертає абсолютний шлях до файлу.
```python
absolute_path = os.path.abspath("file.txt")
print(f"Абсолютний шлях: {absolute_path}")
```
- os.path.basename(path) — повертає базову назву файлу або каталогу.
```python
print(os.path.basename("/user/docs/file.txt"))  # Виведе "file.txt"
```
- os.path.dirname(path) — повертає шлях до каталогу файлу.
```python
print(os.path.dirname("/user/docs/file.txt"))  # Виведе "/user/docs"
```
### 2.3. Навігація по файловій системі
- os.getcwd() — повертає поточний робочий каталог.
```python
current_directory = os.getcwd()
print(f"Поточний каталог: {current_directory}")
```
- os.chdir(path) — змінює поточний робочий каталог.
```python
os.chdir("/new/directory")  # Змінює робочий каталог на "new_directory"
```
### 2.4. Запуск зовнішніх команд
- os.system(command) — виконує зовнішню команду операційної системи.
```python
os.system("ls -l")  # Виконає команду "ls -l" у терміналі Linux або Mac
```
### 2.5. Маніпуляція змінними середовища
- os.getenv(key) — отримує значення змінної середовища.
```python
home_dir = os.getenv("HOME")
print(f"Домашня директорія: {home_dir}")
```
- os.putenv(key, value) — встановлює значення змінної середовища (не рекомендується в нових версіях Python, використовуйте замість цього os.environ).
```python
os.environ["MY_VAR"] = "1234"
```
## 3. Приклади використання
### 3.1. Отримати список всіх файлів у директорії
```python
import os

# Список файлів у поточній директорії
files = os.listdir(".")
for file in files:
    print(file)
```
### 3.2. Створення нового каталогу та запис файлу в нього
```python
import os

# Створення нового каталогу
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")

# Запис файлу в новий каталог
with open("new_folder/new_file.txt", "w") as f:
    f.write("Hello, world!")
```  
### 3.3. Отримання абсолютного шляху до файлу
```python
import os

relative_path = "my_file.txt"
absolute_path = os.path.abspath(relative_path)
print(f"Абсолютний шлях: {absolute_path}")
```
### 3.4. Перевірка існування та видалення файлу
```python
import os

if os.path.exists("old_file.txt"):
    os.remove("old_file.txt")
    print("Файл видалено")
else:
    print("Файл не існує")
```
    
## Висновок

Модуль os — це потужний інструмент для роботи з файловою системою та операційною системою на низькому рівні. Він дозволяє маніпулювати файлами, каталогами, змінними середовища, виконувати системні команди та отримувати інформацію про файл або директорію.
