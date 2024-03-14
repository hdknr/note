# COPY

- [COPYを使用した一括ロード](https://docs.snowflake.com/ja/user-guide/data-load-bulk.html#)
- [Amazon S3からの一括ロード](https://docs.snowflake.com/ja/user-guide/data-load-s3.html)
- [COPY INTO <テーブル>](https://docs.snowflake.com/ja/sql-reference/sql/copy-into-table.html#additional-cloud-provider-parameters)
- [ステップ1。データをターゲットテーブルにコピーする](https://docs.snowflake.com/ja/user-guide/json-basics-tutorial-copy-into.html)

 
## オプション

- `FIELD_OPTIONALLY_ENCLOSED_BY`  - 文字列を囲むのに使用される文字。値は、 NONE、一重引用符（'）、または二重引用符（"）のいずれかです

## ndjson サポート

- [ndjson Newline Delimited JSON](http://ndjson.org/)
- [ndjsonをサポートしている](https://docs.snowflake.com/en/sql-reference/sql/create-file-format.html#required-parameters)
- [使用上の注意](https://docs.snowflake.com/ja/sql-reference/sql/copy-into-table.html#usage-notes)

ソース:

- [MySQL](mysql.md)
- [PostgreSQL](pgsql.md)

## 記事

- [Amazon Aurora MySQLとS3間でデータをロード&アンロードする](https://dev.classmethod.jp/articles/aurora-mysql-integrate-with-s3/)
- [SnowflakeのCOPYコマンド実行時にロードするファイルを指定してみた](https://dev.classmethod.jp/articles/snowflake-copy-option-files-pattern/)
- [SnowflakeのCOPYコマンドでステージのファイルにデータをアンロードしてみた](https://dev.classmethod.jp/articles/snowflake-copy-unload/)
