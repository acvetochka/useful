# React Query

## Що таке React Query (TanStack Query)

`React Query` — це бібліотека для роботи з серверними даними у React.

👉 Вона не зберігає локальний стан UI, а працює саме з:

- запитами до API

- кешуванням

- повторними запитами

- станами loading / error / success

- синхронізацією даних із сервером

📌 Коротко:

`Axios / fetch` — роблять запит

`React Query` — керує результатом цього запиту

🔹 Яку проблему вона вирішує

Без React Query ти зазвичай робиш так:
```jsx
useEffect(() => {
  setLoading(true)
  fetch('/api/users')
    .then(res => res.json())
    .then(data => {
      setUsers(data)
      setLoading(false)
    })
    .catch(err => {
      setError(err)
      setLoading(false)
    })
}, [])
```

І так у кожному компоненті 🤯

React Query робить замість тебе:

❌ не пишеш useEffect

❌ не тримаєш loading, error, data вручну

❌ не думаєш про повторні запити

❌ не думаєш про кеш

🔹 Коли React Query НЕ потрібна

Не використовуй її для:

- isModalOpen

- activeTab

- theme

- стану інпутів

📌 Вона тільки для даних із сервера.

🔹 Основні поняття (дуже важливо)

1️⃣ Query (запит)

Query — це:

- GET-запит

- отримання даних

- кешування результату

Приклади:

- список користувачів

- профіль

- список товарів

2️⃣ Mutation (мутація)

Mutation — це:

- POST

- PUT

- PATCH

- DELETE

Приклади:

- створити користувача

- оновити профіль

- видалити товар

3️⃣ Cache (кеш)

React Query:

- зберігає дані в памʼяті

- повторно використовує їх

- не робить зайвих запитів

🔹 Встановлення
```bash
npm install @tanstack/react-query
```

або
```bash
yarn add @tanstack/react-query
```

🔹 Підключення React Query до застосунку
1️⃣ Створюємо клієнт
import { QueryClient } from '@tanstack/react-query'

const queryClient = new QueryClient()

2️⃣ Обгортаємо App у Provider
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <YourApp />
    </QueryClientProvider>
  )
}


📌 Без цього React Query не працюватиме

🔹 Перший запит (useQuery)
Базовий приклад
import { useQuery } from '@tanstack/react-query'

function Users() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () =>
      fetch('/api/users').then(res => res.json())
  })

  if (isLoading) return <p>Завантаження...</p>
  if (error) return <p>Помилка</p>

  return (
    <ul>
      {data.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  )
}

🔹 Розбір useQuery по частинах
queryKey
queryKey: ['users']


👉 Унікальний ключ для кешу
👉 React Query запамʼятовує дані під цим ключем

Можна з параметрами:

['user', userId]

queryFn
queryFn: () => fetch(...).then(...)


👉 Функція, яка:

робить запит

повертає Promise

Що повертає useQuery
const {
  data,
  error,
  isLoading,
  isError,
  isSuccess,
  refetch
} = useQuery(...)

Поле	Що означає
data	Дані з сервера
isLoading	Перший запит
isError	Помилка
error	Обʼєкт помилки
isSuccess	Дані успішно отримані
refetch	Ручний повтор запиту
🔹 Кеш і повторні запити
React Query автоматично:

повторює запит при:

поверненні на вкладку

перефокусі вікна

використовує кеш

не робить зайвих fetch

Налаштування кешу
useQuery({
  queryKey: ['users'],
  queryFn: fetchUsers,
  staleTime: 1000 * 60, // 1 хв
  cacheTime: 1000 * 60 * 5 // 5 хв
})

Опція	Значення
staleTime	Скільки дані вважаються “свіжими”
cacheTime	Як довго зберігати кеш
🔹 Параметри запиту
useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json()),
  enabled: !!userId
})


👉 enabled — не запускати запит, доки нема userId

🔹 Mutation (POST / PUT / DELETE)
Приклад: створення користувача
import { useMutation } from '@tanstack/react-query'

const mutation = useMutation({
  mutationFn: newUser =>
    fetch('/api/users', {
      method: 'POST',
      body: JSON.stringify(newUser)
    })
})


Використання:

mutation.mutate({ name: 'Anna' })

Що повертає useMutation
const {
  mutate,
  mutateAsync,
  isLoading,
  isError,
  isSuccess,
  error
} = useMutation(...)

Обробка результатів
useMutation({
  mutationFn: createUser,
  onSuccess: () => {
    console.log('Успіх!')
  },
  onError: (error) => {
    console.log('Помилка', error)
  }
})

🔹 Оновлення списку після mutation

📌 Дуже важливо

import { useQueryClient } from '@tanstack/react-query'

const queryClient = useQueryClient()

useMutation({
  mutationFn: createUser,
  onSuccess: () => {
    queryClient.invalidateQueries(['users'])
  }
})


👉 React Query:

видаляє кеш

робить новий GET-запит

🔹 Devtools (ДУЖЕ рекомендую)
npm install @tanstack/react-query-devtools

import { ReactQueryDevtools } from '@tanstack/react-query-devtools'

<QueryClientProvider client={queryClient}>
  <App />
  <ReactQueryDevtools initialIsOpen={false} />
</QueryClientProvider>


📌 Показує:

кеш

активні запити

стани

🔹 Типовий патерн (best practice)
// api/users.js
export const getUsers = async () => {
  const res = await fetch('/api/users')
  return res.json()
}

useQuery({
  queryKey: ['users'],
  queryFn: getUsers
})

🔹 Часті помилки

❌ Використовувати для UI-стану
❌ Міняти data напряму
❌ Забувати queryKey
❌ Не робити invalidateQueries після mutation

🔹 Коли React Query — must have

✅ API
✅ Авторизація
✅ Списки
✅ Дашборди
✅ Профілі
✅ Фільтри + пагінація
