## include されたスクリプトのコンテキストは、した方のコンテキスト

- "インクルード"だからそこに展開される
- できるからと言ってやっていいのか？というのがあるが実際にやられているコードがある(> <)

- main.php

~~~php

<?php

class Greetings{
    function __construct(){
        date_default_timezone_set('Asia/Tokyo');
    }

    function hello(){
        include "hello.php";		// require でも動いてしまう
    }

    function say_hello($msg){
        echo "$msg\n";
    }
}

(new Greetings())->hello();
~~~

- hello.php

~~~php
<?php 
$msg = get_class($this). ":Hello " . date("Y/m/d(D) H:i:s");
$this->say_hello($msg);
				 
~~~

- 実行

~~~
$ php  main.php 
Greetings:Hello 2015/08/13(Thu) 01:58:31
~~~

### python

- Python(2)でもできてしまう
- main.py

~~~py
from datetime import datetime


class Greetings(object):
    def hello(self):
        execfile('hello.py')		## not work with Python3 http://bit.ly/1Mkrg4A
		  
    def say_hello(self, msg):
        print msg

Greetings().hello()
~~~

- hello.py

~~~py
self.say_hello("{0}:Hello {1}".format(
    type(self).__name__ , datetime.now().strftime("%Y/%m/%D %H:%M:%S")))
~~~

