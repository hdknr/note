# psysh

- http://qiita.com/scribble/items/3564bf4b648a4f7f6fce


# インストール

```
$ ./composer.phar require psy/psysh:@stable
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing dnoegel/php-xdg-base-dir (0.1)
    Downloading: 100%         

  - Installing nikic/php-parser (v1.0.2)
    Downloading: 100%         

  - Installing symfony/console (v2.5.7)
    Downloading: 100%         

  - Installing psy/psysh (v0.2.1)
    Downloading: 100%         

symfony/console suggests installing symfony/event-dispatcher ()
symfony/console suggests installing psr/log (For using the console logger)
Writing lock file
Generating autoload files
```

```
$ vendor/bin/psysh 
Psy Shell v0.2.1 (PHP 5.5.19 — cli) by Justin Hileman
>>> $a=1;
=> 1
>>> $a+=3;
=> 4
```