# mysqldump

## `--defaults-file`

```ini
[client]
password = oj6aeDe9aik9AiK9
host = myaws-prod-db-instance.caoopx8dbdd0.ap-northeast-1.rds.amazonaws.com
user = myaws

[mysqldump]
password = oj6aeDe9aik9AiK9
host = myaws-prod-db-instance.caoopx8dbdd0.ap-northeast-1.rds.amazonaws.com
user = myaws
```

```bash
mysqldump --defaults-file=../.secrets/mysql-rds.ini --skip-extended-insert --set-gtid-purged=OFF  --complete-insert myapp
```

## データだけ( --no-create-info, -t)

```bash
$ mysqldump -u $DBU --password=$DBP -t $DBN events_event
```

## テーブルごとダンプ

```
mysqldump -u ユーザ名 -p -t データベース名 テーブル1 テーブル2...> ファイル名
```

## mysqldump が Stored Procudure を吐き出さない

- デフォルトで `—routines` が `False` だからです。

```bash

$ mysqldump -u dbu --password=dbp dbn --routines | grep PROCEDURE

/*!50003 DROP PROCEDURE IF EXISTS `insert_users` */;
CREATE DEFINER=`dbu`@`localhost` PROCEDURE `insert_users`()
```

## INSERT 文

`-c` : `--complete-insert`

```bash
$ mysqldump -c --skip-extended-insert
```

## index 一覧

```bash
$ alias Q='mysql -u root --password=password  mydb'
$ echo "show tables" | Q -N | while read T ; do Q -t -e "show index from $T" ; done > index.txt
```

## 記事

- [mysqldump まとめ](http://qiita.com/PlanetMeron/items/3a41e14607a65bc9b60c)
