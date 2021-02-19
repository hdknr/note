# MySQL: macOS

~~~zsh
$ brew update
$ brew install mysql
~~~

~~~zsh
% brew info mysql
mysql: stable 8.0.22 (bottled)
Open source relational database management system
https://dev.mysql.com/doc/refman/8.0/en/
Conflicts with:
  mariadb (because mysql, mariadb, and percona install the same binaries)
  percona-server (because mysql, mariadb, and percona install the same binaries)
/usr/local/Cellar/mysql/8.0.22_1 (294 files, 296.5MB) *
  Poured from bottle on 2020-12-16 at 09:27:12
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/mysql.rb
License: GPL-2.0
==> Dependencies
Build: cmake ✘
Required: openssl@1.1 ✔, protobuf ✔
==> Caveats
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To have launchd start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  mysql.server start
==> Analytics
install: 85,094 (30 days), 237,313 (90 days), 824,061 (365 days)
install-on-request: 83,653 (30 days), 232,683 (90 days), 798,745 (365 days)
build-error: 0 (30 days)
~~~


~~~zsh
% mysql.server star t
Starting MySQL
..... SUCCESS! 
~~~

~~~zsh
 % mysql.server stop
Shutting down MySQL
. SUCCESS! 
~~~

~~~zsh
% mysql -u root      
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.22 Homebrew

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
~~~

~~~sql
mysql> show variables like '%char%';
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | utf8mb4                                                |
| character_set_connection | utf8mb4                                                |
| character_set_database   | utf8mb4                                                |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8mb4                                                |
| character_set_server     | utf8mb4                                                |
| character_set_system     | utf8                                                   |
| character_sets_dir       | /usr/local/Cellar/mysql/8.0.22_1/share/mysql/charsets/ |
+--------------------------+--------------------------------------------------------+
8 rows in set (0.01 sec)
~~~


## 記事

- [MySQL 5.5 を Homebrew でインストールする手順 (Mac OS X)](https://weblabo.oscasierra.net/mysql-55-homebrew-install-1/)
