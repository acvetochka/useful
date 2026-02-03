# React  Query 

📚 MENU

- 1️⃣ [React Query + Axios](#1%EF%B8%8F%E2%83%A3-react-query--axios)
- 2️⃣ [Пагінація (pagination)](#2%EF%B8%8F%E2%83%A3-%D0%BF%D0%B0%D0%B3%D1%96%D0%BD%D0%B0%D1%86%D1%96%D1%8F-pagination)
- 3️⃣ [Infinite Scroll (безкінечний скрол)](#3%EF%B8%8F%E2%83%A3-infinite-scroll)
- 4️⃣ [React Query + Next.js (App Router)](#4%EF%B8%8F%E2%83%A3-react-query--nextjs-app-router)
- 5️⃣ [Авторизація (token, protected queries)](#5%EF%B8%8F%E2%83%A3-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D1%96%D1%8F--protected-queries)
- 6️⃣ [Оптимістичні оновлення](#6%EF%B8%8F%E2%83%A3-%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D1%96%D1%81%D1%82%D0%B8%D1%87%D0%BD%D1%96-%D0%BE%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F)
- 7️⃣ [Структура проєкту (best practices)](#7%EF%B8%8F%E2%83%A3-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D1%80%D0%BE%D1%94%D0%BA%D1%82%D1%83-best-practice)
- 8️⃣ [Cheat Sheet (коротка шпаргалка)](#8%EF%B8%8F%E2%83%A3-cheat-sheet-%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D0%BE)

## 1️⃣ React Query + Axios
🔹 Навіщо Axios разом з React Query

React Query:

❌ не робить HTTP-запити

✅ керує станом запитів

Axios:

✅ робить запити

✅ інтерсептори

✅ автоматичний JSON

📌 Разом — ідеальна пара

🔹 Встановлення Axios

```bash
npm install axios
```

🔹 Створюємо axios instance (ДУЖЕ важливо)
```js
  // api/axios.js
import axios from 'axios'

export const api = axios.create({
  baseURL: 'https://example.com/api',
  headers: {
    'Content-Type': 'application/json',
  },
})
```

👉 Тепер усі запити в одному місці

🔹 Запит через Axios + useQuery
```js
// api/users.js
import { api } from './axios'

export const getUsers = async () => {
  const { data } = await api.get('/users')
  return data
}

useQuery({
  queryKey: ['users'],
  queryFn: getUsers,
})
```

🔹 Mutation з Axios
```js
export const createUser = async (user) => {
  const { data } = await api.post('/users', user)
  return data
}

useMutation({
  mutationFn: createUser,
})
```

🔹 Axios Interceptors (наприклад token)
```js
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})
```

[Back to menu ↑](#react--query)

## 2️⃣ Пагінація (Pagination)
🔹 Що таке пагінація

👉 Дані приходять частинами:

сторінка 1

сторінка 2

сторінка 3

🔹 API-запит з параметрами
```js
export const getUsers = async (page = 1) => {
  const { data } = await api.get('/users', {
    params: { page, limit: 10 }
  })
  return data
}
```

🔹 useQuery з page
```js
const [page, setPage] = useState(1)

const { data, isLoading } = useQuery({
  queryKey: ['users', page],
  queryFn: () => getUsers(page),
  keepPreviousData: true,
})
```

🔹 Навіщо keepPreviousData

👉 Без нього:

- екран блимає

- дані зникають

👉 З ним:

- стара сторінка показується

- нова вантажиться у фоні

🔹 Кнопки пагінації
```html
<button onClick={() => setPage(p => Math.max(p - 1, 1))}>
  Prev
</button>

<button onClick={() => setPage(p => p + 1)}>
  Next
</button>
```

[Back to menu ↑](#react--query)

## 3️⃣ Infinite Scroll
🔹 Що це

👉 Дані підвантажуються при скролі, а не кнопками

🔹 useInfiniteQuery
```js
useInfiniteQuery({
  queryKey: ['users'],
  queryFn: ({ pageParam = 1 }) => getUsers(pageParam),
  getNextPageParam: (lastPage, pages) => {
    return lastPage.nextPage ?? undefined
  },
})
```

🔹 Що повертає useInfiniteQuery
```js
const {
  data,
  fetchNextPage,
  hasNextPage,
  isFetchingNextPage
} = useInfiniteQuery(...)
```

🔹 Рендер списку
```js
data.pages.map(page =>
  page.items.map(user => (
    <User key={user.id} user={user} />
  ))
)
```

🔹 Кнопка “Завантажити ще”
```html
<button
  disabled={!hasNextPage}
  onClick={() => fetchNextPage()}
>
  Load more
</button>
```

[Back to menu ↑](#react--query)

## 4️⃣ React Query + Next.js (App Router)
🔹 Обовʼязково use client
```js
'use client'
```

🔹 Provider у layout.tsx
```js
'use client'

const queryClient = new QueryClient()

export function Providers({ children }) {
  return (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  )
}
```
```js
// layout.tsx
<Providers>{children}</Providers>
```
🔹 SSR / Hydration (коротко)

📌 React Query підтримує SSR, але:

- це окрема тема

- зазвичай починають без SSR

[Back to menu ↑](#react--query)

## 5️⃣ Авторизація + Protected Queries
🔹 Запит, який потребує token
```js
useQuery({
  queryKey: ['profile'],
  queryFn: getProfile,
  enabled: !!token,
})
```

👉 Без token — запит не виконається

🔹 Logout → очищення кешу
```js
queryClient.clear()
```

[Back to menu ↑](#react--query)

## 6️⃣ Оптимістичні оновлення
🔹 Що це

👉 UI оновлюється до відповіді сервера

🔹 Приклад

```js
useMutation({
  mutationFn: addTodo,
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries(['todos'])

    const prevTodos = queryClient.getQueryData(['todos'])

    queryClient.setQueryData(['todos'], old => [
      ...old,
      newTodo
    ])

    return { prevTodos }
  },
  onError: (err, newTodo, context) => {
    queryClient.setQueryData(['todos'], context.prevTodos)
  },
  onSettled: () => {
    queryClient.invalidateQueries(['todos'])
  }
})
```

[Back to menu ↑](#react--query)

## 7️⃣ Структура проєкту (BEST PRACTICE)
```plaintext
src/
 ├ api/
 │  ├ axios.js
 │  ├ users.js
 │  └ auth.js
 ├ hooks/
 │  ├ useUsers.js
 │  └ useProfile.js
 ├ pages/
 └ components/
```

```js
export const useUsers = () =>
  useQuery({
    queryKey: ['users'],
    queryFn: getUsers,
  })
```

[Back to menu ↑](#react--query)

## 8️⃣ CHEAT SHEET (коротко)

- useQuery({ queryKey, queryFn })
- useMutation({ mutationFn })
- useInfiniteQuery({ queryKey, queryFn })
- queryClient.invalidateQueries()
- queryClient.setQueryData()

🎯 Підсумок

React Query:

🔥 знімає 70% рутини

🔥 робить код чистим

🔥 мастхев для реальних проєктів

[Back to menu ↑](#react--query)
