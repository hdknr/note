## データのバルクインポート

- [Importing Data into PostgreSQL on Amazon RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.html)
- [Amazon RDS 上の PostgreSQL にデータをインポートする](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.html)

### インスタンス設定を一時変更

Modify your DB instance settings to the following:

- Disable DB instance backups (set backup_retention to 0)
- Disable Multi-AZ

### データベースパラメータを一時変更

Modify your DB parameter group to include the following settings.
You should test the parameter settings to find the most efficient settings for your DB instance:

- Increase the value of the maintenance_work_mem parameter
- Increase the value of the checkpoint_segments and checkpoint_timeout parameters to reduce the number of writes to the wal log
- Disable the synchronous_commit parameter (do not turn off FSYNC)
- Disable the PostgreSQL autovacuum parameter

Use the pg_dump -Fc (compressed) or pg_restore -j (parallel) commands with these settings.

Note:

  - The PostgreSQL command pg_dumpall requires super_user permissions
    that are not granted when you create a DB instance, so it cannot be used for importing data.


## リンク

- [A simple Python script for backing up a PostgreSQL database and uploading it to Amazon S3](https://www.calazan.com/a-simple-python-script-for-backing-up-a-postgresql-database-and-uploading-it-to-amazon-s3/)

- [pg_dump and pg_restore (DROP IF EXISTS)](http://stackoverflow.com/questions/22287914/pg-dump-and-pg-restore-drop-if-exists)

~~~
dropdb -h domain.edu -U me mydatabase
createdb -h domain.edu -U me -T template0 mydatabase # adjust encoding/locale if necessary
pg_restore -h domain.edu -p 5432 -U me -d mydatabase -W mydump.sql
~~~
