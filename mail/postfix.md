## Jain環境

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

### postfix-mysql(Debian)

- main.cf

~~~
relay_domains = proxy:mysql:/etc/postfix/db/relay_domains.cf
transport_maps = proxy:mysql:/etc/postfix/db/transport_maps.cf
~~~

- relay_domains.cf

~~~
hosts = localhost
dbname = emailqueue
user = emailqueue
password = emailqueue
table = postfix_transport
select_field = domain
where_field = domain
~~~

- transport_maps.cf

~~~
host = localhost
user = emailqueue
password = emailqueue
dbname = emailqueue
table = postfix_transport
select_field = transport
where_field = domain
~~~

- postfix_transport テーブル

~~~mysql
CREATE TABLE `postfix_transport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(50) NOT NULL,
  `transport` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
~~~

- データ

~~~
mysql> select * from postfix_transport;
+----+----------+----------------------+
| id | domain   | transport            |
+----+----------+----------------------+
|  1 | test.deb | smtp:[192.168.56.10] |
+----+----------+----------------------+
~~~

### 受信

方針:

- エイリアステーブルを作る
- エイリアスアドレスドメインのトランスポートを `error`  で定義する
- これにより、存在しないエリアスに関してはPostfixがDSNでエラーを返す
- エイリアス先アドレスドメインはローカルで受け取る事のできるドメインを定義する
- 定義したドメインに対してトランスポートにプログラムを定義して処理させる(データベースに保存するなど)


master.cf:
~~~
virtual_alias_maps = proxy:mysql:/etc/postfix/db/virtual_alias_maps.cf
~~~

virtual_alias_maps.cf:
~~~
host = localhost
user = emailqueue
password = emailqueue
dbname = emailqueue
table = postfix_alias
select_field = forward
where_field = recipient
~~~

postfix_aliasテーブル:

~~~mysql
CREATE TABLE `postfix_alias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipient` varchar(100) NOT NULL,
  `forward` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `recipient` (`recipient`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
~~~~

- トランスポートを定義(@admin.debで受け取って、@mailbox.local に転送する)

~~~
mysql> select * from postfix_transport;
+----+---------------+----------------------+
| id | domain        | transport            |
+----+---------------+----------------------+
|  3 | mailbox.local | mailbox              |
|  5 | admin.deb     | error                |
+----+---------------+----------------------+
~~~

- エイリアスを定義(webmaster@admin.deb)

~~~
mysql> select * from postfix_alias;
+----+---------------------+-------------------------+
| id | recipient           | forward                 |
+----+---------------------+-------------------------+
|  1 | webmaster@admin.deb | webmaster@mailbox.local |
+----+---------------------+-------------------------+
~~~

- master.cf (mailboxサービスを定義 mailbox.sh に処理させる)

~~~
mailbox unix  -       n       n       -       -       pipe
  flags=FDRq user=vagrant argv=/home/vagrant/mailbox.sh $sender $recipient
~~~


### 受信テスト

- 存在するアドレスに送信

~~~
Sep  3 05:16:50 jessie postfix/pickup[7274]: 239688E5B5: uid=1000 from=<vagrant@jessie.local>
Sep  3 05:16:50 jessie postfix/cleanup[7630]: 239688E5B5: message-id=<20150903051650.239688E5B5@jessie.local>
Sep  3 05:16:50 jessie postfix/qmgr[7275]: 239688E5B5: from=<vagrant@jessie.local>,
                                                      size=388,
                                                      nrcpt=1 (queue active)
Sep  3 05:16:50 jessie postfix/pipe[7669]: 239688E5B5: to=<webmaster@mailbox.local>,
                                                        orig_to=<webmaster@admin.deb>,
                                                        relay=mailbox,
                                                        delay=0.6, delays=0/0/0/0.59, dsn =2.0.0,
                                                        status=sent (delivered via mailbox service)
Sep  3 05:16:50 jessie postfix/qmgr[7275]: 239688E5B5: removed
~~~

- 存在しないアドレスに送信

~~~
Sep  3 05:17:12 jessie postfix/qmgr[7275]: 30D6A8E5AD: from=<vagrant@jessie.local>,
                                                      size=382,
                                                      nrcpt=1 (queue active)
Sep  3 05:17:12 jessie postfix/error[7634]: 30D6A8E5AD: to=<nobody@admin.deb>,
                                                      relay=none,
                                                      delay=448,
                                                      delays=448/0/0/0,
                                                      dsn=5.0.0,
                                                      status=bounced (Address is undeliverable)
Sep  3 05:17:12 jessie postfix/cleanup[7630]: B9C9B8E5B5: message-id=<20150903051712.B9C9B8E5B5@jessie.local>
Sep  3 05:17:12 jessie postfix/bounce[7636]: 30D6A8E5AD: sender non-delivery notification: B9C9B8E5B5
Sep  3 05:17:12 jessie postfix/qmgr[7275]: 30D6A8E5AD: removed
~~~


## Resource

### Postfix
- [pipe](http://www.postfix.org/pipe.8.html)

### Others
- [Postfix/Mysql Virtual Mail How To](http://hostingsoftware.net/index.php?module=pagemaster&PAGE_user_op=view_page&PAGE_id=56)
