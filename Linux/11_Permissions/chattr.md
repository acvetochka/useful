# Команда chattr

## Призначення

`chattr` змінює спеціальні атрибути файлів Linux.

Ці атрибути працюють на рівні файлової системи.

Навіть root іноді не може обійти їх.

## Синтаксис
```bash
chattr [operator][attributes] file
```

## Оператори
| символ | значення       |
| ------ | -------------- |
| +      | додати атрибут |
| -      | прибрати       |
| =      | встановити     |

## Перегляд атрибутів
```bash
lsattr file
```

## Основні атрибути
| атрибут | назва               | опис                      |
| ------- | ------------------- | ------------------------- |
| i       | immutable           | файл не можна змінити     |
| a       | append only         | можна лише дописувати     |
| A       | no atime update     | не оновлювати access time |
| d       | no dump             | ігнорувати backup         |
| S       | synchronous updates | синхронний запис          |
| c       | compressed          | стискати файл             |
| j       | journaled           | запис через journal       |
| t       | no tail merging     | оптимізація ext           |
| u       | undeletable         | можливість відновлення    |

### Атрибут i (immutable)

Найважливіший.
```bash
chattr +i file.txt
```
Файл не можна:
- змінити
- видалити
- перейменувати

Навіть root.

Приклад:
```bash
rm file.txt
```
результат:
> Operation not permitted

**Зняти атрибут**
```bash
chattr -i file.txt
```

### Атрибут a (append only)

Файл можна тільки дописувати.
```bash
chattr +a logfile
```
Можна:
```bash
echo "test" >> logfile
```
Не можна:
```bash
rm logfile
```
або
```bash
> logfile
```

### Атрибут A

Не оновлює:
- atime
- корисно для SSD.

### Атрибут d

Файл ігнорується командою:
```bash
dump
```

### Атрибут S

Усі зміни записуються одразу на диск.

### Атрибут j

Використовує журнал файлової системи.

## Типові сценарії використання
- Захист конфігурації
  ```bash
  chattr +i /etc/passwd
  ```

- Захист логів
  ```bash
  chattr +a /var/log/secure
  ```
- Захист критичних файлів
  ```bash
  chattr +i /etc/ssh/sshd_config
  ```
