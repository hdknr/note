# CodeBuild


## Step Function

- [CodeBuildを呼ぶ時のポリシーhttps://docs.aws.amazon.com/step-functions/latest/dg/codebuild-iam.html)

## `Cannot exceed quota for PoliciesPerRole`

クオータを引き上げ:

- バージニアリージョンの [Service Quotas](https://us-east-1.console.aws.amazon.com/servicequotas/home/)
- IAM:  https://us-east-1.console.aws.amazon.com/servicequotas/home/services/iam/quotas
- Managed Policies per role: https://us-east-1.console.aws.amazon.com/servicequotas/home/services/iam/quotas/L-0DA4ABF3


##  `CLIENT_ERROR: Get i/o timeout`

- [[AWS] CodeBuildでエラー CLIENT_ERROR: Get i/o timeout for primary sourceが出る](https://akamist.com/blog/archives/4594)
- [カスタムイメージを使ってCodebuildでbuildするまで。](https://qiita.com/fake-deli-ca/items/a5ed9b0ea34411273765)

### VPC で動かす場合、 NATゲートウェイが必要

- https://github.com/aws-ia/terraform-aws-codebuild
- [CodeBuildコンテナをNATなしプロキシ環境下で実行した](https://dev.classmethod.jp/articles/codebuild-nat-proxy-vpc/)
- [Setting up a NAT gateway on AWS using Terraform](https://dev.betterdoc.org/infrastructure/2020/02/04/setting-up-a-nat-gateway-on-aws-using-terraform.html)
- [CREATING VPC WITH NAT GATEWAY USING TERRAFORM CODE](https://www.linkedin.com/pulse/creating-vpc-nat-gateway-using-terraform-code-akanksha-gupta)
- [TerraformでVPCを作成](https://zenn.dev/nicopin/books/58c922f51ea349/viewer/5a2839)
- [TerraformでプライベートサブネットとNATゲートウェイを管理する](https://int128.hatenablog.com/entry/2018/06/28/180504)



## 資料

- [CodeBuildプロジェクトをコード化する時のServiceRoleのハマりポイント](https://www.soudegesu.com/post/aws/codebuild_error_with_exceed_policy_num/)