# ArgoCD

Створюємо namespace `argocd`, в якому буде по замовченню встановлено систему
```
kubectl create namespace argocd
```

Маніфест
```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Вивід всіх об'єктів namespace argocd
```
kubectl get all -n argocd
```

Налаштування port-forward для доступу до argocd за допомогою локального порта

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Необхідно налаштувати на https, для цього в середовищі розробки (наприклад codespace) натиснути вкладку Ports, обрати необхідний порт 
`Change Port Protocol -> Https`
та змінити доступність
`Port visibility -> Public`

Отримання пароля для входу в ArgoCD
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

