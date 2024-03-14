# PostgreSQL

- [Aurora PostgreSQL DB クラスターから Amazon S3 へのデータのエクスポート](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export.html)


## aws_s3.query_export_to_s3

- https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export.html#aws_s3.export_query_to_s3

~~~sql
aws_s3.query_export_to_s3(
    query text,    
    s3_info aws_commons._s3_uri_1,    
    options text
)
~~~


## `row_to_json`

~~~sql
SELECT row_to_json(r) FROM my_table AS r;
~~~

- https://github.com/chimpler/postgres-aws-s3/issues/10


~~~sql
select * from aws_s3.query_export_to_s3(
    'select row_to_json(test) from (select * from animals) test',
    aws_commons.create_s3_uri(
        'test-bucket',
        'somedata.json',
        'us-east-1'),
    options :='format text');
~~~


## 資料

- [COPY options](https://www.postgresql.org/docs/current/sql-copy.html)
- [PostgreSQL でダブルクォートを含んだフィールドが正しくインポートできない場合](https://obel.hatenablog.jp/entry/20170113/1484280528)
- [9.15. JSON Functions and Operators](https://www.postgresql.org/docs/9.6/functions-json.html)
- [Export Postgres table as json](https://dba.stackexchange.com/questions/90482/export-postgres-table-as-json)