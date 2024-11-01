# TypeScript в React

Використання TypeScript в React та Next.js: Типізація HTML елементів
TypeScript дозволяє підвищити надійність та зручність роботи з React-компонентами, особливо для великих проєктів, надаючи чітку типізацію для елементів, подій та атрибутів. Для роботи з HTML-елементами в React є набір вбудованих типів, таких як HTMLParagraphElement, HTMLAttributes, DetailedHTMLProps тощо, які дозволяють зручно типізувати властивості та рефери (посилання) на елементи DOM.

## 1. Основи TypeScript з React
Щоб використовувати TypeScript у React, треба додати файл конфігурації TypeScript (tsconfig.json) і змінити розширення файлів з .js на .tsx. Основні особливості:

- Функціональні компоненти: Використовують React.FC (Function Component) або прямий тип для пропсів.
- Компоненти класів: Типізуються за допомогою React.Component.

```typescript
// Функціональний компонент
const MyComponent: React.FC<{ title: string }> = ({ title }) => {
    return <h1>{title}</h1>;
};
```

## 2. Типізація HTML елементів в React
У React з TypeScript можна типізувати HTML-елементи та їх атрибути, використовуючи спеціальні типи з бібліотеки react та react-dom.

Основні типи HTML елементів:
- HTMLAttributes<T>: базовий інтерфейс для стандартних HTML-атрибутів, який приймає тип елемента T.
- DetailedHTMLProps: поєднує HTMLAttributes з більш специфічними типами HTML-елементів, такими як HTMLParagraphElement.
- Конкретні HTML елементи: HTMLDivElement, HTMLInputElement, HTMLButtonElement, HTMLParagraphElement тощо, кожен з яких представляє певний тип HTML-елемента та його властивості.

Приклади використання типів HTML елементів
  1. HTMLParagraphElement — використовується для параграфів (`<p>`), коли треба отримати рефер на цей елемент або передати його атрибути.
  
      ```typescript
      const MyParagraph = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>((props, ref) => (
          <p ref={ref} {...props}>Hello, World!</p>
      ));
      ```
  
  2. DetailedHTMLProps — використовується для більш детальної типізації пропсів HTML-елементів.
  
      ```typescript
      const MyInput: React.FC<React.DetailedHTMLProps<React.InputHTMLAttributes<HTMLInputElement>, HTMLInputElement>> = (props) => (
          <input {...props} />
      );
      ```
  
  3. HTMLAttributes — дозволяє передати стандартні HTML-атрибути, зокрема в кастомні компоненти.
  
      ```typescript
      interface ButtonProps extends React.HTMLAttributes<HTMLButtonElement> {
          label: string;
      }
      
      const MyButton: React.FC<ButtonProps> = ({ label, ...props }) => (
          <button {...props}>{label}</button>
      );
      ```

## 3. Події та їх типізація
TypeScript в React дозволяє типізувати обробники подій, зокрема для елементів введення, кнопок та інших інтерфейсних компонентів.

- MouseEvent для миші, KeyboardEvent для клавіатури та інші.
- React.ChangeEvent<HTMLInputElement>: для елементів введення.
```typescript
const handleClick = (event: React.MouseEvent<HTMLButtonElement>): void => {
    console.log("Button clicked");
};

const handleChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
    console.log(event.target.value);
};
```

## 4. Використання TypeScript в Next.js
Next.js автоматично підтримує TypeScript. Основи застосування:

- Файли сторінок: Next.js дозволяє автоматично створювати сторінки, і в pages папці можна визначити сторінки з типізацією.
- getStaticProps і getServerSideProps: спеціальні функції для статичної генерації та серверної сторони в Next.js, які мають специфічні типи.

  ```typescript
  import { GetStaticProps, NextPage } from 'next';
  
  interface PageProps {
      title: string;
  }
  
  const HomePage: NextPage<PageProps> = ({ title }) => (
      <h1>{title}</h1>
  );
  
  export const getStaticProps: GetStaticProps<PageProps> = async () => {
      return {
          props: {
              title: 'Welcome to Next.js with TypeScript!'
          }
      };
  };
  
  export default HomePage;
  ```
