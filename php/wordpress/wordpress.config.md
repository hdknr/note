## サイトURLを変更する


~~~sql
mysql> update wp_options set option_value = 'http://www.mynewserver.com' where option_name in ('siteurl', 'home');
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0
~~~


### http -> https

wp-config: 127.0.0.1 は特殊な扱いっぽい

~~~php
define('WP_SITEURL', 'http://' . $_SERVER['HTTP_HOST'] . '/');
define('WP_HOME', 'http://' . $_SERVER['HTTP_HOST'] . '/');
~~~

[wp search-replace](https://developer.wordpress.org/cli/commands/search-replace/)コマンド:

~~~bash
$ wp search-replace 'http://127.0.0.1' 'https://127.0.0.1'
~~~

~~~mysql
mysql> select option_name, option_value from wp_options where option_name in ('home', 'siteurl');
+-------------+------------------------------+
| option_name | option_value                 |
+-------------+------------------------------+
| home        | https://127.0.0.1/wordpress/ |
| siteurl     | https://127.0.0.1/wordpress/ |
+-------------+------------------------------+
2 rows in set (0.00 sec)
~~~

#### 管理者画面

wp-config.php:

~~~php
define('FORCE_SSL_LOGIN', true);
define('FORCE_SSL_ADMIN', true);
~~~

#### ELB経由のリダイレクトループを防ぐ

wp-config.phpで強制的にSSL配下で動いているものとする:

~~~php 
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https')
{
    $_SERVER['HTTPS'] = 'on';
}
~~~
