# S3 アクセス制御


## ポリシー


要素:

| **要素**     | **名称**  | **内容**                                | **リンク**                                                                                 |
| ------------ | --------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| リソース     | Resource  | 対象となるファイルなど(ARNで識別される) | [リソース](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/s3-arn-format.html) |
| アクション   | Action    | リソースに行う動作(参照、削除....)      |
| 効力         | Effect    | 許可(`Allow`) もしくは 拒否(`Deny`)     |
| プリンシパル | Principal | アカウントまたはユーザー                |
| 条件         | Condition | ポリシーが有効になる条件                |

## オペレーション

- バケットオペレーション
- オブジェクトオペレーション

バケットオペレーション:

- ![](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/images/AccessControlAuthorizationFlowBucketResource.png)


オブジェクトオペレーション:

- ![](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/images/AccessControlAuthorizationFlowObjectResource.png)


## [ポリシーチェック項目](https://aws.amazon.com/jp/premiumsupport/knowledge-center/s3-troubleshoot-403/)

- バケットとオブジェクトの所有権
- バケットポリシーまたは IAM ユーザーポリシー
- IAM アクセス許可の境界
- Amazon S3 ブロックパブリックアクセス設定
- Amazon S3 にアクセスするための認証情報
- 一時的なセキュリティ認証情報
- Amazon [VPC エンドポイントポリシー](https://docs.aws.amazon.com/ja_jp/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies)
- Amazon S3 アクセスポイントポリシー
- オブジェクトまたは特殊文字を含むオブジェクトが見つかりません
- AWS KMS 暗号化
- バケットで有効化されているリクエスタ支払い
- AWS Organizations のサービスコントロールポリシー


## 資料

- [Amazon S3 のポリシーとアクセス許可](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/access-policy-language-overview.html)
- [Amazon S3 での Identity and Access Management](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/s3-access-control.html)
- [Amazon S3 がリクエストを許可する仕組み](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/how-s3-evaluates-access-control.html)
- [Amazon S3 がバケットオペレーションのリクエストを承認する仕組み](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/access-control-auth-workflow-bucket-operation.html)
- [Amazon S3 がオブジェクトオペレーションのリクエストを許可する仕組み](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/access-control-auth-workflow-object-operation.html)
- [Amazon S3 から 403: Access Denied エラーをトラブルシューティングする方法とは?](https://aws.amazon.com/jp/premiumsupport/knowledge-center/s3-troubleshoot-403/)
- [Amazon Simple Storage Service (S3) > ユーザーガイド > Troubleshooting](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/troubleshooting.html)

