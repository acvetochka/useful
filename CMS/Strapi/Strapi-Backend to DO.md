## 1. ⚙️ Налаштування GitHub Actions для бекенду
Створи файл .github/workflows/deploy-backend.yml з наступним вмістом:

```yaml
name: Deploy Backend to DigitalOcean

on:
  push:
    branches:
      - main
    paths:
      - 'backend/**'

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Deploy over SSH
        uses: appleboy/ssh-action@v1.0.0
        with:
          host: ${{ secrets.DO_HOST }}
          username: ${{ secrets.DO_USER }}
          key: ${{ secrets.DO_SSH_KEY }}
          script: |
            cd ~/handmade-shop/backend
            git pull origin main
            npm install
            npm run build
            pm2 restart backend
```

## 2. 🔐 Secrets у GitHub
У репозиторії на GitHub перейдіть до `Settings` > `Secrets and variables` > `Actions` і додайте наступні секрети:

`DO_HOST`: IP-адреса або домен вашого Droplet на DigitalOcean.

`DO_USER`: Ім'я користувача для SSH (зазвичай root або інше).

`DO_SSH_KEY`: Приватний SSH-ключ для підключення до сервера.

## 3. 🖥️ Налаштування сервера на DigitalOcean
   
1) Клонування репозиторію:

    ```bash
    git clone https://github.com/acvetochka/handmade-shop.git
    ```

2) Перехід до папки бекенду:

    ```bash
    cd handmade-shop/backend
    ```

3) Встановлення залежностей:
  
    ```bash
    npm install
    ```

4) Збірка та запуск:

    ```bash
    npm run build   # якщо потрібно
    pm2 start npm --name "backend" -- run start
    ```

    Примітка: Переконайся, що pm2 встановлено на сервері. Якщо ні, встанови його:

    ```bash
    npm install -g pm2
    ```

## 4. 🌐 Налаштування Nginx для проксі
Щоб зробити бекенд доступним за маршрутом /backend або /admin, налаштуй Nginx:

1) Встановлення Nginx (якщо ще не встановлено):

    ```bash
    sudo apt update
    sudo apt install nginx
    ```

2) Налаштування конфігурації:

- Відкрий файл конфігурації Nginx:

  ```bash
  sudo nano /etc/nginx/sites-available/default
  ```
  
- Додай наступні блоки:

  ```nginx
  location /backend/ {
      proxy_pass http://localhost:1337/;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
  }
  
  location /admin/ {
      proxy_pass http://localhost:1337/admin/;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
  }
  ```
  
  Примітка: Замініть localhost:1337 на порт, на якому працює ваш бекенд.

- Перевірка та перезапуск Nginx:

  ```bash
  sudo nginx -t
  sudo systemctl restart nginx
  ```

## ✅ Підсумок
GitHub Actions автоматично оновлюватиме бекенд при кожному пуші в гілку main.

Nginx проксіює запити до бекенду, роблячи його доступним за маршрутами /backend або /admin.

PM2 забезпечує постійний запуск бекенду на сервері.
