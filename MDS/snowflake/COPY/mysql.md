# MySQL: ndjson

~~~sql
SELECT * FROM score_table
INTO OUTFILE 'C:\\test\\score_table3.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '“';
~~~

### JSON_OBJECT で ndjson を出力

~~~sql
GRANT FILE ON *.* TO 'epm_server'@'%';
~~~

~~~sql
SELECT 
    JSON_OBJECT(
        "id", id, 
        "outstanding_invoice_amount", outstanding_invoice_amount
    ) as unload
FROM    
    sales_clearing;
~~~

- [権限](https://dba.stackexchange.com/questions/17029/cannot-output-mysql-data-to-file)

## 記事

- [[MySQL]CSVファイルのエクスポート・インポート方法とは？基本的な使い方・オプションの指定方法](https://www.fenet.jp/infla/column/technology/mysqlcsv%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9D%E3%83%BC%E3%83%88%E3%83%BB%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88%E6%96%B9%E6%B3%95%E3%81%A8%E3%81%AF/)
- [Amazon Aurora MySQL DB クラスターから Amazon S3 バケット内のテキストファイルへのデータの保存](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.SaveIntoS3.html)
- [Generating Newline-Delimited JSON (NDJSON) Using JSON_OBJECT() In MySQL 5.7.32](https://www.bennadel.com/blog/3962-generating-newline-delimited-json-ndjson-using-json-object-in-mysql-5-7-32.htm)

