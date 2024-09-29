# Testing

Тестування в Python — це процес перевірки правильності та працездатності коду, який допомагає виявити помилки, баги та забезпечити якість програмного забезпечення. Найпоширенішим інструментом для тестування в Python є модуль unittest, але також використовуються інші бібліотеки, такі як pytest та nose.

Основні концепти тестування:

## 1. Модульне тестування (Unit Testing)
Модульне тестування — це тестування окремих модулів чи функцій програми. Це дозволяє перевірити, чи працює кожна частина програми незалежно від інших.

`unittest` — стандартна бібліотека Python для модульного тестування, подібна до бібліотек у інших мовах, таких як JUnit у Java чи NUnit у C#.
Простий приклад використання unittest:

```python
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

Основні методи unittest:

`assertEqual(a, b)` — перевірка на рівність a та b.

`assertTrue(x)` — перевірка, що значення x є істинним.

`assertFalse(x)` — перевірка, що значення x є хибним.

`assertRaises(Exception, func, *args)` — перевірка, що функція func викликає виключення типу Exception.

## 2. Інтеграційне тестування
   
Інтеграційне тестування — це тестування взаємодії між кількома модулями чи компонентами системи, щоб переконатися, що вони працюють разом правильно.

Приклад інтеграційного тестування:

```python
def connect_to_db():
    # Імітація з'єднання з базою даних
    return True

def get_data():
    if connect_to_db():
        return {"name": "John", "age": 30}

class TestIntegration(unittest.TestCase):

    def test_get_data(self):
        data = get_data()
        self.assertEqual(data["name"], "John")
        self.assertEqual(data["age"], 30)
```

## 3. Mocking (Мокація)
   
Mocking дозволяє імітувати поведінку об'єктів чи функцій, які використовуються у коді, щоб ізолювати тестований компонент від зовнішніх залежностей (наприклад, баз даних, мережевих запитів).

Модуль unittest.mock дозволяє створювати мок-об'єкти.

```python
from unittest.mock import patch

class TestMocking(unittest.TestCase):

    @patch('module_name.connect_to_db')
    def test_mocking(self, mock_connect):
        mock_connect.return_value = False
        result = get_data()
        self.assertIsNone(result)
```

## 4. Тестування з використанням бібліотеки pytest
pytest — це потужна альтернатива unittest, яка має простіший синтаксис і дозволяє виконувати тести більш ефективно.

Простий приклад:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
```

Команда для запуску тестів з pytest:

```bash
pytest
```

## 5. Параметризовані тести
pytest дозволяє запускати параметризовані тести, де один і той самий тест виконується з різними наборами даних.

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## 6. Безперервна інтеграція (CI)
CI-тестування — це автоматизація процесу тестування під час кожного внесення змін у коді. Для цього часто використовуються інструменти на зразок Jenkins, Travis CI або GitHub Actions. Тести запускаються автоматично при кожному коміті чи пул-реквесті.

## 7. Покриття коду тестами
Інструменти на зразок coverage.py дозволяють виміряти, який відсоток коду покрито тестами:

```bash
pip install coverage
coverage run -m pytest
coverage report -m
```

Основні переваги тестування:
- Виявлення помилок на ранніх етапах розробки.
- Підвищення стабільності і якості коду.
- Полегшення внесення змін у код (рефакторинг) з упевненістю, що основні функції працюють коректно.
  
Тестування в Python — важливий процес, який допомагає забезпечити надійність та ефективність програмного забезпечення.
