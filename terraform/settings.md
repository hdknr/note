# 設定

- https://www.terraform.io/language/settings


## [バックエンド設定(Backend Configuration)](https://www.terraform.io/language/settings/backends/configuration)


### ファイル指定

~~~ini
address = "demo.consul.io"
path    = "example_app/terraform_state"
scheme  = "https"
~~~

### コマンドライン指定

~~~zsh
terraform init \
    -backend-config="address=demo.consul.io" \
    -backend-config="path=example_app/terraform_state" \
    -backend-config="scheme=https"
~~~


## 資料

- [Terraformのbackendを使いこなしたい](https://repl.info/archives/1435/)
- [バックエンドの設定](https://runebook.dev/ja/docs/terraform/backends/config)

