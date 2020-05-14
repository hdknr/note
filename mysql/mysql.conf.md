# 設定

## カスタムクライアント設定

~~~ini
[client]
default-character-set=utf8
max_allowed_packet = 32M
~~~

## カスタムサーバー設定

~~~ini
[mysqld]
character-set-server=utf8
~~~



## Ubuntu

~~~bash
$ tree /etc/mysql/
/etc/mysql/
├── conf.d
│   ├── mysql.cnf
│   ├── opts.cnf                        # カスタムクライアント設定
│   └── mysqldump.cnf
├── debian-start
├── debian.cnf
├── my.cnf -> /etc/alternatives/my.cnf
├── my.cnf.fallback
├── mysql.cnf
└── mysql.conf.d
    ├── mysqld.cnf
    ├── opts.cnf                        # カスタムサーバー設定
    └── mysqld_safe_syslog.cnf
~~~
