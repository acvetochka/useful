# kubectl

## Конфігурація

Перехід до файлу конфігурації

```
code ~/.kube/config
```

Елемент context у файлі конфігурації використовується для групування параметрів доступу під зручною назвою.

Контекст має три параметри: кластер, простір імен та користувач.

### Управління контекстом відбувається за допомогою команди `kubectl config`:

- Отримання поточного контексту

```
kubectrl config current-context
```

- Налагоджування namespace для дефолтного контексту
```
kubectl config set-context --current --namespace <name>
```

- Переключення на контекст
```
kubectl config use-context 
```


### Список нод 
(виводить роль, версію та поточний статус кожної ноди)

```
kubectl get nodes
```
or
```
kubectl get no
```

### Вивід всіх автивних об'єктів кластеру
```
kubectl get all -A
```

Вивід об'єктів по певному namespace
```
kubectl get all -n <namespace>
```

### Статус контроль-менеджера та планувальника
```
kubectl get componentstatus
```

### Вивід всіх namespaces

```
kubectl get namespaces
```
or
```
kubectl get ns
```


### Вивід подів 
- default namespace
```
kubectl get pods
```
or 
```
kubectl get po
```
- по namespace
```
kubectl get po -n <namespace>
```


# Get commands with basic output
| command                         |                                         |                                    |
| -------------------------------- | --------------------------------------- | ---------------------------------- |
| `kubectl get services`          | List all services in the namespace      | Список всіх служб у просторі імен  |
| `kubectl get pods --all-namespaces`| List all pods in all namespaces         | Список усіх подів в усіх namespace  |
| `kubectl get pods -o wide`         | List all pods in the current namespace, with more details | Список усіх модулів в поточному просторі імен із детальнішою інформацією|
| `kubectl get deployment my-dep`    | List a particular deployment | Виводить конкретне розгортання |
| `kubectl get pods`                 | List all pods in the namespace | Виводить всі модулі в просторі імен|
| `kubectl get pod my-pod -o yaml`   | Get a pod's YAML | Виводить под у форматі YAML |
