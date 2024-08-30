# docker compose

## シャットダウン & イメージ削除

~~~bash
docker-compose down --rmi all --volumes
~~~

## サイドカー

- [サイドカーコンテナをdocker-compose.ymlで指定する方法](https://qiita.com/ynott/items/d5994a7a06e0d10c8e68#1-%E3%82%B5%E3%82%A4%E3%83%89%E3%82%AB%E3%83%BC%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%81%A3%E3%81%A6%E3%81%AA%E3%82%93%E3%82%84%E3%81%AD%E3%82%93)

- `pid` でおなじネームスペースを共有する

~~~yml
version: '3.8'
services:
  nginx:
    image: nginx:1.25
  ubuntu:
    image: ubuntu:22.04
    command: sleep 3000
    pid: "service:nginx"
~~~
