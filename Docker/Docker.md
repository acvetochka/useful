# Конспект по Docker

## 1. Вступ у Docker

`Docker` – це платформа для контейнеризації, яка дозволяє запускати додатки в ізольованих середовищах (контейнерах). Docker забезпечує портативність, ефективність використання ресурсів та зручність розгортання додатків.

### Основні поняття:

`Образ (Image)` – шаблон, з якого створюється контейнер.

`Контейнер (Container)` – запущений екземпляр образу.

`Dockerfile` – файл зі списком команд для створення образу.

`Docker Hub` – репозиторій для зберігання та обміну образами.

`Docker Engin`e – рушій, який керує контейнерами.

## 2. Встановлення Docker

`Для Windows:`

Завантажити Docker Desktop із [офіційного сайту](https://www.docker.com/)

Включити WSL 2 (Windows Subsystem for Linux)

`Для Linux (Ubuntu):`

```bash
sudo apt update
sudo apt install docker.io -y
```

Для macOS:

Завантажити Docker Desktop

Перевірити встановлення:

```bash
docker --version
```

## 3. Основні команди Docker

Робота з контейнерами:

- Запустити контейнер:

  ```bash
  docker run -d --name my_container nginx
  ```

- Переглянути запущені контейнери:

  ```bash
  docker ps
  ```

- Переглянути всі контейнери (включаючи зупинені):

  ```bash
  docker ps -a
  ```

- Зупинити контейнер:

  ```bash
  docker stop my_container
  ```

- Видалити контейнер:
  
  ```bash
  docker rm my_container
  ```

Робота з образами:

- Переглянути список локальних образів:

  ```bash
  docker images
  ```

- Завантажити образ із Docker Hub:

  ```bash
  docker pull ubuntu
  ```

- Видалити образ:

  ```bash
  docker rmi ubuntu
  ```

Робота з Dockerfile:

Створити файл Dockerfile:

  ```yaml
  FROM ubuntu:latest
  RUN apt update && apt install -y curl
  CMD ["bash"]
  ```

Зібрати образ:

  ```bash
  docker build -t my_image .
  ```


## 4. Dockerfile

Dockerfile (Створення власного образу)

`Dockerfile` – це текстовий файл, що містить інструкції для створення образу Docker.

Основні команди Dockerfile:

`FROM` – задає базовий образ:

  ```Dockerfile
  FROM ubuntu:latest
  ```

`RUN` – виконує команди під час побудови образу:

  ```Dockerfile
  RUN apt update && apt install -y curl
  ```

`COPY`– копіює файли з локальної системи в контейнер:

  ```Dockerfile
  COPY index.html /var/www/html/
  ```

`ADD` – копіює файли, підтримує архіви:

  ```Dockerfile
  ADD app.tar.gz /app/
  ```

`WORKDIR` – змінює робочу директорію:

  ```Dockerfile
  WORKDIR /app
  ```

`CMD` – задає команду, що виконується під час запуску контейнера:

  ```Dockerfile
  CMD ["nginx", "-g", "daemon off;"]
  ```

`ENTRYPOINT` – задає основний процес контейнера:

  ```Dockerfile
  ENTRYPOINT ["python", "app.py"]
  ```

`EXPOSE` – відкриває порт:

  ```Dockerfile
  EXPOSE 80
  ```

`ENV` – задає змінні середовища:

  ```Dockerfile
  ENV APP_ENV=production
  ```

Приклад Dockerfile для Node.js:

  ```Dockerfile
  FROM node:16
  WORKDIR /app
  COPY package.json .
  RUN npm install
  COPY . .
  EXPOSE 3000
  CMD ["node", "server.js"]
  ```

Створення образу з Dockerfile:

  ```shell
  docker build -t my_image .
  ```

## 5. Робота з мережами

Переглянути мережі Docker:

  ```bash
  docker network ls
  ```

Створити мережу:

  ```bash
  docker network create my_network
  ```

Підключити контейнер до мережі:

  ```bash
  docker network connect my_network my_container
  ```

## 6. Docker Volumes (Збереження даних)

Створити том:

  ```bash
  docker volume create my_volume
  ```

Запустити контейнер з томом:

  ```bash
  docker run -d -v my_volume:/data nginx
  ```

## 7. Docker Compose (оркестрація контейнерів)

Docker Compose дозволяє запускати декілька контейнерів одночасно за допомогою docker-compose.yml.

Приклад docker-compose.yml:

  ```yaml
  version: '3'
  services:
    web:
      image: nginx
      ports:
        - "8080:80"
    db:
      image: postgres
      environment:
        POSTGRES_PASSWORD: example
  ```

Запустити:

  ```bash
  docker-compose up -d
  ```

Зупинити:

  ```bash
  docker-compose down
  ```

## 8. Моніторинг та налагодження

Переглянути логи контейнера:

  ```bash
  docker logs my_container
  ```

Підключитися до контейнера:

  ```bash
  docker exec -it my_container bash
  ```

Моніторинг ресурсів контейнерів:

  ```bash
  docker stats
  ```

## 9. Оптимізація образів

- Використовуйте мінімальні базові образи (alpine, slim)

- Об’єднуйте RUN команди в одному шарі:

  ```bash
  RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*
  ```

- Використовуйте .dockerignore, щоб виключати непотрібні файли:

  ```
  node_modules
  .git
  *.log
  ```

## Висновки

Docker – це потужний інструмент для контейнеризації додатків, що спрощує розгортання, масштабування та тестування. Він забезпечує ізольоване середовище для роботи, покращує портативність програм та зменшує залежності від хост-системи.

