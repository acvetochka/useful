# Типи даних

## 1. Числові типи (Numeric Types)
### a. int (Ціле число)
Цілий тип даних, що представляє собою ціле число без дробової частини.

```python
x = 42
y = -15
```

### b. float (Число з плаваючою комою)
Тип даних для чисел з дробовою частиною.

```python
a = 3.14
b = -0.001
```

### c. complex (Комплексні числа)
Тип даних для комплексних чисел, які мають реальну і уявну частини.

```python
z = 1 + 2j
```

## 2. Строки (Strings)
Тип даних для роботи з текстовою інформацією.

```python
s1 = "Hello, world!"
s2 = 'Python'
s3 = """Можна використовувати
багаторядкові рядки"""
```

## 3. Логічні типи (Boolean)
Тип даних для представлення істинних і хибних значень.

```python
t = True
f = False
```

## 4. Списки (Lists)
Колекція змінюваних елементів, що зберігаються у визначеному порядку.

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, [4, 5]]
```

## 5. Кортежі (Tuples)
Колекція незмінюваних елементів, що зберігаються у визначеному порядку.

```python
point = (10, 20)
data = ("Alice", 30, "Engineer")
```

## 6. Множини (Sets)
Колекція унікальних елементів без певного порядку.

```python
Копіювати код
unique_numbers = {1, 2, 3, 4, 5}
letters = {'a', 'b', 'c'}
```

## 7. Словники (Dictionaries)
Колекція пар ключ-значення, де кожен ключ унікальний.

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

## 8. Байтові типи (Byte Types)
Типи даних для роботи з байтовими послідовностями.

### a. bytes
Незмінний тип даних, що представляє байти.

```python
b = b"hello"
```

### b. bytearray
Змінний тип даних для байтів.

```python
ba = bytearray([50, 100, 76])
```

### c. memoryview
Тип даних для доступу до байтових даних без копіювання.

```
data = bytearray(b"hello")
mv = memoryview(data)
```

## 9. Нічого (NoneType)
Тип даних, що представляє відсутність значення або "нічого".

```python
n = None
```

# Типи ітерабельних даних
| Feature by Data Structure |	Dictionary |	Set	| List |	String |	Tuple |
| --------------------------| -------------| ------ | ----- | ------- | -------- |
| Definition |	Stores key:value pairs |	An unordered collection of unique elements |	A sequential, mutable collection of any data type |	A sequential, immutable collection of textual data |	A sequential, immutable collection of any data type |
| Representation |	{ 'a':[42], 'b':[23,6,1] } |	{'^2', 'mc', ' equal', 'E'} |	[ 'a','b', 3, 4 ] |	“call me ishmael” |	( 'commander','lambda') |
| How to create? |	x = {}, x = dict()	| x = set()	| x = [], x = list() |	x = (), x = str() |	x = (‘a’,’b’,), x=tuple() |
| Is structure mutable and allow duplicate elements? |	immutable keys but mutable and duplicate values	| mutable but unique elements only |	mutable and allows duplicate elements| immutable but allows duplicate elements|	immutable but allows duplicate elements |
| Is the structure iterable? |	no, it is unordered and random |	no, it is unordered and unique |	yes, and with numeric index assignment |yes, but with a sequence of textual data |	yes, and with numeric index assignment |

# Визначення типів змінних
У Python типи змінних автоматично визначаються на основі значень, які їм присвоюються. Однак, Python також підтримує анотацію типів, яка дозволяє вказувати типи змінних, параметрів функцій і значень, які функції повертають. Це корисно для документування коду та для статичної перевірки типів за допомогою інструментів типу mypy.

Ось основні способи, як можна вказати типи змінних у Python:

## 1. Анотація типів змінних (Python 3.6+)
Анотації типів змінних використовуються для документування типів змінних, але не впливають на виконання коду. Це допомагає читачам коду та інструментам для статичної перевірки.

```s
age: int = 25
name: str = "Alice"
is_active: bool = True
```

## 2. Анотація типів у функціях
Анотації типів також використовуються для параметрів функцій і значень, які функції повертають.

### a. Параметри функцій
```
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### b. Типи значень, що повертаються
```
def add(x: int, y: int) -> int:
    return x + y
```

## 3. Використання стандартних модулів для типів (Python 3.5+)
Модулі typing та collections.abc надають типи для складніших структур даних.

### a. Списки
```
from typing import List

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)
```

### b. Кортежі
```
from typing import Tuple

def get_coordinates() -> Tuple[float, float]:
    return (1.0, 2.0)
```

### c. Словники
```
from typing import Dict

def get_person_info() -> Dict[str, str]:
    return {"name": "Alice", "age": "30"}
```

### d. Множини
```
from typing import Set

def unique_items(items: Set[str]) -> Set[str]:
    return items
```

## 4. Альтернативні типи (Union) і Опціональні типи (Optional)
Іноді змінна може мати кілька можливих типів.

```
from typing import Union, Optional

def process_value(value: Union[int, str]) -> str:
    return str(value)

def find_item(index: int) -> Optional[str]:
    items = ["apple", "banana", "cherry"]
    if 0 <= index < len(items):
        return items[index]
    return None
```

## 5. Генерики (Generics)
Модуль typing також дозволяє створювати типи, які можуть бути параметризовані іншими типами.

```
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Wrapper(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

int_wrapper = Wrapper 
str_wrapper = Wrapper[str]("hello")
```

## Підсумок
Анотації типів у Python забезпечують спосіб документування типів даних і допомагають у статичній перевірці коду, але не є обов’язковими для виконання програми. Вони забезпечують більш чітке і зрозуміле API для вашого коду і можуть бути корисні при роботі з великими проектами та командною розробкою.

