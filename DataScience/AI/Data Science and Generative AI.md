# Конспект: Наука про дані та Генеративний ШІ

## Популярні інструменти GenAI 
| Назва моделі	| Використання	| Посилання |
| ------------ | -------------- | --------- |
| Data Robot	| Простий інструмент, корисний для аналізу даних та побудови моделей	| https://www.datarobot.com/ |
| Mostly.AI	  | Генерація синтетичних даних	                                        | https://mostly.ai/ |
| ChatGPT	    | Модель на основі GPT, що використовується для генерації тексту та коду на основі запитів природною мовою	| https://openai.com/chatgpt |
| DB Sensei   |	Генерація SQL-запитів для баз даних за допомогою запитів природною мовою	| https://dbsensei.com/ |
| Hal9	| Інструмент EDA для виявлення ключових інсайтів у даних | 	https://www.hal9.com/ |
| Columns.ai	| Інструмент візуалізації даних для створення корисних графіків	| https://columns.ai/ |
| Akkio |	Інструмент візуалізації даних для створення графіків даних, таких як регресійні графіки, графіки коробок, кореляційні теплові карти тощо	| https://www.akkio.com/ |

## Важливі підказки для підготовки даних
| Завдання	| Підказка |
| --------- | -------- |
| Прочитати CSV файл даних і завантажити його в дата-фрейм.	| Напишіть код на Python, який може виконати такі завдання: <br/> Прочитати CSV файл, розташований за вказаним шляхом, у дата-фрейм Pandas, припускаючи, що перші рядки файлу є заголовками для даних. |
| Очистка даних: Визначити та замінити відсутні значення відповідно до наступних рекомендацій. <br/>1. Ви замінюєте відсутні записи в стовпцях, що містять категоріальні значення, на найчастіші записи <br/>2. Ви замінюєте відсутні записи в стовпцях з безперервними даними на середнє значення стовпця. <br/>3. Якщо значення відсутнє в цільовому стовпці, вам, можливо, потрібно буде видалити цей рядок	| Напишіть код на Python для виконання наступних завдань: <br/>1. Визначити атрибути з відсутніми значеннями. <br/>2. Сегрегувати ці атрибути на категоріальні та атрибути з безперервними значеннями. <br/>3. Видалити весь рядок, якщо значення відсутнє в цільовій змінній. <br/>4. Якщо значення відсутнє в категоріальному атрибуті, замініть відсутні значення на найчастіше значення в стовпці. <br/>5. Якщо значення відсутнє в атрибуті з безперервним значенням, замініть відсутні значення на середнє значення записів у стовпці. |
| Нормалізація даних: Нормалізувати атрибут до його максимального значення.	| Напишіть код на Python для нормалізації вмісту під вказаним атрибутом у дата-фреймі df до його максимального значення. Внесіть зміни в оригінальні дані і не створюйте новий атрибут.|
| Перетворення категоріальної змінної в індикаторні змінні	| Напишіть код на Python для виконання наступних завдань. <br/>1. Перетворіть атрибут дата-фрейму df в індикаторні змінні, збережені як df1, з правилами іменування “Name_<унікальне значення атрибута>”.<br/>2. Додайте df1 до оригінального дата-фрейму df.<br/>3. Видаліть оригінальний атрибут з дата-фрейму df. |

## Важливі підказки для генерації даних, інсайтів та візуалізацій
| Завдання |	Підказка |
| -------- | --------- |
| Генерувати статистичний опис даних. |	Напишіть код на Python для генерації статистичного опису всіх ознак, використаних у наборі даних. Включіть також типи даних “об’єкт”. |
| Створити регресійні графіки між цільовою змінною та змінною з неперервними значеннями.	| Напишіть код на Python для генерації регресійного графіка між цільовою змінною та змінною джерела з датафрейму. |
| Створити коробкові графіки між цільовою та категоріальною змінною.	| Напишіть код на Python для генерації коробкового графіка між цільовою змінною та змінною джерела з датафрейму. |
| Оцінити параметричну взаємозалежність за допомогою кореляції, p-значення та коефіцієнта Пірсона. |	Напишіть код на Python для оцінки кореляції, коефіцієнта Пірсона та p-значень для всіх атрибутів датафрейму відносно цільового атрибута. |
| Групувати змінні для створення зведених таблиць. Створити графік p-color для зведеної таблиці.	| Напишіть код на Python, який виконує наступні дії: <br/>1. Групує три атрибути, як це доступно в датафреймі df. <br/>2. Створює зведену таблицю для цієї групи, використовуючи цільовий атрибут та агрегатну функцію як середнє.<br/>3. Будує графік pcolor для цієї зведеної таблиці. |

## Важливі запити для розробки та вдосконалення моделі
| Завдання	| Запит |
| --------- | ----- |
| Лінійна регресія між одним атрибутом джерела та цільовим атрибутом і його оцінка	| Напишіть код на Python, який виконує такі завдання: <br/>1. Розробляє та навчає модель лінійної регресії, яка використовує один атрибут дата-фрейму як змінну джерела та інший як цільову змінну. <br/>2. Обчислює та відображає значення MSE та R^2 для навченої моделі. |
| Лінійна регресія між кількома атрибутами джерела та цільовими атрибутами і її оцінка	| Напишіть код на Python, який виконує такі завдання:<br/>1. Розробляє та навчає модель лінійної регресії, яка використовує деякі атрибути дата-фрейму як змінні джерела та один з атрибутів як цільову змінну.<br/>2. Обчислює та відображає значення MSE та R^2 для навченої моделі. |
| Поліноміальна регресійна модель з одною змінною джерела та цільовою змінною |	Напишіть код на Python, який виконує такі завдання: <br/>1. Розробляє та навчає кілька моделей поліноміальної регресії з порядками 2, 3 та 5, які використовують один атрибут дата-фрейму як змінну джерела та інший як цільову змінну.<br/>2. Обчислює та відображає значення MSE та R^2 для навчених моделей.<br/>3. Порівнює продуктивність моделей. |
| Створення конвеєра для масштабування, створення поліноміальних ознак та лінійної регресії	| Напишіть код на Python, який виконує такі завдання: <br/>1. Створіть конвеєр, який виконує масштабування параметрів, генерацію поліноміальних ознак та лінійну регресію. Використовуйте набір кількох ознак, як раніше, для створення цього конвеєра.<br/>2. Обчисліть та відобразіть значення MSE та R^2 для навченої моделі. |
| Пошук по сітці з рідж-регресією та крос-валідацією |	Напишіть код на Python, який виконує такі завдання: <br/>1. Використовуйте поліноміальні ознаки для деяких з атрибутів дата-фрейму.<br/>2. Виконайте пошук по сітці для моделі рідж-регресії для набору значень гіперпараметра alpha та поліноміальних ознак як вхідних даних.<br/>3. Використовуйте крос-валідацію в пошуку по сітці.<br/>4. Оцініть значення MSE та R^2 отриманої моделі. |



## Відповідальна генеративна ШІ для фахівців з даних

Генеративний ШІ, включаючи моделі, такі як GPT-3 або GPT-4, представляє як виклики, так і можливості. Виклики можуть включати упередженість і справедливість, етичне використання, пояснення, проблеми конфіденційності та екологічний вплив.

Щоб вирішити ці виклики, слід впроваджувати відповідальний ШІ, який також називають етичним або надійним ШІ, що включає усунення упередженості, кураторство різноманітних наборів даних та постійний моніторинг наявності упередженості.

### Відповідальна штучна інтелектуальна система 
AI-системи IBM побудовані на п’яти стовпах: `Пояснюваність`, `Справедливість`, `Стійкість`, `Прозорість` та `Конфіденційність`. Ці стовпи є критично важливими для розробки, впровадження та використання AI-систем.

Відповідальна штучна інтелектуальна система заохочує прозорість та відповідальність, дозволяючи користувачам розуміти процеси прийняття рішень і сприяючи довірі до технології. Вона також встановлює механізми, які дозволяють притягувати до відповідальності розробників, організації та AI-системи за їх дії та наслідки. Етичні принципи повинні бути розроблені та впроваджені, а галузеві стандарти повинні бути встановлені. Вкрай важливо інвестувати в дослідження для покращення інтерпретованості моделей і надання пояснень для згенерованих результатів. Питання конфіденційності повинні бути вирішені шляхом впровадження технологій, що зберігають конфіденційність, таких як федеративне навчання або диференційна конфіденційність.

Співпраця між дослідниками AI, етиками, політиками та громадськістю також є критично важливою для створення рекомендацій та політик для відповідальної розробки та впровадження AI. Користувачам слід надати можливість контролю, а також сприяти освіті та обізнаності щодо етичних наслідків генеративного AI. Відповідальна штучна інтелект дозволяє користувачам контролювати AI-системи, що дає їм змогу приймати обґрунтовані рішення щодо своїх взаємодій. Це формує довіру суспільства до технологій AI, що є критично важливим для їх широкого впровадження.

### Юридична та регуляторна відповідність
Відповідальна ШІ забезпечує відповідність систем ШІ існуючим законам та регуляціям, запобігаючи проблемам, пов’язаним з неетичною практикою. Її практики також можуть сприяти формуванню майбутніх регуляцій та стандартів у цій сфері.

### Соціальний вплив
Відповідальна ШІ є важливою для вирішення етичних, соціальних і практичних питань, пов’язаних з розробкою та впровадженням штучного інтелекту. Вона сприяє розвитку систем ШІ, які позитивно впливають на суспільство, вирішуючи реальні проблеми та сприяючи добробуту окремих осіб і спільнот. Її мета - запобігти шкоді, поважати права людини та забезпечити справедливе ставлення до всіх осіб. Крім того, вона сприяє інклюзивному дизайну, уникненню дискримінації та сприянню різноманітності. Екологічний вплив є ще однією перевагою, оскільки відповідальна ШІ сприяє сталим та екологічно чистим практикам у дослідженнях і впровадженні ШІ.

Довгострокова життєздатність також є критично важливою, оскільки неетичні чи безвідповідальні практики ШІ можуть призвести до суспільного протесту, правових дій та обмежень, що заважає довгостроковій життєздатності технологій ШІ.

Практики відповідальної ШІ включають прозорість, інклюзивність, безперервний моніторинг, співпрацю, надання можливостей користувачам, освіту та обізнаність, а також дотримання юридичних та регуляторних вимог. Прозорість щодо можливостей і обмежень генеративних моделей ШІ, інклюзивне представлення в навчальних даних та активна участь зацікавлених сторін є суттєвими.

Дотримання існуючих і нових регуляцій, пов’язаних із ШІ, та підтримка законодавства про відповідальну ШІ є важливими для розробки та впровадження генеративних моделей ШІ, які відповідають етичним принципам і суспільним цінностям.

Додаткове читання
[3 ключові причини, чому вашій організації потрібен Відповідальний ШІ](https://www.ibm.com/downloads/cas/NK0J1VEN) (Щоб відкрити цей PDF, утримуйте CTRL і клацніть правою кнопкою миші на посиланні, потім виберіть “Відкрити в новій вкладці”.)
