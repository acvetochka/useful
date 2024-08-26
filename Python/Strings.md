# Strings (Рядки)

## Операції з рядками

- len(string) - Повертає довжину рядка
```python
print(len("abcde"))         # prints 5
```

- for character in string - Ітерації над кожним символом рядка
```python
for c in "abcde":  print(c)                  # prints "a", then "b", then "c", etc.
```

- if substring in string - Перевіряє, чи підрядок є частиною рядка
```python
print("abc" in "abcde")     # prints True
print("def" in "abcde")     # prints False
```

- string[i] - Доступ до символу з індексом i рядка, починаючи з нуля
```python
print("abcde"[2])           # prints "c"
print("abcde"[-1])          # prints "e"
```

- string[i:j] - Отримує доступ до підрядка, починаючи з індексу i і закінчуючи індексом j мінус 1. Якщо i пропущено, його значення за замовчуванням дорівнює 0. Якщо j пропущено, Python повертає все, починаючи з i і до кінця рядка.
```python
print("abcde"[0:2])         # prints "ab"
print("abcde"[2:])          # prints "cde"
```

## Рядкові методи

- string.lower() - Повертає копію рядка з усіма малими літерами
```python
print("AaBbCcDdEe".lower())             # prints "aabbccddee"
```

- string.upper() - Повертає копію рядка з усіма великими символами
```python
print("AaBbCcDdEe".upper())             # prints "AABBCCDDEE"
```

- string.lstrip() - Повертає копію рядка з видаленими лівими пробілами
```python
print("   Hello   ".lstrip())           # prints "Hello   "
```

- string.rstrip() - Повертає копію рядка з видаленими пробілами з правого боку
```python
print("   Hello   ".rstrip())           # prints "   Hello"
```

- string.strip() - Повертає копію рядка з видаленими лівими та правими пробілами
```python
print("   Hello   ".strip())            # prints "Hello"
```

- string.count(substring)- Повертає кількість разів, які підрядок присутній у рядку
```python
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))               # prints 2
```

- string.isnumeric() - Повертає True, якщо рядок містить лише числові символи. Якщо ні, повертає False.
```python
print("12345".isnumeric())              # prints True
print("-123.45".isnumeric())            # prints False
```

- string.isalpha() - Повертає True, якщо рядок містить лише літери. Інакше повертає False.
```python
print("xyzzy".isalpha())                # prints True
```

- string.split() - Повертає список підрядків, які було розділено пропуском (пропуском може бути пробіл, табуляція або новий рядок)
```python
print(test.split())    # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
```

- string.split(delimiter) - Повертає список підрядків, які було розділено пропуском або іншим рядком
```python
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))                  # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
```

- string.replace(old, new) - Повертає новий рядок, у якому всі входження старого рядка замінено на новий.
```python
print(test.replace("wood", "plastic"))  # prints "How much plastic would a plasticchuck chuck"
```

- delimiter.join(list of strings) - Повертає новий рядок з усіма рядками, з'єднаними роздільником
```python
print("-".join(test.split()))           # prints "How-much-wood-would-a-woodchuck-chuck"
```

[Рядкові методи у документації Python](https://docs.python.org/3/library/stdtypes.html#string-methods)

