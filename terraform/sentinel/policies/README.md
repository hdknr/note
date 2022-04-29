# ポリシー定義 (Sentinel Policy)

- Sentinel Language で定義される imports


| **imports**         | 内容                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| [tfplan](tfplan.md) | `terraform plan` で作られるファイル。プラン: インフラが設定(`tf`ファイル)で望まれる状態になるための変更を表現 |
| tfconfig            | `tf`ファイル                                                                                                  |
| tfstate             | 設定 == 現在のリソース 、の対応表                                                                             |
| tfrun               | Terraform Cloudでの `run` の関連付けデータ                                                                    |


## 資料

- https://www.terraform.io/cloud-docs/sentinel/import