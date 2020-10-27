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
Остановить контейнер:
```
docker stop my-server
```
Чтобы синхронизировтаь папки/файлы из контейнера, используется volume:
```
docker run  --name my-server -p 5000:5000 --rm  -v .docker/storage.json:/home/docker_project/storage.json docker-project
```

# Docker-compose
ЧТобы не мучаться с длинными командами, можно просто создать `docker-compose.yaml` и 
собирать и запускать всё с помощью команды:
```
docker-compose up --build
```
Пример файла:
```yaml
version: '2'

services:
    docker_project:
      container_name: my_server
      build:
        context: .
        dockerfile: Dockerfile
      ports:
        - 5000:5000
      volumes:
        - .docker/storage.json:/home/docker_project/storage.json
```
