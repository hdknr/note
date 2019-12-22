# Jail環境

- main.cf でデフォルトトランスポートを定義

~~~
default_transport=jail
~~~

- master.cf で定義したトランスポートを処理するコマンド

~~~
jail unix  -       n       n       -       -       pipe
  flags=FDRq user=vagrant argv=/home/vagrant/inbound.sh $sender $recipient
~~~



## サーバー間でJail:特定のドメインを指定したサーバーに転送

- transport

~~~bash
$ sudo mkdir -p /etc/postfix/db
$ sudo vim /etc/postfix/db/transport

tact.deb smtp:[192.168.56.10]

$ sudo postmap /etc/postfix/db/transport
$ tree /etc/postfix/db
/etc/postfix/db
├── transport
└── transport.db
~~~

- main.cf

~~~bash
relay_domains = tact.deb
transport_maps = hash:/etc/postfix/db/transport
default_transport=jail
~~~