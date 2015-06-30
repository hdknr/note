# MySQL


## 現在のデータベース

~~~
msql> SELECT database();
~~~

## 見つかった件数

- [参考](https://stackoverflow.com/questions/2229218/does-mysql-have-an-equivalent-to-rowcount-like-in-mssql)

## フィールド間でスワップ

- [こちら](https://stackoverflow.com/questions/37649/swapping-column-values-in-mysql)

##  ３月までは前年度

```
$ echo "select (CASE WHEN MONTH(NOW()) >= 4 THEN YEAR(NOW()) ELSE YEAR(NOW(    ))-1 END), NOW()" | QT
+---------------------------------------------------------------------------+---------------------+
| (CASE WHEN MONTH(NOW()) >= 4 THEN YEAR(NOW()) ELSE YEAR(NOW(    ))-1 END) | NOW()               |
+---------------------------------------------------------------------------+---------------------+
|                                                                      2016 | 2016-04-01 00:26:29 |
+---------------------------------------------------------------------------+---------------------+
```



## プロシージャ一覧の内容確認

- 一覧

```
SHOW PROCEDURE STATUS;
SHOW FUNCTION STATUS;
```

```
select name from mysql.proc 
```

- 詳細

```
show create procedure _name_ 
```

## UPDATE文の更新件数

- `-vvv` オプションで実行する
- 全部でてしまいますが...


## Unixユーザーに権限を与える

- vagrant ユーザーに全権与える

~~~
mysql> create user `vagrant`@`localhost` identified  by '';
~~~
~~~
mysql> grant all privileges on *.* to 'vagrant'@'localhost' with grant option;
~~~
