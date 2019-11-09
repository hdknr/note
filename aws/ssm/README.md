# SSM: [AWS System Manager](https://docs.aws.amazon.com/systems-manager/index.html)

- [ユーザーガイド](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/what-is-systems-manager.html)
- [以前はSimple System Managerとか呼ばれていた](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/what-is-systems-manager.html#service-naming-history)

`SSM` はまだ使われている:

| **用途**              | **例** |
| ---------------------| ------ |
| Systems Manager Agent| SSM エージェント
| Systems Manager パラメータ| SSM パラメータ
| Systems Manager サービスエンドポイント| `ssm.us-east-2.amazonaws.com`
| AWS CloudFormation リソースタイプ| `AWS::SSM::Document`
| AWS Config ルール識別子| `EC2_INSTANCE_MANAGED_BY_SSM`
| AWS CLI コマンド| `aws ssm describe-patch-baselines`
| AWS Identity and Access Management (IAM) 管理ポリシー名| `AmazonSSMReadOnlyAccess`
| Systems Manager リソース ARN| `arn:aws:ssm:us-east-2:111222333444:patchbaseline/pb-07d8884178EXAMPLE`

[機能](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/features.html):

| **機能**              |  **内容**     |
| :-------------------- | :----------- |
| Operations Management     |  CloudWatch Dashboards/ OpsCenter / Resource Groups / Trusted Advisor & Personal Health Dashboard (PHD) |
| アクションと変更 | Automation  / メンテナンスウィンドウ  |
| インスタンスとノード | Configuration Compliance/ Inventory Management/ Managed Instances / Activations / Session Manager/ Run Command/ State Management / Patch Management / Distributor |
| 共有リソース | Systems Manager Documents / パラメータストア |
