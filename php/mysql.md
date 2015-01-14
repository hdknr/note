# mysqli::mysqli(): (HY000/2002): No such file or directory

```
PHP Warning:  mysqli::mysqli(): (HY000/2002): No such file or directory in /home/vagrant/projects/wordpress/test/wp.php on line 11
PHP Stack trace:
```
- ["MySQLのソケットファイル(mysql.sock)が見当たらない場合にこのエラーが発生することがあるようです。"](http://k-holy.hatenablog.com/entry/2014/05/28/192707)

```
$ php --ri mysqli | grep socket

mysqli.default_socket => no value => no value
```
```
$ php --ri pdo_mysql | grep socket
pdo_mysql.default_socket => /var/run/mysqld/mysqld.sock => /var/run/mysqld/mysqld.sock
```

```
$ ls -la /var/run/mysqld/mysqld.sock
srwxrwxrwx 1 mysql mysql 0 Dec 24 08:00 /var/run/mysqld/mysqld.sock
```

- $PHP_PATH/etc/php.ini に設定すること。

```
$ vi /home/vagrant/.phpenv/versions/5.5.19/etc/php.ini

mysqli.default_socket = /var/run/mysqld/mysqld.sock

```

- php-fpm は再起動すること！

```
$ sudo killall php-fpm
$ sudo $PHP_PATH/sbin/php-fpm 
```

# multi_query

- [参考](http://phpspot.net/php/man/php/mysqli.multi-query.html)

```
<?php
require_once(dirname(dirname(__FILE__))."/config.php");

function get_database(){
    global $sugar_config; 
    $dbp = $sugar_config['dbconfig'];
    $db = new mysqli(
        $dbp['db_host_name'],
        $dbp['db_user_name'], $dbp['db_password'],
        $dbp['db_name']);
    
    $db->set_charset('utf8');
    return $db;
}
```

```
<?php
require_once(dirname(__FILE__)."/bootstrap.php");

$SQL='show tables;';

$db = get_database();
if( $db->multi_query($SQL)){
    $res= $db->store_result();
    while($res && $row = $res->fetch_array()){
        var_dump($row);
    }   
}
```