# CMS

# Menu
1. [CMS: Що це таке?](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-cms-%D1%89%D0%BE-%D1%86%D0%B5-%D1%82%D0%B0%D0%BA%D0%B5)
2. [Основні функції CMS](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97-cms)
3. [Типи CMS](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-%D1%82%D0%B8%D0%BF%D0%B8-cms)
4. [Різниця між типами CMS](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-%D1%80%D1%96%D0%B7%D0%BD%D0%B8%D1%86%D1%8F-%D0%BC%D1%96%D0%B6-%D1%82%D0%B8%D0%BF%D0%B0%D0%BC%D0%B8-cms)
5. [eCommerce CMS](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-ecommerce-cms)
   - [Типи eCommerce CMS](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#%D1%82%D0%B8%D0%BF%D0%B8-ecommerce-cms)
6. [Загальна таблиця CMS: традиційні та headless](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-%D0%B7%D0%B0%D0%B3%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8F-cms-%D1%82%D1%80%D0%B0%D0%B4%D0%B8%D1%86%D1%96%D0%B9%D0%BD%D1%96-%D1%82%D0%B0-headless)
7. [Headless CMS (API-first, JAMstack-підхід)](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-headless-cms-api-first-jamstack-%D0%BF%D1%96%D0%B4%D1%85%D1%96%D0%B4)
8. [Яку CMS обрати — за потребами](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#-%D1%8F%D0%BA%D1%83-cms-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%B8--%D0%B7%D0%B0-%D0%BF%D0%BE%D1%82%D1%80%D0%B5%D0%B1%D0%B0%D0%BC%D0%B8)
9. [Технологічна відповідність](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#%EF%B8%8F-%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%87%D0%BD%D0%B0-%D0%B2%D1%96%D0%B4%D0%BF%D0%BE%D0%B2%D1%96%D0%B4%D0%BD%D1%96%D1%81%D1%82%D1%8C)
10. [Актуальність CMS у 2025 році?](https://github.com/acvetochka/useful/blob/main/CMS/CMS.md#%D0%B0%D0%BA%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%D1%81%D1%82%D1%8C-cms-%D1%83-2025-%D1%80%D0%BE%D1%86%D1%96)
    

## 📚 CMS: Що це таке?
`CMS (Content Management System)` — це система керування контентом, яка дозволяє створювати, редагувати, публікувати та керувати вебсайтами без необхідності програмування (або з мінімальним знанням коду).

## 🔑 Основні функції CMS:
- Додавання та редагування контенту (текстів, зображень, відео)

- Створення сторінок та структур сайту

- Користувацьке управління (ролі, доступи)

- SEO-налаштування, розширення через плагіни

- Зберігання даних (іноді з БД, іноді — у файлах)

## 🧩 Типи CMS
| Тип CMS	| Опис	| Приклади |
| ------- | ----- | -------- |
| Традиційна CMS	| Фронтенд і бекенд у єдиній системі. Відразу виводить сторінки з бази на сервері.	| WordPress, Joomla, Drupal |
| Headless CMS	| Лише бекенд для контенту. Фронтенд підключається через API (REST або GraphQL).	| Strapi, Sanity, Contentful |
| Decoupled CMS	| Переходна форма між традиційною та headless — має API, але також і фронтенд.	| Directus, Drupal (у headless режимі) |
| Статична CMS (Flat-file)	| Контент зберігається у вигляді файлів (без бази даних), швидкий та легкий варіант.	| Grav, Hugo, Jekyll |

## 🆚 Різниця між типами CMS
| Ознака | 	Традиційна CMS	| Headless CMS |	Статична CMS |
| ------ | ---------------- | ------------ | ------------- |
| Контроль над фронтендом	| Є (вбудовані шаблони)	| Немає, підключається окремо |	Повний контроль, сам код|
| Гнучкість	| Середня	| Висока	| Висока |
| Швидкість |	Помірна (сервер рендерить) |	Висока (через API + CDN)	| Дуже висока (статичні файли) |
| Для кого підходить	| Контент-мейкерів, блогерів	| Розробників, команд	| Розробників, технічних сайтів |

## 🛒 eCommerce CMS 
eCommerce CMS — це не зовсім окремий архітектурний тип, а спеціалізована категорія CMS, яка:

- створена для продажу товарів і керування інтернет-магазином;

- має модулі або інтегровані функції: каталог, корзина, оплата, доставка, аналітика.

### Типи eCommerce CMS:
| Категорія	| Опис	| Приклади| 
| --------- | ----- | ------- |
| Спеціалізовані eCommerce CMS	| Побудовані виключно для eCommerce	| Magento, PrestaShop, Shopware |
| Плагіни до класичних CMS	| Класичні CMS із eCommerce-модулями	| WordPress + WooCommerce, Joomla + VirtueMart |
| Headless eCommerce CMS |	API-орієнтовані платформи для створення JAMstack-магазинів | Commerce Layer, Medusa, Saleor |

## 📚 Загальна таблиця CMS: традиційні та headless
| CMS	| Тип	| Мова / Фреймворк |	Призначення	| Особливості	| Недоліки |
| --- | --- | ---------------- | ------------ | ----------- | -------- |
| WordPress	| Класична |	PHP, MySQL	| Блоги, сайти, малі магазини| 	Найпопулярніша CMS, багато тем/плагінів, легко налаштовується |	Безпека, повільність без оптимізації, залежність від плагінів |
| Joomla!	| Класична	| PHP | 	Портали, каталоги, багатомовні сайти	| Гнучка система ACL, підтримка розширень |	Складніша структура, нижча популярність |
| Drupal	| Класична |	PHP (Symfony) |	Великі портали, урядові сайти |	Висока безпека, гнучкість, кастомізація |	Високий поріг входу |
| Typo3	| Класична	| PHP	| Корпоративні сайти, інституції	| Потужна система доступу, масштабованість	| Складне налаштування, мало розробників |
| Magento	| eCommerce	| PHP (Zend)	| Великі онлайн-магазини	| Потужна функціональність, мульти-магазинність |	Важка система, потребує ресурсів |
| PrestaShop	| eCommerce	| PHP (частково Symfony)	| Малі/середні магазини	Велика база модулів, кастомізація |	Повільна при великій кількості товарів |
| OpenCart	| eCommerce	| PHP, MVC	| Простий інтернет-магазин	| Простота використання, багато тем	| Слабка масштабованість |
| WooCommerce	| eCommerce	| PHP (плагін до WordPress)	| Невеликі магазини	| Інтеграція з WP, гнучкість, багато платіжних шлюзів |	Важко масштабувати, залежність від WP | 
| Ghost |	Класична |	Node.js, Express	| Блоги, публікації	| Markdown, мінімалізм, висока швидкість	| Обмежене розширення |
| Grav |	Flat-file	| PHP, YAML |	Легкі сайти без БД	| Без БД, швидкий рендеринг, flat-file структура |	Складна інтеграція плагінів|

## 🧩 Headless CMS (API-first, JAMstack-підхід)
| CMS	| Тип	| Мова / Фреймворк |	Призначення	| Особливості	| Недоліки |
| --- | --- | ---------------- | ------------ | ----------- | -------- |
| Sanity | 	Headless |	Node.js, JavaScript	| Контент для веб/моб. додатків	| Real-time редагування, GROQ, інтеграція з React/Next.js	| SaaS-модель, потребує хмарного акаунта, обмеження тарифу |
| Strapi	| Headless |	Node.js, JavaScript	| Створення API для контенту |	REST/GraphQL API, UI панель, self-hosted або cloud	| ACL, I18n — платні функції у безкоштовній версії |
| Payload CMS |	Headless |	Node.js, TypeScript |	Повний backend + CMS |	Кастомізований backend, TypeScript, self-hosted	| Потрібен хостинг і досвід з Node.js| 
| Contentful	| Headless	| SaaS, GraphQL/REST API	| Сайти, мобільні додатки |	Cloud CMS, гнучке моделювання, SDK	| Висока ціна, залежність від хмари |
| Directus	| Headless	| Node.js, MySQL/Postgres	| No-code/low-code контентні системи |	Автоматичне API, UI інтерфейс, self-hosted/cloud	| Орієнтація на SQL, складніші кастомні інтеграції |

## 🔧 Яку CMS обрати — за потребами:
| Ситуація / Проєкт	| Рекомендовані CMS |
| ----------------- | ----------------- |
| Блог, особистий сайт	| WordPress, Ghost, Grav |
| Корпоративний сайт	| Joomla, Drupal, Typo3 |
| Онлайн-магазин (eCommerce)	| WooCommerce, Magento, Shopify, PrestaShop| 
| JAMstack сайт (React, Next.js, Vue)	| Strapi, Payload CMS, Sanity |
| Мобільний застосунок або SPA | 	Contentful, Strapi |
| Потрібен no-code / auto-генерація API |	Directus |
| Повний контроль над бекендом + CMS	| Payload CMS |

## 🗃️ Технологічна відповідність
| Мова / Стек	| Сумісні CMS |
| ----------- | ----------- |
| PHP	| WordPress, Joomla, Drupal, Magento, PrestaShop, Typo3, Grav |
| Node.js / JS	| Ghost, Sanity, Strapi, Payload CMS, Directus |
| SaaS (пропрієтарний) |	Shopify, Contentful |
| SQL (MySQL/Postgres) |	WordPress, Joomla, Strapi, Directus |

## Актуальність CMS у 2025 році?
| CMS |	Актуальність 2025	| Коментар |
| ---- | ---------------- | --------- |
| WordPress	| 🔥 Дуже актуальна	 | Лідер ринку CMS (понад 40% усіх сайтів), активно підтримується. |
| Joomla	| ⚠️ Спад популярності	| Ще використовується, але спільнота скорочується, оновлення рідше. |
| Drupal	| ✅ Актуальна	| Широко використовується в урядових та корпоративних системах. |
| Typo3	| ✅ Локальна актуальність	| Часто використовується в Німеччині та Австрії, особливо в B2B. |
| Magento	| ⚠️ Менш популярна |	Adobe активно підтримує Magento 2, але Shopify її витісняє. |
| PrestaShop	| ✅ Помірна популярність	| Все ще використовується в малому eCommerce. |
| OpenCart	| ⚠️ Застаріває	| Має свою нішу, але поступається сучасним рішенням. |
| WooCommerce	| 🔥 Дуже актуальна	| Найпопулярніше рішення eCommerce на WordPress. |
| Ghost	| ✅ Сучасна	| Активно використовується для блогів, швидкий, з мінімалістичним дизайном. |
| Grav	| 🔍 Нішевий варіант	| Популярний серед розробників, які не хочуть використовувати БД. |
| Strapi	| 🔥 Суперактуальна	| Один з топових headless CMS, активно зростає. |
| Sanity	| 🔥 Суперактуальна	| Один з лідерів серед хмарних headless CMS для JAMstack. |
| Payload CMS	| 🔥 Дуже перспективна	| Нове, активно розвивається, улюблене серед TypeScript-розробників.|
| Directus |	✅ Актуальна	| Популярний серед no-code/low-code рішень для SQL-баз. |
| Contentful	| 🔥 Сучасна	| Часто використовується в великих SaaS проєктах і мобільних застосунках. |
