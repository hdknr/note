# デプロイ

## サービスのタスクを再起動

- [AWS ECS restart Service with the same task definition and image with no downtime](https://stackoverflow.com/questions/42735328/aws-ecs-restart-service-with-the-same-task-definition-and-image-with-no-downtime)
- 強制更新して、新規のタスクが起動するので、古いタスクを手動で削除する

サービス名: `djdocker`, クラスタ名: `services`

```bash
aws ecs update-service --force-new-deployment --service djdocker --cluster services --profile spindd
```

## ブルーグリーンデプロイメント

- もう１セットのサービスを用意して、テストしてから切り替えることで安全に、ダウンタイムもほぼ無いリリースができる技術
- CodeDeploy サービスを利用することで、ブルーグリーンデプロイの構成を作成することができるが、関連するサービスのデプロイも考慮する必要がある

- [ECS ブルーグリーンデプロイメントをゼロから構築する。（その１：ネットワークの設定）](https://qiita.com/sakai00kou/items/234318b980ded1aa7577#%E3%83%96%E3%83%AB%E3%83%BC%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%B3%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%83%A1%E3%83%B3%E3%83%88%E3%81%A8%E3%81%AF)
