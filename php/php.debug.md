## 真っ白: エラーを表示させたい

~~~php
<?php
ini_set('display_errors', 1); 
error_reporting(E_ALL);
~~~

## phpinfo

~~~bash
$ php -r 'phpinfo();'
~~~

## 関数がある？

~~~bash
$ php -r "var_dump(function_exists('gettext'));"

bool(false)
~~~