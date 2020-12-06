# AWS: RDS: SQL Server

- [Microsoft SQL Server データベースエンジンを実行する DB インスタンスに接続する - Amazon Relational Database Service](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html)

## 料金

- [料金 - Amazon RDS for SQL Server | AWS](https://aws.amazon.com/jp/rds/sqlserver/pricing/)

    | ap-east-1     |          |
    | ------------- | -------- |
    | db.t2.micro	| 0.031USD |
    | db.t2.small	| 0.062USD | 
    | db.t2.medium	| 0.124USD |

## データベース数

- [Amazon RDS for SQL Server が各データベースインスタンスのデータベース制限を最大 100 個に拡大しました](https://aws.amazon.com/jp/about-aws/whats-new/2019/05/amazon_rds_for_sql_server_increases/)
- [AWS Developer Forums: Multiple databases on one instance? ...](https://forums.aws.amazon.com/thread.jspa?messageID=771296)
- [mysql - How many databases can I create on a single Amazon RDS instance - Stack Overflow](https://stackoverflow.com/questions/16328807/how-many-databases-can-i-create-on-a-single-amazon-rds-instance)
- [よくある質問 - Amazon RDS | AWS](https://aws.amazon.com/jp/rds/faqs/#2)

Q: 1 つの DB インスタンスで何個のデータベースまたはスキーマを実行できますか?

    - RDS for Amazon Aurora: ソフトウェアによる制限はありません
    - RDS for MySQL: ソフトウェアによる制限はありません
    - RDS for MariaDB: ソフトウェアによる制限はありません
    - RDS for Oracle: インスタンスあたり 1 個のデータベース。データベースあたりのスキーマの数については、ソフトウェアによる制限はありません
    - RDS for SQL Server: インスタンスあたり最大 100 個のデータベース。こちらをご覧ください: Amazon RDS SQL Server ユーザーガイド
    - RDS for PostgreSQL: ソフトウェアによる制限はありません

## ネイティブバックアップ

- [Microsoft SQL Server のネイティブバックアップおよび復元のサポート - Amazon Relational Database Service](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.BackupRestore.html)
- [RDS for SQL Server へのインポート - Qiita](https://qiita.com/nis_nagaid_1984/items/99870c7a6e9ea5b777a4)
- [S3 にある SQLServer のバックアップ (.bak) から RDS へバッチを使ってリストアしてみる - Qiita](https://qiita.com/kusokamayarou/items/6eee9b8d0bb36820b35b)
- [RDS for Microsoft SQL Serverのバックアップ・リストアが簡単にできるようになりました！ ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/import-export-mssql-by-s3-bak-file/)

## インポート

データのインポートとエクスポートの詳細については、

- [SQL Server のデータインポートガイド](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html)、

S3:

- RDS インスタンスのオプショングループに `SQLSERVER_BACKUP_RESTORE` を追加
- 追加しただけでは有効になっていないので、 `[オプションの追加]` をおこなう。
- ここで、IAM Role を作って S3 にアクセスできるようになる。

復元(SSMSで接続):

~~~sql
exec msdb.dbo.rds_restore_database
@restore_db_name='database_name',
@s3_arn_to_restore_from='arn:aws:s3:::bucket_name/file_name';
~~~
