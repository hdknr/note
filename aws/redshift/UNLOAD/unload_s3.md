# S3へのアンロード

- [UNLOAD](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/r_UNLOAD.html)
- [データを Amazon S3 にアンロードする](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/t_Unloading_tables.html)


指定したバケットにアンロード:

~~~sql
unload ('select * from venue')   
to 's3://mybucket/tickit/unload/venue_' 
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
~~~

ファイル一覧:

~~~
venue_0000_part_00
venue_0001_part_00
venue_0002_part_00
venue_0003_part_00
~~~

- データファイルの最大サイズは 6.2 GB 
- ファイルのサイズはクラスター内のスライスの数で決まる
- PARALLEL OFF を指定すると単一ファイルになる

## maxfilesize

ファイルサイズを制限:

~~~sql
unload ('select * from venue')
to 's3://mybucket/tickit/unload/venue_' 
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
parallel off
maxfilesize 100 mb;
~~~

## manifest

~~~
unload ('select * from venue')
to 's3://mybucket/tickit/venue_' 
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest;
~~~

ファニフェスト(`manifest`ファイル):

~~~json
{
  "entries": [
    {"url":"s3://mybucket/tickit/venue_0000_part_00"},
    {"url":"s3://mybucket/tickit/venue_0001_part_00"},
    {"url":"s3://mybucket/tickit/venue_0002_part_00"},
    {"url":"s3://mybucket/tickit/venue_0003_part_00"}
  ]
}
~~~

## 強制上書き(`allowoverwrite`)

- すでに同名のファイルがあると異常終了するのがデフォルト

~~~sql
unload ('select * from venue') 
to 's3://mybucket/venue_pipe_' 
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest 
allowoverwrite;
~~~


## 記事

- [RedshiftでJSONファイル形式のUNLOADを試してみた](https://dev.classmethod.jp/articles/redshift-unloading-data-to-json-files/) (JSONオブジェクト行ファイル)
