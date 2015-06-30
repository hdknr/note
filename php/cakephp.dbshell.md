CakePHP: python manage.py dbshell みたいなやつ

## app/vendors/shells/db.php

- データベース関係の諸々
- mysql()が重要

~~~php

<?php
App::import('Model', 'AppModel');
App::import('Core', 'ConnectionManager'); 

class DbShell extends Shell {

    function _welcome() {
        // parent::_welcomde();
        // echo 'another code';
    }

    protected function query($sql){
        return (new AppModel())->query($sql);
    }
    
    protected function query_print($sql)
    {
        echo json_encode($this->query($sql), JSON_PRETTY_PRINT);
    }

    protected function mysqldump($file, $table="", $opts=array() )
    {
        $db =& ConnectionManager::getDataSource('default');

        $cmd = sprintf("mysqldump %s -u %s --password='%s' %s {$table} > {$file}",
            join(" ", $opts),
            $db->config['login'],
            $db->config['password'],
            $db->config['database']);

        exec($cmd);
    }

    protected function mysql($file)
    {
        $db =& ConnectionManager::getDataSource('default');

        $redir = @$file ? "<" : "";
        $file = @$file ?: '';
        $cmd = sprintf("mysql --default-character-set=utf8 %s -u %s --password='%s' %s {$redir} {$file}",
            '',
            $db->config['login'],
            $db->config['password'],
            $db->config['database']);
        
        if( $file != '' ){
            exec($cmd);
        } else {
            echo "{$cmd}\n";
        }
    }
    function echo_mysql()		// <-- これ
    {
        $this->mysql('');
    }
        
    function main()
    {
        echo "1)Tools:\n"; 
        echo "conf: database configration\n";
        echo "tables:  list tables\n";
        echo "schema:  list field infos for a table\n";
        echo "exec: execute SQL script and print output\n";
        echo "\n\n";
        echo "2)mysqldump related:\n";
        echo "dump_ddl: dump DDL in SQL file\n";
        echo "dump_data: dump data in SQL file\n";
        echo "load: load SQL script\n";
       
    }

    function conf()
    {
        $datasource = ConnectionManager::getDataSource('default');
        echo json_encode($datasource->config, JSON_PRETTY_PRINT);
    }

    function schema()
    {
        $columns = array(
            "Field", "Type", "Null", "Key", "Default", "Extra" );

        echo join("\t|", $columns), "\n";
        foreach($this->query("desc {$this->args[0]}") as $field)
        {
            $x = array_values($field)[0];
            foreach($columns as $c ){
                echo "{$x[$c]} \t|";
            }
            echo "\n";
        }
    }  

    function dump_ddl()
    {
        $table = @$this->args[0] ?: '';
        $file = sprintf("ddl.%s.sql", @$table ?: "all");
        $this->mysqldump($file, $table, array("-d"));
    }

    function dump_data()
    {
        $table = @$this->args[0] ?: '';
        $file = sprintf("data.%s.sql", @$table ?: "all");
        $this->mysqldump($file, $table, 
            array(
                "--skip-extended-insert",
                "-c",
                "-t")
        );
    }

    function load()
    {
        if(count($this->args) < 1){
            echo "SQLスクリプト名を指定してください\n";
            return ;
        }
        $this->mysql($this->args[0]);
    }

    function exec()
    {
        if(count($this->args) < 1){
            echo "SQLスクリプト名を指定してください\n";
            return ;
        }
        $res = $this->query(file_get_contents($this->args[0])); 
        echo json_encode($res, JSON_PRETTY_PRINT);
    }
}
?>
~~~

## app/vendors/shells/cakesh.bash

- "dbshell" が指定されたらmysqlコマンドのフロントエンドとして動く

~~~bash

#!/bin/bash
BASEDIR=$(readlink -f $0 | xargs dirname | xargs dirname | xargs dirname | xargs dirname)


if [ "$1" == "dbshell" ] ; then
    $BASEDIR/cake/console/cake -app $BASEDIR/app db echo_mysql;
    eval "`$BASEDIR/cake/console/cake -app $BASEDIR/app db echo_mysql` -t";
else
    COMMAND=${1%.*}
    ARGS=${@:2}
    $BASEDIR/cake/console/cake -app $BASEDIR/app $COMMAND $ARGS
fi
~~~

## 例

~~~
$ ../app/vendors/shells/cakesh.bash dbshell

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1446
Server version: 5.5.41-0+wheezy1-log (Debian)

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
~~~

~~~
$ echo "select count(*) from users" | ../app/vendors/shells/cakesh.bash dbshell

+----------+
| count(*) |
+----------+
|       90 |
+----------+
~~~
