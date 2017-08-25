## サイトURLを変更する


~~~sql
mysql> update wp_options set option_value = 'http://www.mynewserver.com' where option_name in ('siteurl', 'home');
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0
~~~
