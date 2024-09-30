# Конспект по регулярним виразам (regex) у Python

Регулярні вирази (regex) — це потужний інструмент для пошуку і маніпуляції з текстом. У Python їх можна використовувати за допомогою модуля re. Вони дозволяють виконувати пошук за шаблоном у рядках.

## Зміст

I. Re
- [Основні функції модуля re](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8F-re)
- [Спеціальні символи в регулярних виразах](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D1%81%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D0%B8%D1%85-%D0%B2%D0%B8%D1%80%D0%B0%D0%B7%D0%B0%D1%85)
- [Квантифікатори](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BA%D0%B2%D0%B0%D0%BD%D1%82%D0%B8%D1%84%D1%96%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D0%B8)
- [Групування та альтернативи](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%B3%D1%80%D1%83%D0%BF%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F-%D1%82%D0%B0-%D0%B0%D0%BB%D1%8C%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%82%D0%B8%D0%B2%D0%B8)
- [Екранізація спеціальних символів](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F-%D1%81%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D1%85-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%96%D0%B2)
- [Приклади регулярних виразів](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%B8-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D0%B8%D1%85-%D0%B2%D0%B8%D1%80%D0%B0%D0%B7%D1%96%D0%B2)
- [Корисні посилання](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D0%BD%D1%96-%D0%BF%D0%BE%D1%81%D0%B8%D0%BB%D0%B0%D0%BD%D0%BD%D1%8F)

II. [Основи використання grep](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D0%BD%D1%8F-grep)
- [Приклади використання grep](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D0%BD%D1%8F-grep)
- [Ключові опції grep](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BA%D0%BB%D1%8E%D1%87%D0%BE%D0%B2%D1%96-%D0%BE%D0%BF%D1%86%D1%96%D1%97-grep)
- [Використання з регулярними виразами](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D0%BD%D1%8F-%D0%B7-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D0%B8%D0%BC%D0%B8-%D0%B2%D0%B8%D1%80%D0%B0%D0%B7%D0%B0%D0%BC%D0%B8)
- [Корисні приклади](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D0%BD%D1%96-%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%B8)


## Основні функції модуля re

У модулі re (регулярні вирази) Python є кілька корисних методів для роботи з результатами пошуку.

1️⃣ `search()`

Шукає перше входження шаблону в рядку і повертає об'єкт матчу або None, якщо збіг не знайдено.

Синтаксис:
```python
re.search(pattern, string)
```

Приклад:
```python
import re
result = re.search(r'\d+', 'Hello 123 World')  # Шукає перше число
print(result.group())  # Виведе: 123
```

2️⃣ `group()`

Метод group() повертає частину рядка, яка відповідає шаблону регулярного виразу.

Синтаксис:
```python
result.group([group_number])
```

Якщо викликати без аргументів — повертає весь збіг.

Якщо передати число — повертає відповідну групу (див. приклад нижче).

Приклад:
```python
import re
result = re.search(r'(\d{3})-(\d{2})-(\d{4})', 'My number is 123-45-6789')
print(result.group())    # Весь збіг: '123-45-6789'
print(result.group(1))   # Перша група: '123'
print(result.group(2))   # Друга група: '45'
print(result.group(3))   # Третя група: '6789'
```

3️⃣ `groups()`

Метод groups() повертає всі захоплені групи як кортеж.

Синтаксис:
```python
result.groups()
```

Приклад:
```python
import re
result = re.search(r'(\d{3})-(\d{2})-(\d{4})', 'My number is 123-45-6789')
print(result.groups())   # ('123', '45', '6789')
```

4️⃣ `start()` та `end()`

Ці методи використовуються для визначення позиції початку і кінця знайденого збігу або групи в рядку.

Синтаксис:
```python
result.start([group_number])
result.end([group_number])
```

Без аргументів повертають позиції початку і кінця всього збігу.

Якщо вказати номер групи, повертають позиції відповідної групи.

Приклад:
```python
import re
result = re.search(r'(\d{3})-(\d{2})-(\d{4})', 'My number is 123-45-6789')
print(result.start())    # 11 (початок всього збігу)
print(result.end())      # 22 (кінець всього збігу)
print(result.start(1))   # 11 (початок першої групи)
print(result.end(1))     # 14 (кінець першої групи)
```

5️⃣ `span()`

Метод span() повертає кортеж з двох значень: початок і кінець збігу (аналогічно до start() і end(), але в одному методі).

Синтаксис:
```python
result.span([group_number])
```

Приклад:
```python
import re
result = re.search(r'(\d{3})-(\d{2})-(\d{4})', 'My number is 123-45-6789')
print(result.span())     # (11, 22) для всього збігу
print(result.span(1))    # (11, 14) для першої групи
```

6️⃣ `match()`

Метод match() перевіряє, чи відповідає рядок регулярному виразу з самого початку.

Синтаксис:
```python
re.match(pattern, string)
```

Приклад:
```python
import re
result = re.match(r'\d+', '123abc')
print(result.group())   # '123'
```

Але якщо рядок починається не з числа:
```python
result = re.match(r'\d+', 'abc123')
print(result)           # None
```

7️⃣ `findall()`

Метод findall() повертає список всіх збігів у рядку. Якщо є захоплюючі групи, повертає список груп.

Синтаксис:
```python
re.findall(pattern, string)
```

Приклад:

```python
import re
result = re.findall(r'\d+', 'There are 3 cats, 4 dogs, and 5 birds.')
print(result)    # ['3', '4', '5']
```

8️⃣ `finditer()`

Метод finditer() повертає ітератор з усіма збігами. Кожен елемент — це об'єкт MatchObject, який дозволяє отримати більше інформації про кожен збіг.

Синтаксис:
```python
re.finditer(pattern, string)
```

Приклад:
```python
import re
result = re.finditer(r'\d+', 'There are 3 cats, 4 dogs, and 5 birds.')
for match in result:
    print(match.group(), match.start(), match.end())
```

9️⃣ `split()`

Розбиває рядок за шаблоном.

Синтаксис:
```python
re.split(pattern, string)
```

Приклад:
```python
result = re.split(r'\s+', 'Hello   World')  # Розбиває рядок за пробілами
print(result)  # Виведе: ['Hello', 'World']
```

1️⃣0️⃣ `sub()`

Метод sub() використовується для заміни всіх збігів в рядку на вказаний текст.

Синтаксис:
```python
re.sub(pattern, replacement, string)
```

Приклад:
```python
import re
result = re.sub(r'\d+', 'X', 'There are 3 cats, 4 dogs, and 5 birds.')
print(result)    # 'There are X cats, X dogs, and X birds.'
```

Метод `re.sub()` можна використовувати для заміни частин рядка з використанням захоплюючих груп у регулярних виразах. При цьому можна звертатися до цих груп за допомогою спеціальних позначень, таких як \1, \2, і так далі. Це дозволяє робити заміни, використовуючи частини самого рядка.

Синтаксис:
```python
re.sub(pattern, replacement, string)
```
`pattern` — регулярний вираз із захоплюючими групами.

`replacement` — рядок, на який треба замінити збіг, із посиланнями на групи за допомогою \1, \2, і т.д.

`string` — рядок, у якому відбувається пошук і заміна.

📝 Приклади:

1. Зміна формату імені

```python
import re

text = "Doe, John; Smith, Alice; Black, Bob"

# Використовуємо захоплюючі групи: (\w+) для імені та прізвища
result = re.sub(r'(\w+), (\w+)', r'\2 \1', text)

print(result)  # Результат: 'John Doe; Alice Smith; Bob Black'
```

Пояснення:

Регулярний вираз (\w+), (\w+) має дві захоплюючі групи:

Перша група `(\w+)` захоплює прізвище.

Друга група `(\w+)` захоплює ім'я.

У рядку для заміни r'\2 \1', ми посилаємося на групи:

`\2` — це ім'я (друга група).

`\1` — це прізвище (перша група).

Таким чином, прізвище та ім'я міняються місцями.

2. Зміна формату (порядку) чисел

```python
import re

text = "12-34, 56-78, 90-12"

# Захоплюючі групи для чисел перед і після тире
result = re.sub(r'(\d+)-(\d+)', r'\2\1', text)

print(result)  # Результат: '3412, 7856, 1290'
```

Пояснення:

Регулярний вираз (\d+)-(\d+) захоплює числа перед та після тире.

У заміні r'\2\1', групи міняються місцями, отримуючи новий порядок чисел без тире.

## Спеціальні символи в регулярних виразах:
`.` — будь-який символ, окрім символу нового рядка.

```python
re.search(r'H.llo', 'Hello')  # Поверне збіг
```

`^` — початок рядка.

```python
re.search(r'^Hello', 'Hello World')  # Поверне збіг
```

`$` — кінець рядка.

```python
re.search(r'World$', 'Hello World')  # Поверне збіг
```

`\d` — будь-яка цифра.

```python
re.findall(r'\d+', '123 apples')  # Знайде: ['123']
```

`\w` — будь-який буквений символ або цифра (алфавіт + цифри).

```python
re.findall(r'\w+', 'Hello 123!')  # Знайде: ['Hello', '123']
```

`\s` — будь-який пробільний символ (пробіл, табуляція, новий рядок).

```python
re.split(r'\s+', 'Hello   World')  # Розіб'є на ['Hello', 'World']
```

## Квантифікатори:
Квантифікатори в регулярних виразах (regex) визначають, скільки разів певний елемент (символ або група символів) має зустрічатися в рядку, щоб вважатися збігом. Давайте розберемо кожен квантифікатор докладніше з прикладами, щоб було зрозуміло, як вони працюють.

`*` — 0 або більше повторень

Цей квантифікатор вказує, що символ може зустрічатися будь-яку кількість разів, включаючи 0 разів.

Приклад:
```python
import re

# Шукає 'ab', після якого йде будь-яка кількість символів 'c' (0 або більше)
result = re.search(r'abc*', 'ab')
print(result.group())  # Виведе: 'ab', бо 'c' може бути 0 разів

result = re.search(r'abc*', 'abcc')
print(result.group())  # Виведе: 'abcc', бо 'c' зустрічається 2 рази
```

abc* означає, що після ab може йти 0 або більше символів c. У першому випадку збігається просто ab, а в другому — abcc.

`+` — 1 або більше повторень

Цей квантифікатор вимагає, щоб символ зустрічався принаймні один раз, але може бути і більше.

Приклад:
```python
import re

# Шукає 'ab', після якого йде хоча б один символ 'c'
result = re.search(r'abc+', 'ab')
print(result)  # Виведе: None, бо 'c' не зустрічається

result = re.search(r'abc+', 'abc')
print(result.group())  # Виведе: 'abc', бо 'c' зустрічається 1 раз

result = re.search(r'abc+', 'abcccc')
print(result.group())  # Виведе: 'abcccc', бо 'c' зустрічається більше 1 раз
```

abc+ означає, що після ab повинен бути хоча б один символ c.

`?` — 0 або 1 повторення

Цей квантифікатор означає, що символ може зустрічатися або один раз, або взагалі не зустрічатися.

Приклад:
```python
import re

# Шукає 'ab', після якого може бути або 1, або 0 символів 'c'
result = re.search(r'abc?', 'ab')
print(result.group())  # Виведе: 'ab', бо 'c' може бути 0 разів

result = re.search(r'abc?', 'abc')
print(result.group())  # Виведе: 'abc', бо 'c' зустрічається 1 раз
```

abc? означає, що після ab може бути 0 або 1 символ c.

`{n}` — рівно n повторень

Цей квантифікатор задає точну кількість повторень символу.

Приклад:
```python
import re

# Шукає рівно три символи 'a'
result = re.search(r'a{3}', 'aa')
print(result)  # Виведе: None, бо є тільки 2 'a'

result = re.search(r'a{3}', 'aaa')
print(result.group())  # Виведе: 'aaa', бо є рівно 3 'a'

result = re.search(r'a{3}', 'aaaa')
print(result.group())  # Виведе: 'aaa', бо квантифікатор шукає рівно 3 символи 'a'
```

a{3} шукає рівно 3 символи a. Навіть якщо в рядку більше символів, буде знайдено тільки 3.

`{n,}` — не менше n повторень

Цей квантифікатор означає, що символ має зустрічатися принаймні n разів, але може і більше.

Приклад:
```python
import re

# Шукає принаймні три символи 'a'
result = re.search(r'a{3,}', 'aa')
print(result)  # Виведе: None, бо є тільки 2 'a'

result = re.search(r'a{3,}', 'aaa')
print(result.group())  # Виведе: 'aaa', бо є рівно 3 'a'

result = re.search(r'a{3,}', 'aaaa')
print(result.group())  # Виведе: 'aaaa', бо є більше 3 'a'
```

a{3,} означає, що має бути принаймні 3 символи a, але допускається більше.

`{n,m}` — від n до m повторень

Цей квантифікатор визначає діапазон кількості повторень символу — мінімум n і максимум m.

Приклад:
```python
import re

# Шукає від 2 до 4 символів 'a'
result = re.search(r'a{2,4}', 'a')
print(result)  # Виведе: None, бо є тільки 1 'a'

result = re.search(r'a{2,4}', 'aa')
print(result.group())  # Виведе: 'aa', бо є 2 'a'

result = re.search(r'a{2,4}', 'aaaaa')
print(result.group())  # Виведе: 'aaaa', бо обмеження до 4 символів
```

a{2,4} означає, що має бути від 2 до 4 символів a. Якщо в рядку більше 4 символів, буде знайдено тільки перші 4.

🔚 Підсумок:

`*` — 0 або більше повторень.

`+` — 1 або більше повторень.

`?` — 0 або 1 повторення.

`{n}` — рівно n повторень.

`{n,}` — не менше n повторень.

`{n,m}` — від n до m повторень.

Квантифікатори допомагають уточнити, скільки разів повинен зустрічатися певний елемент у рядку, щоб його можна було вважати збігом із шаблоном регулярного виразу.

## Групування та альтернативи:
`|` — або (альтернатива).

```python
re.search(r'cat|dog', 'dog')  # Знайде: 'dog'
```

`( )` — групування.

```python
re.search(r'(ab)+', 'abab')  # Знайде: 'abab'
```
### Захоплюючі групи
result[1], result[2] та інші подібні вирази використовуються для доступу до захоплених (captured) груп при використанні методу re.search() у Python. Давайте розглянемо це детальніше.

📋 Основна ідея:

`re.search()` шукає перший збіг з регулярним виразом у рядку.
Якщо шаблон має захоплюючі групи (тобто підшаблони, взяті у дужки ()), то результат пошуку (result) буде містити ці групи.
Кожна захоплена група може бути доступною через індекси, починаючи з 1 (оскільки 0 індексується як весь збіг, а не окремі групи).

📝 Приклад:
```python
import re

# Створюємо рядок та шаблон з групами
string = "My phone number is 123-456-7890"
pattern = r"My phone number is (\d{3})-(\d{3})-(\d{4})"

# Використовуємо re.search() для пошуку збігу
result = re.search(pattern, string)

# Виводимо результат
print(result[0])  # Повний збіг: "My phone number is 123-456-7890"
print(result[1])  # Перша захоплена група: "123"
print(result[2])  # Друга захоплена група: "456"
print(result[3])  # Третя захоплена група: "7890"
```

Що відбувається в цьому коді:

Шаблон: r"My phone number is (\d{3})-(\d{3})-(\d{4})"

`(\d{3})` — захоплює три цифри як першу групу.

`(\d{3})` — друга група.

`(\d{4})` — третя група.

`result[0]`: Повертає весь рядок, що відповідає шаблону (весь збіг): "My phone number is 123-456-7890".

`result[1]`: Повертає першу захоплену групу — "123".

`result[2]`: Повертає другу захоплену групу — "456".

`result[3]`: Повертає третю захоплену групу — "7890".

❓ Що таке захоплюючі групи:

Коли у регулярному виразі використовуються дужки (), Python захоплює частини рядка, які відповідають вмісту дужок.
Кожна група отримує свій індекс (починаючи з 1).

📝 Приклад без груп:

Якщо шаблон не містить захоплюючих груп, result[1], result[2] будуть недоступні, і при спробі звернутися до них Python викличе помилку.

```python
# Шаблон без захоплюючих груп
pattern = r"My phone number is \d{3}-\d{3}-\d{4}"
result = re.search(pattern, string)

# Тут не можна використовувати result[1] або result[2], тому що немає груп
print(result[0])  # Повертає весь рядок, що відповідає: "My phone number is 123-456-7890"
```

💡 Важливо:

`result[0]` — завжди повертає весь збіг, тобто те, що знайдено відповідно до всього регулярного виразу.

`result[1]`, `result[2]`, і т.д. — повертають відповідні групи (якщо вони є) в порядку їх появи у шаблоні.

Таким чином, захоплюючі групи дозволяють витягувати частини рядка, що відповідають певним частинам регулярного виразу.

## Екранізація спеціальних символів:
Якщо потрібно шукати спеціальні символи, їх треба екранувати за допомогою \.

```python
re.search(r'\.', 'www.example.com')  # Знайде: '.'
```

Практичний приклад:
```python
import re

text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(emails)  # Виведе: ['support@example.com', 'sales@example.com']
```
Цей приклад знаходить усі email-адреси в тексті.

## Приклади регулярних виразів
`r”\d{3}-\d{3}-\d{4}”`   Цей рядок коду відповідає номерам телефонів у США у форматі 111-222-3333.


`r”^-?\d*(\.\d+)?$”`  Цей рядок коду відповідає будь-якому додатному чи від’ємному числу з десятковими знаками чи без них.


`r”^(.+)\/([^\/]+)\/”` Цей рядок коду відповідає будь-якому шляху та імені файлу.


## Корисні посилання
Іноді регулярні вирази можуть бути складними, їх важко прочитати та зрозуміти — навіть для досвідчених програмістів! Є інструменти, які допоможуть розбити регулярний вираз і пояснити, що робить кожна частина виразу. Загальний інструмент, який можна використовувати, щоб допомогти зрозуміти кожен етап регулярного виразу:

[regex101](https://regex101.com/)

Регулярні вирази пропонують програмістам потужні можливості, але часом вони можуть бути складними та важкими для розуміння. Чим більше ви кодуєте регулярні вирази, тим зручніше вам буде їх використовувати та розуміти. Щоб дізнатися більше про регулярний вираз, перегляньте такі посилання:

[Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

[re-library](https://docs.python.org/3/library/re.html)

[greedy-versus-non-greedy](https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy)


# Основи використання grep

`grep` (Global Regular Expression Print) — це потужна утиліта командного рядка в операційних системах на основі Unix (Linux, macOS), яка використовується для пошуку тексту в файлах за допомогою регулярних виразів або простих рядків. Вона виводить рядки, які відповідають вказаному шаблону.


📋 Основний синтаксис:

```bash
grep [опції] шаблон файл
```

### Приклади використання grep:
- Простий пошук рядка:

```bash
grep "text" filename.txt
```
Ця команда виведе всі рядки у файлі filename.txt, які містять слово "text".

- Реєстронезалежний пошук (`-i`):

```bash
grep -i "text" filename.txt
```
Пошук слова "text" без врахування регістру. Збігатимуться як "Text", так і "TEXT".

- Пошук за допомогою регулярних виразів (`-E`):

```bash
grep -E "text[0-9]+" filename.txt
```
Це команда для пошуку рядків, які містять слово "text", за яким йдуть одна або більше цифр (наприклад, text1, text123).

- Пошук точного слова (`-w`):

```bash
grep -w "text" filename.txt
```
Ця команда знайде тільки точні збіги для слова "text", але не "textual" або "context".

- Пошук у всіх файлах у поточній директорії:

```bash
grep "text" *
```
Пошук всіх рядків, що містять "text", у всіх файлах поточної директорії.

- Пошук у підкаталогах (`-r`):

```bash
grep -r "text" /path/to/directory
```
Рекурсивний пошук у всіх файлах і підкаталогах заданого каталогу.

- Виведення рядків без збігів (`-v`):

```bash
grep -v "text" filename.txt
```
Виводить усі рядки у файлі filename.txt, які не містять "text".

- Підрахунок кількості збігів (`-c`):

```bash
grep -c "text" filename.txt
```
Виводить кількість рядків у файлі, які містять слово "text".

- Виведення номерів рядків (`-n`):

```bash
grep -n "text" filename.txt
```
Показує номер рядка разом з рядком, де було знайдено "text".

- Ігнорування бінарних файлів:

```bash
grep --binary-files=without-match "text" *
```
Ігнорує бінарні файли та не показує їх у результатах пошуку.

### Ключові опції grep:

`-i` — реєстронезалежний пошук.

`-r` — рекурсивний пошук у каталогах.

`-v` — виводить рядки, що не відповідають шаблону.

`-n` — виводить номери рядків.

`-c` — підраховує кількість рядків зі збігами.

`-w` — шукає точне слово.

`-E` — використовує розширені регулярні вирази.

### Використання з регулярними виразами:
Початок рядка (`^`):

```bash
grep "^start" filename.txt
```
Знайде всі рядки, які починаються зі слова "start".

Кінець рядка (`$`):

```bash
grep "end$" filename.txt
```
Знайде всі рядки, які закінчуються на слово "end".

Будь-який один символ (`.`):

```bash
grep "c.t" filename.txt
```
Знайде слова на зразок "cat", "cot", "cut" і так далі.

Альтернативи (`|`):

```bash
grep -E "cat|dog" filename.txt
```
Шукає рядки, що містять або "cat", або "dog".

Групування (`()`):

```bash
grep -E "(cat|dog)s" filename.txt
```
Шукає слова "cats" або "dogs".

### Корисні приклади:
Пошук усіх рядків, що містять цифри:

```bash
grep '[0-9]' filename.txt
```
Пошук порожніх рядків:

```bash
grep '^$' filename.txt
```

🔚 Висновок:
grep — це надзвичайно потужний інструмент для пошуку тексту з використанням як простих шаблонів, так і складних регулярних виразів. Залежно від вимог, ви можете використовувати різні опції для роботи з файлами, папками та навіть для пошуку всередині системних журналів чи великих баз даних текстової інформації.