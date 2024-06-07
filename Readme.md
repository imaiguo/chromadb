
# ChromaDB 0.5.0

## 安装虚拟环境
```bash
> sudo apt install python3-venv python3-pip
> mkdir /opt/Data/PythonVenv
> cd /opt/Data/PythonVenv
> python3 -m venv chromadb
> source /opt/Data/PythonVenv/chromadb/bin/activate
```

## 安装依赖

```bash
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 启动服务端

指定服务ip和端口号方式启动

```bash
> chroma run --path /opt/Data/DBdata/chromadb.netfile --host 192.168.2.199 --log-path /opt/Data/DBdata/chromadb.netfile/chromadb.log --port 6000
```

设置登录认证用户名密码方式 启动

生产密码文件
```bash
> sudo apt install apache2-utils
> htpasswd -Bbn admin 123456 > /opt/Data/DBdata/chromadb.netfile/server.htpasswd
```

启动服务
```bash
> export CHROMA_SERVER_AUTH_CREDENTIALS_FILE="/opt/Data/DBdata/chromadb.netfile/server.htpasswd"
> export CHROMA_SERVER_AUTH_CREDENTIALS_PROVIDER="chromadb.auth.providers.HtpasswdFileServerAuthCredentialsProvider"
> export CHROMA_SERVER_AUTH_PROVIDER="chromadb.auth.basic.BasicAuthServerProvider"
>
> chroma run --path /opt/Data/DBdata/chromadb.netfile --host 192.168.2.199 --log-path /opt/Data/DBdata/chromadb.netfile/chromadb.log --port 6000
```
