# MySQL

## Topic

- [pytz](mysql.pytz.md)
- [照合順序](mysql.collate.md)
- [rootパスワード変更](mysql.password.md)


## ファイルから読み込んでBLOBに入れる

~~~sql
INSERT INTO
  my_table (stamp, docFile)
VALUES
  (NOW(), LOAD_FILE('/tmp/my_file.odt'))
~~~

## truncate : `Cannot truncate a table referenced in a foreign key constraint`


~~~sql
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE table1;
SET FOREIGN_KEY_CHECKS = 1;
~~~


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

- [MySQL の権限のコマンドまとめ。](http://qiita.com/PallCreaker/items/0b02c5f42be5d1a14adb)


## 時刻

~~~mysql
SELECT UNIX_TIMESTAMP('2005-03-27 03:00:00');

+---------------------------------------+
| UNIX_TIMESTAMP('2005-03-27 03:00:00') |
+---------------------------------------+
|                            1111892400 |
+---------------------------------------+
1 row in set (0.00 sec)
~~~

## スキーマ変更

- [テーブル変更](sql.alter.table.md)

## ERROR 1267 (HY000) at line 1: Illegal mix of collations (utf8_unicode_ci,IMPLICIT) and (utf8_general_ci,IMPLICIT) for operation '='


~~~msyql
UPDATE score as A
  INNER JOIN researchers as R
ON(A.personal_no = R.personal_no COLLATE  utf8_general_ci)
SET
  A.grade = R.grade
WHERE
   A.grade = '' and A.personal_no <> '';
~~~


## CAST

~~~mysql
mysql> select CAST('43214' as unsigned);                                                                                                                                      
+---------------------------+
| CAST('43214' as unsigned) |
+---------------------------+
|                     43214 |
+---------------------------+
1 row in set (0.01 sec)
~~~
