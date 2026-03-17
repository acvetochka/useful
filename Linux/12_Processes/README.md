🧩 Розділ 1. Основи процесів
Що таке процес
Програма vs процес
PID, PPID
Ієрархія процесів (дерево)
init / systemd

⚙️ Розділ 2. Життєвий цикл процесу
Стани процесу (running, sleeping, zombie…)
Створення процесу (fork, exec)
Завершення процесу (exit, signal)
Zombie та orphan процеси

🧠 Розділ 3. Планування процесів (Scheduling)
Що таке scheduler
Пріоритети (nice, renice)
Типи планування (CFS)
CPU time

🧵 Розділ 4. Потоки (Threads)
Процес vs потік
User threads vs kernel threads
multithreading в Linux

📊 Розділ 5. Управління процесами (команди)
ps
top / htop
kill / pkill / killall
jobs, fg, bg
nohup

🔗 Розділ 6. Міжпроцесна взаємодія (IPC)
pipes
signals
sockets
shared memory
message queues

🧬 Розділ 7. Сигнали (Signals)
Що це таке
Основні сигнали (SIGTERM, SIGKILL…)
Обробка сигналів

🧱 Розділ 8. Control groups (cgroups) і limits
обмеження ресурсів
ulimit
systemd slices

🔐 Розділ 9. Безпека процесів
права процесів
UID, EUID
setuid

🧰 Розділ 10. Systemd і сервіси
що таке unit
як працюють сервіси
daemon процеси

🧪 Розділ 11. Практичні сценарії
як знайти "важкий" процес
як дебажити
як вбити завислий процес
best practices
