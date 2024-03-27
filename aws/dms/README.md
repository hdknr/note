# DMS

- [エンドポイント:MySQL](endpoint_mysql.md)
- [エンドポイント:S3](endpoint_s3.md)

## 資料

- [AWS Database Migration Service](https://aws.amazon.com/jp/dms/)
- [DMS で AWS RDS へ継続的に移行してみた](https://dev.classmethod.jp/articles/rdb-dms-rds/)
- [DMS Endpoint Connection Test Failed with Secret Manager](https://repost.aws/questions/QUSjXHLPIgSyuTSfETynK0Cg/dms-endpoint-connection-test-failed-with-secret-manager)
- [Manage your AWS DMS endpoint credentials with AWS Secrets Manager](https://aws.amazon.com/jp/blogs/database/manage-your-aws-dms-endpoint-credentials-with-aws-secrets-manager/)
- [How to connect to AWS Secrets Manager service within a Virtual Private Cloud](https://aws.amazon.com/jp/blogs/security/how-to-connect-to-aws-secrets-manager-service-within-a-virtual-private-cloud/)
- [AWS Database Migration Service (AWS DMS) の CDC レプリケーションを使ってみた](https://www.skyarch.net/blog/aws-database-migration-service-aws-dms-%E3%81%AE-cdc-%E3%83%AC%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F/)

サーバーレス:

- [AWS DMS Serverless を使ってみた](https://www.skyarch.net/blog/aws-dms-serverless-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F/)
- [AWS DMS サーバーレスの制約](https://docs.aws.amazon.com/ja_jp/dms/latest/userguide/CHAP_Serverless.Limitations.html)

### `The parameter ReplicationSubnetGroupDescription must not contain non-printable control characters.`

- サブネットグループを先に作ること

### KMS

- [AWS KMS リソースにアクセスするための IAM ポリシーの作成](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.KMSCreatePolicy.html)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["kms:Decrypt"],
      "Resource": "arn:aws:kms:<region>:<123456789012>:key/<key-ID>"
    }
  ]
}
```

## VPC エンｄポイント

VPC エンドポイントには、インターフェイスエンドポイント、ゲートウェイロードバランサーのエンドポイント、およびゲートウェイエンドポイントの 3 種類があります。

インターフェイスエンドポイントとゲートウェイロードバランサーのエンドポイントは AWS PrivateLink を使用し、サービスを送信先とするトラフィックのためのエントリポイントとして Elastic Network Interface (ENI) を使用します。

インターフェイスエンドポイントは通常、サービスに関連付けられたパブリックまたはプライベート DNS 名を使用してアクセスされ、
ゲートウェイエンドポイントとゲートウェイロードバランサーのエンドポイントは、サービスを送信先とするトラフィックのためのルートテーブル内のルートのターゲットとして機能します。

- [VPC エンドポイントの設定 AWSDMS ソースエンドポイントとターゲットエンドポイント](https://docs.aws.amazon.com/ja_jp/dms/latest/userguide/CHAP_VPC_Endpoints.html)
