# Amazon Aurora to Snowflake ETL: 5 Steps to Move Data Easily

多くの場合、企業はトランザクションを保存するために別のデータベース（例：Amazon Aurora）を持ち、
企業の分析ニーズに対応するために別のデータウェアハウス（例：Snowflake）を持っています。
トランザクションデータベースからウェアハウスへデータを移行する主な理由は2つあります
（例：Amazon AuroraからSnowflake）。

まず、トランザクションデータベースは高速な書き込みとレスポンスに最適化されています。
大規模なデータセットに対して、多くの集計や結合を伴う分析クエリを実行すると、データベースの速度が低下します。
これは、最終的に顧客体験に影響を与える可能性があります。
次に、データウェアハウスはデータセットと分析クエリのスケーリングに対応できるように構築されています。
さらに、複数のデータソースからのデータをホストし、より深い分析を支援することができます。

この記事では、AuroraとSnowflakeを紹介します。
また、AuroraからSnowflakeにデータを移動する手順も紹介します。
さらに、この方法に関連するいくつかの制限を探ります。
これらの課題を解決するための、より簡単な代替案も紹介されます。
AuroraからSnowflakeへのデータ移行について理解し、洞察を得るためにお読みください。


## Table of Contents

- Understanding Aurora and Snowflake
- Move Data from Aurora to Snowflake using ETL Scripts

    - Extract Data from Aurora Cluster to S3
    - Convert Data Types and Format them
    - Stage Data Files to the Snowflake Staging Area
    - Import Staged Files to Snowflake Table

- Update Snowflake Table
- Limitations of Writing Custom ETL Code to Move Data from Aurora to Snowflake
- Conclusion

## Understanding Aurora and Snowflake


AWS RDS (Relational Database) は、オープンソースとプロプライエタリのデータベースのほとんどをサポートするAWSの最初のリレーショナルデータベースサービスです。
MySQLやPostgreSQLのようなRDSのオープンソースオファリングは、
Oracleのようなエンタープライズデータベースソリューションに比べてはるかにコスト効率的です。
しかし、ほとんどの場合、オープンソースのソリューションは、パフォーマンスや同時接続などの他の側面でエンタープライズRDBMSと同等になるために、
多くのパフォーマンスチューニングを必要とします。


AWSは、MySQLやPostgreSQLと互換性のある新しいリレーショナルデータベースサービス「Aurora」を導入し、
これらのデータベースがエンタープライズデータベースよりはるかに安価であるという弱点を克服しました。
多くの組織が主要なトランザクションデータベースシステムとしてAuroraに移行しているのも不思議ではありません。


一方、Snowflakeは費用対効果が高く、高速なデータウェアハウスソリューションと言えるでしょう。
動的なスケーリングが可能なコンピュート・リソースと、完全に分離・課金されるストレージを備えています。
Snowflakeは、AWSを含むさまざまなクラウドベンダー上で動作させることができます。
そのため、AuroraからSnowflakeへのデータ移動も少ないコストで行うことができます。
Snowflakeの特徴については[こちら](https://hevodata.com/blog/snowflake-data-warehouse-features/)をご覧ください。



この記事では、AuroraからSnowflakeにデータを移行するための方法1について詳しく説明します。また、この方法の限界とそれを解決するための回避策をブログで紹介します。

## Move Data from Aurora to Snowflake using ETL Scripts


上図のように、AuroraからSnowflakeへのデータ移行は以下の手順で行います。

- AuroraクラスタからS3へデータを抽出する
- データ型を変換し、フォーマットする
- データファイルをSnowflakeのステージングエリアにステージングする
- ステージングされたファイルをSnowflakeのテーブルにインポートする
- Snowflakeテーブルの更新



### 1. AuroraクラスタからS3へデータを抽出する

`SELECT INTO OUTFILE S3` ステートメントは、Aurora MySQLクラスタからデータを照会し、結果をS3に保存するために使用することができます。
この方法では、データは高速かつ効率的な方法でクライアントサイドに到達します。
Aurora クラスタから S3 にデータを保存するために、適切なパーミッションが設定されている必要があります。

そのためには

- S3オブジェクトにアクセスするために適切なIAMポリシーを作成する - こちらで[AWSのドキュメント](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.S3CreatePolicy.html)を参照してください。
- 新しいIAMロールを作成し、上記のステップで作成したIAMポリシーをアタッチします。
- `aurora_select_into_s3_role` または `aws_default_s3_role` クラスタパラメータを新しいIAMロールのARNに設定します。
- 作成したIAMロールをAuroraクラスターに関連付けます。
- S3へのアウトバウンド接続を許可するようにAuroraクラスタを設定します - [詳しくはこちら](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.Network.html)。


ユーザー特権:

SELECT INTO OUTFILE S3 を発行するユーザーは、そのための特権を持っている必要があります。
アクセスを許可するために -


~~~
GRANT SELECT INTO S3 ON *.* TO 'user'@'domain'.
~~~


この権限はAuroraに特有のものであることに注意してください。
RDSにはそのような権限オプションはありません。

マニフェストファイル :

MANIFEST ON オプションを設定すると、S3 パスにアップロードされた出力ファイルをリストアップする JSON 形式のマニフェストファイルを作成することができます。
ファイルは、作成されたのと同じ順序でリストされることに注意してください。

例

~~~json
{
  "entries": [
    {
      "url": "s3-us-east-1://s3_bucket/file_prefix.part_00000"
    },
    {
      "url": "s3-us-east-1://s3_bucket/file_prefix.part_00001"
    },
    { "url": "s3-us-east-1://s3_bucket/file_prefix.part_00002" }
  ]
}

~~~


出力ファイル :

- 出力は区切られたテキストファイルとして保存されます。現在のところ、圧縮ファイルや暗号化されたファイルはサポートされていません。

既存のファイルを上書きする:

- S3に正確な名前のファイルが存在する場合、削除するためにオプションOVERWRITE ONを設定します。
- デフォルトのファイルサイズは6GBです。
- ステートメントで選択されたデータがより小さい場合、1つのファイルが作成されます。
- それ以外の場合は、複数のファイルが作成されます。ファイルの境界を越えて行が分割されることはありません。
- エクスポートするデータ量が25GBを超える場合、複数のステートメントを実行してデータをエクスポートすることをお勧めします。
- 各ステートメントで、データの異なる部分を処理します。
- テーブルスキーマのようなメタデータはS3にアップロードされません。
- 現在のところ、データエクスポートの進捗を直接監視する方法はありません。1つの簡単な方法は、マニフェストオプションをオンに設定し、マニフェストファイルを最後に作成されたファイルにすることです。例

    - 以下の文は、異なる地域に位置するS3に書き込む。各フィールドはカンマで、各行は'n'で終了する。

~~~sql
SELECT * FROM students INTO OUTFILE S3 's3-us-west-2://aurora-out/sample_students_data' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY 'n';
~~~

- 以下は、同じリージョンにあるS3に書き込む例です。マニフェストファイルも作成されます。

~~~sql
SELECT * FROM students INTO OUTFILE S3 's3://aurora-out/sample_students_data' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY 'n' 
MANIFEST ON;
~~~

### 2. データ型の変換とフォーマット

AuroraからSnowflakeにデータを転送する際に、ビジネスロジックや組織標準に対応したデータ変換を行う場合があります。
このようなハイレベルなマッピングとは別に、一般的に考慮すべき基本的な事柄を以下に列挙します。

UTF-8、UTF-16を含むすべての一般的な文字セットはSnowflakeでサポートされています。
完全なリストはここで見ることができます。
多くのクラウドベースおよびオープンソースのビッグデータシステムは、主キーのような標準的なリレーショナルデータベースの制約を妥協しています。

しかし、SnowflakeはUNIQUE、PRIMARY KEY、FOREIGN KEY、NOT NULL制約など、すべてのSQL制約をサポートしていることに注意してください。
これは、データをロードするときに役立つかもしれません。
Snowflake のデータ型サポートは、配列のようなネストされたデータ構造も含め、かなり豊富です。

以下は、Snowflake のデータ型とそれに対応する MySQL のAurora型のリストです。

[型変換表]

Snowflakeは、日付や時刻のフォーマットを柔軟に変更することができます。
カスタムフォーマットを使用する場合、テーブルにデータをロードする際にファイルフォーマットオプションを使用して明示的に指定することができます。
[日付と時刻のフォーマットの完全なリストはこちらでご覧になれます](https://docs.snowflake.net/manuals/sql-reference/data-types-datetime.html#date-and-time-formats)。


### 3. データファイルをSnowflakeのステージングエリアにアップロードする

Snowflakeでは、テーブルにロードする前に、データを一時的な場所にアップロードする必要があります。
この一時的な場所は、SnowflakeがアクセスできるS3ロケーションです。
このプロセスはステージングと呼ばれます。
Snowflakeのステージは、内部または外部のいずれかにすることができます。

(A) 内部ステージ

Snowflakeでは、ユーザやテーブルごとに、データファイル用の内部ステージが自動的に割り当てられます。また、明示的に内部ステージを作成し、名前を付けることも可能です。

- ユーザーに割り当てられたステージは「@〜」のような名前になります。
- テーブルに割り当てられたステージは、そのテーブルの名前を持ちます。
- ユーザーやテーブルに割り当てられたデフォルトのステージは、変更したり削除したりすることはできません。
- ユーザーまたはテーブルに割り当てられたデフォルトのステージは、ファイル形式オプションの設定をサポートしていません。

上記のように、内部ステージはSQLステートメントを使用してユーザーが明示的に作成することもできます。このように明示的にステージを作成している間、ファイル形式、日付形式など、多くのデータロードオプションをそれらのステージに割り当てることができます。

データロードやテーブル作成のためにSnowflakeとやり取りする際、SnowSQLはLinux/Mac/Windowsで利用可能な非常に便利なクライアントとしてこのツールおよびオプションの詳細については、[こちらをご覧ください。](https://docs.snowflake.net/manuals/user-guide/snowsql.html)

以下は、ステージを作成するためのコマンドの例です。

以下のように、名前を付けた内部ステージを作成します。

~~~sql
my_aurora_stage  and assign some default options:

create or replace stage my_aurora_stage

copy_options = (on_error='skip_file')

file_format = (type = 'CSV' field_delimiter = '|' skip_header = 1);
~~~

PUTは、Snowflakeの内部ステージにファイルをステージングするために使用されるコマンドです。
PUTコマンドの構文は、:

~~~
PUT file://path_to_file/filename internal_stage_name
~~~


例

tmp/aurora_data/data/ ディレクトリにある students_data.csv というファイルを aurora_stage という名前の内部ステージにアップロードします．

~~~
put file:////tmp/aurora_data/data/students_data.csv @aurora_stage;
~~~


Snowflakeには、ファイルアップロード時の並列数、自動圧縮など、データロードのパフォーマンスを向上させるために使用できるオプションが多数用意されています。
詳細とオプションの完全なリストは、[ここにリストされています](https://docs.snowflake.net/manuals/sql-reference/sql/put.html)。



(B) 外部ステージ

内部ステージと同様に、Snowflakeは外部ステージング場所としてAmazon S3およびMicrosoft Azureをサポートしています。
Snowflakeからアクセスできる外部ステージに既にデータがアップロードされている場合、そのデータをSnowflakeのテーブルに直接読み込むことができます。
内部ステージにデータを移動する必要はありません。

S3上に外部ステージを作成するには、適切なアクセス権限を持つIAMクレデンシャルを提供する必要があります。
データが暗号化されている場合は、暗号化キーを提供する必要があります。

~~~sql
create or replace stage aurora_ext_stage url='s3://snowflake_aurora/data/load/files/'

credentials=(aws_key_id='13311a23344rrb3c' aws_secret_key='abddfgrrcd4kx5y6z');

encryption=(master_key = 'eSxX0jzsdsdYfIjkahsdkjamNNNaaaDwOaO8=');
~~~


各クラウドサービスを利用して外部ステージにデータをアップロードすることができます。
Amazon AuroraのデータはS3にエクスポートされ、その場所自体を外部ステージング場所として使用できるため、データの移動を最小化することができます。


### 4. ステージングされたファイルのSnowflakeテーブルへのインポート

ここで、データは外部または内部ステージに存在し、Snowflakeテーブルにロードする必要があります。
これを行うために使用するコマンドはCOPY INTOです。
COPY INTOコマンドを実行するには、Snowflakeの仮想ウェアハウスという形で計算リソースが必要で、消費量に応じて課金されることになります。

例

名前付き内部ステージから読み込む場合。

~~~
copy into aurora_table
from @aurora_stage;
~~~

外部ステージからデータを読み込む場合。指定するファイルは1つだけです。


~~~
copy into my_external_stage_table
from @aurora_ext_stage/tutorials/dataloading/students_ext.csv
~~~

外部からの直接コピーも可能です。

~~~
copy into aurora_table
from s3://mybucket/aurora_snow/data/files
credentials=(aws_key_id='$AWS_ACCESS_KEY_ID' aws_secret_key='$AWS_SECRET_ACCESS_KEY')
encryption=(master_key = 'eSxX009jhh76jkIuLPH5r4BD09wOaO8=')
file_format = (format_name = csv_format);
~~~

ファイルはパターンで指定することができます。

~~~
copy into aurora_pattern_table
from @aurora_stage
file_format = (type = 'TSV')
pattern='.*/.*/.*[.]csv[.]gz';
~~~

COPYコマンドを使ったCSVファイルの読み込みでよく使われるオプション

- COMPRESSION - ファイルに使用する圧縮アルゴリズムを指定します。
- RECORD_DELIMITERは、行の区切り文字を指定します。
- FIELD_DELIMITERは、ファイル内のフィールドを区切る文字です。
- SKIP_HEADER は，スキップするヘッダ行の数である。
- DATE_FORMATは日付の書式指定子である。
- TIME_FORMATは，時刻の書式指定子です。

その他にも多くのオプションがあります。[全リストはここをクリックしてください](https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html#format-type-options-formattypeoptions)。

### 5. Snowflakeテーブルの更新

ここまでのブログでは、Auroraからデータを抽出し、Snowflakeテーブルに単純に挿入する方法について説明しました。
次に、Snowflakeテーブルへの増分データのアップロードをどのように処理するかを深く見ていきましょう。

Snowflakeのアーキテクチャはユニークです。
現在/既存のどのビッグデータフレームワークに基づいているわけでもありません。
Snowflakeは行レベルの更新に何の制限もありません。
このため、Snowflakeテーブルへのデルタデータのアップロードは、Hiveのようなシステムと比較してはるかに簡単です。
進め方は、抽出したデータを中間テーブルにインクリメンタルにロードすることです。
次に、中間テーブルのデータに従って、最終テーブルのレコードを修正します。

中間テーブルにデータをロードした後、最終テーブルを修正するために使用される3つの一般的な方法を以下に示します。

1. 対象テーブルの行を更新する。次に、中間テーブルまたはランディングテーブルから、最終テーブルにない新しい行を挿入する。


~~~sql
UPDATE  aurora_target_table t SET t.value = s.value 
FROM  landing_delta_table in  WHERE t.id = in.id; 
 
INSERT INTO auroa_target_table (id, value)  
SELECT id, value FROM  landing_delta_table  WHERE NOT id IN (SELECT id FROM aurora_target_table);
~~~

2. ターゲットテーブルからランディングテーブルにあるすべてのレコードを削除する。その後、ランディングテーブルから最終テーブルにすべての行を挿入する。

~~~sql
DELETE .aurora_target_table f 
WHERE f.id IN (SELECT id from landing_table); 

INSERT aurora_target_table (id, value) 
SELECT id, value FROM  landing_table;
~~~


3. MERGE文 - 挿入と更新を1つのMERGE文に結合し、1つのSQL文で着陸テーブルの変更をターゲットテーブルに適用するために使用されます。

~~~sql
MERGE into aurora_target_table t1 using landing_delta_table t2 on t1.id = t2.id 
WHEN matched then update set value = t2.value 
WHEN not matched then INSERT (id, value) values (t2.id, t2.value);
~~~

## Limitations of Writing Custom ETL Code to Move Data from Aurora to Snowflake


AuroraからSnowflakeへのデータ移行は非常に簡単なアプローチに見えますが、限界があります。以下にそのいくつかを挙げます。

- パイプラインをハンドコーディングするために、貴重なエンジニアリングリソースを投資する必要があります。これにより、Snowflakeでデータを利用できるようになるまでの時間が長くなります。
- インフラストラクチャを常に監視し、維持するためにエンジニアリングリソースを投資する必要があります。コードブレーク、ソースでのスキーマ変更、デスティネーションが利用できない - これらの問題は、ETLプロジェクトを開始する際に想定していたよりも頻繁に発生することになります。
- AuroraからSnowflakeにリアルタイムでデータを流す必要がある場合、上記のアプローチは失敗します。これを実現するには、追加のステップを追加したり、cronジョブをセットアップしたりする必要があります。

そこで、これらの制限を克服し、Amazon AuroraからSnowflakeにシームレスにデータをロードするために、Hevoのようなサードパーティツールを使用することができます。

次世代のデジタル組織のためには、トランザクションシステムと分析システム間のシームレスなデータ移動が必要です。Hevo のような直感的で信頼性の高いプラットフォームを使用して Aurora から Snowflake にデータを移行することで、正確で一貫性のあるデータをリアルタイムに Snowflake で利用できるようになります。


## まとめ

この記事では、AWS AuroraとSnowflakeの基本的な理解を得ることができました。
さらに、カスタムETLスクリプトを使用してAuroraからSnowflakeにデータを移行する手順も理解できました。
さらに、この方法の制限を検討しました。
そこで、Amazon AuroraからSnowflakeにシームレスにデータを移行するための、より簡単な代替手段であるHevoを紹介します。