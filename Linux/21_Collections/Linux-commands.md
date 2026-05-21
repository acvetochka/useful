# Команди Linux

## Зміст

- [Основні команди Linux](#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8-linux)
  1. [Навігація по файловій системі](#1-%D0%BD%D0%B0%D0%B2%D1%96%D0%B3%D0%B0%D1%86%D1%96%D1%8F-%D0%BF%D0%BE-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D1%96%D0%B9-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%96)
  2. [Перегляд та обробка файлів](#2-%D0%BF%D0%B5%D1%80%D0%B5%D0%B3%D0%BB%D1%8F%D0%B4-%D1%82%D0%B0-%D0%BE%D0%B1%D1%80%D0%BE%D0%B1%D0%BA%D0%B0-%D1%84%D0%B0%D0%B9%D0%BB%D1%96%D0%B2)
  3. [Користувачі та права доступу](#3-%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D1%83%D0%B2%D0%B0%D1%87%D1%96-%D1%82%D0%B0-%D0%BF%D1%80%D0%B0%D0%B2%D0%B0-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D1%83)
  4. [Процеси](#4-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D0%B8)
  5. [Мережеві команди](#5-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B5%D0%B2%D1%96-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8)
  6. [Управління пакетами](#6-%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%96%D0%BD%D0%BD%D1%8F-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%B0%D0%BC%D0%B8)
  7. [Журнали та логи](#7-%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB%D0%B8-%D1%82%D0%B0-%D0%BB%D0%BE%D0%B3%D0%B8)
  8. [Робота з архівами](#8-%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%B0-%D0%B7-%D0%B0%D1%80%D1%85%D1%96%D0%B2%D0%B0%D0%BC%D0%B8)
- [Управління службами та демонами](#%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%96%D0%BD%D0%BD%D1%8F-%D1%81%D0%BB%D1%83%D0%B6%D0%B1%D0%B0%D0%BC%D0%B8-%D1%82%D0%B0-%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D0%B0%D0%BC%D0%B8)
  1. [systemd](#1-systemd--%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%B0-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D1%96%D0%BD%D1%96%D1%86%D1%96%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%97-%D1%83-%D0%B1%D0%B0%D0%B3%D0%B0%D1%82%D1%8C%D0%BE%D1%85-%D1%81%D1%83%D1%87%D0%B0%D1%81%D0%BD%D0%B8%D1%85-%D0%B4%D0%B8%D1%81%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B8%D0%B2%D0%B0%D1%85-linux-%D0%BD%D0%B0%D0%B9%D1%81%D1%83%D1%87%D0%B0%D1%81%D0%BD%D1%96%D1%88%D0%B0-%D1%96-%D0%BF%D0%BE%D0%BF%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D0%B0-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D1%96%D0%BD%D1%96%D1%86%D1%96%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%97-%D0%B2-%D0%B1%D1%96%D0%BB%D1%8C%D1%88%D0%BE%D1%81%D1%82%D1%96-%D0%B4%D0%B8%D1%81%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B8%D0%B2%D1%96%D0%B2-%D1%8F%D0%BA-%D0%BE%D1%82-ubuntu-fedora-centos)
  2. [SysVinit](#2-sysvinit-%D1%81%D1%82%D0%B0%D1%80%D1%96%D1%88%D0%B0-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D1%96%D0%BD%D1%96%D1%86%D1%96%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%97-%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%BE%D0%B2%D1%83%D1%94%D1%82%D1%8C%D1%81%D1%8F-%D0%B2-%D1%82%D0%B0%D0%BA%D0%B8%D1%85-%D0%B4%D0%B8%D1%81%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B8%D0%B2%D0%B0%D1%85-%D1%8F%D0%BA-debian-centos-%D0%B4%D0%BE-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D1%83-%D0%BD%D0%B0-systemd)
  3. [Upstart](#3-upstart-%D0%B1%D1%83%D0%BB%D0%B0-%D0%B7%D0%B0%D0%BC%D1%96%D0%BD%D0%BE%D1%8E-sysvinit-%D1%83-%D0%B4%D0%B5%D1%8F%D0%BA%D0%B8%D1%85-%D0%B2%D0%B5%D1%80%D1%81%D1%96%D1%8F%D1%85-ubuntu-%D0%B7%D0%B0%D1%80%D0%B0%D0%B7-%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE-%D0%B7%D0%B0%D0%BC%D1%96%D0%BD%D0%B5%D0%BD%D0%B0-%D0%BD%D0%B0-systemd)
  4. [OpenRC](#4-openrc-%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%BE%D0%B2%D1%83%D1%94%D1%82%D1%8C%D1%81%D1%8F-%D0%B2-%D0%B4%D0%B5%D1%8F%D0%BA%D0%B8%D1%85-%D0%B4%D0%B8%D1%81%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B8%D0%B2%D0%B0%D1%85-%D1%82%D0%B0%D0%BA%D0%B8%D1%85-%D1%8F%D0%BA-gentoo-alpine-linux)
  5. [runit](#5-runit-%D0%BB%D0%B5%D0%B3%D0%BA%D0%B0-%D1%82%D0%B0-%D1%88%D0%B2%D0%B8%D0%B4%D0%BA%D0%B0-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D1%96%D0%BD%D1%96%D1%86%D1%96%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%97-%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%BE%D0%B2%D1%83%D1%94%D1%82%D1%8C%D1%81%D1%8F-%D0%B2-%D1%82%D0%B0%D0%BA%D0%B8%D1%85-%D0%B4%D0%B8%D1%81%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B8%D0%B2%D0%B0%D1%85-%D1%8F%D0%BA-void-linux)
- [Bash-скрипти](#bash-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B8)

## Основні команди Linux
### 1. Навігація по файловій системі:
- `pwd` — показати поточний каталог.
- `ls` — переглянути вміст каталогу.
  <details>
    <summary>Детальніше...</summary>

  - `ls -l` — показати вміст каталогу у форматі довгого списку (права доступу, власник, розмір, дата модифікації, ім'я файлу):

     ```bash
      ls -l
     # Вивід:
     -rw-r--r-- 1 user group  4096 Oct 15 12:00 file.txt
     drwxr-xr-x 2 user group  4096 Oct 15 12:00 dir/
     ```
  - `ls -a` — показати всі файли, включаючи приховані (ті, що починаються з крапки):

     ```bash
      ls -a
     # Вивід:
     .  ..  .bashrc  file.txt  dir/
     ```

   - `ls -lh` — показати розміри файлів у зручному для читання форматі (KB, MB):

     ```bash
      ls -lh
     # Вивід:
     -rw-r--r-- 1 user group 4.0K Oct 15 12:00 file.txt
     ```

  - `ls -R` — рекурсивно показати всі файли в поточному каталозі та підкаталогах:

    ```bash
     ls -R
    ```

    [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
    
  </details>
  
- `cd <каталог>` — змінити поточний каталог.
- `mkdir <каталог>` — створити новий каталог.
- `rmdir <каталог>` — видалити порожній каталог.
- `touch <файл>` — створити новий файл.
- `find` — пошук файлів
  <details>
    <summary>Детальніше...</summary>
    
  - `find /path/ -name "file.txt"` — знайти файл з іменем file.txt у каталозі /path/:
  
    ```bash
     find /home/user/ -name "file.txt"
    ```
  
  - `find /path/ -type f -size +10M` — знайти файли розміром більше 10 МБ:
  
    ```bash
     find /home/user/ -type f -size +10M
    ```
  
  - `find /path/ -mtime -7` — знайти файли, змінені за останні 7 днів:
  
    ```bash
     find /home/user/ -mtime -7
    ```
  
  - `find /path/ -exec rm {} \;` — знайти файли і виконати команду (в даному випадку — видалити їх):
  
    ```bash
     find /home/user/temp/ -name "*.tmp" -exec rm {} \;
    ```

    [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  </details>
  
- `cp <файл> <шлях>` — копіювати файл.

  <details>
    <summary>Детальніше...</summary>
      
  - `cp file.txt /path/to/destination/` — копіювати файл у зазначене місце:

    ```bash
     cp file.txt /home/user/docs/
    ```

  - `cp -r dir/ /path/to/destination/` — рекурсивно копіювати каталог із вмістом:

    ```bash
     cp -r dir/ /home/user/docs/
    ```

  - `cp -i file.txt /path/` — запитати підтвердження перед перезаписом існуючих файлів:

    ```bash
     cp -i file.txt /home/user/docs/
    ```

  - `cp -v file.txt /path/` — показати інформацію про кожен файл під час копіювання:
    ```bash
     cp -v file.txt /home/user/docs/
    ```

    [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  </details>

- `mv <файл> <шлях>` — перемістити або перейменувати файл.
  
  <details>
    <summary>Детальніше...</summary>
    
  - `mv file.txt /path/` — перемістити файл до іншого каталогу:

    ```bash
     mv file.txt /home/user/docs/
    ```
  
  - `mv file.txt newfile.txt` — перейменувати файл:
  
    ```bash
     mv file.txt newfile.txt
    ```
  
  - `mv -i file.txt /path/` — запитати підтвердження перед перезаписом:
  
    ```bash
     mv -i file.txt /home/user/docs/
    ```
  
  - `mv -v file.txt /path/` — показати інформацію про кожен файл під час переміщення:
  
    ```bash
     mv -v file.txt /home/user/docs/
    ```

    [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  </details>

- `rm <файл>` — видалити файл.

  <details>
    <summary>Детальніше...</summary>
  
  - `rm file.txt` — видалити файл:

    ```bash
     rm file.txt
    ```
  
  - `rm -r dir/` — рекурсивно видалити каталог і його вміст:
    
    ```bash
     rm -r dir/
    ```
  
  - `rm -i file.txt` — запитати підтвердження перед видаленням файлу:
  
    ```bash
     rm -i file.txt
    ```

  - `rm -f file.txt` — примусово видалити файл без запиту підтвердження (навіть якщо немає прав доступу):
    
    ```bash
     rm -f file.txt
    ```

    [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  </details>
  
- `grep` — пошук тексту в файлах

  <details>
    <summary>Детальніше...</summary>
      
  - `grep "pattern" file.txt` — знайти рядки, які містять pattern у файлі:

    ```bash
     grep "hello" file.txt
    ```

  - `grep -i "pattern" file.txt` — виконати пошук без врахування регістру:
  
    ```bash
     grep -i "hello" file.txt
    ```
  
  - `grep -r "pattern" /path/` — рекурсивно шукати шаблон у файлах каталогу:
  
    ```bash
     grep -r "error" /var/log/
    ```
  
  - `grep -v "pattern" file.txt` — показати всі рядки, які не містять pattern:
    
    ```bash
     grep -v "hello" file.txt
    ```

  Докладніше про grep за [посиланням](https://github.com/acvetochka/useful/blob/main/Python/Regex.md#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D0%BD%D1%8F-grep)

  </details>

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 2. Перегляд та обробка файлів:
- `cat <файл>` — перегляд вмісту файлу.
- `less <файл>` — посторінковий перегляд файлу.
- `head <файл>` — показати початкові рядки файлу.
- `tail <файл>` — показати останні рядки файлу.
- `nano <файл>` або `vim <файл>` — редагування файлів у текстових редакторах.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 3. Користувачі та права доступу:
- `whoami` — показати ім’я поточного користувача.
- `id` — показати інформацію про користувача та його групи.
- `useradd <ім'я>` — додати нового користувача.
- `passwd <ім'я>` — змінити пароль користувача.
- `usermod <опції> <користувач>` — змінити параметри користувача.
- `chown <власник>:<група> <файл>` — змінити власника та групу файлу.

  <details>
    <summary>Детальніше...</summary>

  - `chown user file.txt` — змінити власника файлу:

    ```bash
     chown user file.txt
    ```
  
  - `chown user:group file.txt` — змінити власника і групу файлу:
  
    ```bash
     chown user:group file.txt
    ```
  
  - `chown -R user:group dir/` — рекурсивно змінити власника і групу для всіх файлів у каталозі:
  
    ```bash
     chown -R user:group dir/
    ```

    [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  </details>

- `chmod <права> <файл>` — змінити права доступу до файлу.

  <details>
    <summary>Детальніше...</summary>
      
  - `chmod 755 file.txt` — встановити права на файл: власник має читання, запис і виконання, група та інші — тільки читання і виконання:

    ```bash
     chmod 755 file.txt
    ```
  
  - `chmod -R 644 dir/` — рекурсивно змінити права для всіх файлів у каталозі: власник має читання і запис, група та інші — тільки читання:
  
    ```bash
     chmod -R 644 dir/
    ```
  
  - `chmod u+x file.sh` — додати право на виконання для власника:
  
    ```bash
     chmod u+x file.sh
    ```
  
  - `chmod g-w file.txt` — забрати право на запис для групи:
  
    ```bash
     chmod g-w file.txt
    ```

    <details>
    <summary><b>💡 Права доступу:</b></summary>
    
    У Linux права доступу до файлів та директорій визначаються за допомогою трьох основних рівнів доступу: власник файлу (`u`), група (`g`) та інші користувачі (`o`). Ці права можна виразити як за допомогою символів (r, w, x), так і за допомогою чисел (цифрового значення).
    
    **Символічні позначення прав:**
    
    - `r` (read) — право читати файл або вміст директорії.-
    - `w` (write) — право записувати або змінювати файл чи вміст директорії.
    - `x` (execute) — право виконувати файл або отримувати доступ до вмісту директорії.
    
    **Цифрове значення прав:**
    
    Кожне з прав має числове значення:
    
    - r (читання) = `4`
    - w (запис) = `2`
    - x (виконання) = `1`
    
    Права комбінуються за допомогою додавання значень. Наприклад:
    
    - rw- = 6 (4 + 2) — право читання і запису.
    - r-x = 5 (4 + 1) — право читання і виконання.
    - rwx = 7 (4 + 2 + 1) — повний доступ: читання, запис і виконання.
    
    **Структура прав:**
    
    Права доступу в Linux організовані в три групи:
    
    - Власник файлу (owner) - `u`.
    - Група користувачів (group) - `g`.
    - Інші користувачі (others) - `o`.
      
    Щоб встановити права доступу за допомогою цифр, використовується команда chmod. Цифрові права записуються у вигляді тризначного числа, де кожна цифра відповідає рівню доступу для власника, групи та інших.
    
    **Приклад:**
    
    Якщо ви бажаєте надати:
    
    - власнику права читання, запису та виконання,
    - групі права читання та виконання,
    - іншим користувачам права лише читання,
    це можна зробити наступним чином:
    
      ```bash
       chmod 754 file.txt
      ```
    
    Пояснення цифр:
    
    - 7 (rwx) — власник має повні права: читати, записувати та виконувати.
    - 5 (r-x) — група має право читати і виконувати.
    - 4 (r--) — інші користувачі мають право лише читати.
    
    Інші приклади:
    
    1. `chmod 777` — усі мають повний доступ (читання, запис і виконання) до файлу або директорії:
    
        ```bash
         chmod 777 file.txt
        ```
      
    - 7 (rwx) для власника.
    - 7 (rwx) для групи.
    - 7 (rwx) для інших користувачів.
      
    2. `chmod 644` — власник має права читати і записувати, група і інші можуть лише читати:
    
        ```bash
         chmod 644 file.txt
        ```
      
    - 6 (rw-) для власника.
    - 4 (r--) для групи.
    - 4 (r--) для інших користувачів.
      
    3. `chmod 755` — власник має повний доступ, група і інші можуть лише читати і виконувати:
    
        ```bash
         chmod 755 script.sh
        ```
      
    - 7 (rwx) для власника.
    - 5 (r-x) для групи.
    - 5 (r-x) для інших користувачів.
      
    **Додаткові прапори:**
    - SUID (Set User ID): встановлюється на файл, щоб запустити його від імені власника файлу, а не користувача, який виконує команду.
    - SGID (Set Group ID): дозволяє виконувати файл від імені групи.
    - Sticky Bit: захищає файли в директорії від видалення іншими користувачами, навіть якщо у них є права на запис.
    
    Команда для додавання SUID, SGID або Sticky Bit:
    
    - `chmod 4755 файл` — встановлює SUID (4).
    - `chmod 2755 файл` — встановлює SGID (2).
    -` chmod 1755 директорія` — встановлює Sticky Bit (1).
    
    Таким чином, цифрове значення прав є зручним і точним способом налаштування доступу до файлів у Linux.
    </details>
  </details>

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 4. Процеси:
- `ps` — показати активні процеси.
  <details>
    <summary>Детальніше...</summary>
    
    - `ps` (без параметрів): Показує процеси поточного терміналу.

      ```bash
      ps
      ```
      Виводить список процесів, що запущені в поточній сесії:

      ```yaml
        PID TTY          TIME CMD
       1234 pts/1    00:00:00 bash
       5678 pts/1    00:00:01 ps
      ```
    - `ps -e` або `ps -A`: Виводить інформацію про всі процеси в системі.

      ```bash
      ps -e
      ```
      або
      
      ```bash
      ps -A
      ```
      Виведе список усіх процесів у системі:
      
      ```yaml
        PID TTY          TIME CMD
          1 ?        00:00:01 systemd
        567 ?        00:00:00 kthreadd
      ```
    - `ps -f`: Формат повного списку (більш детальний вигляд, включаючи інформацію про батьківський процес).
    
      ```bash
      ps -f
      ```
      
      Виведе:
      
      ```yaml
      UID        PID  PPID  C STIME TTY          TIME CMD
      user1     1234     1  0 08:55 pts/1    00:00:00 bash
      user1     5678  1234  0 08:56 pts/1    00:00:01 ps -f
      ```
      
    - `ps -ef`: Показує всі процеси в повному форматі.
    
      ```bash
      ps -ef
      ```
      Виведе:
      
      ```yaml
      UID        PID  PPID  C STIME TTY          TIME CMD
      root         1     0  0 08:00 ?        00:00:01 systemd
      root       567     1  0 08:00 ?        00:00:00 kthreadd
      ```
      
    - `ps -u <username>`: Виводить процеси, запущені конкретним користувачем.
      
      ```bash
      ps -u user1
      ```

      Виведе процеси, запущені користувачем user1:
      
      ```yaml
        PID TTY          TIME CMD
       1234 pts/1    00:00:00 bash
       5678 pts/1    00:00:01 python
      ```
      
    - `ps aux`: Один з найпопулярніших варіантів — показує всі процеси у детальному форматі, включаючи інформацію про використання процесора та пам’яті.
    
      ```bash
      ps aux
      ```
      
      Виведе:
      
      ```yaml
      USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
      root         1  0.0  0.1  16384  5120 ?        Ss   08:00   0:01 /usr/lib/systemd/systemd
      user1     5678  1.2  1.3  1024   5124 pts/1    S+   08:56   0:01 python my_script.py
      ```
      
    - `ps -l`: Виводить додаткову інформацію про процеси, включаючи стан (STAT) і пріоритет (PRI).
    
      ```bash
      ps -l
      ```
      
      Виведе:
      
      ```yaml
      F S UID        PID  PPID  PRI  NI   VSZ   RSS TTY   STAT TIME CMD
      4 S user1     1234     1   20   0 16384  5120 pts/1 S    00:00:00 bash
      4 R user1     5678  1234   20   0 1024  5124 pts/1 R+   00:00:01 ps -l
      ```
      
    - `ps -p <pid>`: Виводить інформацію про конкретний процес за його PID.
    
      ```bash
      ps -p 5678
      ```
      
      Виведе інформацію про процес із PID 5678:
      
      ```yaml
        PID TTY          TIME CMD
       5678 pts/1    00:00:01 python
      ```
      
    - `ps --sort <key>`: Сортує виведення за вказаним ключем, наприклад, за використанням CPU чи пам'яті.
    
      ```bash
      ps aux --sort=-%cpu
      ```
      
      Сортує всі процеси за рівнем використання процесора:
      
      ```yaml
      USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
      user1     5678  80.0  1.3  1024  5124 pts/1    R+   08:56   0:01 python my_script.py
      root         1  0.0  0.1  16384  5120 ?        Ss   08:00   0:01 /usr/lib/systemd/systemd
      ```
      
    - `ps -C <command>`: Виводить процеси, що відповідають конкретній команді.
    
      ```bash
      ps -C python
      ```
      
      Виведе:
      
      ```yaml
       PID TTY          TIME CMD
      5678 pts/1    00:00:01 python
      ```
  
    - `ps -o <format>`: Дозволяє виводити певні поля, вказані користувачем.
    
      ```bash
      ps -o pid,cmd,%cpu
      ```
      
      Виведе тільки PID, команду та використання CPU:
      
      ```yaml
       PID CMD                         %CPU
      1234 bash                        0.0
      5678 python my_script.py         80.0
      ```
      
    - `ps --forest`: Виводить процеси у вигляді дерева (зручно для перегляду батьківських і дочірніх процесів).
    
      ```bash
      ps aux --forest
      ```
      
      Виведе:
      
      ```sql
      USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
      root         1  0.0  0.1  16384  5120 ?        Ss   08:00   0:01 /usr/lib/systemd/systemd
        ├─kthreadd
        └─bash
           └─python my_script.py
      ```
  
    - `ps -H`: Виводить процеси у вигляді ієрархії (з батьківськими і дочірніми процесами).
    
      ```bash
      ps -H
      ```
      
      Виведе:
      
      ```yaml
       PID TTY          TIME CMD
      1234 pts/1    00:00:00 bash
      5678 pts/1    00:00:01 python my_script.py
      ```

    **Комбінування кількох прапорів:**
  
    Ви можете комбінувати прапори для отримання потрібної інформації. Наприклад:
    
    - `ps -ef --sort=-%mem` — показує всі процеси у повному форматі та сортує їх за використанням пам’яті.
    
      ```bash
      ps -ef --sort=-%mem
      ```
      
    - `ps -u user1 -o pid,%cpu,%mem,cmd` — показує процеси користувача user1 з відображенням PID, використання CPU, пам'яті та команди.
    
      ```bash
      ps -u user1 -o pid,%cpu,%mem,cmd
      ```

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  
  </details>
- `top` — моніторинг процесів у реальному часі.
- `kill <PID>` — завершити процес за ідентифікатором (PID).
- `bg` / `fg` — перевести процес у фоновий/передній режим.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 5. Мережеві команди:
- `ifconfig` — налаштування мережевих інтерфейсів.
- `ping <адреса>` — перевірка доступності вузла.
- `netstat` — перегляд мережевих з'єднань.
- `ssh <користувач>@<хост>` — підключення до віддаленого сервера через SSH.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 6. Управління пакетами:
- Debian-based (Ubuntu, Debian):
  - `apt-get update` — оновити список пакетів.
  - `apt-get install <пакет>` — встановити новий пакет.
  - `apt-get remove <пакет>` — видалити пакет.
- RedHat-based (CentOS, Fedora):
  - `yum update` — оновити пакети.
  - `yum install <пакет>` — встановити пакет.
  - `yum remove <пакет>` — видалити пакет.
 
  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 7. Журнали та логи:
- `dmesg` — перегляд системних повідомлень.
- `journalctl` — перегляд логів systemd.
- `tail -f /var/log/syslog` — постійне стеження за системними логами.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 8. Робота з архівами:
- `tar -cvf <архів.tar> <каталог>` — створити архів з каталогу.
  
    ```bash
     tar -cvf archive.tar /home/user/docs/
    ```
  
- `tar -xvf <архів.tar>` — розпакувати архів.
    ```bash
     tar -xvf archive.tar
    ```
- `tar -czvf <archive.tar> <каталог>` — створити стиснутий архів:
  
    ```bash
     tar -czvf archive.tar.gz /home/user/docs/
    ```
  
- `tar -xzvf <archive.tar>` — розпакувати стиснутий архів:
  
    ```bash
     tar -xzvf archive.tar.gz
    ```
 
- `gzip <файл>` — стиснути файл.
- `gunzip <файл.gz>` — розпакувати стиснутий файл.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

## Управління службами та демонами
### 1. systemd — основна система ініціалізації у багатьох сучасних дистрибутивах Linux (найсучасніша і популярна система ініціалізації в більшості дистрибутивів, як-от Ubuntu, Fedora, CentOS):
- `systemctl status <служба>` — перевірити статус служби:

  ```bash
   systemctl status apache2
  ```
  Ця команда показує інформацію про поточний статус служби, включаючи її активність, PID і журнали.

- `systemctl start <служба>` — запустити службу:

  ```bash
   systemctl start apache2
  ```

  Використовується для запуску служби, якщо вона не працює.

- `systemctl stop <служба>` — зупинити службу:

  ``` bash
   systemctl stop apache2
  ```

  Зупиняє поточну роботу служби.

- `systemctl restart <служба>` — перезапустити службу:

  ```bash
   systemctl restart apache2
  ```

  Перезапуск служби використовується для перезавантаження конфігурацій або після внесення змін до служби.

- `systemctl enable <служба>` — активувати службу при завантаженні системи:

  ```bash
   systemctl enable apache2
  ```

  Встановлює службу для автоматичного запуску при кожному завантаженні системи.

- `systemctl disable <служба>` — вимкнути автозапуск служби:

  ```bash
   systemctl disable apache2
  ```

  Відключає службу від автоматичного запуску при завантаженні системи.

- `systemctl reload <служба>` — перезавантажити конфігурацію служби:

  ```bash
   systemctl reload apache2
  ```

  Використовується для перезавантаження конфігурації служби без її повного перезапуску.

- `systemctl is-enabled <служба>` — перевірити, чи активовано службу для автозапуску:

  ```bash
   systemctl is-enabled apache2
  ```

  Ця команда виведе, чи служба включена для автозапуску.

- `systemctl list-units --type=service` — показати список усіх активних служб:

  ```bash
   systemctl list-units --type=service
  ```

  Ця команда показує список усіх активних служб на системі.

- `journalctl -u <служба>` — переглянути журнал для конкретної служби:

  ```bash
   journalctl -u apache2
  ```

  Показує детальний лог служби з її помилками, повідомленнями та іншою інформацією.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 2. SysVinit (старіша система ініціалізації, використовується в таких дистрибутивах, як Debian, CentOS, до переходу на systemd)

**Основні команди:**

- `service <служба> status` — перевірити статус служби.
  ```bash
   service apache2 status
  ```
  
- `service <служба> start` — запустити службу.

  ```bash
   service apache2 start
  ```
  
- `service <служба> stop` — зупинити службу.
  ```bash
   service apache2 stop
  ```

- `service <служба> restart` — перезапустити службу.
  ```bash
   service apache2 restart
  ```
  
- `update-rc.d <служба> defaults` — активувати службу для автозапуску при завантаженні системи.
  ```bash
   update-rc.d apache2 defaults
  ```

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 3. Upstart (була заміною SysVinit у деяких версіях Ubuntu, зараз переважно замінена на systemd)

**Основні команди:**
- `status <служба>` — перевірити статус служби.
  ```bash
   status apache2
  ```
- `start <служба>` — запустити службу.
  ```bash
   start apache2
  ```
  
- `stop <служба>` — зупинити службу.
  ```bash
   stop apache2
  ```
  
- `restart <служба>` — перезапустити службу.
  ```bash
   restart apache2
  ```
  
- `initctl reload-configuration` — перезавантажити конфігурацію Upstart для нових служб.

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
  
### 4. OpenRC (використовується в деяких дистрибутивах, таких як Gentoo, Alpine Linux)
   
**Основні команди:**
- `rc-service <служба> status` — перевірити статус служби.
  
  ```bash
  rc-service apache2 status
- `rc-service <служба> start` — запустити службу.
  
  ```bash
   rc-service apache2 start
  ```
- `rc-service <служба> stop` — зупинити службу.
  
  ```bash
   rc-service apache2 stop
  ```
- `rc-service <служба> restart` — перезапустити службу.
  
  ```bash
   rc-service apache2 restart
  ```
- `rc-update add <служба>` — активувати службу для автозапуску.
  
  ```bash
   rc-update add apache2
  ```

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

### 5. runit (легка та швидка система ініціалізації, використовується в таких дистрибутивах, як Void Linux)
   
**Основні команди:**
- `sv status <служба>` — перевірити статус служби.
  
  ```bash
   sv status apache2
  ```
- `sv start <служба>` — запустити службу.
  
  ```bash
   sv start apache2
  ```
- `sv stop <служба>` — зупинити службу.
  
  ```bash
   sv stop apache2
  ```
- `sv restart <служба>` — перезапустити службу.
  
  ```bash
   sv restart apache2
  ```

  [Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)

  **Підсумок:**
  systemd є найпопулярнішою системою ініціалізації на сьогодні, і більшість сучасних дистрибутивів використовують саме її.
  Інші системи, такі як SysVinit, Upstart, OpenRC, runit, продовжують використовуватись в деяких спеціалізованих дистрибутивах або старих версіях систем.
  Тому, коли ти налаштовуєш служби та демони, залежно від дистрибутиву, ти використовуватимеш одну з цих систем.

## Bash-скрипти
**Bash** — це популярний командний інтерпретатор для Linux.

**Скрипт** — це файл з командами, який виконується послідовно.

**Приклад простого скрипта:**
```bash
#!/bin/bash
echo "Привіт, світ!"
```

**Основні елементи Bash-скриптів:**
- Змінні: variable_name=value
- Умовні оператори: if, else, elif.
- Цикли: for, while.
- Функції: створюються для повторного використання коду.

Докладніше про Bash за [посиланням](https://github.com/acvetochka/useful/blob/main/Bash.md)

[Повернутися до зміcту](https://github.com/acvetochka/useful/blob/main/Linux/Linux-commands.md#%D0%B7%D0%BC%D1%96%D1%81%D1%82)
