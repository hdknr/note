

## 他のShellをextends する

~~~
$ ls -l ../app/vendors/shells/*.php


-rwxr-xr-x 1 cakenr cakenr   220  3月  4 15:20 ../app/vendors/shells/check.php
-rwxr-xr-x 1 cakenr cakenr  3663  3月  4 15:03 ../app/vendors/shells/db.php
~~~

~~~
<?php
App::import('Vendor', 'DbShell', array('file' => 'shells'.DS.'db.php'));

class CheckShell extends DbShell {

    function hello()
    {   
    	  // DbShell#query_print(sqlstatements) を呼ぶ
        $this->query_print('select count(*) from users');    
    }   
}
?>
~~~

- DbShell#query_print で SQL文の実行結果をJSONダンプ

~~~
$ ../app/vendors/shells/cakesh.bash check hello
[
    [
        {
            "count(*)": "90"
        }
    ]
]
~~~
