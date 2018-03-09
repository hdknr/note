# AWS RDS

- [RDS](aws.rds.md)
- [RDS PostgreSQL関連](aws.rds.md)

## Aurora

- [aurora](aws.rds.aurora.md)
- [charset](aws.rds.character-set.md)


## 記事

- [RDSで日本語が文字化けする問題](http://qiita.com/reoy/items/e355debf1e2b2abd703b)
- [Auroraでキャラクター変更](aws.rds.character-set.md)


## TIP

パスワード変更([pgsql](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyPostgreSQLInstance.html), [mysql](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.MySQL.html)):

~~~bash
$ aws rds modify-db-instance --db-instance-identifier <rds-endpoint> --master-user-password <new-password>
~~~
