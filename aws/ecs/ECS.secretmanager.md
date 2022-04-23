# シークレットマネージャ連携


- [ECSでコンテナ環境変数をSecretManagerから取得する際にResourceInitializationErrorが発生したときの対処方法](https://dev.classmethod.jp/articles/tsnote-ecs-resourceinitializationerror/)

1. 実行 IAM ロールの権限不足
2. 誤った形式での SecretsManager への参照
3. SecretsManager エンドポイントへの不到達 (プライベートネットワーク内のECSから)


- [AWS Secrets Managerへの接続がうまく行かなかったとき。](https://zenn.dev/fagai/articles/7fafa11807ef19)
- [Fargate 1.4.0 に対応する（VPCエンドポイントの設定）](https://blog.fakiyer.com/entry/2020/05/11/184759)
- [[Terraform] Fargate v1.4で必要なVPC endpoint設定](https://zenn.dev/samuraikun/articles/0d22699a9878cd)