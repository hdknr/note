# AWS RDS

- [RDS](aws.rds.md)
- [RDS PostgreSQL 関連](aws.rds.md)

## MySQL

- [RDS MySQL](MySQL/README.md)
- [MySQL を立てる](MySQL/aws.rds.mysql.md)

## Aurora

- [aurora](aws.rds.aurora.md)
- [charset](aws.rds.character-set.md)

## 記事

- [RDS で日本語が文字化けする問題](http://qiita.com/reoy/items/e355debf1e2b2abd703b)
- [Aurora でキャラクター変更](aws.rds.character-set.md)

## TIP

パスワード変更([pgsql](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyPostgreSQLInstance.html), [mysql](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.MySQL.html)):

```bash
$ aws rds modify-db-instance --db-instance-identifier <rds-endpoint> --master-user-password <new-password>
```
