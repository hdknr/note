
## FastCGI

- https://fastcgi-archives.github.io/FastCGI_Specification.html


## php-fpm コマンド

~~~bash
php-fpm --help
Usage: php [-n] [-e] [-h] [-i] [-m] [-v] [-t] [-p <prefix>] [-g <pid>] [-c <file>] [-d foo[=bar]] [-y <file>] [-D] [-F [-O]]
  -c <path>|<file> Look for php.ini file in this directory
  -n               No php.ini file will be used
  -d foo[=bar]     Define INI entry foo with value 'bar'
  -e               Generate extended information for debugger/profiler
  -h               This help
  -i               PHP information
  -m               Show compiled in modules
  -v               Version number
  -p, --prefix <dir>
                   Specify alternative prefix path to FastCGI process manager (default: /usr/local).
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


## 例

### wordpress

- [wordpress php-fpm](wordpress/wordpress.nginx.md)

### symfony

- [symfony nginx](https://symfony.com/doc/current/setup/web_server_configuration.html#nginx)
- [How to install symfony2 app in a subdirectory in nginx](https://stackoverflow.com/questions/12266297/how-to-install-symfony2-app-in-a-subdirectory-in-nginx)

## CPUのロード問題

pm.max_children:

- [php-fpmのエラーにぶつかりながら設定の最適化を図る](http://qiita.com/nnmr/items/a521fb4e18931cc647d6)
- [Php-fpm causing high cpu usage](http://community.rtcamp.com/t/php-fpm-causing-high-cpu-usage/3141)


Wordpress/wp-cron.php:


- [.php-fpm-bin 100% CPU usage. How to track the exact script causing it?
](https://stackoverflow.com/questions/44570064/php-fpm-bin-100-cpu-usage-how-to-track-the-exact-script-causing-it)
- [WordPress の wp-cron.php を無効にする](http://www.webdesignleaves.com/wp/wordpress/432/)
