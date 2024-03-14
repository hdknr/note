# [UNLOAD](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/r_UNLOAD.html)

Amazon S3 のサーバー側の暗号化 (SSE-S3) を使用して、Amazon S3 上の 1 つ、または複数のテキスト、JSON、または Apache Parquet ファイルにクエリの結果をアンロードします。
AWS Key Management Service キーを使用したサーバー側の暗号化 (SSE-KMS)、またはカスタマーマネージド型キーを使用したクライアント側の暗号化を指定することもできます。

デフォルトでは、アンロードされたファイルの形式はパイプ区切り (|) テキストです。

Amazon S3 のファイルは、サイズ、拡張子、ファイル数、MAXFILESIZE パラメータを設定することで管理できます。
S3 IP 範囲が許可リストに追加されていることを確認します。必要な S3 IP 範囲の詳細については、「ネットワークの隔離」を参照してください。

分析用の効率的なオープン列型ストレージ形式である Apache Parquet では、Amazon Redshift クエリの結果を Amazon S3 データレイクにアンロードできます。
Parquet 形式は、テキスト形式と比較して、アンロードが最大 2 倍速く、さらにストレージ使用量が Amazon S3 で最大 6 倍少なくすみます。
これにより、Amazon S3 で行ったデータ変換とエンリッチメントをオープン形式で Amazon S3 データレイクに保存できます。
その後、Redshift Spectrum や Amazon Athena、Amazon EMR、SageMaker などの他の AWS のサービスを使用してデータを分析できます。


## `FORMAT JSON`

~~~sql
UNLOAD ('
  SELECT
    code,
    name
  FROM
    prefecture
')
TO
  's3://foo-bar/redshift/unload/prefecture/'
FORMAT JSON
IAM_ROLE 'arn:aws:iam::123456789012:role/cm-ootaka-daisuke-redshift-role'
;
~~~

- [ndjson](http://ndjson.org/) 形式でアンロードされる

## 関連

- [[Fivetran] S3に置いてる色々な形式のファイルをDWHに同期してみた](https://dev.classmethod.jp/articles/fivetran-file-s3-avro-toka-csv-toka/)
- [RedshiftでJSONファイル形式のUNLOADを試してみた](https://dev.classmethod.jp/articles/redshift-unloading-data-to-json-files/)

