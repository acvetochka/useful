# Zustand

## Що таке Zustand?
`Zustand` (з нім. «стан») — це бібліотека для керування глобальним станом у React-додатках. Вона мінімалістична, швидка та дуже проста у використанні.

## Переваги:
- Без шаблонного коду (boilerplate)

- Проста API

- Працює з React і без нього

- Підтримує middleware, persist, devtools тощо

## 🛠️ Встановлення
Використовуйте npm або yarn:

  ```bash
  npm install zustand
  ```
або

  ```bash
  yarn add zustand
  ```

⚠️ Якщо хочеш використовувати з DevTools або Persist middleware, встанови:

  ```bash
  npm install zustand-middleware
  ```

## 🧠 Основні поняття Zustand
Zustand дозволяє створювати "store" — джерело правди для твого стану.

```ts
// store.ts
import { create } from 'zustand'

type BearState = {
  bears: number
  increase: () => void
}

export const useBearStore = create<BearState>((set) => ({
  bears: 0,
  increase: () => set((state) => ({ bears: state.bears + 1 })),
}))
```

Пояснення:
- create: створює стор

- useBearStore: твій кастомний хук, який можна використовувати в компонентах

- set: функція, яка змінює стан

- bears: стан

- increase: функція, яка змінює стан

## 📦 Використання у React-компонентах
```tsx
// BearCounter.tsx
import { useBearStore } from './store'

function BearCounter() {
  const bears = useBearStore((state) => state.bears)
  return <h1>{bears} ведмедів</h1>
}
```

```tsx
// Controls.tsx
import { useBearStore } from './store'

function Controls() {
  const increase = useBearStore((state) => state.increase)
  return <button onClick={increase}>Додати ведмедя</button>
}
```

## 🧩 Поради щодо структурування
- Окремий файл на кожен store — зручно при масштабуванні

- Використовуй TypeScript для повного контролю типів

## 🛠️ Middleware (Persist, Devtools)

### 🔒 Persist (локальне збереження)
```ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

type BearState = {
  bears: number
  increase: () => void
}

export const useBearStore = create<BearState>()(
  persist(
    (set) => ({
      bears: 0,
      increase: () => set((state) => ({ bears: state.bears + 1 })),
    }),
    {
      name: 'bear-storage', // ключ у localStorage
    }
  )
)
```

### 🧰 DevTools
```ts
import { create } from 'zustand'
import { devtools } from 'zustand/middleware'

type BearState = {
  bears: number
  increase: () => void
}

export const useBearStore = create<BearState>()(
  devtools((set) => ({
    bears: 0,
    increase: () => set((state) => ({ bears: state.bears + 1 })),
  }))
)
```

## 💡 Корисні патерни

### 🔄 Оновлення частини стану
```ts
type UserState = {
  name: string
  age: number
  updateName: (name: string) => void
}

export const useUserStore = create<UserState>((set) => ({
  name: 'Іван',
  age: 25,
  updateName: (name) => set(() => ({ name })),
}))
```

### 🧪 Селектори — лише вибірка необхідних даних
```tsx
const name = useUserStore((state) => state.name)
```

### ⚡ Оптимізація: уникнення непотрібних перерендерів
Zustand автоматично мінімізує перерендери, якщо ти вибираєш лише частину стану.

## 🧵 Стор з декількома сутностями
```ts
type Todo = { id: number; title: string; done: boolean }

type TodoStore = {
  todos: Todo[]
  addTodo: (title: string) => void
  toggleTodo: (id: number) => void
}

export const useTodoStore = create<TodoStore>((set) => ({
  todos: [],
  addTodo: (title) =>
    set((state) => ({
      todos: [...state.todos, { id: Date.now(), title, done: false }],
    })),
  toggleTodo: (id) =>
    set((state) => ({
      todos: state.todos.map((t) =>
        t.id === id ? { ...t, done: !t.done } : t
      ),
    })),
}))
```

## 🔗 Інтеграція з React Context (опціонально)
Zustand працює без Context API, але при потребі можна його комбінувати з ним.

## ✅ Тестування
Zustand-стори легко тестуються:

```ts
import { useBearStore } from './store'

test('adds a bear', () => {
  useBearStore.getState().increase()
  expect(useBearStore.getState().bears).toBe(1)
})
```

## 🧰 Інструменти та розширення
`zustand-devtools-extension` — для DevTools

`Immer` — для іммутабельних оновлень (можна комбінувати)

```ts
import produce from 'immer'

increase: () =>
  set(
    produce((state) => {
      state.bears += 1
    })
  )
```

## 📚 Офіційна документація
➡️ [Документація Zustand](https://docs.pmnd.rs/zustand/getting-started/introduction)
