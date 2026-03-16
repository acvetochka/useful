# Команда chown

## Призначення

- `chown` (change owner) змінює власника і групу файлу.

## Синтаксис
```bash
chown [OPTIONS] OWNER[:GROUP] FILE
```

## Основні ключі
| ключ        | значення           |
| ----------- | ------------------ |
| -R          | рекурсивно         |
| -v          | verbose            |
| -c          | тільки змінені     |
| --reference | копіювати власника |

## Власник і група

Кожен файл має:
- owner
- group

Перевірити:
```bash
ls -l
```
Приклад
```
-rw-r--r-- 1 user developers 1200 file.txt
```

## Приклади використання
- Зміна власника
  ```bash
  chown user1 file.txt
  ```

- Зміна групи
  ```bash
  chown :developers file.txt
  ```

- Зміна власника і групи
  ```bash
  chown user1:developers file.txt
  ```

- Рекурсивна зміна
  ```bash
  chown -R user1 project/
  ```

- Копіювання власника
  ```bash
  chown --reference=file1 file2
  ```

## Важливі нюанси

Змінювати власника може:
- root
- суперкористувач