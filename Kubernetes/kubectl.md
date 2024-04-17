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