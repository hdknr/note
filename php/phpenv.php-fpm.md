[FastCGI Process Manager for PHP](https://secure.php.net/manual/ja/install.fpm.php)

- [XCache](http://xcache.lighttpd.net/)

## php-fpm

~~~
$ `phpenv prefix`/sbin/php-fpm --help

Usage: php-fpm [-n] [-e] [-h] [-i] [-m] [-v] [-t] [-p <prefix>] [-g <pid>] [-c <file>] [-d foo[=bar]] [-y <file>] [-D] [-F [-O]]
  -c <path>|<file> Look for php.ini file in this directory
  -n               No php.ini file will be used
  -d foo[=bar]     Define INI entry foo with value 'bar'
  -e               Generate extended information for debugger/profiler
  -h               This help
  -i               PHP information
  -m               Show compiled in modules
  -v               Version number
  -p, --prefix <dir>
                   Specify alternative prefix path to FastCGI process manager (default: /home/vagrant/.anyenv/envs/phpenv/versions/5.6.10).
  -g, --pid <file>
                   Specify the PID file location.
  -y, --fpm-config <file>
                   Specify alternative path to FastCGI process manager config file.
  -t, --test       Test FPM configuration and exit
  -D, --daemonize  force to run in background, and ignore daemonize option from config file
  -F, --nodaemonize
                   force to stay in foreground, and ignore daemonize option from config file
  -O, --force-stderr
                   force output to stderr in nodaemonize even if stderr is not a TTY
  -R, --allow-to-run-as-root
                   Allow pool to run as root (disabled by default)
~~~    

## php-fpm.conf

~~~bash
$ find `phpenv prefix` -name "php-fpm.conf*" -print
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/etc/php-fpm.conf.default
~~~

~~~bash
$ cp `phpenv prefix`/etc/php-fpm.conf.default `phpenv prefix`/etc/php-fpm.conf
~~~

編集。例えば、単純に以下のようにして他を削除。

~~~
[wordpress]
listen = /home/vagrant/projects/wordpress/conf/run/php-fpm.sock
listen.mode = 0666
user = vagrant
group = vagrant
pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
~~~

## 起動/終了

~~~bash
$ sudo `phpenv prefix`/sbin/php-fpm
~~~

~~~bash
$ ps ax | grep php-fpm
29078 ?        Ss     0:00 php-fpm: master process (/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/etc/php-fpm.conf)
29079 ?        S      0:00 php-fpm: pool wordpress                                       
29080 ?        S      0:00 php-fpm: pool wordpress    
~~~               
~~~bash
$ sudo killall php-fpm
~~~

## mysqli 

- ソケットファイルをOSに合わせて、 php-fpmを再起動

~~~
$ grep mysqli.default_socket `phpenv prefix`/etc/php.ini

mysqli.default_socket = /var/run/mysqld/mysqld.sock~~~