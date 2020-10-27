## Шпаргалка по Docker
Собираем образ будущего контейнера:
```
docker build -t docker-project .
```
Посмотреть, какие образы есть в системе:
```
docker images
```
Создать и запустить контейнер из образа:
```
docker run docker-project
```
Можно указать дополнительные параметры:
```
docker run --name my-server -p 5000:5000 --rm docker-project
```
Посмотреть запущенные контейнеры:
```
docker ps
```
Остановить контейнейр
```
docker stop my-server
```
