# [How To: Upload Data from AWS s3 to Snowflake in a Simple Way](https://community.snowflake.com/s/article/How-To-Upload-Data-from-AWS-s3-to-Snowflake-in-a-Simple-Way)

現在では、データをソースからデスティネーションにインポートすることは、たいていの場合、些細な作業である。
適切なツールを使用すれば、複雑なデータセットをデータ処理エンジンに簡単にアップロード、変換することができます。

例えば、Snowflakeのクラウドデータウェアハウスにデータを追加するには、Fivetran、Alooma、StichなどのELTまたはETLツールを使用することができます。
また、Snowflake自体もデータの取り込みを支援するロードデータウィザードを提供しています。
これらのツールは高度なものであり、時には学習と練習が必要です。

最も重要なことは、これらのツールは非常に効果的であるため、その利便性に見合った対価を支払うことです。
しかし、もしあなたが、単にあるファイルに目を通し、それをアップロードしてプレビューを行う必要がある場合はどうでしょうか？
シンプルなカミソリで十分な場合、スイスナイフのようなフル機能は必要ないかもしれません。
このような観点から、私は、ローカルPCやAWSからデータを取り込むためのプロトタイプを作成するために、より軽量なアプローチを取ることにしました。
このアプリケーションは、ファイルを読み込み、適切なデータ型でデータベーステーブルを作成し、Snowflake Data Warehouseにデータをコピーする方法を知っておく必要があります。


私はCSVから始めました。
CSVの構造をSQLのテーブルに変換する適切なライブラリが見つかれば、私のプロジェクトは半日で終わると見積もっていました。
私は数時間かけてブログをググり、stackoverflowで調べ、Java、Python、C#を含む様々なライブラリをチェックしました。
その結果、私はとても驚き、他の多くの人たちもそのような解決策を探していることが分かりました。

この投稿では、Pythonと特別なライブラリ、Pandas、PySparkから始まる、CSVファイルによる多くの異なるアプローチを説明します。
これは、CSVやParquetの「インポーター」を自作することが可能であることを示すための簡単なプロジェクトに過ぎないのです。
CSVのすべての（100％）シナリオをカバーすることはできないかもしれませんが、後で改良することができます。

このアプリケーションを実行するには、Java（最新版）とSnowflakeのアカウントが必要です。無料トライアルアカウントを取得するには、ここにアクセスしてください。

## Importing Data into Snowflake Data Warehouse

Snowflake にデータをインポートするには、多くの方法があります。1つの方法は、
[Snowflakeウィザード](https://docs.snowflake.com/ja/user-guide/data-load-web-ui.html)を使用することです。
ウィザードはシンプルで効果的なツールですが、いくつかの制限があります。
私は、短いコマンドラインを実行して結果を確認するような、より簡単で「開発者」的なアプローチを好みますが、
他の人はウィザードがプロセスを案内してくれるのを好むかもしれません。

私のプロジェクトでは、CSV、Parquetファイルを指し、Headerを読み、Snowflake DBで宛先SQLテーブルスキーマを作成し、テーブルに入力する、という処理手順を紹介します。

さっそく、素朴な疑問が湧いてきた。
ファイルにはHeaderが必要なのか？
おそらく、この疑問はML/AIタスクのためのもので、将来的には私の解決すべき課題になるのだろう。
今のところ、これは単純な決定です。
ということで、ヘッダがあることをアプリケーションに知らせるように、設定ファイルをいじります。
また、ファイルにヘッダーがない場合のデフォルトのカラム名の行をconfigに追加することにします。
Snowflakeは完全なANSI SQLとSQL型をサポートしているので、今回のデモでは以下の型を処理することができます。
integer, float, boolean, date, varchar, timestamp. 設定ファイルでは、データ型を評価するために何行処理するかを指定することができます。

## Executing the Application

アプリケーションは、Snowflake アカウントに接続し、設定ファイルからすべてのプロパティを読み込みます。
次に、選択したデータベース/スキーマの場所に、ファイル名をテーブル名とするテーブルを作成します。
次に、中間的な場所にファイルをコピーするための一時的なステージが作成されます。


~~~
put file:////”+paramsInCSV.get(“fileNameWithPath”)+” @~/staged
~~~

ファイルに日付欄がある場合、コピー処理の日付形式として追加されます。


~~~
(“Copy into “+paramsInCSV.get(“fileName”)+” from @~/staged file_format = (type = csv field_delimiter = ‘“+paramsInCSV.get(“delimiter”)+”’ skip_header = 1 FIELD_OPTIONALLY_ENCLOSED_BY=’\”’ NULL_IF = (‘’,’NULL’, ‘null’, ‘\\N’) EMPTY_FIELD_AS_NULL = true “+sDateFormatSql+”);”);
~~~


この行は非常に重要で、インポート処理に大いに役立ちます。
デリミタは自動的に適用され、ヘッダーパラメータはスキップされ、必要に応じて引用符で囲まれたデータはそれらから消去され、どの値がNULLを使用しているかをチェックし、日付フォーマットを指定する。


AWS S3からCSVやCSV.gzのデータをコピーするためには、資格情報を持つS3を指すExternal Stageを作成する必要があります。


~~~
statement.execute(“create or replace stage my_csv_stage url = ‘s3://”+paramsInCSV.get(“bucketName”)+”’ credentials = (aws_key_id=’”+connParams.get(“accessKey”)+”’ aws_secret_key=’”+connParams.get(“secretKey”)+”’);”);
~~~

## Getting Data from a Parquet File

パーケットファイルからカラムや型を取得するには、単にS3バケットに接続するだけです。
パーケットファイルからスキーマを取得する最も簡単な方法は、「ParquetFileReader」コマンドを使用することです。
私は、ファイルのスキーマを取得するためにSparkを使用するいくつかのプロジェクトを見たことがあります。
これは可能ですが、私たちはAWSからではなくデスクトップからアプリケーションを実行することを計画しているので、非常に非効率的です。

さて、型変換について少し。
Parquetファイルの文字列値は、UTFオプション付きの'Binary'として保存されていることが非常に多い。
それを捕捉して'VARCHAR'にキャストすることにしました。
もう一つのトリックは、INT96がタイムスタンプ値として格納されていることがあり、アプリケーションは自動的にそれもキャストすることです。
'BYTE_ARRAY' はSnowflakeの 'BINARY' にキャストされます。他のすべてのParquet型は互換性があります。


Here are the Parquet types:

~~~
BOOLEAN: 1 bit boolean
INT32: 32 bit signed ints
INT64: 64 bit signed ints
INT96: 96 bit signed ints
FLOAT: IEEE 32-bit floating point values
DOUBLE: IEEE 64-bit floating point values
BYTE_ARRAY: arbitrarily long byte arrays
~~~


ParquetとSnowflakeのマージ方法については、
[こちらで詳しく説明](https://docs.snowflake.com/ja/user-guide/script-data-load-transform-parquet.html)しています。
Parquetファイルでは、カラム名とキャストを指定する必要があります。
ここで2つのヒントがあります。
まず、SQL は大文字と小文字を区別しませんが、Parquet ファイルで指定したカラム名をクエリで使用する必要があります。
2つ目のヒント：キャストは時々スキップされることがあります。
以下は、S3パーケットファイルからデータをアップロードするためのCOPYコマンドの例です。


~~~sql
COPY INTO userdata1 FROM (SELECT $1:registration_dttm::TIMESTAMP, $1:id::INTEGER,  $1:first_name::VARCHAR, $1:last_name::VARCHAR, $1:email::VARCHAR,  $1:gender::VARCHAR, $1:ip_address::VARCHAR, $1:cc::VARCHAR, $1:country::VARCHAR, $1:birthdate::VARCHAR, $1:salary::DOUBLE,  $1:title::VARCHAR, $1:comments::VARCHAR FROM @my_csv_stage/userdata1.parquet)  on_error = 'skip_file' file_format = (type = parquet);
~~~

validation_mode = 'RETURN_ERRORS'; とすれば、実行前に文のエラーを検証することができます。
[詳細はこちら](https://docs.snowflake.com/ja/sql-reference/functions/validate.html)。

そして最後は、STAGEをDROPします。これで、Snowflakeでテーブルを確認することができます。

例えば、ORCのサポート、Parquetファイルの処理リストの取得、ファイルのパターンの指定、複雑な型のサポートの追加、...巨大なローカルCSVファイルの分割と圧縮、適切なログの追加、その他多数、多数、です。

- [COPY INTO <テーブル>](https://docs.snowflake.com/ja/sql-reference/sql/copy-into-table.html)


## 資料

- https://github.com/kipgorr/pub



