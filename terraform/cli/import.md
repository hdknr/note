# `import`



## DNSレコードのインポート

- [aws_route53_record](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route53_record#import)

データ形式:

    "{zone identifier}_{record name}_{record type}"

例:

    Z3CW3N3C2PAVK6_yoursite.com_TXT

~~~bash
terraform 'module.ses.aws_route53_record.spf_carrier["yoursite.com"]' Z3CW3N3C2PAVK6_yoursite.com_TXT
~~~


## 資料

- [Terraform import のススメ 〜開発効率化編〜](https://tech.layerx.co.jp/entry/improve-iac-development-with-terraform-import)

- [TerraformでAmazon Route 53をインポートする](https://qiita.com/sin9270/items/22b9aa8e7b8aeb631fc3)