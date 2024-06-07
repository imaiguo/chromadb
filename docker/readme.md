# chromadb docker部署


## 生产口令

```bash
> sudo apt install apache2-utils
> htpasswd -Bbn admin 123456 > /opt/Service/chromadb/data/server.htpasswd
```

## 启动服务

```bash
> sudo docker compose up -d
>
```