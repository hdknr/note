# tfplan/v2

## 構造

~~~
tfplan/v2
├── terraform_version (string)
├── variables
│   └── (indexed by name)
│       ├── name (string)
│       └── value (value)
├── planned_values
│   ├── outputs (tfstate/v2 outputs representation)
│   └── resources (tfstate/v2 resources representation)
├── resource_changes
│   └── (indexed by address[:deposed])
│       ├── address (string)
│       ├── module_address (string)
│       ├── mode (string)
│       ├── type (string)
│       ├── name (string)
│       ├── index (float (number) or string)
│       ├── provider_name (string)
│       ├── deposed (string)
│       └── change (change representation)
├── output_changes
│   └── (indexed by name)
│       ├── name (string)
│       └── change (change representation)
└── raw (map)

~~~


| コレクション     | 内容                                                              |
| ---------------- | ----------------------------------------------------------------- |
| variables        | プランでセットされている変数。ルートモジュールの変数のみ。        |
| planned_values   | プランされた値/適用後にリソースがどうなるか、 の表現              |
| resource_changes | このプランでのリソース変更とデータソース                          |
| output_changes   | このプランでのoutputに対する変更。ルートモジュールのoutoputのみ。 |
| raw              | Terraform Cloudに保存された生データ                               |

## 例:

[showコマンド](../../cli/show.md) で JSON にする:

~~~bash
% terraform -chdir=prod show -json all.plan  | jq "." > ~/Downloads/plan.json
~~~

EC2のインスタンスのAMIの変更の確認:

~~~bash
% cat ~/Downloads/plan.json |  jq -r '.resource_changes[] | select(.type == "aws_instance")|[.address,.change.before.ami,.change.after.ami]|@tsv'
~~~

~~~
module.ec2.aws_instance.server1 ami-0fee947c1a4ce5acd   ami-0ed27e49709b07bca
module.ec2.aws_instance.server2 ami-08805955956c745e6   ami-0618c025f83180f1a
module.ec2.aws_instance.server3 ami-0eee4c08be2aaefc2   ami-0eee4c08be2aaefc2
module.ec2.aws_instance.server4 ami-0f1a341b74c7b99d4   ami-00204b4ba135956a0
~~~

## 資料

- https://www.terraform.io/cloud-docs/sentinel/import/tfplan-v2