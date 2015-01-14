# mysqlでSQLファイルを実行する

```
<?php
$path = dirname(__FILE__);
require_once('config.php');

function get_database(){
    global $config; 
    $dbp = $config['dbconfig'];
    $db = new mysqli(
        $dbp['db_host_name'],
        $dbp['db_user_name'], $dbp['db_password'],
        $dbp['db_name']);
    
    $db->set_charset('utf8');
    return $db;
}


$TABLES = array(
    'create_table1.sql',
    'create_table2.sql',
    'create_table3.sql',       
);

foreach($TABLES as $i){
  $sql = file_get_contents("{$path}/{$i}");
  echo get_database()->multi_query($sql);
}
```

# include/database/DBManagerFactory.php

- 要するに "{$db_manager_class}.php" を require_once しているだけです
- config.php の $sugar_config に設定で入っています

```
        // sanitize the name
        $my_db_manager = preg_replace("/[^A-Za-z0-9_-]/", "", $my_db_manager);

        if(!empty($config['db_manager_class'])){
            $my_db_manager = $config['db_manager_class'];
        } else {
            if(file_exists("custom/include/database/{$my_db_manager}.php")) {
                require_once("custom/include/database/{$my_db_manager}.php");
            } else {
                require_once("include/database/{$my_db_manager}.php");
            }   
        }   

        if(class_exists($my_db_manager)) {
            return new $my_db_manager();
        } else {
            return null;
        }   
```        
