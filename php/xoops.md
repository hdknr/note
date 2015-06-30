## 設定情報


- [psysh](http://psysh.org/)

~~~
$ ../../php/vendor/bin/psysh 
~~~

- mainfile.php

~~~
>>> require_once('mainfile.php')
~~~

- [get\_defined\_constants](http://php.net/manual/en/function.get-defined-constants.php) , [strpos](http://php.net/manual/en/function.strpos.php)

~~~
>>> foreach(get_defined_constants() as $k => $v){
   echo strpos($k, "XOOPS_", 0) === 0 ? "$k: $v\n":"";
}
XOOPS_MAINFILE_INCLUDED: 1
XOOPS_ROOT_PATH: /home/www.mysite.net/public_html
XOOPS_TRUST_PATH: /home/www.mysite.net/public_html/class
XOOPS_URL: https://www.mysite.net
XOOPS_DB_TYPE: mysql
XOOPS_DB_PREFIX: xoops
XOOPS_DB_HOST: localhost
XOOPS_DB_USER: xoops
XOOPS_DB_PASS: my_site_password
XOOPS_DB_NAME: my_site_database
XOOPS_DB_PCONNECT: 1
XOOPS_GROUP_ADMIN: 1
XOOPS_GROUP_USERS: 2
XOOPS_GROUP_ANONYMOUS: 3
=> null
~~~
