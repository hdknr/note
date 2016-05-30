

~~~php
>>> use Cake\Core\Configure;
=> null

>>> Configure::load('app')
=> true

>>> Configure::read('Datasources.default')                                                                                                                            
=> [
     "className" => "Cake\Database\Connection",
     "driver" => "Cake\Database\Driver\Mysql",
     "persistent" => false,
     "host" => "localhost",
     "username" => "my_app",
     "password" => "secret",
     "database" => "my_app",
     "encoding" => "utf8",
     "timezone" => "UTC",
     "flags" => [],
     "cacheMetadata" => true,
     "log" => false,
     "quoteIdentifiers" => false,
     "url" => null,
~~~
