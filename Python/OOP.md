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

- Метод `__repr__` повертає більш насичене інформацією, або офіційне, рядкове представлення об’єкта.

```python
class Ocean:
    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age
    
    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'

c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))

# prints str- The creature type is Jellyfish and the age is 5
# prints repr- Ocean('Jellyfish', 5)
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

- `__eq__` перевіряє, чи є два об'єкти рівними (визначає поведінку рівності)

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

- `__ne__(self, other)` - Визначає поведінку оператора нерівності!=
```python
class Person:
    def __init__(self, age):
        self.age = age

    def __ne__(self, other):
        return self.age != other.age


alice = Person(18)
bob = Person(19)
carl = Person(18)

print(alice != bob)
# True

print(alice != carl)
# False
```

- `__lt__(self, other)` - Визначає поведінку оператора менше ніж<

```python
class GFG: 
    def __init__(self, Marks): 
        self.Marks = Marks 
    def __lt__(self, marks): 
          return self.Marks < marks.Marks 
  
student1_marks = GFG(90) 
student2_marks = GFG(88) 
  
print(student1_marks < student2_marks)
# False

print(student2_marks < student1_marks)
# True
```

- `__gt__(self, other)` - Визначає поведінку оператора більшого>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
        
if __name__ == "__main__":
    simone = Person('Simone', 20)
    karl = Person('Karl', 33)
    anna = Person('Anna', 55)
    print(f'Compare people: {karl > simone}')  # True
    print(f'Compare people: {simone > anna}')  # False
```

- `__le__(self, other)` - Визначає поведінку оператора менше або рівно<=

```python
class Person:
    def __init__(self, age):
        self.age = age
    def __le__(self, other):
        return self.age <= other.age
alice = Person(18)
bob = Person(17)
carl = Person(18)
print(alice <= bob)
# False
print(alice <= carl)
# True
print(bob <= alice)
# True
```

- `__ge__(self, other)` - Визначає поведінку оператора «більше або рівно».>=

```python
class Person:
    def __init__(self, age):
        self.age = age

    def __ge__(self, other):
        return self.age >= other.age

alice = Person(18)
bob = Person(17)
carl = Person(18)

print(alice >= bob)
# True

print(alice >= carl)
# True

print(bob >= alice)
# False
```
