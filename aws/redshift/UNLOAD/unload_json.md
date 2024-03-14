# Export JSON data to Amazon S3 using Amazon Redshift UNLOAD

https://aws.amazon.com/jp/blogs/big-data/export-json-data-to-amazon-s3-using-amazon-redshift-unload/


Amazon Redshiftは、高速でスケーラブル、かつ安全で完全に管理されたクラウドデータウェアハウスであり、
標準SQLを使用してすべてのデータを分析することを簡単かつコスト効率的に実現します。
Amazon Redshiftは、他のクラウドデータウェアハウスと比較して、最大3倍の価格パフォーマンスを提供します。
何万ものお客様がAmazon Redshiftを使用して、1日あたりエクサバイトのデータを処理し、
高性能なビジネスインテリジェンス（BI）レポート、ダッシュボードアプリケーション、データ探索、
リアルタイム分析などの分析ワークロードを強力にサポートしています。

IoTデバイス、ソーシャルメディア、クラウドアプリケーションから生成されるデータの量が増え続ける中、
企業はこのデータを簡単かつコスト効率よく分析し、洞察を得るまでの時間を短縮することを求めています。
このようなデータの大部分は半構造化形式で提供されており、アクセス可能にしたり、構造化データと統合して分析したりするには、抽出、変換、ロード（ETL）プロセスを追加する必要があります。
Amazon Redshift は、データウェアハウス、データレイク、運用データベースを横断してデータを照会し、
他では得られないより迅速で深い洞察を得ることができる、モダンなデータアーキテクチャを後押しします。
モダンデータアーキテクチャでは、Amazon Simple Storage Service（Amazon S3）データレイクに半構造化形式でデータを保存し、
Amazon Redshift上の構造化データと統合することが可能です。
これにより、このデータをサイロに閉じ込めるのではなく、他の分析アプリケーションや機械学習アプリケーションで利用できるようにすることができます。

この記事では、Amazon RedshiftのUNLOAD機能と、Amazon RedshiftクラスタからAmazon S3データレイク上のJSONファイルへデータをエクスポートする方法について説明します。

## JSON support features in Amazon Redshift

Amazon RedshiftのCOPY、UNLOAD、[Amazon Redshift Spectrum](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/c-getting-started-using-spectrum.html)などの機能により、データウェアハウスとデータレイク間でデータの移動とクエリを実行することができます。

UNLOADコマンドを使用すると、テキスト、JSON、またはApache Parquetファイル形式でAmazon S3にクエリ結果セットをエクスポートすることができます。
UNLOADコマンドは、データウェアハウスから大きな結果セットを取得する必要がある場合にも推奨されます。
UNLOADはAmazon Redshiftの計算ノードからAmazon S3へ並列にデータを処理・エクスポートするため、ネットワークのオーバーヘッドを削減し、大量の行の読み込みにかかる時間を短縮することができます。
UNLOADでJSONオプションを使用する場合、Amazon Redshiftは、クエリ結果の完全なレコードを表すJSONオブジェクトを含む各行のJSONファイルへのアンロードを行います。
JSONファイルでは、Amazon Redshiftのタイプは、最も近いJSON表現としてアンロードされます。
例えば、ブール値はtrueまたはfalseとしてアンロードされ、NULL値はnullとしてアンロードされ、タイムスタンプ値は文字列としてアンロードされます。
デフォルトのJSON表現が特定のユースケースに合わない場合は、UNLOAD文のSELECTクエリで希望の型にキャストすることで変更することができます。

さらに、有効なJSONオブジェクトを作成するために、クエリ結果の各カラムの名前は一意でなければなりません。
クエリ結果のカラム名が一意でない場合、JSON UNLOAD処理は失敗する。
これを避けるには、適切なカラム・エイリアスを使用して、クエリ結果の各カラムがアンロードされる間も一意であるようにすることをお勧めします。
この投稿の後半で、この動作を説明します。

Amazon Redshift [SUPERデータ型](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/r_SUPER_type.html)を使用すると、
ローカルのAmazon RedshiftテーブルにJSON形式でデータを保存することができます。
この方法では、ネットワークオーバーヘッドなしでデータを処理し、Amazon Redshiftスキーマプロパティを使用して、半構造化データを最適にローカルに保存し、クエリすることができます。
低レイテンシーを実現するだけでなく、クエリに強い一貫性、予測可能なクエリパフォーマンス、複雑なクエリサポート、進化するスキーマやスキーマレスデータでの使いやすさが求められる場合、SUPERデータ型を使用することが可能です。
Amazon Redshiftは、クエリ結果がSUPERカラムを含む場合、ネストされたJSONの書き込みをサポートします。

常に進化するスキーマを持つデータの更新と維持は困難であり、分析パイプラインに余分なETLステップを追加することになります。
JSONファイル形式は、スキーマ定義のサポートを提供し、軽量で、さまざまなサービス、ツール、テクノロジーによってデータ転送メカニズムとして広く使用されています。

Amazon OpenSearch Serviceは、リアルタイムアプリケーション監視、ログ分析、ウェブサイト検索などの幅広いユースケースに使用される、分散型のオープンソース検索・分析スイートです。
データ取り込みのためのファイル形式として、JSONをサポートしています。
Amazon RedshiftからAmazon S3データレイクにJSON形式のデータをネイティブにアンロードできるため、
そのデータをさらに分析するためにAmazon OpenSearch Serviceに取り込む必要がある場合、複雑さや追加のデータ処理ステップを減らすことができます。

これは、Amazon S3上のデータレイク、Amazon Redshift上のデータウェアハウス、Amazon OpenSearch Serviceやその他のJSON指向のダウンストリーム分析ソリューションによる検索とログ分析で、シームレスなデータ移動が統合データプラットフォームの構築を支援する一つの例です。
レイクハウスアプローチの詳細については、Build a Lake House Architecture on AWSを参照してください。

## Examples of Amazon Redshift JSON UNLOAD

この記事では、次のようなさまざまなシナリオを紹介します。

### Example 1: Export customer data

この例では、TPCDSデータセットのcustomerテーブルとデータを使用しました。
データベーススキーマと顧客テーブルを作成し、そこにデータをコピーしました。次のコードをご覧ください。


~~~sql
-- Created a new database
create schema json_unload_demo; 

-- created and populated customer table in the new schema

create table json_unload_demo.customer
(
  c_customer_sk int4 not null ,                 
  c_customer_id char(16) not null ,             
  c_current_cdemo_sk int4 ,   
  c_current_hdemo_sk int4 ,   
  c_current_addr_sk int4 ,    
  c_first_shipto_date_sk int4 ,                 
  c_first_sales_date_sk int4 ,
  c_salutation char(10) ,     
  c_first_name char(20) ,     
  c_last_name char(30) ,      
  c_preferred_cust_flag char(1) ,               
  c_birth_day int4 ,          
  c_birth_month int4 ,        
  c_birth_year int4 ,         
  c_birth_country varchar(20) ,                 
  c_login char(13) ,          
  c_email_address char(50) ,  
  c_last_review_date_sk int4 ,
  primary key (c_customer_sk)
) distkey(c_customer_sk);

copy json_unload_demo.customer from 's3://redshift-downloads/TPC-DS/2.13/3TB/customer/' 
iam_role '<<AWS IAM role attached to your amazon redshift cluster>>' 
gzip delimiter '|' EMPTYASNULL;
~~~

Amazon S3ロケーションからコピーしてアンロードするために、Amazon RedshiftクラスタのデフォルトのAWS Identity and Access Management（IAM）ロールを作成することができます。詳細については、Amazon RedshiftのデフォルトIAMロールを使用して、他のAWSサービスへのアクセスを簡素化するを参照してください。

この例では、誕生年1992年のすべての顧客データをJSON形式で、パーティションなしでAmazon S3にアンロードしています。UNLOAD文に以下のような変更を加えています。

- c_preferred_cust_flagカラムを文字列からブール値に変換します。
- c_first_name, c_last_name, c_email_address 列から btrim 関数を使用して先頭および末尾のスペースを除去します。
- Amazon S3 でエクスポートされるファイルの最大サイズを 64MB に設定しました

See the following code:

~~~sql
unload ('SELECT c_customer_sk,
    c_customer_id ,
    c_current_cdemo_sk ,
    c_current_hdemo_sk ,
    c_current_addr_sk ,
    c_first_shipto_date_sk ,
    c_first_sales_date_sk ,
    c_salutation ,
    btrim(c_first_name),
    btrim(c_last_name),
    c_birth_day ,
    c_birth_month ,
    c_birth_year ,
    c_birth_country ,
    c_last_review_date_sk,
    DECODE(c_preferred_cust_flag, ''Y'', TRUE, ''N'', FALSE)::boolean as c_preferred_cust_flag_bool,
    c_login, 
    btrim(c_email_address) 
    from customer where c_birth_year = 1992;')
to 's3://<<Your Amazon S3 Bucket>>/non-partitioned/non-super/customer/' 
FORMAT JSON 
partition by (c_birth_month)  include
iam_role '<<AWS IAM role attached to your amazon redshift cluster>>'
MAXFILESIZE 64 MB;
~~~


UNLOADコマンドを実行すると、btrim関数を使用した列がすべてbtrimとしてエクスポートされようとしたため、エラーが発生しました（同じ関数が一緒に選択されている複数の列に適用された場合のAmazon Redshiftのデフォルト動作です）。このエラーを回避するには、btrim関数が使用された各列に一意の列エイリアスを使用する必要があります。  

c_first_name、c_last_name、c_email_address列をbtrim関数とc_preferred_cust_flagを適用して選択すると、文字からBooleanに変換することができます。

Amazon Redshift Query Editor v2にて、以下のクエリを実行しました。


~~~sql
SELECT btrim(c_first_name) ,
    btrim(c_last_name),
    btrim(c_email_address) , 
    DECODE(c_preferred_cust_flag, 'Y', TRUE, 'N', FALSE)::boolean c_preferred_cust_flag_bool  
    from customer where c_birth_year = 1992 limit 10; 
~~~

btrim関数を使用した3つの列は、出力結果にそれぞれの列名ではなくbtrimとして設定されています。

