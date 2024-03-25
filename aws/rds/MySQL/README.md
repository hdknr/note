# RDS MySQL

## mysqldump

- [MySQL の mysqldump でローカルにファイルを作成せず s3 にバックアップ&リストアする方法](https://rooter.jp/infra-ops/mysql_dump_s3_directly/)

```bash
mysqldump -u root db_name table_name | bzip2 | aws s3 cp - s3://test-bucket/test/xxx.bz2
```

### [テーブルロック](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_lock-tables):

`--lock-table`:

- [mysqldump した時にテーブルロックが起こる](https://qiita.com/Nedward/items/ee790b7ebd713c93eb22)

```bash
mysqldump -u root -p -d db_name --lock-tables=false > db_name.sql
```

`--skip-lock-tables`:

- [InnoDB データベースで mysqldump する時は、single-transaction と skip-lock-tables のオプションをつけよう](https://masyus.work/articles/if-using-mysqldump-add-single-transaction-skip-lock-table/)

`--set-gtid-purged=OFF`:

- MariaDB には存在しません ([今日は、mysqldump コマンドで「unknown variable 'set-gtid-purged=OFF'」が出るの日。](https://updraft.hatenadiary.com/entry/2023/05/23/070029))

## 資料

- [Python でシェルコマンドを実行する](https://tech.mobilefactory.jp/entry/2018/12/27/150000)
