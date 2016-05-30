## PHP7 + Composer

- [PHP7インストール](../php.7.md)
- [Composerインストール](../composer.md)
- [CakePHP Application Skeleton](https://github.com/cakephp/app)

~~~bash
$ ./composer.phar --version
Composer version 1.1.1 2016-05-17 12:25:44

~~~

~~~bash
$ ./composer.phar create-project --prefer-dist cakephp/app web
You are running composer with xdebug enabled. This has a major impact on runtime performance. See https://getcomposer.org/xdebug
Installing cakephp/app (3.2.6)
  - Installing cakephp/app (3.2.6)
    Downloading: 100%         

Created project in web
Loading composer repositories with package information
Updating dependencies (including require-dev)
Your requirements could not be resolved to an installable set of packages.

  Problem 1
    - cakephp/cakephp 3.2.9 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.8 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.7 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.6 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.5 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.4 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.3 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.2 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.1 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - cakephp/cakephp 3.2.0 requires ext-intl * -> the requested PHP extension intl is missing from your system.
    - Installation request for cakephp/cakephp ~3.2 -> satisfiable by cakephp/cakephp[3.2.0, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5, 3.2.6, 3.2.7, 3.2.8, 3.2.9].

  To enable extensions, verify that they are enabled in those .ini files:
    - /home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/etc/php.ini
    - /home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/etc/conf.d/xdebug.ini
  You can also run `php --ini` inside terminal to see which files are used by PHP in CLI mode.
~~~

~~~bash
$ vi $(phpenv root)/plugins/php-build/share/php-build/default_configure_options

--enable-intl

$ phpenv install 7.0.6

$ php -r "phpinfo();" | grep "Configure Command" | tr ' ' '\n' | grep intl

'--enable-intl'
~~~


~~~bash
$ ./composer.phar create-project --prefer-dist cakephp/app web

You are running composer with xdebug enabled. This has a major impact on runtime performance. See https://getcomposer.org/xdebug
Installing cakephp/app (3.2.6)
  - Installing cakephp/app (3.2.6)
    Loading from cache

Created project in web
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing aura/installer-default (1.0.0)
    Downloading: 100%

  - Installing cakephp/plugin-installer (0.0.15)
    Downloading: 100%

  - Installing psr/log (1.0.0)
    Downloading: 100%

  - Installing mobiledetect/mobiledetectlib (2.8.22)
    Downloading: 100%

  - Installing aura/intl (1.1.1)
    Downloading: 100%

  - Installing cakephp/chronos (0.4.9)
    Downloading: 100%

  - Installing cakephp/cakephp (3.2.9)
    Downloading: 100%

  - Installing symfony/yaml (v3.0.6)
    Downloading: 100%

  - Installing symfony/filesystem (v3.0.6)
    Downloading: 100%

  - Installing symfony/config (v3.0.6)
    Downloading: 100%

  - Installing symfony/polyfill-mbstring (v1.2.0)
    Downloading: 100%

  - Installing symfony/console (v3.0.6)
    Downloading: 100%

  - Installing robmorgan/phinx (v0.5.3)
    Downloading: 100%

  - Installing cakephp/migrations (1.5.8)
    Downloading: 100%

  - Installing jakub-onderka/php-console-color (0.1)
    Downloading: 100%

  - Installing jakub-onderka/php-console-highlighter (v0.3.2)
    Downloading: 100%

  - Installing dnoegel/php-xdg-base-dir (0.1)
    Downloading: 100%

  - Installing nikic/php-parser (v2.1.0)
    Downloading: 100%

  - Installing symfony/var-dumper (v3.0.6)
    Downloading: 100%

  - Installing psy/psysh (v0.7.2)
    Downloading: 100%

  - Installing jdorn/sql-formatter (v1.2.17)
    Downloading: 100%

  - Installing cakephp/debug_kit (3.2.8)
    Downloading: 100%

  - Installing cakephp/bake (1.2.4)
    Downloading: 100%

cakephp/app suggests installing phpunit/phpunit (Allows automated tests to be run without system-wide install.)
cakephp/app suggests installing cakephp/cakephp-codesniffer (Allows to check the code against the coding standards used in CakePHP.)
symfony/console suggests installing symfony/event-dispatcher ()
symfony/console suggests installing symfony/process ()
symfony/var-dumper suggests installing ext-symfony_debug ()
psy/psysh suggests installing ext-pdo-sqlite (The doc command requires SQLite to work.)
cakephp/debug_kit suggests installing ext-sqlite (DebugKit needs to store panel data in a database. SQLite is simple and easy to use.)
Writing lock file
Generating autoload files
> Cake\Composer\Installer\PluginInstaller::postAutoloadDump
> App\Console\Installer::postInstall
Created `config/app.php` file
Set Folder Permissions ? (Default to Y) [Y,n]? y
Permissions set on /home/vagrant/projects/researchdb/web/tmp/cache
Permissions set on /home/vagrant/projects/researchdb/web/tmp/cache/models
Permissions set on /home/vagrant/projects/researchdb/web/tmp/cache/persistent
Permissions set on /home/vagrant/projects/researchdb/web/tmp/cache/views
Permissions set on /home/vagrant/projects/researchdb/web/tmp/sessions
Permissions set on /home/vagrant/projects/researchdb/web/tmp/tests
Permissions set on /home/vagrant/projects/researchdb/web/tmp
Permissions set on /home/vagrant/projects/researchdb/web/logs
Updated Security.salt value in config/app.php

~~~

~~~bash
$ tree -d web

web/
├── bin
├── config
│   └── schema
├── logs
├── plugins
├── src
│   ├── Console
│   ├── Controller
│   │   └── Component
│   ├── Model
│   │   ├── Behavior
│   │   ├── Entity
│   │   └── Table
│   ├── Shell
│   ├── Template
│   │   ├── Element
│   │   │   └── Flash
│   │   ├── Email
│   │   │   ├── html
│   │   │   └── text
│   │   ├── Error
│   │   ├── Layout
│   │   │   ├── Email
│   │   │   │   ├── html
│   │   │   │   └── text
│   │   │   └── rss
│   │   └── Pages
│   └── View
│       └── Helper
├── tests
│   ├── Fixture
│   └── TestCase
│       ├── Controller
│       │   └── Component
│       ├── Model
│       │   └── Behavior
│       └── View
│           └── Helper
├── tmp
│   ├── cache
│   │   ├── models
│   │   ├── persistent
│   │   └── views
│   ├── sessions
│   └── tests
├── vendor
└── webroot
    ├── css
    ├── img
    └── js

50 directories
~~~


## PHPExcle 追加

- http://phpoffice.github.io/
- https://github.com/PHPOffice/PHPExcel

~~~bash
$ ../composer.phar require phpoffice/phpexcel                                                                                  

You are running composer with xdebug enabled. This has a major impact on runtime performance.
See https://getcomposer.org/xdebug
Using version ^1.8 for phpoffice/phpexcel
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing phpoffice/phpexcel (1.8.1)
    Downloading: 100%         

Writing lock file
Generating autoload files
> Cake\Composer\Installer\PluginInstaller::postAutoloadDump
~~~

~~~bash
$ git diff composer.json

diff --git a/composer.json b/composer.json
index 1809586..88304a2 100644
--- a/composer.json
+++ b/composer.json
@@ -9,7 +9,8 @@
         "cakephp/cakephp": "~3.2",
         "mobiledetect/mobiledetectlib": "2.*",
         "cakephp/migrations": "~1.0",
-        "cakephp/plugin-installer": "*"
+        "cakephp/plugin-installer": "*",
+        "phpoffice/phpexcel": "^1.8"
     },
     "require-dev": {
         "psy/psysh": "@stable",
~~~

~~~bash
$ ls vendor/phpoffice/

phpexcel
~~~


~~~bash
$ bin/cake console
Psy Shell v0.7.2 (PHP 7.0.6 — cli) by Justin Hileman
>>> PHPExcel_IOFactory::createReader("CSV");
=> PHPExcel_Reader_CSV {#204}
~~~
