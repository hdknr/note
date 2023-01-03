# AWS Config

- [設定内容、相互の関連、時間の経過とともに設定と関係がどのように変化するかなど、AWS アカウントに関連付けられたリソースの詳細が提供されます。](https://docs.aws.amazon.com/ja_jp/config/index.html)
- [aws > configservice](https://docs.aws.amazon.com/cli/latest/reference/configservice/index.html)


|     | コンポーネント            | terraform                                                                                                                                      | 説明                               |
| --- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| #1  | Config 出力先 S3 バケット | [aws_s3_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket)                                         | #2 の出力先(履歴/スナップショット) |
| #2  | Config レコーダー         | [aws_config_configuration_recorder](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/config_configuration_recorder) | どのリソースを記録するか           |
| #3  | Config 配信チャネル       | [aws_config_delivery_channel](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/config_delivery_channel)             | #2の結果を#1に配信する             |
| #4  | Athena                    |                                                                                                                                                | #1 の中身をクエリ                  |
| #5  | Athena 出力先 S3 バケット |                                                                                                                                                | #4 の結果が格納                    |


## ポリシー

必要な権限:

- Read権限ポリシー: 各AWSリソースに対するRead の権限
- 配送ポリシー: 監査結果を配送するための S3バケットおよび SNS トピックに対する権限
- 信頼ポリシー: AWS Config サービス(config.amazonaws.com)のAssume


arn:aws:iam::aws:policy/service-role/AWS_ConfigRole:

- Default policy for AWS Config service role. Provides permissions required for AWS Config to track changes to your AWS resources.

arn:aws:iam::aws:policy/service-role/AWSConfigRole:

- Default policy for AWS Config service role.

arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy:

- Allows Config to call AWS services and collect resource configurations on your behalf.
- このポリシーはサービスにリンクされていて、そのサービス用のサービスにリンクされたロールでのみ使用されます。このポリシーのアタッチ、デタッチ、変更、または削除はできません。

## 資料

- [How To Get All Resources Deployed In AWS](https://cloudaffaire.com/how-to-get-all-resources-deployed-in-aws/)

    - Step 1: Create an S3 bucket to store your config recordings.
    - Step 2: Create an IAM role for AWS Config service.
    - Step 3: Enable AWS Config service.
    - Step 4: Create a configuration delivery channel for AWS Config.
    - Step 5: Start AWS config recordings.

- [無呼吸になって死ぬ前にAWS Configでやっておきたいこと(terraformでAWS Config設定編)](https://qiita.com/gamisan9999/items/7ae592531e2aaf4b56d5)
- [AWS Configの初期設定とマネージドルールを Terraform で設定して、非準拠項目を確認して対処してみる](https://qiita.com/tonishy/items/5f1f03057c1b2e56f13a)
- [AWS Config の料金がなぜこんなに高い？ Amazon Athena でどのリソースが Config の記録対象になっているか調べてみた](https://dev.classmethod.jp/articles/aws-config-amazon-athena/)
- [AWS Configに関するIAMロールについて](https://blog.serverworks.co.jp/tech/2016/05/13/awsconfig-iam-role/)
- [AWS 用の管理ポリシーAWS Config](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/security-iam-awsmanpol.html)
