## root の再設定

~~~bash
$ sudo /etc/init.d/mysql stop
mysql stop/waiting
~~~


~~~bash
$ sudo mysqld_safe --skip-grant-tables &

[1] 17642
system@ip-172-31-22-118:~$ 160805 07:49:51 mysqld_safe Can't log to error log and syslog at the same time.  Remove all --log-error configuration options for --syslog to take effect.
160805 07:49:51 mysqld_safe Logging to '/var/log/mysql/error.log'.
160805 07:49:51 mysqld_safe Starting mysqld daemon with databases from /var/lib/mysql
~~~

~~~bash
$ sudo lsof -i:3306
COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  18003 mysql   10u  IPv4  29307      0t0  TCP localhost:mysql (LISTEN)
~~~


~~~bash
$ sudo mysql -u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.5.50-0ubuntu0.14.04.1 (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
~~~

~~~bash
mysql> update user set password=PASSWORD('c00lp@ssword') where User='root';
Query OK, 0 rows affected (0.00 sec)
Rows matched: 4  Changed: 0  Warnings: 0

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
~~~


~~~bash
$ sudo /etc/init.d/mysql restart
stop: Unknown instance:
mysql start/running, process 18231
~~~

~~~bash
$ echo "select now()" | mysql -u root -t -p
Enter password:
+---------------------+
| now()               |
+---------------------+
| 2016-08-05 07:56:17 |
+---------------------+

~~~

### Ubuntu

~~~bash
$ cat /etc/debian_version
stretch/sid
~~~

~~~bash
$ sudo mysqladmin password -u root     
New password:                                                                      
Confirm new password:                                   

Warning: Since password will be sent to server in plain text, use ssl connection to ensure password safety.
mysqladmin:      
You cannot use 'password' command as mysqld runs
 with grant tables disabled (was started with --skip-grant-tables).
Use: "mysqladmin flush-privileges password '*'" instead
root@ubuntu:~# mysql -u root -p
~~~
