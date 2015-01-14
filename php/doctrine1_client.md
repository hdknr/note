Doctrine1: フロントエンドコマンド

# db.php

- phpenvで入れたPHP5.5.19で確認
- Doctrine1はcomposerでいれてる(../vender/doctrine/doctrine1)
- db.php で以下をコピペ

```php:db.php

#!/usr/bin/env php
<?php

# Configuration
require_once(dirname(__FILE__).'/db.conf.php'); // $DB にパラメータを設定

$dsn = "mysql:dbname={$DB['DBN']};host={$DB['DBH']}"; 
$user = $DB['DBU'];
$password = $DB['DBP'];

$BASE = dirname(__FILE__). "/data";

# Directory Configuration for Doctrine
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

# Doctorine Configuration
$manager = Doctrine_Manager::getInstance();

$manager->setAttribute(Doctrine::ATTR_VALIDATE, Doctrine::VALIDATE_ALL);
$manager->setAttribute(Doctrine::ATTR_EXPORT, Doctrine::EXPORT_ALL);
$manager->setAttribute(Doctrine::ATTR_MODEL_LOADING, Doctrine::MODEL_LOADING_CONSERVATIVE);
$manager->setAttribute(Doctrine::ATTR_AUTO_ACCESSOR_OVERRIDE, true);
$manager->setAttribute(Doctrine::ATTR_AUTOLOAD_TABLE_CLASSES, true);

# Connect Database
$conn = Doctrine_Manager::connection(new PDO($dsn, $user, $password));


# Command Execution

(new Doctrine_Cli($config))->run($_SERVER['argv']);

?>
```

# 確認

```
$ ./db.php 

Doctrine Command Line Interface

./db.php compile
./db.php rebuild-db
./db.php generate-migrations-diff
./db.php build-all-load
./db.php create-db
./db.php build-all-reload
./db.php dump-data
./db.php load-data
./db.php build-all
./db.php dql
./db.php generate-models-db
./db.php generate-migration
./db.php generate-yaml-models
./db.php drop-db
./db.php generate-migrations-models
./db.php generate-models-yaml
./db.php generate-sql
./db.php generate-migrations-db
./db.php generate-yaml-db
./db.php migrate
./db.php create-tables

```
