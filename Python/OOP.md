## Методи класу

- `__init__` - конструктор класу. Метод __init__ викликається щоразу під час створення нового екземпляра класу (об'єкта)

```python
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)

# prints "red"
```

- `__str__` керує тим, як ваш об'єкт буде перетворено у рядкове представлення для виводу

```python
  class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
print(honeycrisp)

# prints "an apple which is red and sweet"
```

- `__len__` повертає довжину об'єкта або колекції.

```python
  class FruitSalad:
    def __init__(self, size, fruits):
        self.size = size
        self.fruits = fruits

    def __len__(self):
        return len(self.fruits)
  my_salad = FruitSalad('large', ['apple', 'banana', 'cherry'])

  print(len(my_salad))
  # print "3"
```

- `__contains__` перевіряє, чи містить об'єкт елемент.

```python
class Player():
    def __init__(self, name):
        self.name=name

    def __contains__(self, substring):
        return substring in self.name

obj1=Player("Sam")
print ('am' in obj1)    ----> True
print ('ami' in obj1)   ----> False
```

- `__eq__` перевіряє, чи є два об'єкти рівними.

```python
  class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    
x = Person('Mike', 25)
y = Person('Sarah', 27)
z = Person('Mike', 25)

print(x==z)
```
