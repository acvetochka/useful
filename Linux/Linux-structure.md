# Структура Linux

## Вступ до Linux
Linux — це операційна система з відкритим вихідним кодом, заснована на ядрі Linux, розробленому Лінусом Торвальдсом у 1991 році. Вона належить до класу Unix-подібних ОС і відома своєю стабільністю, безпекою та масштабованістю. Linux використовується у серверних, десктопних та вбудованих системах.

## Структура Linux
### 1. Ядро (Kernel):
Ядро — це серце операційної системи, яке керує апаратними ресурсами, пам'яттю, процесами та взаємодією між компонентами системи.

**Типи ядер:**
- Монолітне ядро (включає в себе всі необхідні драйвери та служби).
- Мікроядро (забезпечує мінімальний функціонал, а решта працює у просторі користувача).

### 2. Дистрибутиви Linux:
Дистрибутив — це пакет, що складається з ядра Linux і програмного забезпечення (наприклад, менеджери пакетів, утиліти, графічні оболонки).

**Популярні дистрибутиви:**
- `Ubuntu` (заснований на Debian, зручний для початківців).
- `CentOS/RHEL` (для корпоративних серверів).
- `Fedora` (новаторський дистрибутив від спільноти).
- `Arch Linux` (для досвідчених користувачів, мінімалізм і гнучкість).
- `Debian` (стабільний та надійний).

### 3. Файлова система:
У Linux використовується ієрархічна файлова система (HFS), де кореневий каталог — це /.

**Основні каталоги:**
- `/bin` — основні виконувані файли (команди).
- `/sbin` — виконувані файли для адміністрування.
- `/etc` — конфігураційні файли.
- `/home` — домашні каталоги користувачів.
- `/var` — змінні файли (логи, дані веб-серверів).
- `/dev` — пристрої, представлені як файли (диски, USB, принтери).
- `/tmp` — тимчасові файли.
- `/usr` — програми та бібліотеки користувача.
