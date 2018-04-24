## インストール

- [WP-CLIの使い方](http://qiita.com/IK12_info/items/4a9190119be2a0f347a0)





## composer

~~~bash
$ curl -sS https://getcomposer.org/installer | php
All settings correct for using Composer
Downloading...

Composer successfully installed to: /home/admin/projects/wordpress/composer.phar
Use it: php composer.phar
admin@ip-10-186-155-16:~/projects/wordpress$ ls -al
total 1528
drwxr-xr-x 3 admin admin    4096 Feb 20 11:23 .
drwxr-xr-x 6 admin admin    4096 Jan 31 20:57 ..
-rwxr-xr-x 1 admin admin 1552186 Feb 20 11:23 composer.phar
drwxr-xr-x 6 admin admin    4096 Feb 20 11:05 jp
~~~

## psysh

~~~bash
$ ./composer.phar require psy/psysh
Using version ^0.6.1 for psy/psysh
./composer.json has been created
Loading composer repositories with package information
Updating dependencies (including require-dev)
....
~~~

## wp-cli

- psysh いれると wp-cli が 入らない

~~~bash
admin@ip-10-186-155-16:~/projects/wordpress$ rm -rf vendor/
admin@ip-10-186-155-16:~/projects/wordpress$ rm composer.json composer.lock
~~~

~~~bash
admin@ip-10-186-155-16:~/projects/wordpress$ ./composer.phar require wp-cli/wp-cli
Using version ^0.22.0 for wp-cli/wp-cli
./composer.json has been created
Loading composer repositories with package information
Updating dependencies (including require-dev)
....
~~~

## 実行

~~~bash
admin@ip-10-186-155-16:~/projects/wordpress$ export WP_CLI_CONFIG_PATH=$PWD
~~~

~~~bash
admin@ip-10-186-155-16:~/projects/wordpress$ vendor/bin/wp --version
WP-CLI 0.22.0
~~~

~~~bash
admin@ip-10-186-155-16:~/projects/wordpress$ vi wp-cli.yml
$ cat wp-cli.yml
path: jp
~~~

~~~bash
$ vendor/bin/wp core version --extra
WordPress version: 4.4.1
Database revision: 35700
TinyMCE version:   4.208 (4208-20151113)
~~~


## プラグインリスト

~~~bash
$ vendor/bin/wp plugin list

+-------------------------+----------+-----------+--------------+
| name                    | status   | update    | version      |
+-------------------------+----------+-----------+--------------+
| akismet                 | inactive | available | 3.1.11       |
.....
| rest-api                | active   | none      | 2.0-beta13.1 |
+-------------------------+----------+-----------+--------------+
~~~


## wp-config.php

~~~php
if ( defined( 'WP_CLI' ) ) {
    $_SERVER['HTTP_HOST'] = 'localhost';
}

if ( !defined( 'WP_CLI' ) ) {
    // remove x-pingback HTTP header
    add_filter('wp_headers', function($headers) {
        unset($headers['X-Pingback']);
        return $headers;
    });
    // disable pingbacks
    add_filter( 'xmlrpc_methods', function( $methods ) {
            unset( $methods['pingback.ping'] );
            return $methods;
    });
    add_filter( 'auto_update_translation', '__return_false' );
}
~~~
