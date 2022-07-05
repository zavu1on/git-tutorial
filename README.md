# git-tutorial

### Инициализация
```shell
git init
git add .
git commit -m "initial"
```

### Подключение к удалённому репозиторию и push
```shell
git remote add origin https://github.com/zavu1on/git-tutorial.git
git push -u origin master
```

### Добавили изменения
```shell
git add .
git commit -m "add entrypoint"
git push
```

### Создать ветку и сделать push в удалённый репозиторий
```shell
git branch test
git checkout test

git add .
git commit -m "add test"
git push --set-upstream origin test
```