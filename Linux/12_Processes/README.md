# 12_Processes

## 🧩 Розділ 1. Основи процесів
- Що таке процес
- Програма vs процес
- PID, PPID
- Ієрархія процесів
- init / systemd

## 🧠 Розділ 2. Типи процесів
- Користувацькі процеси (user processes)
- Процеси ядра (kernel processes / kernel threads)
- Демони (daemons)
- Інтерактивні vs фонові
- CPU-bound vs IO-bound

## ⚙️ Розділ 3. Життєвий цикл процесу
- Стани процесу
- fork(), exec()
- exit()
- zombie / orphan

## 🧵 Розділ 4. Потоки (Threads)
- Процес vs потік
- Kernel threads vs user threads
- multithreading

## 🔄 Розділ 5. Планування (Scheduling)
- scheduler
- nice / renice
- пріоритети

## 💻 Розділ 6. Jobs і робота shell
- Що таке job (завдання shell)
- foreground vs background
- &, jobs, fg, bg
- job ≠ process (важливе!)
- job control

## 📊 Розділ 7. Управління процесами (команди)
- ps
- top / htop
- kill / pkill / killall
- nohup

## 🔗 Розділ 8. Міжпроцесна взаємодія (IPC)
- pipes
- signals
- sockets
- shared memory

## 🔌 Розділ 9. Стандартні потоки (stdin, stdout, stderr)
👉 (це окремий фундаментальний розділ, не про threads!)
- stdin (0)
- stdout (1)
- stderr (2)
- перенаправлення (>, >>, <)
- пайпи (|)

## 🧬 Розділ 10. Signals
- що це
- основні сигнали
- обробка

## 🧱 Розділ 11. Ресурси і обмеження
- ulimit
- cgroups
- systemd slices

## 🔐 Розділ 12. Безпека процесів
- UID, EUID
- setuid

## 🧰 Розділ 13. systemd і демони
- сервіси
- daemon processes

## 🧪 Розділ 14. Практика і дебаг
- як знайти проблему
- як аналізувати процеси
