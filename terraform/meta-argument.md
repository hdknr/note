# Resources: Meta-Arguments  (リソースメタ引数)

- どんなリソースタイプにも使える
- そのリソースの動作を変更


## `for_each`

- [The for_each Meta-Argument](https://www.terraform.io/language/meta-arguments/for_each)

- resource block内でリソースのリストを指定する事が可能
- 同じ設定だけど名前だけ違うような場合等に使用すると、リストに記載した名前でリソースを作成する事が出来きる(マップで作成される)

### AWS シークレットマネージャで環境変数を登録する
~~~tf
locals {
    env = {
        DB_NAME = null
        DB_HOST = null
        DB_USER = null
        DB_PASSWORD = null
    }
}
~~~tf
resource "aws_secretsmanager_secret" "secrets" {
  for_each                = local.env 
  name                    = "${var.app}-${var.environment}-${each.key}"
  recovery_window_in_days = var.secret_retention_days
}
~~~

以下のようにリソースが `for_each`で指定したマップ のキーの分、作成されている:

~~~
aws_secretsmanager_secret.secrets["DB_NAME"] = res1
aws_secretsmanager_secret.secrets["DB_HOST"] = res1
...
~~~

これを key=環境変数名 , value=ARNのマップに変換

~~~tf
locals {
  secret_arns_map = zipmap(keys(aws_secretsmanager_secret.secrets), values(aws_secretsmanager_secret.secrets)[*].arn)
}
~~~ 


## 資料

- [Terraformのかゆい所に手をのばす 〜 meta-arguments 〜](https://qiita.com/donko_/items/0e276b45ddea5e39abd7)
- [Azureリソース作成しながらTerraformのメタ引数(Count,for each)を試してみた](https://www.tama-negi.com/2021/12/31/terraform-meta-argument-01/#)
