# Redshiftをパイプする

- [Use Lambda Functions to Move Data From Redshift](https://www.fivetran.com/blog/data-migration-from-redshift)


Fivetranでは、様々な技術スタックとユースケースに対応するために、複数の異なる[データウェアハウス](https://fivetran.com/docs/destinations)にデータをパイプで接続しています。
異なるデータウェアハウスには異なる特性やトレードオフがありますが、[性能はほぼ同じです](https://www.fivetran.com/blog/warehouse-benchmark)。

当社のお客様で、RedshiftからSnowflakeやBigQueryに適度な量のデータを移動する必要があることがあります。
RedshiftはAmazon Web Services（AWS）のクラウドプラットフォームの一部であるため、Redshiftを使っている人は誰でもAWS Lambdaにアクセスすることも可能です。


AWSのいくつかの設定とPythonをつかって、[Fivetran Lambdaコネクタ](https://fivetran.com/docs/functions/aws-lambda)を使用して、
Redshiftクラスタから選択したデータウェアハウスにデータをストリームする方法を説明します。
これは、特に小規模でアドホックな移行を意図していることに注意してください。
スキーマの完全なレプリケーションのためには、より従来のアプローチを検討する必要があります。
このチュートリアルは、読者がPythonとSQLの実用的な知識を持っていることを想定しています。

ここでのアイデアは、小サイズの（つまりギガバイト以下のスケールの）テーブルから移行先のデータウェアハウスにデータを段階的に追加する軽量な処理を実証することです。
AWS Lambdaには6MBのペイロード制限があるため、この方法で非常に大きなテーブルを移行するのは現実的ではありません。

Designate Your Source Redshift Table:


AWS Lambdaに適用される6MBのペイロード制限を考えると、
適度な時間で移行できる比較的小さなテーブルが欲しいところです。
テーブルの大きさと、それをロードするのにかかる6MB以下の増分を把握します。
SQLクエリツール（私はRedshiftへのアクセスに[SQL Workbench/J](https://www.sql-workbench.eu/)を使用しています）を使用して、
以下のSQLを実行します（''はシングルクォートで囲まれたテーブル名です）。

~~~sql
SELECT "table", size, tbl_rows 
FROM SVV_TABLE_INFO 
WHERE "table" = '[table_name]'
~~~

このクエリーを実行する権限がない場合は、所属する組織の指定されたスーパーユーザーに問い合わせてください。
これにより、テーブルの行数とそのサイズ（メガバイト単位）がわかります。
後で、この情報を使って、スクリプト内のSQLクエリのLIMIT句を適宜調整することになります。

1. Database name
2. Host
3. Port
4. User
5. Password
6. Table name
7. Primary key(s) if you’re migrating to Snowflake; BigQuery doesn’t care about primary keys
8. Cursor column(s) – identify a column or set of columns with unique values that you can order sequentially and use to bookmark your progress
9. LIMIT increment


これらのパラメータは、後でスクリプトに保持します。
別のファイルに保存するか、より現実的な方法として、Fivetranでは「Secret」パラメータとして、
AWS Lambdaではテストイベントとして入力することができます。
後者の場合、全く同じLambda関数をそのまま（Secretが違うだけ）複数のコネクターで再利用できるのがメリットです。


Write a Python Script:

- https://github.com/fivetran/functions/blob/master/redshift/aws_lambda/lambda_function.py

~~~py
from datetime import datetime, date
from time import struct_time, mktime
import decimal
import pg8000


# Connect via pg8000
def get_connection(database, host, port, user, password):
    conn = None
    try:
        conn = pg8000.connect(database=database, host=host, port=port, user=user, password=password, ssl=True)
    except Exception as err:
        print(err)
    return conn


# Handle Python data types such as datetime and decimal
def encode_json(data):
    if isinstance(data, datetime):
        return str(data)
    if isinstance(data, date):
        return str(data)
    if isinstance(data, decimal.Decimal):
        return float(data)
    if isinstance(data, struct_time):
        return datetime.fromtimestamp(mktime(data))
    return data


# Handler function
def lambda_handler(request, context):
    # 1. AWS/データベースのクレデンシャル
    # These and other parameters should be wrapped up in 'request,' which is relayed from the connector's 'secrets'
    dbname = request['secrets']['dbname']
    host = request['secrets']['host']
    port = int(request['secrets']['port'])
    user = request['secrets']['user']
    password = request['secrets']['password']

    # 2. 状態をセット
    try:
        cursor_value = request['state']['cursor']
    except KeyError:
        cursor_value = '1970-01-01T00:00:00'

    # 3. Redshift接続
    con = get_connection(dbname, host, port, user, password)
    cur = con.cursor()

    # Make sure you should know these details about the table you are migrating beforehand
    # Set the 'limit' according to your estimates of the table's size and row count
    # Again, these can also be stored in 'request'
    table = request['secrets']['table']
    primary_key = request['secrets']['primary_key']
    cursor = request['secrets']['cursor']
    limit = request['secrets']['limit']

    # 4. Query redshift; check for the existence of your save state
    cur.execute("""
        SELECT * FROM {table} 
        WHERE {cursor} > '{cursor_value}' 
        ORDER BY {cursor} LIMIT {limit}""".format(
            cursor_value=cursor_value, cursor=cursor, limit=limit, table=table))

    # Get column names
    columns = [item[0].decode() for item in cur.description]

    # Get data
    output_data = cur.fetchall()

    # Handle exception; stop once you reach the end of the table. Avoids 'out of index' error on line 113
    if len(output_data) == 0:
        return {}

    # 5. Generate a JSON response
    response = dict()
    response['insert'] = {table: []}

    for row in output_data:
        serialized_row = [encode_json(item) for item in row]
        row_data = dict(zip(columns, serialized_row))
        response['insert'][table].append(row_data)

    response['state'] = request['state'] if len(output_data) == 0 else {'cursor': response['insert'][table][-1][cursor]}
    response['schema'] = {table: {'primary_key': [primary_key]}}
    response['hasMore'] = False if len(output_data) < limit else True

    print(response)

    return response
~~~

このスクリプトは Python 3.7 を対象としていますが、Python 3.6 や Python 2.7 との後方互換性もあります。
また、redshiftにアクセスするためにpg8000が必要です。
pg8000の利点は、より一般的なpsycopg2よりもコンパイルされていないため、AWS Lambdaの依存関係をより簡単にインストールすることができます。

通常通りpip installで依存関係をローカルにインストールします。


実際のマイグレーションを実行するハンドラは、このスクリプトではlambda_handlerと呼ばれます。
あなたのスクリプトは以下のアクションを実行します（スクリプト内でもこのように番号が振られています）。


1. Import AWS and database credentials
2. Set your state
3. Connect to Redshift
4. Query Redshift. You will ORDER BY your cursor and apply the appropriate LIMIT increment. The pg8000 package we are using is a wrapper for SQL, so there will be SQL embedded in your Python code.
5. Generate the JSON response and save your state. The response is a JSON object in the format described here. You won’t need to return a 200 status, unlike with Google Cloud Functions.

ローカルで何度かスクリプトを実行して、何が起こるか見てください。
アップロードされたスクリプトは単なる関数の集まりなので、メインプログラムとして直接実行するには、一時的にスクリプトの末尾に lambda_handler() を追加する必要があることに注意してください。

Set Up an AWS Lambda Function

Make sure you have access to the following in AWS:

1. IAM policies with access to Redshift and Lambda
2. An IAM role with the above policies attached



そうでない場合は、アクセス権を取得します。Lambda関数も作成する必要があります。詳細な手順はこちらのドキュメントに記載されています。

Lambdaを作成したら、RedshiftでIAMロール、Lambdaのアクセスは "Execution role "を選択します。基本設定」では、タイムアウトを最大で「15分」に設定する必要があります。実際に実行した時間分しか課金されないので、制限時間を低く設定する必要はありません。

実行時間を Python 3.7 (または 3.6 か 2.7) に設定し、ハンドラの形式を .

Pythonスクリプトがあるディレクトリに戻ります。コマンドラインを入力し、次のコマンドを使用して、Pythonの依存関係をスクリプトと同じディレクトリに配置します。


~~~
pip install pg8000 --target .
~~~

最後にピリオドを入れることを確認してください-タイプミスではありません。この例では、pg8000をインストールするだけです。boto3パッケージはAWS LambdaのPythonランタイムにプリインストールされています。

ここで、スクリプトとpg8000フォルダ（"dist-info "で終わるフォルダは必要ありません）をzipで圧縮します。

Macでは、ハイライトして右クリックし、「圧縮」アクションを使用して圧縮しました。Windowsマシンでは、右クリックし、「送信」「圧縮（zip）フォルダ」を使用しても同じように圧縮することができます。また、コマンドラインを使用することもできます。


これらのアイテムを含むzipアーカイブを、ラムダを設定するページのCode entry typeのドロップダウンメニューからアップロードしてください。

Set Up Fivetran Lambda Function Connector:

他のコネクタと同じようにAWS Lambdaコネクタを作成します。使用するロールからARNを入力し、それぞれのテキストボックスにlambda関数の名前を入力します。External ID」はすぐに必要になるのでメモしておきます。


使用しているIAMロールを再確認する必要があります。信頼関係]に移動し、[信頼関係の編集]をクリックします。Statementキーに以下のJSONを追加する必要があります。

~~~json
{
  "Effect": "Allow",
  "Principal": { "Service": "lambda.amazonaws.com" },
  "Action": "sts:AssumeRole"
}
~~~

さらに、Statement.Condition.StringEquals.sts:ExternalIdの値が、あなたの外部IDであることを二重引用符で囲んで確認すること。私のExternal Idは "associated_legged "でしたので、Policy Documentはこのようになっています。


~~~json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::834469178297:root" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": { "sts:ExternalId": "accompanying_legged" }
      }
    },
    {
      "Effect": "Allow",
      "Principal": { "Service": "lambda.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
~~~


これで準備は完了です。必要なだけ同期を実行し、不要になったら停止させることができます。

先に述べたように、完全なPythonのソースコードはここで見ることができます。私は、すべての機能を徹底的に文書化するために苦心し、あなたがそれを見つけることを望みます。もし、現在Fivetranを使っていないが、興味があれば、ここでデモをリクエストしてください。



