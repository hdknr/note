# mysqldump

##  テーブルごとダンプ

```
mysqldump -u ユーザ名 -p -t データベース名 テーブル1 テーブル2...> ファイル名
```

## mysqldumpがStored Procudureを吐き出さない

- デフォルトで `—routines` が `False` だからです。

```bash

$ mysqldump -u dbu --password=dbp dbn --routines | grep PROCEDURE

/*!50003 DROP PROCEDURE IF EXISTS `insert_users` */;
CREATE DEFINER=`dbu`@`localhost` PROCEDURE `insert_users`()
```

## index 一覧

```bash
$ alias Q='mysql -u root --password=password  mydb'
$ echo "show tables" | Q -N | while read T ; do Q -t -e "show index from $T" ; done > index.txt
```