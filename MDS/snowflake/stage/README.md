# STAGE

- [CREATE STAGE](https://docs.snowflake.com/ja/sql-reference/sql/create-stage.html)
- [データレイクの過去と現在、そして未来](https://news.mynavi.jp/techplus/kikaku/snowflake-workload-5/)
- [ステップ3。データファイルをステージングする](https://docs.snowflake.com/ja/user-guide/getting-started-tutorial-stage-data-files.html)


## Snowflakeステージ

- テーブルからデータをロードおよびアンロードするために使用するクラウドストレージ内の場所

内部ステージ:

- Snowflake内にデータファイルを内部的に保存
- Snowflakeの各ユーザーとテーブルは、データファイルをステージングするためにデフォルトで内部ステージを取得します。

外部ステージ:

- Amazon S3、Google Cloud Storage、またはMicrosoft Azureで外部データファイルを保存


## S3

- [Amazon S3へのセキュアアクセスの構成](https://docs.snowflake.com/ja/user-guide/data-load-s3-config.html)
- [オプション1：Amazon S3にアクセスするためのSnowflakeストレージ統合の構成](https://docs.snowflake.com/ja/user-guide/data-load-s3-config-storage-integration.html)
- [S3ステージの作成](https://docs.snowflake.com/ja/user-guide/data-load-s3-create-stage.html)


### [クラウドストレージへの安全なアクセスの構成](https://docs.snowflake.com/ja/user-guide/data-load-s3-config-storage-integration.html#configuring-secure-access-to-cloud-storage)

- ステップ1：S3バケットのアクセス許可を構成する
- ステップ2：IAM AWS ロールを作成する
- ステップ3：Snowflakeでクラウドストレージ統合を作成する
- ステップ4：Snowflakeアカウントの AWS IAM ユーザーを取得する
- ステップ5：バケットオブジェクトにアクセスするために IAM ユーザー権限を付与する
- ステップ6：外部ステージを作成する
