# 🔐 Як налаштувати SSH-доступ до GitHub:

## ✅ 1. Перевір, чи в тебе вже є SSH-ключ:
```bash
ls ~/.ssh
```
Шукай файли типу id_rsa / id_ed25519 та відповідні .pub.

## ✅ 2. Якщо нема — створи новий ключ:
```bash
ssh-keygen -t ed25519 -C "твій-email@пошта.com"
```
(або -t rsa якщо ed25519 не підтримується)

Після цього натискай Enter кілька разів (можеш задати пароль до ключа або залишити порожнім).

Файл зазвичай створиться в:

`~/.ssh/id_ed25519` (приватний)

`~/.ssh/id_ed25519.pub`(публічний)

## ✅ 3. Додай SSH-ключ до GitHub:
Скопіюй вміст публічного ключа:

```bash
cat ~/.ssh/id_ed25519.pub
```

Скопійований текст додай тут:

👉 https://github.com/settings/keys

→ New SSH key
→ Назви ключ (наприклад, "my-laptop")
→ Встав → Зберегти

## ✅ 4. (Опціонально) Додай агенту SSH:
Щоб не вводити пароль до ключа щоразу:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

## ✅ 5. Перевір підключення до GitHub:
```bash
ssh -T git@github.com
```

У відповідь має бути щось типу:

```rust
Hi {username}! You've successfully authenticated...
```

## ✅ 6. Переконайся, що використовуєш SSH-URL репозиторію:
```bash
git remote -v
```

Ти маєш побачити:

```scss
origin  git@github.com:username/your-repo.git (fetch)
```
❗ Якщо ти бачиш https://..., зміни:

```bash
git remote set-url origin git@github.com:username/your-repo.git
```
