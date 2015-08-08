wp-cli/wp-cli:install

## Resource

- [WP-CLIの使い方](http://qiita.com/IK12_info/items/4a9190119be2a0f347a0)
- [A command line interface for WordPress](http://wp-cli.org/blog/)

## インストールしてみる

~~~bash
$ curl -sS https://getcomposer.org/installer | php
#!/usr/bin/env php
All settings correct for using Composer
Downloading...

Composer successfully installed to: /home/vagrant/projects/wordpress4/composer.phar
Use it: php composer.phar
~~~

- [Alternative Install Methods](https://github.com/wp-cli/wp-cli/wiki/Alternative-Install-Methods)

~~~
$ ./composer.phar  create-project wp-cli/wp-cli --no-dev
Installing wp-cli/wp-cli (v0.19.2)
  - Installing wp-cli/wp-cli (v0.19.2)
    Loading from cache

Created project in /home/vagrant/projects/wordpress4/wp-cli
Loading composer repositories with package information
Installing dependencies
  - Installing wp-cli/php-cli-tools (v0.10.4)
    Loading from cache

  - Installing nb/oxymel (v0.1.0)
    Loading from cache

  - Installing mustache/mustache (v2.8.0)
    Loading from cache

  - Installing ramsey/array_column (1.1.3)
    Loading from cache

  - Installing rmccue/requests (v1.6.1)
    Loading from cache

  - Installing symfony/finder (v2.7.3)
    Loading from cache

Writing lock file
Generating autoload files

~~~

~~~
$ ./composer.phar require "wp-cli/wp-cli"
Using version ^0.19.2 for wp-cli/wp-cli
./composer.json has been created
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing nb/oxymel (v0.1.0)
    Loading from cache

  - Installing symfony/finder (v2.7.3)
    Loading from cache

  - Installing rmccue/requests (v1.6.1)
    Loading from cache

  - Installing ramsey/array_column (1.1.3)
    Loading from cache

  - Installing mustache/mustache (v2.8.0)
    Loading from cache

  - Installing wp-cli/php-cli-tools (v0.10.4)
    Loading from cache

  - Installing wp-cli/wp-cli (v0.19.2)
    Loading from cache

wp-cli/wp-cli suggests installing psy/psysh (Enhanced `wp shell` functionality)
Writing lock file
Generating autoload files
~~~


## Error: Required file 'autoload.php' doesn't exist

~~~
$pwd
/home/vagrant/projects/wordpress4
~~~

~~~
WP_CLI_ROOT : /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli
~~~

- ここでエラー(vendor/wp-cli/wp-cli/php/wp-cli.php)

~~~
WP_CLI::get_runner()->before_wp_load();
~~~

- vendor/wp-cli/wp-cli/php/utils.php

~~~
function load_dependencies() {
	// WP_CLI_ROOT=/home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli
	
    if ( 0 === strpos( WP_CLI_ROOT, 'phar:' ) ) { 
        require WP_CLI_ROOT . '/vendor/autoload.php';
        return;
    }   

    $has_autoload = false;

    foreach ( get_vendor_paths() as $vendor_path ) { 
        if ( file_exists( $vendor_path . '/autoload.php' ) ) { 
            require $vendor_path . '/autoload.php';
            $has_autoload = true;
            break;
        }   
    }   


    if ( !$has_autoload ) { 
        fputs( STDERR, "Internal error: Can't find Composer autoloader.\nTry running: composer install\n" );
        exit(3);
    }   
    // echo "HDKNR*********\n";
}
~~~

## わからん

~~~
$ ./composer.phar remove wp-cli/wp-cli
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Removing wp-cli/wp-cli (v0.19.2)
Writing lock file
Generating autoload files

$ rm -rf vendor/wp-cli
~~~

~~~
$ ./composer.phar require wp-cli/wp-cli:0.15.1
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing rhumsaa/array_column (1.1.3)
    Downloading: 100%         

  - Installing wp-cli/php-cli-tools (v0.9.4-patch46)
    Downloading: 100%         

  - Installing wp-cli/wp-cli (v0.15.1)
    Downloading: 100%         

wp-cli/wp-cli suggests installing psy/psysh (Enhanced `wp shell` functionality)
Package rhumsaa/array_column is abandoned, you should avoid using it. Use ramsey/array_column instead.
Writing lock file
Generating autoload files
~~~

~~~
$ vendor/bin/wp
PHP Warning:  require(/home/vagrant/.wp-cli/
  - vendor/autoload.php): failed to open stream: No such file or directory in /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/utils.php on line 41
PHP Stack trace:
PHP   1. {main}() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:0
PHP   2. include() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:17
PHP   3. WP_CLI\Runner->before_wp_load() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/wp-cli.php:20
PHP   4. WP_CLI\Utils\load_file() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php:486
PHP Fatal error:  require(): Failed opening required '/home/vagrant/.wp-cli/
  - vendor/autoload.php' (include_path='.::/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php') in /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/utils.php on line 41
PHP Stack trace:
PHP   1. {main}() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:0
PHP   2. include() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:17
PHP   3. WP_CLI\Runner->before_wp_load() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/wp-cli.php:20
PHP   4. WP_CLI\Utils\load_file() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php:486
~~~

~~~
$ ./composer.phar require psy/psysh                                               [1/1930]
Using version ^0.5.2 for psy/psysh
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing jakub-onderka/php-console-color (0.1)
    Loading from cache

  - Installing jakub-onderka/php-console-highlighter (v0.3.2)
    Loading from cache

  - Installing dnoegel/php-xdg-base-dir (0.1)
    Loading from cache

  - Installing nikic/php-parser (v1.4.0)
    Loading from cache

  - Installing symfony/var-dumper (v2.7.3)
    Loading from cache

  - Installing symfony/console (v2.7.3)
    Loading from cache

  - Installing psy/psysh (v0.5.2)
    Loading from cache

symfony/var-dumper suggests installing ext-symfony_debug ()
symfony/console suggests installing symfony/event-dispatcher ()
symfony/console suggests installing symfony/process ()
symfony/console suggests installing psr/log (For using the console logger)
psy/psysh suggests installing ext-pdo-sqlite (The doc command requires SQLite to work.)
Package rhumsaa/array_column is abandoned, you should avoid using it. Use ramsey/array_column instead.
Writing lock file
Generating autoload files
~~~

~~~
$ vendor/bin/wp
PHP Warning:  require(/home/vagrant/.wp-cli/
  - vendor/autoload.php): failed to open stream: No such file or directory in /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/utils.php on line 41
PHP Stack trace:
PHP   1. {main}() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:0
PHP   2. include() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:17
PHP   3. WP_CLI\Runner->before_wp_load() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/wp-cli.php:20
PHP   4. WP_CLI\Utils\load_file() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php:486
PHP Fatal error:  require(): Failed opening required '/home/vagrant/.wp-cli/
  - vendor/autoload.php' (include_path='.::/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php:/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/share/pyrus/.pear/php') in /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/utils.php on line 41
PHP Stack trace:
PHP   1. {main}() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:0
PHP   2. include() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/boot-fs.php:17
PHP   3. WP_CLI\Runner->before_wp_load() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/wp-cli.php:20
PHP   4. WP_CLI\Utils\load_file() /home/vagrant/projects/wordpress4/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php:486
~~~

## うーん

~~~

$ ./composer.phar create-project wp-cli/wp-cli:0.15.1 
Installing wp-cli/wp-cli (v0.15.1)
  - Installing wp-cli/wp-cli (v0.15.1)
    Loading from cache

Created project in /home/vagrant/projects/wordpress4/wp-cli
Loading composer repositories with package information

Installing dependencies (including require-dev)
  - Installing wp-cli/php-cli-tools (v0.9.4-patch46)
    Loading from cache

  - Installing nb/oxymel (v0.1.0)
    Loading from cache

  - Installing mustache/mustache (v2.8.0)
    Loading from cache

  - Installing rhumsaa/array_column (1.1.3)
    Loading from cache

  - Installing rmccue/requests (v1.6.1)
    Loading from cache

  - Installing symfony/yaml (v2.7.3)
    Loading from cache

  - Installing phpunit/php-text-template (1.2.1)
    Loading from cache

  - Installing phpunit/phpunit-mock-objects (1.2.3)
    Downloading: 100%         

  - Installing phpunit/php-timer (1.0.7)
    Loading from cache

  - Installing phpunit/php-file-iterator (1.4.1)
    Loading from cache

  - Installing phpunit/php-token-stream (1.2.2)
    Downloading: 100%         

  - Installing phpunit/php-code-coverage (1.2.18)
    Downloading: 100%         

  - Installing phpunit/phpunit (3.7.38)
    Downloading: 100%         

  - Installing symfony/finder (v2.7.3)
    Loading from cache

  - Installing symfony/translation (v2.7.3)
    Downloading: 100%         
  - Installing symfony/translation (v2.7.3)                                                                               [0/1879]
    Downloading: 100%         

  - Installing symfony/event-dispatcher (v2.7.3)
    Downloading: 100%         

  - Installing symfony/dependency-injection (v2.7.3)
    Downloading: 100%         

  - Installing symfony/filesystem (v2.7.3)
    Downloading: 100%         

  - Installing symfony/config (v2.7.3)
    Downloading: Connecting...

  - Installing symfony/console (v2.7.3)
    Loading from cache

  - Installing behat/gherkin (v2.3.5)
    Downloading: 100%         

  - Installing behat/behat (v2.5.5)
    Downloading: 100%         

phpunit/phpunit suggests installing phpunit/php-invoker (~1.1)
symfony/translation suggests installing psr/log (To use logging capability in translator)
symfony/event-dispatcher suggests installing symfony/http-kernel ()
symfony/dependency-injection suggests installing symfony/proxy-manager-bridge (Generate service proxies to lazy load them)
symfony/console suggests installing symfony/process ()
symfony/console suggests installing psr/log (For using the console logger)
behat/behat suggests installing behat/symfony2-extension (for integration with Symfony2 web framework)
behat/behat suggests installing behat/yii-extension (for integration with Yii web framework)
behat/behat suggests installing behat/mink-extension (for integration with Mink testing framework)
Package rhumsaa/array_column is abandoned, you should avoid using it. Use ramsey/array_column instead.
Writing lock file
Generating autoload files
        
~~~

## WP_CLI_CONFIG_PATH + config.yml

- ディレクトリごと削除して composer, wp-cli をインストール

~~~bash
$ export WP_CLI_CONFIG_PATH=$PWD
~~~

~~~bash
$ cat config.yml 

require:
    - vendoer/autoload.php
~~~    

~~~bash
$ vendor/bin/wp --version
WP-CLI 0.19.2
~~~
