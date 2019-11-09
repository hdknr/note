# AWS: CloudWatch

- [CloudWatch Logs エージェント](aws.cloudwatch.log.md)
- [料金請求/アラート](billing.md)
- [aws logs](awscli.logs.md)

## ドキュメント

- [Amazon CloudWatch](https://docs.aws.amazon.com/ja_jp/cloudwatch/)

API:

- [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/APIReference/Welcome.html)
- [Amazon EventBridge API Reference](https://docs.aws.amazon.com/ja_jp/eventbridge/latest/APIReference/Welcome.html)
- [Amazon CloudWatch Logs API Reference](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatchLogs/latest/APIReference/Welcome.html)

Python:

- [boto3: CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html)
- [Creating Alarms in Amazon CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/cw-example-creating-alarms.html)

## Eventbridge

- Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources.
- EventBridge delivers a stream of real-time data from your own applications, software-as-a-service (SaaS) applications, and AWS services and routes that data to targets such as AWS Lambda.
- You can set up routing rules to determine where to send your data to build application architectures that react in real time to all of your data sources.
- EventBridge enables you to build event-driven architectures that are loosely coupled and distributed.

## [Logs](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

### Logs 機能

EC2 インスタンスのログのモニタリング:

- ログデータを使用してアプリケーションとシステムをモニタリングできます。
- アプリケーションログに存在するエラーの数をトラッキングし、エラー率が指定のしきい値を超えたときに管理者に通知を送ることができます。
- お客様のログが CloudWatch Logs によるモニタリングに使用されるので、コードの変更は不要です。
- アプリケーションログの特定のリテラルターム (例:「NullReferenceException」) をモニタリングしたり、ログデータの特定の場所でリテラルターム (例: Apache アクセスログの「404」ステータスコード) の発生数をカウントしたりできます。
- 検索した語句が見つかると、指定された CloudWatch メトリクスにデータをレポートします。
- ログデータは、転送時や保管時に暗号化されます。

CloudTrail のログに記録されたイベントのモニタリング:

- CloudWatchにアラームを作成して、CloudTrail がキャプチャした特定の API アクティビティの通知を受け取り、通知をトラブルシューティングの実行に使用できます。

ログの保持期間:

- デフォルトでは、ログは無制限に保持され、失効しません。
- ロググループごとに保持ポリシーを調整し、無制限の保持期間を維持するか、1 日間～10 年間の保持期間を選択することができます。

ログデータをアーカイブする:

- 耐久性が高いストレージにログデータを保存できます。
- CloudWatch Logs エージェントにより、ローテーションするログデータもローテーションしないログデータも、ホストからログサービスに簡単にすばやく送信できます。
- その後は、必要なときに生のログデータにアクセスできます。

Route 53 DNS クエリのログ:

– Route 53 が受け取る DNS クエリに関するログ情報を使用できます。


