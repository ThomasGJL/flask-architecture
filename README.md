# flask-architecture

拉取容器  
```
docker pull postgres:14.2
```

运行容器  
```
docker run --name postgres-db -e POSTGRES_DB=database -e POSTGRES_PASSWORD=admin -e PGDATA=/var/lib/postgresql/data -p 5432:5432 -d postgres:14.2
```

查看容器日志  
```
docker logs postgres-db
```

进入容器  
```
docker exec -it postgres-db /bin/bash
```
