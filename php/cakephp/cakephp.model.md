## テーブル名

~~~php
//controller
$this->モデル名->useTable;

//model
$this->useTable;
~~~

## モデル参照

~~~php
App::import('Model', 'Researcher');
$model = new Researcher();
~~~

## SQL文実行

~~~php 
$model_class->query("select * from ....");
~~~
