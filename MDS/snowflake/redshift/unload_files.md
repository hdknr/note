# [How To: Migrate Data from Amazon Redshift into Snowflake](https://community.snowflake.com/s/article/How-To-Migrate-Data-from-Amazon-Redshift-into-Snowflake)

## Solution

Because Redshift runs in AWS, 
the [UNLOAD command](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/t_Unloading_tables.html) can unload table data directly to an S3 bucket. 

## example

empテーブルからデータをアンロード 
をそれぞれ mybucket と mypath という名前のプライベート S3 バケットとパスにアンロードします。:


~~~sql
unload ('select * from emp')
to 's3://mybucket/mypath/emp-'
credentials 'aws_access_key_id=XXX;aws_secret_access_key=XXX'
delimiter '\001'
null '\\N'
escape
[allowoverwrite]
[gzip];
~~~

Notes:

- デフォルトでは、UNLOADコマンドはRedshiftから並列にファイルをアンロードし、複数のファイルを作成します。
- 1つのファイルにアンロードするには、PARALLEL FALSEオプションを使用します。

S3バケットからSnowflakeの対応するempテーブルのデータをロードします。


~~~sql
copy into emp
from s3://mybucket/mypath/
credentials = (aws_key_id = 'XXX' aws_secret_key = 'XXX')
file_format = (
  type = csv
  field_delimiter = '\001'
  null_if = ('\\N')
);
~~~

Notes:

