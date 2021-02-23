# SSH


- [Docker | 公開鍵でコンテナにssh接続する出来るようにするDockerfileの例](https://qiita.com/YumaInaura/items/7509061e4b27e03ea538)
- [Docker 初心者 — ssh で接続できるサーバーを立てる](https://qiita.com/YumaInaura/items/adb20c8083fce2da86e1)
- [docker 「コンテナを ssh 接続できるようにするDockerfile」チュートリアル解説](https://qiita.com/YumaInaura/items/1d5c18a9e55484ccad89)

## 起動時に sshd を立ち上げる

~~~Dockerfile
FROM python:3.8.3
WORKDIR /usr/src/app

## SSH
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22

RUN mkdir ~/.ssh
RUN echo $SSH_PUBLIC_KEY > ~/.ssh/authorized_keys
RUN chmod 0600 ~/.ssh/authorized_keys

RUN  chmod a+x /usr/src/app/bin/sshd.bash
~~~

bin/sshd.bash:

~~~bash
#!/bin/bash 
echo "restart ssh service"
service ssh restart
exec "$@"           # !!!!!!! 
~~~