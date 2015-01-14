Doctrine1+psysh: Djangoのpython manage.py shell みたいにモデルデータの確認とかしてみる

# Doctrine1 設定

- Django のデータベースに設定を合わせる

```php:db.conf.php

<?php
$DB=array(
    "DBU" => "myapp",
    "DBP" => "myapp",
    "DBN" => "myapp",
    "DBH" => "localhost"
); 
?>
```

- Doctrine 設定

```php:db.boot.php

<?php
require_once(dirname(__FILE__).'/db.conf.php');

$dsn = "mysql:dbname={$DB['DBN']};host={$DB['DBH']}"; 
$user = $DB['DBU'];
$password = $DB['DBP'];

# Database
$BASE = dirname(__FILE__). "/data";
$config = array();
foreach(['data_fixtures', 'models', 'migrations', 'sql', 'yaml_schema'] 
        as $i ){
    $p = "{$BASE}/{$i}";
    $config["{$i}_path"] = $p;
    @mkdir($p, 0777);
}

# Load & Register Library
require_once(dirname(dirname(__FILE__)) . '/vendor/doctrine/doctrine1/lib/Doctrine.php');

spl_autoload_register(array('Doctrine', 'autoload')); 
spl_autoload_register(array('Doctrine', 'modelsAutoload'));
spl_autoload_register(array('Doctrine', 'extensionsAutoload'));

# Doctorine Congigure
$manager = Doctrine_Manager::getInstance();

$manager->setAttribute(Doctrine::ATTR_VALIDATE, Doctrine::VALIDATE_ALL);
$manager->setAttribute(Doctrine::ATTR_EXPORT, Doctrine::EXPORT_ALL);
$manager->setAttribute(Doctrine::ATTR_MODEL_LOADING, Doctrine::MODEL_LOADING_CONSERVATIVE);
$manager->setAttribute(Doctrine::ATTR_AUTO_ACCESSOR_OVERRIDE, true);
$manager->setAttribute(Doctrine::ATTR_AUTOLOAD_TABLE_CLASSES, true);

$dbh = new PDO($dsn, $user, $password);

# Connect Database
$conn = Doctrine_Manager::connection($dbh);
?>
```

- クライアントツール

```php:db.php

#!/usr/bin/env php
<?php
require_once(dirname(__FILE__).'/db.boot.php');

(new Doctrine_Cli($config))->run($_SERVER['argv']);

?>
```

# DjagoのDBからクラス作成

```bash

$ ./db.php generate-models-db

generate-models-db - Generated models successfully from databases
```

```bash

$ tree data
data
└── models
    ├── AuthGroupPermissions.php
    ├── AuthGroup.php
    ├── AuthPermission.php
    ├── AuthUserGroups.php
    ├── AuthUser.php
    ├── AuthUserUserPermissions.php
    ├── DjangoAdminLog.php
    ├── DjangoContentType.php
    ├── DjangoMigrations.php
    ├── DjangoSession.php
    └── generated
        ├── BaseAuthGroupPermissions.php
        ├── BaseAuthGroup.php
        ├── BaseAuthPermission.php
        ├── BaseAuthUserGroups.php
        ├── BaseAuthUser.php
        ├── BaseAuthUserUserPermissions.php
        ├── BaseDjangoAdminLog.php
        ├── BaseDjangoContentType.php
        ├── BaseDjangoMigrations.php
        └── BaseDjangoSession.php

2 directories, 20 files
```

# PHPのアプリケーション設定

- 生成したモデルをロードするようにする

```php:app.conf.php

<?php
require_once(dirname(__FILE__).'/db.boot.php');
Doctrine_Core::loadModels( $BASE.'/models/generated');
Doctrine_Core::loadModels( $BASE.'/models');
```

# psysh で確認

- psysh 起動

```
$ ../vendor/bin/psysh 
Psy Shell v0.2.1 (PHP 5.5.19 — cli) by Justin Hileman

```
- モデルクラスを読み込む(mkdirで警告)

```
>>> require_once("app.conf.php");
PHP warning:  mkdir(): File exists on /home/vagrant/projects/doctrine/php/db.boot.phpon line 15

=> 1
```

- AuthUser モデルのクエリ

```
>>> $q = Doctrine_Query::create()->from('AuthUser u');
=> <Doctrine_Query #000000001e2b3fc50000000057b1d722> {}
```

- 実行(全件取得)

```
>>> $r = $q->fetchArray();
=> [
       [
           "id"           => "1",
           "password"     => "pbkdf2_sha256$12000$US9PWnuJx7ab$sF6qo8/3fdf+U2jvIuDtP9EYM7rPLKudWWhj5BrBkaI=",
           "last_login"   => "2014-12-03 04:35:02",
           "is_superuser" => "1",
           "username"     => "admin",
           "first_name"   => "",
           "last_name"    => "",
           "email"        => "admin@admin.admin",
           "is_staff"     => "1",
           "is_active"    => "1",
           "date_joined"  => "2014-12-03 04:35:02"
       ]
   ]
```

- username == 'admin'

```
>>> $r[0]['username']
=> "admin"
```

- Where条件入れてみる(存在しないので０件)

```
>>> $q = $q->Where("u.username = 'hoge'");
=> <Doctrine_Query #000000001e2b3fc50000000057b1d722> {}
>>> $q->fetchArray();
=> []
```
