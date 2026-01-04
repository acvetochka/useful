# ДОВІДНИК ПО TESTING LIBRARY + JEST

## 🔹 0. Хто є хто
| Елемент |	Що це |
| ------- | ------ |
| test / it |	Опис одного тесту |
| describe |	Група тестів |
| render |	Малює компонент |
| screen	| Пошук елементів |
| expect |	Перевірка |
| mock |	Підміна функцій |
| userEvent |	Дії користувача |
| query / get / find	| Способи пошуку |

## 1️⃣ test / it
📌 Що це

Описує один тест — одну перевірку.

Синтаксис
```js
test('опис тесту', () => {
  // код тесту
});
```


Або:
```js
it('опис тесту', () => {
  // код тесту
});
```

🔹 test і it — повністю однакові

Приклад
```js
test('renders title', () => {
  render(<App />);
  expect(screen.getByText('Hello')).toBeInTheDocument();
});
```


## 🔹 describe
Для чого

Групує тести логічно.
```js
describe('Button component', () => {
  test('renders', () => {});
  test('handles click', () => {});
});
```

📌 Зручно для великих компонентів

## 2️⃣ render
📌 Що робить

render монтує React-компонент у віртуальний DOM

Синтаксис
```js
render(<Component />);
```

Приклад
```js
render(<Hello name="Anna" />);
```


🔹 Після цього компонент “існує” у тестовому браузері
```js
// render з props
render(<Button disabled />);

// render з wrapper (Router, Provider)
render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

## 3️⃣ screen
📌 Що це

screen — єдиний глобальний обʼєкт для пошуку елементів

❌ Погано:
```js
const { getByText } = render(...)
```

✅ Добре:
```js
screen.getByText(...)
```

## 4️⃣ QUERY — способи пошуку елементів

🔥 Головна формула
- `getByX`    → елемент МАЄ бути
- `queryByX`  → елемент МОЖЕ бути
- `findByX`   → елемент зʼявиться ПІЗНІШЕ

### 4.1 getBy...
📌 Для чого

Коли елемент обовʼязково є

Поведінка

❌ якщо нема — тест впаде

- 🔹 getByText

📌 Шукає видимий текст

```js
screen.getByText('Save');

screen.getByText(/save/i); // regex
```



- 🔹 getByRole ⭐ НАЙКРАЩИЙ
```js
screen.getByRole('button');

screen.getByRole('button', { name: 'Save' });
```

Часті ролі:
| Role |	HTML |
| ---- | ------| 
| button	| <button> |
| textbox |	<input> |
| heading |	<h1-h6> |
| link	| <a> |
| checkbox |	<input type="checkbox">|

- 🔹 getByLabelText
```js
<label>
  Email
  <input />
</label>

screen.getByLabelText('Email');
```

📌 Для форм — ідеально

- 🔹 getByPlaceholderText
```
<input placeholder="Email" />

screen.getByPlaceholderText('Email');
```

- 🔹 getByAltText
```js
<img alt="Avatar" />

screen.getByAltText('Avatar');
```

- 🔹 getByTitle
```js
<span title="Close" />

screen.getByTitle('Close');
```

- 🔹 *AllBy

📌 Повертає масив

```js
getAllByText
screen.getAllByRole('listitem');
```



- 🔹 getByTestId (останній варіант)
❗ Краще уникати

```js
<div data-testid="loader" />

screen.getByTestId('loader');
```




### 4.2 queryBy...
📌 Для чого

Коли елемент може бути або ні

Приклад
```js
expect(screen.queryByText('Error')).not.toBeInTheDocument();
```

❌ getByText тут би впав

### 4.3 findBy...
📌 Для асинхронного коду

⏱️ Чекає (за замовчуванням до 1000ms)
```
const message = await screen.findByText('Loaded');
```






## 5️⃣ expect
📌 Що це

expect — перевірка результату

Синтаксис
```js
expect(значення).matcher();
````

### 5.1 Основні матчери
- 🔹 toBeInTheDocument ⭐
```js
expect(element).toBeInTheDocument();
```

✔️ елемент є в DOM

🔹 not
expect(element).not.toBeInTheDocument();

🔹 toHaveTextContent
expect(element).toHaveTextContent('Hello');

🔹 toBeVisible
expect(element).toBeVisible();

🔹 toBeDisabled / Enabled
expect(button).toBeDisabled();

🔹 toHaveValue
expect(input).toHaveValue('Anna');

🔹 toHaveAttribute
expect(link).toHaveAttribute('href', '/home');

6️⃣ mock
📌 Що таке mock

Підміна реальної логіки

6.1 jest.fn()
const onClick = jest.fn();

<button onClick={onClick} />

expect(onClick).toHaveBeenCalled();

6.2 mockReturnValue
jest.fn().mockReturnValue(5);

6.3 mockResolvedValue (async)
fetchData = jest.fn().mockResolvedValue(data);

6.4 jest.mock()
jest.mock('./api', () => ({
  fetchUsers: jest.fn(),
}));

7️⃣ userEvent
📌 Для чого

Імітує реальні дії користувача

click
await user.click(button);

type
await user.type(input, 'Hello');

clear
await user.clear(input);

tab
await user.tab();

8️⃣ Асинхронні перевірки
waitFor
await waitFor(() => {
  expect(screen.getByText('Done')).toBeInTheDocument();
});

9️⃣ Що тестувати, а що ні

✅ кнопки
✅ тексти
✅ форми
✅ поведінку

❌ стейти
❌ хуки
❌ CSS

🔟 Золоте правило

❝ Пиши тести так, ніби ти користувач, а не розробник ❞
