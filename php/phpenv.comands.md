- [phpenv/phpenv](https://github.com/phpenv/phpenv)
- [libexec](https://github.com/phpenv/phpenv/tree/dev/libexec)

## commands

~~~bash
$ phpenv commands
commands
completions
exec
global
help
hooks
init
install
local
prefix
rehash
root
shell
shims
uninstall
update
version
--version
version-file
version-file-read
version-file-write
version-name
version-origin
versions
whence
which
~~~

## prefix

- [phpenv-prefix](https://github.com/phpenv/phpenv/blob/dev/libexec/phpenv-prefix)

~~~bash
$ phpenv prefix
/home/admin/.anyenv/envs/phpenv/versions/5.6.17
~~~

~~~bash
$ $(phpenv prefix)/sbin/php-fpm --help

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
                   Specify alternative prefix path to FastCGI process manager (default: /home/admin/.anyenv/envs/phpenv/versions/5.6.17).
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

## shims
