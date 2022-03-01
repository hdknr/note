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

## 資料

- [Amazon S3 のポリシーとアクセス許可](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/access-policy-language-overview.html)
- [Amazon S3 での Identity and Access Management](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/s3-access-control.html)
- [Amazon S3 がリクエストを許可する仕組み](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/how-s3-evaluates-access-control.html)
- [Amazon S3 がバケットオペレーションのリクエストを承認する仕組み](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/access-control-auth-workflow-bucket-operation.html)
- [Amazon S3 がオブジェクトオペレーションのリクエストを許可する仕組み](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/access-control-auth-workflow-object-operation.html)




