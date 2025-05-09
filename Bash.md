# Конспект по Bash скриптам

## Зміст

[1. Що таке Bash скрипт](https://github.com/acvetochka/useful/blob/main/Bash.md#1-%D1%89%D0%BE-%D1%82%D0%B0%D0%BA%D0%B5-bash-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82)

[2. Створення та виконання Bash скриптів](https://github.com/acvetochka/useful/blob/main/Bash.md#2-%D1%81%D1%82%D0%B2%D0%BE%D1%80%D0%B5%D0%BD%D0%BD%D1%8F-%D1%82%D0%B0-%D0%B2%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D0%BD%D1%8F-bash-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D1%96%D0%B2)

[3. Змінні](https://github.com/acvetochka/useful/blob/main/Bash.md#3-%D0%B7%D0%BC%D1%96%D0%BD%D0%BD%D1%96)

[4. Основні команди](https://github.com/acvetochka/useful/blob/main/Bash.md#4-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8)

[5. Цикли](https://github.com/acvetochka/useful/blob/main/Bash.md#5-%D1%86%D0%B8%D0%BA%D0%BB%D0%B8)

[6. Умовні оператори](https://github.com/acvetochka/useful/blob/main/Bash.md#6-%D1%83%D0%BC%D0%BE%D0%B2%D0%BD%D1%96-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8)

[7. Функції](https://github.com/acvetochka/useful/blob/main/Bash.md#7-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97)

[8. Редирекція та канали](https://github.com/acvetochka/useful/blob/main/Bash.md#8-%D1%80%D0%B5%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%86%D1%96%D1%8F-%D1%82%D0%B0-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8)

[9. Корисні команди Bash](https://github.com/acvetochka/useful/blob/main/Bash.md#9-%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D0%BD%D1%96-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8-bash)

[10. Коментарі](https://github.com/acvetochka/useful/blob/main/Bash.md#10-%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D1%96)

[11. Режими налагодження](https://github.com/acvetochka/useful/blob/main/Bash.md#11-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B8-%D0%BD%D0%B0%D0%BB%D0%B0%D0%B3%D0%BE%D0%B4%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F)

[12. Обробка помилок](https://github.com/acvetochka/useful/blob/main/Bash.md#12-%D0%BE%D0%B1%D1%80%D0%BE%D0%B1%D0%BA%D0%B0-%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BE%D0%BA)

[13. Корисні оператори](https://github.com/acvetochka/useful/blob/main/Bash.md#13-%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D0%BD%D1%96-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8)


## 1. Що таке Bash скрипт
Bash скрипт — це текстовий файл, який містить послідовність команд, що виконуються оболонкою Bash у Linux/Unix системах. Сценарії використовуються для автоматизації задач, керування системою та написання програм.

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 2. Створення та виконання Bash скриптів
Створення скрипта: Використовуйте будь-який текстовий редактор (наприклад, nano, vim):
```bash
nano script.sh
```
Шебанг: Кожен скрипт повинен починатися з шебанга, щоб вказати інтерпретатор:
```bash
#!/bin/bash
```
Виконання скрипта:
- Надати права на виконання:
```bash
chmod +x script.sh
```
- Запустити скрипт:
```bash
./script.sh
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 3. Змінні
Оголошення змінних:

```bash
my_var="Hello, World"
```

Щоб використовувати змінну, ставте перед її назвою символ $:

```bash
echo $my_var
```

Отримання змінної з аргументу командного рядка:

```bash
$1, $2, ...  # доступ до аргументів
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 4. Основні команди
- Ехо для виведення:

```bash
echo "Text to output"
```

Операції з файлами:

- Створити порожній файл:
```bash
touch filename.txt
```

- Переміщення/перейменування файлу:
```bash
mv oldname.txt newname.txt
```

- Копіювання файлу:
```bash
cp file.txt /destination/
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 5. Цикли
- `for`:

```bash
for item in list; do
  # команди
done
```
Приклад:

```bash
for i in {1..5}; do
  echo "Number: $i"
done
```

- `while`:

```bash
while [ condition ]; do
  # команди
done
```

- `until`: Виконується, поки умова хибна:

```bash
until [ condition ]; do
  # команди
done
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 6. Умовні оператори
- if-else:

```bash
if [ condition ]; then
  # команди
elif [ condition ]; then
  # команди
else
  # команди
fi
```
Приклад:

```bash
if [ -f myfile.txt ]; then
  echo "File exists"
else
  echo "File does not exist"
fi
```

Пояснення

`if`: Це початок умовного виразу. Команда перевіряє умову, що слідує за ним.

`[`: Це команда `test`, яка використовується для оцінки умов у Bash. Можна також використовувати test замість [.

`-f` myfile.txt: Ця умова перевіряє, чи є myfile.txt звичайним файлом.

Якщо myfile.txt існує і є звичайним файлом (а не директорією, сокетом або іншим типом файлу), то умова повертає true.

`then`: Це вказує на початок блоку команд, які будуть виконані, якщо умова виявиться істинною.

`echo "File exists"`: Ця команда виконується, якщо файл існує.

`else`: Якщо умова -f myfile.txt повертає false, то виконуються команди, які слідують за else.

`echo "File does not exist"`: Ця команда виконується, якщо файл не існує або не є звичайним файлом.

`fi`: Це кінець блоку if.

- Оператори порівняння для чисел
  
`-eq` (дорівнює) - Використовується для порівняння двох чисел на рівність.

```bash
num1=5
num2=5
if [ $num1 -eq $num2 ]; then
  echo "Числа рівні"
else
  echo "Числа не рівні"
fi
```

`-ne` (не дорівнює) - Використовується для перевірки, чи два числа не рівні.

```bash
num1=5
num2=10
if [ $num1 -ne $num2 ]; then
  echo "Числа не рівні"
else
  echo "Числа рівні"
fi
```

`-gt` (більше ніж) - Перевіряє, чи одне число більше іншого.

```bash
num1=10
num2=5
if [ $num1 -gt $num2 ]; then
  echo "$num1 більше ніж $num2"
fi
```

`-lt` (менше ніж) - Перевіряє, чи одне число менше іншого.

```bash
num1=3
num2=8
if [ $num1 -lt $num2 ]; then
  echo "$num1 менше ніж $num2"
fi
```

`-ge` (більше або дорівнює) - Використовується для перевірки, чи одне число більше або дорівнює іншому.

```bash
num1=5
num2=5
if [ $num1 -ge $num2 ]; then
  echo "$num1 більше або дорівнює $num2"
fi
```

`-le` (менше або дорівнює) - Використовується для перевірки, чи одне число менше або дорівнює іншому.

```bash
num1=3
num2=10
if [ $num1 -le $num2 ]; then
  echo "$num1 менше або дорівнює $num2"
fi
```

- Оператори порівняння для рядків
  
`=` (рядки рівні) - Використовується для перевірки, чи два рядки ідентичні.

```bash
str1="apple"
str2="apple"
if [ "$str1" = "$str2" ]; then
  echo "Рядки рівні"
else
  echo "Рядки не рівні"
fi
```

`!=` (рядки не рівні) - Перевіряє, чи два рядки не ідентичні.

```bash
str1="apple"
str2="orange"
if [ "$str1" != "$str2" ]; then
  echo "Рядки не рівні"
fi
```

`-z` (порожній рядок) - Перевіряє, чи рядок є порожнім.

```bash
str=""
if [ -z "$str" ]; then
  echo "Рядок порожній"
fi
```

`-n` (не порожній рядок) - Перевіряє, чи рядок не порожній.

```bash
Копіювати код
str="hello"
if [ -n "$str" ]; then
  echo "Рядок не порожній"
fi
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 7. Функції
Функції в Bash використовуються для організації коду в блоки, які можна викликати кілька разів.

```bash
function_name() {
  # команди
}
```

Приклад:

```bash
greet() {
  echo "Hello, $1!"
}
greet "World"  # Виведе "Hello, World!"
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 8. Редирекція та канали
- Перенаправлення виводу:

`>` — перезапис файлу:
```bash
echo "text" > file.txt
```

`>>` — додавання до файлу:

```bash
echo "more text" >> file.txt
```

- Перенаправлення помилок:

`2>` — перенаправлення стандартного потоку помилок:

```bash
command 2> errors.log
```

- Канали (`|`) — передача результату однієї команди як вхід для іншої:

```bash
command1 | command2
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 9. Корисні команди Bash
`grep` — пошук по тексту:

```bash
grep "pattern" file.txt
```

`cut` — витягує частини рядка:

Синтаксис:

```bash
cut [опції] [файл]
```

Приклад:
```bash
cut -d ',' -f 1 file.txt
```

Типові прапори:

`-d` 'роздільник': Визначає, який символ використовувати для розділення рядків на поля.
`-f n`: Вибирає одне або кілька полів (можна вказати кілька, наприклад -f 1,3 для вибору першого і третього поля).
`-c n`: Вибирає символи за їхніми позиціями, наприклад -c 1-5 вибере перші 5 символів з кожного рядка.
`--complement`: Вибирає всі поля, окрім вказаних.

Інші приклади використання cut

- Вибір кількох полів:

```bash
cut -d ',' -f 1,3 file.txt
```
Ця команда витягне перше та третє поле з кожного рядка файлу file.txt.

- Вибір діапазону полів:

```bash
cut -d ',' -f 2-4 file.txt
```
Ця команда витягне друге, третє та четверте поля з кожного рядка.

- Вибір символів:

```bash
cut -c 1-5 file.txt
```
Ця команда витягне перші 5 символів з кожного рядка файлу file.txt.

`find` — пошук файлів:

Синтаксис команди
```bash
find [шлях] [опції] [критерії]
```

Приклад: 
```bash
find /path -name "file.txt"
```

Пояснення кожного компонента

`/path`:

Це шлях, де буде виконуватися пошук. Ви можете вказати абсолютний шлях (наприклад, /home/user/documents) або відносний шлях (наприклад, documents, якщо ви знаходитесь у каталозі home/user).
У даному випадку /path означає, що пошук буде здійснюватися в каталозі, що знаходиться за цим шляхом та у всіх його підкаталогах.

`-name "file.txt"`:

Це опція і критерій, які вказують, які файли слід шукати.

`-name`: ця опція дозволяє шукати файли за їхньою назвою.

`"file.txt"`: це шаблон для назви файлу, який ви шукаєте. У цьому випадку, команда шукає точну відповідність файлу з ім’ям file.txt.

Якщо ви виконаєте команду:
```bash
find /home/user/documents -name "file.txt"
```
Це знайде всі файли з ім’ям `file.txt`, які знаходяться у каталозі documents і всіх його підкаталогах.

Додаткові параметри

`-iname "file.txt"`: якщо ви хочете зробити пошук нечутливим до регістру, можна використати -iname замість -name. Це знайде file.txt, File.txt, FILE.TXT тощо.

`-type f`: щоб шукати тільки файли (не каталоги), ви можете додати -type f:

```bash
find /path -type f -name "file.txt"
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 10. Коментарі

- Однорядкові коментарі:
```bash
# Це коментар
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 11. Режими налагодження
Режим налагодження скрипта (виводить всі команди перед їх виконанням):
```bash
bash -x script.sh
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 12. Обробка помилок
Команда trap використовується для виконання певних дій при виникненні помилки або сигналу:
```bash
trap 'echo "An error occurred."' ERR
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## 13. Корисні оператори
`&&` — виконує другу команду, якщо перша успішна:
```bash
command1 && command2
```

[Повернутися до змісту](https://github.com/acvetochka/useful/blob/main/Bash.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)


`||` — виконує другу команду, якщо перша не вдалася:
```bash
command1 || command2
```

Цей конспект охоплює основи Bash скриптів, що дозволяють автоматизувати завдання в Linux-системах.
