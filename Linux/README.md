# Linux Knowledge Base <!-- omit in toc -->

Цей репозиторій містить структуровану довідку та навчальні матеріали по операційній системі **Linux**.

Матеріали охоплюють ключові підсистеми Linux:

- архітектуру системи
- роботу оболонки (shell)
- файлову систему та зберігання даних
- роботу з файлами і текстом
- користувачів та права доступу
- процеси і керування системою
- мережу
- встановлення програм
- безпеку та продуктивність

Репозиторій організований у тематичні розділи відповідно до основних компонентів Linux.

---

# Зміст (Table of Contents) <!-- omit in toc -->

- [01\_Fundamentals](#01_fundamentals)
- [02\_Environment](#02_environment)
- [03\_Shell](#03_shell)
- [04\_Shell-Scripting](#04_shell-scripting)
- [05\_FileSystem](#05_filesystem)
- [06\_Storage](#06_storage)
- [07\_FileManagement](#07_filemanagement)
- [08\_TextProcessing](#08_textprocessing)
- [09\_Archives](#09_archives)
- [10\_Users](#10_users)
- [11\_Permissions](#11_permissions)
- [12\_Processes](#12_processes)
- [13\_System](#13_system)
- [14\_Networking](#14_networking)
- [15\_Package-Management](#15_package-management)
- [16\_Logs](#16_logs)
- [17\_Processes-Control](#17_processes-control)
- [18\_Security](#18_security)
- [19\_Performance](#19_performance)
- [20\_Documentation](#20_documentation)
- [21\_Collections](#21_collections)

---

# 01_Fundamentals

У цьому розділі описуються **базові концепції Linux та його архітектури**.

Тут розглядаються:

- структура операційної системи Linux
- відмінності між **Linux kernel** і **GNU tools**
- стандарт **POSIX**
- сімейства дистрибутивів Linux
- основні компоненти операційної системи

Цей розділ дає **теоретичну основу**, необхідну для розуміння подальших тем.

---

# 02_Environment

Розділ присвячений **середовищам доступу до Linux**.

Тут описується:

- робота Linux у **WSL (Windows Subsystem for Linux)**
- термінали та термінальні емулятори
- **TTY та псевдотермінали**
- віддалене підключення до системи
- робота через **SSH**

Цей розділ пояснює, **як користувач взаємодіє з Linux**.

---

# 03_Shell

Розділ описує **оболонку командного рядка (shell)**.

Тут розглядаються:

- синтаксис команд
- стандартні потоки (**stdin, stdout, stderr**)
- оператори та спеціальні символи
- історія команд
- змінні середовища
- налаштування Bash

Shell є **основним інтерфейсом взаємодії з системою**.

---

# 04_Shell-Scripting

Цей розділ присвячений **автоматизації за допомогою Bash-скриптів**.

Розглядаються:

- структура Bash-скрипта
- змінні
- умовні конструкції
- цикли
- функції
- виконання скриптів

Скрипти дозволяють **автоматизувати адміністративні та системні задачі**.

---

# 05_FileSystem

Розділ описує **внутрішню організацію файлової системи Linux**.

Тут пояснюється:

- структура файлової системи
- ієрархія директорій Linux
- **inode**
- жорсткі та символічні посилання
- монтування файлових систем

Цей розділ допомагає зрозуміти **як Linux зберігає дані**.

---

# 06_Storage

Розділ присвячений **зберіганню даних та роботі з дисками**.

Розглядаються:

- диски та блочні пристрої
- таблиці розділів (**MBR, GPT**)
- розділи диска
- використання дискового простору
- інструменти аналізу дисків

---

# 07_FileManagement

Розділ описує **основні команди роботи з файлами та директоріями**.

Тут розглядаються:

- створення файлів і директорій
- копіювання файлів
- переміщення файлів
- видалення файлів
- перегляд файлів
- пошук файлів у файловій системі

---

# 08_TextProcessing

Розділ присвячений **обробці текстових потоків у Linux**.

Розглядаються утиліти:

- `grep`
- `sed`
- `awk`
- `sort`
- `uniq`
- `cut`
- `tr`

Ці інструменти використовуються для **аналізу логів, конфігураційних файлів та виводу команд**.

---

# 09_Archives

Розділ описує **архівування та стиснення файлів**.

Розглядаються:

- створення архівів
- розпакування архівів
- популярні формати архівів
- інструменти стиснення

---

# 10_Users

Розділ присвячений **керуванню користувачами системи**.

Тут описується:

- створення користувачів
- зміна паролів
- групи користувачів
- адміністративні привілеї
- команда `sudo`

---

# 11_Permissions

Розділ пояснює **систему прав доступу Linux**.

Тут розглядаються:

- права читання, запису та виконання
- власник файлу
- група файлу
- зміна прав (`chmod`)
- зміна власника (`chown`)
- маска прав (`umask`)
- ACL

---

# 12_Processes

Розділ присвячений **процесам у Linux**.

Тут описується:

- що таке процес
- життєвий цикл процесу
- перегляд процесів
- сигнали
- завершення процесів

---

# 13_System

Розділ описує **керування системою**.

Тут розглядаються:

- процес завантаження Linux
- система ініціалізації
- керування сервісами
- systemd
- системні журнали

---

# 14_Networking

Розділ присвячений **мережевим інструментам Linux**.

Тут описуються:

- мережеві утиліти
- перевірка з’єднання
- віддалений доступ
- передача даних через мережу

---

# 15_Package-Management

Розділ описує **встановлення та керування програмами**.

Розглядаються:

- пакетні менеджери
- репозиторії програм
- встановлення і видалення пакетів
- альтернативні системи пакетів

---

# 16_Logs

Розділ присвячений **журналам системи**.

Тут розглядаються:

- системні логи
- журнал systemd
- ротація логів
- аналіз журналів

---

# 17_Processes-Control

Розділ описує **керування процесами у shell**.

Розглядаються:

- фонові процеси
- foreground і background jobs
- `nohup`
- робота з `screen` і `tmux`

---

# 18_Security

Розділ присвячений **безпеці системи Linux**.

Тут описується:

- безпека SSH
- брандмауери
- фільтрація мережевого трафіку
- системи захисту від атак

---

# 19_Performance

Розділ присвячений **моніторингу продуктивності системи**.

Тут розглядаються інструменти для:

- аналізу навантаження системи
- моніторингу CPU
- використання пам'яті
- аналізу дискової активності

---

# 20_Documentation

Розділ описує **вбудовану документацію Linux**.

Тут розглядаються:

- `man`
- `help`
- `info`

Ці інструменти дозволяють знаходити **документацію прямо в системі**.

---

# 21_Collections

Розділ містить **довідкові матеріали та збірки команд**.

Тут можуть бути:

- списки команд
- шпаргалки
- короткі довідники

```
Linux/

01_Fundamentals/
│
├── Linux-structure.md
├── Сімейства дистрибутивів.md
├── Kernel.md
├── GNU.md
└── POSIX.md


02_Environment/
│
├── WSL.md
├── Terminal.md
├── TTY.md
├── SSH.md
└── Remote-access.md


03_Shell/
│
├── Standard Streams.md
├── Оператори та символи.md
├── history.md
├── Change Bash-prompt.md
├── Environment variables.md
└── Bash configuration.md


04_Shell-Scripting/
│
├── Bash scripts.md
├── Variables.md
├── Conditions.md
├── Loops.md
└── Functions.md


05_FileSystem/
│
├── FileSystem.md
├── LinuxHierarchy.md
├── Inodes.md
├── Hard-links.md
├── Symbolic-links.md
└── Mount.md


06_Storage/
│
├── Partitions.md
├── MBR-GPT.md
├── lsblk.md
├── df.md
├── du.md
└── Disk usage.md


07_FileManagement/
│
├── Робота з файлами.md
├── Способи відображення файлів команд Linux.md
├── cp.md
├── mv.md
├── rm.md
├── touch.md
└── find.md


08_TextProcessing/
│
├── grep.md
├── sed.md
├── awk.md
├── cut.md
├── sort.md
├── uniq.md
└── tr.md


09_Archives/
│
├── Робота з архівами.md
├── tar.md
├── gzip.md
├── bzip2.md
└── zip.md


10_Users/
│
├── Users.md
├── useradd.md
├── passwd.md
├── groups.md
└── sudo.md


11_Permissions/
│
├── FilePermissions.md
├── chmod.md
├── chown.md
├── umask.md
└── ACL.md


12_Processes/
│
├── Processes.md
├── ps.md
├── top.md
├── htop.md
├── kill.md
├── nice.md
└── signals.md


13_System/
│
├── systemctl.md
├── services.md
├── journalctl.md
└── boot-process.md


14_Networking/
│
├── wget.md
├── curl.md
├── ping.md
├── netstat.md
├── ss.md
├── SSH.md
└── SSH-proxy.md


15_Package-Management/
│
├── Встановлення ПЗ.md
├── apt.md
├── snap.md
├── flatpak.md
└── repositories.md


16_Logs/
│
├── syslog.md
├── logrotate.md
└── journal.md


17_Processes-Control/
│
├── background-jobs.md
├── fg-bg.md
├── nohup.md
└── screen-tmux.md


18_Security/
│
├── SSH-security.md
├── firewall.md
├── iptables.md
└── fail2ban.md


19_Performance/
│
├── uptime.md
├── free.md
├── vmstat.md
└── iostat.md


20_Documentation/
│
├── Manual.md
├── help.md
└── info.md


21_Collections/
│
├── Linux-commands.md
└── CheatSheet.md

```