# Перенесення сайту на сервер DigitalOcean

## Крок 1: Створення облікового запису DigitalOcean
1. Зареєструйся на DigitalOcean, якщо в тебе ще немає облікового запису.
2. Після реєстрації додай спосіб оплати (для використання хмарного сервера).

## Крок 2: Створення Droplet (сервера)
1. Увійди в обліковий запис DigitalOcean.
2. На панелі керування натисни Create і вибери Droplets.
3. Вибери образ операційної системи. Зазвичай використовують Ubuntu (рекомендую останню стабільну версію, наприклад, Ubuntu 22.04).
4. Вибери план. Для невеликих проєктів вистачить базового плану з 1 CPU та 1 GB RAM.
5. Вибери локацію (регіон), де розміщуватиметься сервер. Вибирай найближчий регіон до твоєї аудиторії.
6. Вибери спосіб автентифікації: SSH-ключі (рекомендовано для безпеки) або пароль.
   Якщо обираєш SSH-ключ, створений на твоєму комп’ютері, додай його.
   <details>
      <summary>Кроки для створення Droplet з SSH-ключем:</summary>
    Створення SSH-ключа (якщо у тебе його ще немає):
      
    - Відкрий термінал на своєму комп’ютері.
    
    - Виконай команду:
      ```bash
      ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
      ```
      Ти можеш залишити значення за замовчуванням для збереження файлу ключа, натиснувши Enter.
  
      <details>
        <summary>Значення параметрів</summary>
        
        - `-t rsa`: Цей параметр вказує тип ключа, який ти створюєш. У цьому випадку, це RSA (Rivest–Shamir–Adleman) — один із найпоширеніших алгоритмів для генерації ключів.
        
        - `-b 4096`: Це параметр, який визначає довжину ключа в бітах. Значення 4096 означає, що ключ буде мати довжину 4096 біт. Чим більший розмір ключа, тим більша його безпека, оскільки він буде важчим для злому.
        
          Зазвичай рекомендується використовувати ключі завдовжки не менше 2048 біт, але 4096 біт забезпечує ще більший рівень захисту.
        - `-C "your_email@example.com"`: Цей параметр дозволяє додати коментар до ключа. Зазвичай це використовується для того, щоб вказати, кому належить ключ (часто це адреса електронної пошти).
      </details>
      
      Ключ буде згенеровано, і ти зможеш знайти його в папці `~/.ssh/` (файли за замовчуванням: `id_rsa` — приватний ключ, `id_rsa.pub` — публічний ключ).
    
    - Скопіювати публічний ключ:
    
      Використай команду, щоб скопіювати публічний ключ у буфер обміну:
      ```bash
      cat ~/.ssh/id_rsa.pub
      ```
      
      Скопіюй вміст, який з'явиться в терміналі.
    
    - Створення нового Droplet:
    
      - Увійди до панелі керування DigitalOcean.
      - Перейди до розділу Droplets та натисни Create Droplet.
      - Вибери образ операційної системи, тип Droplet, та інші параметри.
    
    - Додати SSH-ключ:
    
      - На етапі створення Droplet знайди секцію `Authentication`.
      - Вибери опцію `SSH keys`.
      - Встав публічний ключ, який ти скопіювала раніше, у поле для ключа.
      - Дай Droplet ім'я та заверши його створення, натиснувши на Create Droplet.
    
    - Отримання IP-адреси:
    
      Після створення Droplet ти зможеш побачити його IP-адресу у списку Droplets.
    </details>
   
8. Натисни Create Droplet.

## Крок 3: Підключення до Droplet
1. Після створення Droplet, ти отримаєш IP-адресу.
2. Відкрий термінал на своєму комп'ютері та підключись до сервера за допомогою SSH:
    ```bash
    ssh root@IP-адреса
    ```
    Якщо використовується пароль, введи його або використай SSH-ключ.

## Крок 4: Встановлення необхідного ПЗ на сервері
1. Онови систему:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
2. Встанови веб-сервер Nginx:
    ```bash
    sudo apt install nginx -y
    ```
3. Встанови Node.js та npm (якщо потрібно для твого проєкту):
    - Додай репозиторій:
      ```bash
        curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
      ```
    - Встанови Node.js:
      ```bash
      sudo apt install -y nodejs
      ```

4. Встанови Git, щоб клонувати репозиторій проєкту:
    ```bash
    sudo apt install git -y
    ```

## Крок 5: Клонування твого проєкту на сервер
1. Увійди в потрібну директорію (наприклад, /var/www/):
    ```bash
    cd /var/www/
    ```

2. Клонуй репозиторій фронтенду та бекенду:
    ```bash
    git clone https://github.com/твій-акаунт/твій-фронтенд.git
    git clone https://github.com/твій-акаунт/твій-бекенд.git
    ```

## Крок 6: Налаштування Nginx для хостингу сайту
1. Створи новий конфігураційний файл Nginx:

    ```bash
    sudo nano /etc/nginx/sites-available/твій-сайт
    ```

2. Додай конфігурацію (приклад для Node.js або статичного сайту):

    ```nginx
    server {
        listen 80;
        server_name твій_домен або IP;
    
        root /var/www/твій-фронтенд;
    
        location / {
            try_files $uri $uri/ =404;
        }
    
        location /api/ {
            proxy_pass http://localhost:порт_твого_бекенду;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
    
    - root — шлях до твого фронтенд проєкту.
    - location /api/ — для пересилання запитів до бекенду.

3. Створи символічне посилання для активації конфігурації:

    ```bash
    sudo ln -s /etc/nginx/sites-available/твій-сайт /etc/nginx/sites-enabled/
    ```

4. Перевір конфігурацію на помилки:

    ```bash
    sudo nginx -t
    ````

5. Перезапусти Nginx:

    ```bash
    sudo systemctl restart nginx
    ```

## Крок 7: Налаштування домену (якщо в тебе є домен)

1. Увійди до свого провайдера домену та зміни DNS-записи:
   - Створи A-запис, який вказуватиме на IP-адресу твого сервера.
2. У Nginx заміни `server_name` на твій домен.

<details>
  <summary>Детальна інструкція налаштування домену Namecheap</summary>

  1. Налаштуй DNS на Namecheap

     Вхід до панелі управління Namecheap
      - Увійди до свого облікового запису на Namecheap.
      - Перейди до "Domain List" на лівій панелі і знайди свій домен.
      - Натисни кнопку "Manage" біля домену.
     
      Налаштування DNS
      - У вкладці "Domain" шукай розділ "Nameservers". За замовчуванням, Namecheap використовує свої власні сервери імен. Тобі слід змінити ці налаштування на DNS-сервери DigitalOcean.
      - Вибери опцію "Custom DNS" і введи наступні значення:
          ```
          ns1.digitalocean.com
          ns2.digitalocean.com
          ns3.digitalocean.com
          ```
      - Натисни кнопку "Save", щоб зберегти зміни.
      Це налаштує твої DNS-записи для використання з серверами DigitalOcean.
      
   2. Налаштуй DNS-записи в DigitalOcean

      Додавання домену до DigitalOcean
      - Увійди до свого облікового запису на DigitalOcean.
      - Перейди до Networking у верхньому меню.
      - У розділі "Domains", введи свій домен і натисни "Add Domain".
      
      Додавання A-запису
      - Попередньо треба повернути управління DNS назад до Namecheap:
          - У вкладці "Domain" шукай розділ "Nameservers"
          - Натисни на опцію "Change DNS Type".
          - Обери "Namecheap BasicDNS".
      - Перейди у розділ "Advanced DNS" - HOST RECORDS - "Add new record"
      - у розділі "Type" обери "A Record".
      - В полі "Hostname" залиш порожнє місце (або введи "@" для основного домену).
      - Введи свою IP-адресу сервера (IP-адреса твого серверу DigitalOcean, яку ти використовувала раніше).
      - Натисни "Create Record".
      
      Додавання CNAME-запису (для піддоменів)
      Якщо ти хочеш налаштувати піддомен (наприклад, `www.yourdomain.com`):
      
      - Створи новий запис типу CNAME.
      - У полі "Hostname" введи `www`.
      - У полі "Value" введи свій основний домен, наприклад `yourdomain.com`.
        
  3. Налаштування сервера на DigitalOcean

      Онови конфігурацію Nginx
      - Зайди на свій сервер через SSH.
      - Відкрий конфігураційний файл Nginx для свого сайту. Наприклад:
          ```bash
          sudo nano /etc/nginx/sites-available/default
          ```
      
      - Онови налаштування server_name у конфігураційному файлі Nginx, щоб включити твій новий домен. Наприклад:
          ```nginx
          server {
              listen 80;
              server_name yourdomain.com www.yourdomain.com;
          
              location / {
                  proxy_pass http://localhost:3000; # Або порт твого бекенду
                  proxy_http_version 1.1;
                  proxy_set_header Upgrade $http_upgrade;
                  proxy_set_header Connection 'upgrade';
                  proxy_set_header Host $host;
                  proxy_cache_bypass $http_upgrade;
              }
          }
          ```
      
      - Перевір конфігурацію Nginx на наявність помилок:
          ```bash
          sudo nginx -t
          ```
      
      - Перезапусти Nginx:
          ```bash
          sudo systemctl restart nginx
          ```

</details>

## Крок 8: SSL-сертифікат (HTTPS)
1. Встанови Certbot для автоматичної установки SSL-сертифікатів:
    ```shell
    sudo apt install certbot python3-certbot-nginx -y
    ```

2. Виконай команду для отримання сертифіката:
    ```bash
    sudo certbot --nginx -d твій_домен
    ```
3. Certbot налаштує автоматичне оновлення сертифікатів.

   Let's Encrypt SSL-сертифікати діють протягом 90 днів. Certbot може автоматично оновлювати сертифікати за допомогою системної утиліти cron.

    Щоб перевірити оновлення, запусти:

    ```bash
    sudo certbot renew --dry-run
    ```
    
    Якщо все працює правильно, сертифікат буде оновлено автоматично перед закінченням терміну.

<details>
  <summary>Встановлення SSL-сертифікату домену Namecheap</summary>

  Крок 1: Активувати SSL-сертифікат на Namecheap
  Якщо ти вже придбав SSL-сертифікат на Namecheap, активуй його:
  - Перейди в свій акаунт Namecheap.
  - Знайди свій сертифікат SSL.
  - Активуй SSL-сертифікат.
  - Тобі буде потрібно створити CSR (Certificate Signing Request). Це робиться на твоєму сервері DigitalOcean.
  
  Крок 2: Створення CSR на DigitalOcean
  - Увійди в свій сервер через SSH.
  - Запусти команду для створення CSR:
      ```bash
      openssl req -new -newkey rsa:2048 -nodes -keyout domain.key -out domain.csr
      ```
      Це запитає деякі дані:
      - Common Name (CN): Введи своє доменне ім'я (наприклад, `yourdomain.com`).
      - Інші поля можеш пропустити або заповнити як потрібно.
  - Скопіюй вміст файлу .csr, який ти створила (domain.csr), і встав його у відповідне поле на сторінці активації SSL-сертифіката на Namecheap.
    
  Крок 3: Встановлення сертифіката SSL на сервері
  
  Після активації Namecheap надасть тобі сертифікат і інші файли (або ти отримаєш їх на електронну пошту). Тобі потрібно буде завантажити їх на сервер і налаштувати Nginx або Apache.
  
  Для Nginx:
  1. Завантаж сертифікат на сервер: Наприклад, завантаж його в `/etc/ssl/yourdomain.com/`.
  
  2. Змінити конфігурацію Nginx: Відкрий конфігураційний файл твого сайту:
  
      ```bash
      sudo nano /etc/nginx/sites-available/your-site
      ```
      І додай або зміні свої налаштування:
      
      ```nginx
      server {
          listen 443 ssl;
          server_name yourdomain.com;
      
          ssl_certificate /etc/ssl/yourdomain.com/your_cert.crt;
          ssl_certificate_key /etc/ssl/yourdomain.com/your_cert.key;
      
          root /var/www/your-site;
          index index.html;
      
          location / {
              proxy_pass http://localhost:3000;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header X-Forwarded-Proto $scheme;
          }
      }
      
      server {
          listen 80;
          server_name yourdomain.com;
          return 301 https://$server_name$request_uri;
      }
      ```
  3. Перезапустити Nginx:
  
      ```bash
      sudo systemctl restart nginx
      ```
  
  Крок 4: Перевірка SSL
    
  Після завершення налаштування ти можеш перевірити роботу SSL на таких сайтах, як:
    
  [SSL Checker](https://www.sslshopper.com/ssl-checker.html)
  
</details>

## Крок 9: Перенаправлення HTTP на HTTPS (для Nginx)
Після успішного отримання сертифіката, необхідно змінити конфігурацію веб-сервера для автоматичного перенаправлення з HTTP на HTTPS.

- Відкрий конфігураційний файл Nginx:

    ```bash
    sudo nano /etc/nginx/sites-available/твій-сайт
    ```
- Додай наступні налаштування для перенаправлення HTTP на HTTPS:

    ```nginx
    server {
        listen 80;
        server_name твій_домен_або_IP;
    
        location / {
            return 301 https://$server_name$request_uri;
        }
    }
    
    server {
        listen 443 ssl;
        server_name твій_домен_або_IP;
    
        ssl_certificate /etc/letsencrypt/live/твій_домен_або_IP/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/твій_домен_або_IP/privkey.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
    
        location / {
            proxy_pass http://localhost:3000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
    ```

- Перевір правильність конфігурації:

    ```bash
    sudo nginx -t
    ```
- Перезавантаж Nginx:

    ```bash
    sudo systemctl reload nginx
    ```

## Перевірка роботи сайту
1. Відкрий браузер і перейди за IP-адресою або доменом, щоб перевірити, чи сайт працює коректно.
2. Якщо є проблеми, перевір логи Nginx:
    ```lua
    sudo tail -f /var/log/nginx/error.log
    ```
<details>
  <summary>Перевірити статус бекенду</summary>
  
  - SSH-підключення до сервера: Якщо ти ще не підключився до свого сервера через SSH, зроби це, використовуючи команду:

      ```bash
      ssh root@IP_адреса_сервера
      ```

  - Перевірити активні процеси: Щоб побачити, чи запущений твій бекенд (наприклад, на Node.js, Python Flask, або будь-який інший), виконай команду для перегляду всіх запущених процесів:
  
      ```bash
      ps aux | grep <назва твого бекенду або технології>
      ```
      
      Наприклад,
      для бекенду, що запускається з файлу server.js
      ```bash
      ps aux | grep server.js
      ```

      для Node.js:
      
      ```bash
      ps aux | grep node
      ```
      Це виведе список процесів, де ти зможеш побачити, чи запущений твій додаток.
  
  - Перевірити порти: Твій бекенд, швидше за все, використовує певний порт для роботи (наприклад, 5000 або 3000). Щоб перевірити, чи щось працює на цьому порту:
  
      ```bash
      sudo lsof -i :<порт>
      ```
      
      Наприклад, для порту 3000:
      
      ```bash
      sudo lsof -i :3000
      ```
      
      Якщо є активний процес, ти побачиш виведення з інформацією про нього.
    
  </details>




## Передача секретів у DigitalOcean
Секрети (такі як ключі API, токени або паролі до баз даних) повинні бути збережені безпечно. Є кілька способів передати секрети на сервер у DigitalOcean.

### 1.1 Використання змінних середовища
Найбільш стандартний і безпечний спосіб зберігати секрети — використовувати змінні середовища.

1. Додай змінні середовища у свої конфігураційні файли: Наприклад, у твоєму бекенді може бути файл .env, де зберігаються секрети:

    ```makefile
    DB_PASSWORD=your_db_password
    API_KEY=your_api_key
    JWT_SECRET=your_jwt_secret
    ```

2. Завантаження файлу на сервер: Переконайся, що цей файл ніколи не додається у систему контролю версій, як-от GitHub. Для цього додай його до .gitignore. Завантаж файл .env на сервер через SCP або інший метод.

    ```bash
    scp .env root@IP_адреса_сервера:/var/www/your-backend-directory
    ```

3. Завантаження змінних через командний рядок: Якщо ти хочеш встановити змінні середовища через командний рядок, додай їх до конфігурації, наприклад, у файлі /etc/environment:

    ```bash
    sudo nano /etc/environment
    ```
    
    Впиши змінні:
    
    ```bash
    DB_PASSWORD=your_db_password
    API_KEY=your_api_key
    JWT_SECRET=your_jwt_secret
    ```
    
    Потім перезавантаж систему або сесію:
    
    ```bash
    source /etc/environment
    ```

### 1.2 Використання DigitalOcean Secrets (App Platform)
Якщо ти використовуєш DigitalOcean App Platform для хостингу, ти можеш додати секрети через інтерфейс платформи:

- Перейди до свого проекту на App Platform.
- Обери вкладку Settings та знайди розділ Secrets.
- Додай секрети, як-от API ключі, токени, паролі.
- Під час налаштування сервера, ти зможеш використати їх у своєму додатку.

## Використання PM2 для фонового запуску
Якщо хочеш запустити додаток у фоновому режимі, щоб він працював після виходу з SSH, встанови та використовуй PM2:

- Встанови PM2:

    ```bash
    sudo npm install -g pm2
    ```

- Запусти додаток через PM2:

    ```bash
    pm2 start server.js
    ```

- Перевір, чи додаток працює:

    ```bash
    pm2 list
    ```

## Моніторинг ресурсів сервера
Якщо ти хочеш перевірити ресурси конкретного Droplet (наприклад, використання диску, CPU або пам'яті), ти можеш скористатися наступними командами на своєму сервері через SSH:

- Перевірка використання диску:

    ```bash
    df -h
    ```
    Це покаже, скільки місця на диску використано і скільки залишилось.

- Перевірка використання пам'яті:

    ```bash
    free -h
    ```
    Це покаже, скільки оперативної пам'яті використано та скільки залишилось.

- Перевірка завантаженості CPU:

    ```bash
    top
    ```
    або
    
    ```bash
    htop
    ```
    Ці команди показують поточне навантаження на процесор і інші системні ресурси.
