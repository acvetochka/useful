# ERRORS - Конспект по типам помилок і способам їх вирішення

[Типи помилок](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#%D1%82%D0%B8%D0%BF%D0%B8-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BE%D0%BA)

   - [1. Синтаксичні помилки (Syntax Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#1-%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%BD%D1%96-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-syntax-errors)

   - [2. Помилки під час виконання (Runtime Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#2-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-%D0%BF%D1%96%D0%B4-%D1%87%D0%B0%D1%81-%D0%B2%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D0%BD%D1%8F-runtime-errors)

   - [3. Логічні помилки (Logical Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#3-%D0%BB%D0%BE%D0%B3%D1%96%D1%87%D0%BD%D1%96-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-logical-errors)

   - [4. Індексаційні помилки (Index Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#4-%D1%96%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0%D1%86%D1%96%D0%B9%D0%BD%D1%96-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-index-errors)

   - [5. Типові помилки (Type Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#5-%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%96-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-type-errors)
   
   - [6. Помилки з файлами (File Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#6-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-%D0%B7-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0%D0%BC%D0%B8-file-errors)

   - [7. Помилки імпорту (Import Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#7-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-%D1%96%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D1%83-import-errors)

   - [8. Помилки доступу до змінних (Name Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#8-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D1%83-%D0%B4%D0%BE-%D0%B7%D0%BC%D1%96%D0%BD%D0%BD%D0%B8%D1%85-name-errors)

   - [9. Помилки пам'яті (Memory Errors)](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#9-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8-%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%96-memory-errors)

[Загальні стратегії вирішення помилок](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#%D0%B7%D0%B0%D0%B3%D0%B0%D0%BB%D1%8C%D0%BD%D1%96-%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D1%96%D1%97-%D0%B2%D0%B8%D1%80%D1%96%D1%88%D0%B5%D0%BD%D0%BD%D1%8F-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BE%D0%BA)

[Вбудовані винятки](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#%D0%B2%D0%B1%D1%83%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D1%96-%D0%B2%D0%B8%D0%BD%D1%8F%D1%82%D0%BA%D0%B8)

   - [1. ValueError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#1-valueerror)

   - [2. OSError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#2-oserror)

   - [3. TypeError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#3-typeerror)

   - [4. KeyError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#4-keyerror)

   - [5. IndexError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#5-indexerror)

   - [6. FileNotFoundError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#6-filenotfounderror)

   - [7. AttributeError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#7-attributeerror)

   - [8. ZeroDivisionError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#8-zerodivisionerror)

   - [9. NameError](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#9-nameerror)

   - [Як обробляти помилки](https://github.com/acvetochka/useful/blob/main/Python/Errors.md#%D1%8F%D0%BA-%D0%BE%D0%B1%D1%80%D0%BE%D0%B1%D0%BB%D1%8F%D1%82%D0%B8-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8)

## Типи помилок
У процесі програмування зустрічаються різні типи помилок. Розуміння цих помилок і вміння їх вирішувати є ключовими навичками для ефективного написання коду.

### 1. Синтаксичні помилки (Syntax Errors)
Опис:

- Ці помилки виникають, коли код написаний з порушенням правил синтаксису мови програмування.
- Наприклад, відсутність дужки, крапки з комою або неправильне використання операторів.

Приклади:

```python
# Помилка: відсутня дужка
print("Hello, world"
```

```python
# Помилка: неправильна синтаксична конструкція
if True
    print("Hello")
```

Як вирішити:
- Перевірте код на наявність пропущених або зайвих символів.
- Використовуйте підсвічування синтаксису в IDE, щоб легко знаходити помилки.
- Зверніть увагу на повідомлення інтерпретатора або компілятора — вони підказують місце і тип помилки.

### 2. Помилки під час виконання (Runtime Errors)
Опис:

- Помилки, що виникають під час виконання програми, хоча синтаксис був правильним. Вони можуть бути спричинені проблемами з вхідними даними, файлами, мережею або іншими зовнішніми факторами.
- Програма не в змозі продовжити виконання після виникнення такої помилки.

Приклади:
```python
# Помилка: ділення на нуль
x = 5 / 0
```
```python
# Помилка: звертання до невизначеної змінної
print(y)
```

Як вирішити:
- Використовуйте обробку виключень (exceptions), щоб передбачити і реагувати на можливі помилки під час виконання.
- Перевіряйте вхідні дані або ресурси на наявність потенційних проблем перед використанням.

Приклад обробки виключень:

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Не можна ділити на нуль!")
```

### 3. Логічні помилки (Logical Errors)
Опис:
- Ці помилки виникають, коли програма виконується без синтаксичних чи runtime помилок, але не дає правильного результату.
- Зазвичай такі помилки пов'язані з неправильним використанням алгоритмів або некоректною логікою умов.

Приклади:
```python
# Логічна помилка: неправильний оператор для пошуку мінімального значення
def find_min(a, b):
    if a > b:
        return a  # має бути return b
    else:
        return b
```

Як вирішити:
- Використовуйте інструменти для налагодження (debugging), щоб покроково проходити через код і знаходити помилки в логіці.
- Додавайте print() для виведення проміжних результатів або використовувати логування для відстеження роботи програми.
- Проводьте тестування різних варіантів вхідних даних, щоб виявити, коли результат не відповідає очікуванням.
  
### 4. Індексаційні помилки (Index Errors)
Опис:
- Помилки, що виникають при зверненні до елементів списку, масиву або рядка за індексом, який виходить за межі допустимого діапазону.

Приклад:
```python
# Помилка: індекс виходить за межі списку
lst = [1, 2, 3]
print(lst[3])  # Список містить лише елементи з індексами 0, 1, 2
```

Як вирішити:
- Перевіряйте довжину списків або рядків перед зверненням до їх елементів.
- Використовуйте конструкції на зразок if або циклів для запобігання виходу за межі.

```python
if len(lst) > 3:
    print(lst[3])
else:
    print("Елемент з таким індексом не існує")
```

### 5. Типові помилки (Type Errors)
Опис:
- Виникають, коли операції або функції застосовуються до об'єктів невідповідного типу.

Приклад:
```python
# Помилка: неможливо скласти рядок і число
x = "5" + 2
```

Як вирішити:
- Перевіряйте типи змінних перед виконанням операцій.
- Використовуйте явне перетворення типів, якщо необхідно.
```python
x = int("5") + 2  # Перетворюємо рядок у число
```

### 6. Помилки з файлами (File Errors)
Опис:
- Виникають при роботі з файлами, коли неможливо відкрити файл, бо його не існує, або коли немає прав доступу.

Приклад:
```python
# Помилка: файл не існує
with open("non_existent_file.txt", "r") as file:
    data = file.read()
```
Як вирішити:
- Перевіряйте наявність файлу перед його відкриттям.
- Використовуйте обробку виключень для запобігання аварійного завершення програми.
```python
import os

if os.path.exists("non_existent_file.txt"):
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
else:
    print("Файл не знайдено")
```

### 7. Помилки імпорту (Import Errors)
Опис:
- Виникають, коли Python не може знайти модуль для імпорту, через те, що модуль або не існує, або знаходиться не в доступному для Python шляхові.

Приклад:
```python
# Помилка: модуль не існує
import non_existent_module
```

Як вирішити:
- Перевірте, чи встановлений потрібний модуль.
- Переконайтеся, що шлях до модуля правильний або що він доданий у змінну PYTHONPATH.
- Використовуйте інструмент pip для встановлення сторонніх модулів.
```bash
pip install module_name
```

### 8. Помилки доступу до змінних (Name Errors)
Опис:
- Виникають, коли програма намагається звернутися до змінної, яка ще не визначена.

Приклад:
```python
# Помилка: змінна не визначена
print(my_variable)
```
Як вирішити:
- Переконайтеся, що всі змінні визначені перед їх використанням.
- Ініціалізуйте змінні перед тим, як їх використовувати в обчисленнях або умовах.
```python
my_variable = 10
print(my_variable)
```

### 9. Помилки пам'яті (Memory Errors)
Опис:

- Виникають, коли програма використовує більше пам'яті, ніж доступно в системі. Це може траплятися через неправильну обробку великих даних або цикли, що ніколи не завершуються.

Як вирішити:
- Оптимізуйте використання пам'яті, обробляючи дані частинами або використовуючи ефективні алгоритми.
- Використовуйте генератори замість списків для економії пам'яті.
- Визначайте та виправляйте нескінченні цикли, які можуть викликати витрати пам'яті.

### Загальні стратегії вирішення помилок:
- Використовуйте налагоджувач (debugger): Налагоджувачі дозволяють покроково виконувати програму, переглядати значення змінних і відстежувати логіку.

- Логування: Додавайте логування, щоб відстежувати поведінку програми та виявляти проблеми.

- Тестування: Пишіть модульні та інтеграційні тести для перевірки роботи коду з різними типами вхідних даних.

- Обробка виключень: Завжди обробляйте потенційні виключення для запобігання аварійному завершенню програми.

- Документація: Звертайтеся до офіційної документації мови або бібліотек для розуміння можливих помилок і їх вирішення.

## Вбудовані винятки

Python має багатий набір вбудованих винятків для обробки різних типів помилок. У цій частині розглянемо помилки типу ValueError, OSError, а також приклади їх виводу.

### 1. ValueError
Опис:

- Виникає, коли функція отримує аргумент правильного типу, але з некоректним значенням.
- Наприклад, ви намагаєтеся перетворити рядок, який не є числом, на число.

Приклад:
```python
# Виклик ValueError: не можна перетворити рядок "abc" на ціле число
try:
    number = int("abc")
except ValueError as e:
    print(f"Помилка значення: {e}")
```
Вивід:

```csharp
Помилка значення: invalid literal for int() with base 10: 'abc'
```

### 2. OSError
Опис:

- Це загальна помилка операційної системи, що виникає при роботі з файлами, каталогами, мережею або при інших операціях, що взаємодіють із системою.
- До підтипів цього винятку належать, наприклад, FileNotFoundError, PermissionError, IsADirectoryError.
Приклад:
```python
# Виклик OSError: файл не існує
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except OSError as e:
    print(f"Помилка операційної системи: {e}")
```
Вивід:

```arduino
Помилка операційної системи: [Errno 2] No such file or directory: 'non_existent_file.txt'
```
### 3. TypeError
Опис:
- Виникає, коли операція або функція застосовується до об'єкта невідповідного типу.
- Наприклад, спроба скласти рядок і число викличе цю помилку.

Приклад:
```python
# Виклик TypeError: додавання рядка і числа
try:
    result = "5" + 10
except TypeError as e:
    print(f"Помилка типу: {e}")
```
Вивід:

```python
Помилка типу: can only concatenate str (not "int") to str
```

### 4. KeyError
Опис:
- Виникає, коли намагаються звернутися до ключа у словнику, який не існує.
Приклад:
```python
# Виклик KeyError: ключа "age" немає в словнику
my_dict = {"name": "Alice"}
try:
    print(my_dict["age"])
except KeyError as e:
    print(f"Помилка ключа: {e}")
```
Вивід:

```arduino
Помилка ключа: 'age'
```
### 5. IndexError
Опис:
- Виникає, коли намагаються звернутися до елемента списку або іншого індексованого об'єкта за індексом, що виходить за межі його довжини.
Приклад:
```python
# Виклик IndexError: звернення до елемента з індексом, який виходить за межі списку
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print(f"Помилка індексу: {e}")
```
Вивід:

```sql
Помилка індексу: list index out of range
```
### 6. FileNotFoundError
Опис:
- Підтип OSError, виникає, коли Python не може знайти файл, який ви намагаєтеся відкрити.
Приклад:
```python
# Виклик FileNotFoundError: файл не знайдено
try:
    with open("missing_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    print(f"Файл не знайдено: {e}")
```
Вивід:

```arduino
Файл не знайдено: [Errno 2] No such file or directory: 'missing_file.txt'
```
### 7. AttributeError
Опис:
- Виникає, коли об'єкт не має атрибута або методу, до якого звертаються.
Приклад:
```python
# Виклик AttributeError: у числа немає атрибуту "append"
number = 42
try:
    number.append(5)
except AttributeError as e:
    print(f"Помилка атрибуту: {e}")
```
Вивід:

```csharp
Помилка атрибуту: 'int' object has no attribute 'append'
```
### 8. ZeroDivisionError
Опис:
- Виникає, коли намагаються поділити число на нуль.
Приклад:
```python
# Виклик ZeroDivisionError: ділення на нуль
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Помилка ділення на нуль: {e}")
```
Вивід:

```csharp
Помилка ділення на нуль: division by zero
```
### 9. NameError
Опис:
- Виникає, коли змінна або функція не визначені, але до них намагаються звернутися.
Приклад:
```python
# Виклик NameError: змінна не визначена
try:
    print(unknown_variable)
except NameError as e:
    print(f"Помилка імені: {e}")
```
Вивід:

```csharp
Помилка імені: name 'unknown_variable' is not defined
```

### Як обробляти помилки:
Для того щоб уникнути аварійного завершення програми та обробляти помилки коректно, рекомендується використовувати блоки try-except. Це дозволяє програмі реагувати на помилки і продовжувати виконання або надсилати користувачу корисну інформацію.

Приклад обробки кількох винятків:

```python
try:
    # Код, що може викликати кілька типів помилок
    with open("file.txt", "r") as file:
        data = file.read()
    number = int("abc")
except FileNotFoundError:
    print("Файл не знайдено.")
except ValueError:
    print("Неможливо перетворити рядок на число.")
except Exception as e:  # Загальна обробка всіх інших помилок
    print(f"Виникла непередбачена помилка: {e}")
```

Підсумок:

Python має безліч вбудованих винятків, що охоплюють різні типи помилок.
Кожен виняток має своє повідомлення, яке допомагає зрозуміти, що саме пішло не так.
Використовуйте блоки try-except для безпечного оброблення помилок і покращення надійності вашого коду.
  
