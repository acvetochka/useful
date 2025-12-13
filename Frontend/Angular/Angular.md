# Angular — повна інструкція з прикладами

## 1. Що таке Angular

Angular — це фреймворк для створення SPA (Single Page Applications) від Google. Він використовує TypeScript, має чітку архітектуру та підходить для великих і складних проєктів.

Ключові особливості:

- Component-based архітектура

- TypeScript з коробки

- Dependency Injection

- RxJS (реактивне програмування)

- Вбудований router

- Форми (Template-driven та Reactive)

- HTTP клієнт

- Signals (Angular 16+)



---

## 2. Встановлення Angular

Що тут відбувається простими словами?

Angular — це не одна бібліотека, а цілий набір інструментів. Щоб було зручно з ними працювати, існує Angular CLI — консольна програма, яка:

- створює проєкт

- запускає сервер

- збирає проєкт для продакшену


Вимоги:

Node.js — середовище для запуску JavaScript

npm — менеджер пакетів


Встановлення Angular CLI
```bash
npm install -g @angular/cli
```

Створення проєкту
```
ng new my-app
cd my-app
ng serve
```

👉 ng serve запускає локальний сервер


---

3. Структура проєкту
```
src/
 ├── app/
 │   ├── app.component.ts
 │   ├── app.component.html
 │   ├── app.component.scss
 │   ├── app.module.ts
 ├── assets/
 ├── environments/
```

---

## 4. Компоненти

Що таке компонент?

Компонент — це окремий шматок сторінки.

Наприклад:

- кнопка

- форма логіну

- список користувачів


У Angular вся сторінка складається з компонентів.

Створення компонента
```bash
ng generate component users
```

Компонент (логіка)
```javaStript
@Component({
  selector: 'app-users',
  templateUrl: './users.component.html'
})
export class UsersComponent {
  name = 'Anna';
}
```

👉 Тут ми просто створили змінну name

HTML (шаблон)
```html
<h1>Hello {{ name }}</h1>
```

👉 {{ }} означає: "покажи значення змінної"


---

## 5. Data Binding

Data Binding — це звʼязок між кодом і HTML.

1️⃣ Interpolation
```
{{ title }}
```
👉 Просто показуємо значення


---

2️⃣ Property binding
```
<img [src]="imageUrl">
```
👉 Передаємо значення в HTML-атрибут


---

3️⃣ Event binding
```
<button (click)="handleClick()">Click</button>
```
👉 Реагуємо на дію користувача


---

4️⃣ Two-way binding
```
<input [(ngModel)]="username">
```
👉 Дані синхронізуються в обидві сторони


---

## 6. Директиви

Директиви — це механізм Angular для розширення HTML. Вони дозволяють змінювати DOM, поведінку елементів та структуру шаблонів.

Типи директив:

- Структурні — змінюють DOM (*ngIf, *ngFor)

- Атрибутні — змінюють вигляд або поведінку (ngClass, ngStyle)

- Кастомні — власні директиви



---

## 7. Керуючі конструкції шаблонів (новий синтаксис Angular 17+)

Angular 17 представив новий template control flow синтаксис: @if, @for, @switch.
```
@if

@if (isLoggedIn) {
  <p>Welcome!</p>
} @else {
  <p>Please login</p>
}
```

🔹 *Плюси порівняно з ngIf:

- Немає прихованого <ng-template>

- Краще читається

- Менше магії

- Працює як звичайний JS if



---
```
@for

@for (user of users; track user.id) {
  <li>{{ user.name }}</li>
} @empty {
  <p>No users</p>
}
```
🔹 *Плюси порівняно з ngFor:

- Вбудований track (обовʼязковий → краща продуктивність)

- Є @empty без додаткового *ngIf

- Менше boilerplate



---
```
@switch

@switch (role) {
  @case ('admin') { <p>Admin</p> }
  @case ('user') { <p>User</p> }
  @default { <p>Guest</p> }
}
```
🔹 Переваги:

- Читабельніше за *ngSwitch

- JS-подібний синтаксис



---

Порівняльна таблиця

|Старий синтаксис	|Новий синтаксис|
|-----------------|---------------|

|*ngIf |	@if |
|*ngFor	|@for|
|*ngSwitch|	@switch|


✅ Рекомендація: використовувати новий синтаксис у нових проєктах


---

## 8. Сервіси та Dependency Injection

Створення сервісу
```bash
ng generate service auth
```

```
@Injectable({ providedIn: 'root' })
export class AuthService {
  isLoggedIn = false;
}
```
Використання

constructor(private auth: AuthService) {}


---

## 9. Routing
```
app-routing.module.ts

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'users', component: UsersComponent }
];
```

Router outlet
```
<router-outlet></router-outlet>
```

Навігація
```
<a routerLink="/users">Users</a>
```

---

## 10. Форми

Template-driven
```
<form #f="ngForm">
  <input name="email" ngModel>
</form>
```

Reactive Forms
```
this.form = new FormGroup({
  email: new FormControl('', Validators.required)
});

<form [formGroup]="form">
  <input formControlName="email">
</form>

```
---

## 11. HTTP Client
```
constructor(private http: HttpClient) {}

getUsers() {
  return this.http.get<User[]>('https://api.example.com/users');
}
```

---

## 12. RxJS

Observable
```
this.http.get(...).subscribe(data => {
  console.log(data);
});
```

Pipe
```
this.http.get(...).pipe(
  map(res => res.data),
  catchError(err => of([]))
)
```

---

## 13. Pipes

Вбудовані
```
{{ date | date:'short' }}
```

Кастомний pipe
```
@Pipe({ name: 'uppercaseCustom' })
export class UppercasePipe implements PipeTransform {
  transform(value: string) {
    return value.toUpperCase();
  }
}
```

---

## 14. Guards
```
canActivate(): boolean {
  return this.auth.isLoggedIn;
}
```

---

## 15. Lazy Loading
```
{
  path: 'admin',
  loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule)
}
```

---

## 16. Standalone Components (Angular 15+)
```
@Component({
  standalone: true,
  selector: 'app-demo',
  imports: [CommonModule]
})
export class DemoComponent {}
```

---

## 17. Signals (Angular 16+)

Signals — це новий реактивний примітив в Angular, альтернатива RxJS для локального та глобального стану.

Створення signal
```
count = signal(0);
```

Читання
```
<p>{{ count() }}</p>
```

Оновлення
```
this.count.set(10);
this.count.update(v => v + 1);
```

computed
```
double = computed(() => this.count() * 2);
```

effect
```
effect(() => {
  console.log(this.count());
});
```

🔹 Переваги:

- Синхронні

- Простіші за RxJS

- Автоматичний change detection



---

## 18. Керування стейтом (State Management)

Що таке стейт простими словами?

Стейт — це дані, які зберігає застосунок.

Наприклад:

- залогінений користувач

- список товарів

- кількість в кошику



---

1️⃣ Локальний стейт

count = 0;

👉 Дані живуть лише в одному компоненті

✔ Дуже просто ❌ Не підходить для великих застосунків


---

2️⃣ Сервіс як сховище даних
```
@Injectable({ providedIn: 'root' })
export class CounterStore {
  count = signal(0);
}
```
👉 Дані доступні багатьом компонентам

✔ Найпопулярніший варіант


---

3️⃣ Signals Store (найкращий варіант)
```
@Injectable({ providedIn: 'root' })
export class UserStore {
  user = signal<User | null>(null);
}
```
👉 Простий, швидкий, сучасний

✔ Рекомендовано Angular командою


---

4️⃣ RxJS

Складні потоки подій (websocket, autocomplete)


---

5️⃣ NgRx

Для дуже великих enterprise-проєктів


---

2️⃣ Сервіси як стейт-контейнер
```
@Injectable({ providedIn: 'root' })
export class CounterStore {
  count = signal(0);
}

constructor(public store: CounterStore) {}
```
✔ Поширений підхід ✔ Працює з Signals


---

3️⃣ Signals Store (рекомендовано)
```
@Injectable({ providedIn: 'root' })
export class UserStore {
  user = signal<User | null>(null);

  setUser(u: User) {
    this.user.set(u);
  }
}
```
✔ Мінімум коду ✔ Без RxJS ✔ Просте тестування


---

4️⃣ RxJS + BehaviorSubject
```
private user$ = new BehaviorSubject<User | null>(null);
```

✔ Потужний ❌ Багато boilerplate


---

5️⃣ NgRx

Redux-подібний state manager

Actions → Reducers → Store → Selectors


✔ Enterprise-рівень ❌ Складний


---

Порівняння

Підхід	Коли використовувати

Local state	Малий компонент
Service + Signals	90% проєктів
RxJS	Потоки подій
NgRx	Великий enterprise



---

## 19. Оптимізація

- OnPush ChangeDetection

- Lazy loading

- Signals замість RxJS де можливо



---

## 20. Тестування
```
it('should create', () => {
  expect(component).toBeTruthy();
});
```

---

## 21. Робота з API (HTTP)

Що таке API?

API — це сервер, з яким ми спілкуємося:

отримати дані

відправити дані



---

Підключення HttpClient
```
@import { HttpClient } from '@angular/common/http';

constructor(private http: HttpClient) {}
```

---

GET — отримати дані
```
getUsers() {
  return this.http.get<User[]>('https://api.example.com/users');
}
```
👉 get — отримати


---

POST — відправити дані
```
createUser(user: User) {
  return this.http.post('https://api.example.com/users', user);
}
```

👉 post — створити


---

Виклик у компоненті
```
this.api.getUsers().subscribe(users => {
  this.users = users;
});
```
👉 subscribe означає: "коли сервер відповість"


---

Обробка помилок
```
.pipe(
  catchError(() => of([]))
)
```

---

## 22. Білд і деплой
```
ng build --configuration=production
```
Результат у папці dist/


---

## 23. Коли використовувати Angular

✅ Великі проєкти ✅ Корпоративні системи ❌ Маленькі лендинги

