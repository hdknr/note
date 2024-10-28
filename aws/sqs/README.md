# SQS

## terraform 例

```hcl
provider "aws" {
  region = "us-west-2"
}

resource "aws_sqs_queue" "example_queue" {
  name                      = "example-queue"
  message_retention_seconds = 86400  # メッセージの保持期間（秒）
  visibility_timeout_seconds = 30    # 可視性タイムアウト（秒）
  tags = {
    Environment = "production"
  }
}
```

このスクリプトは、`example-queue`という名前のSQSキューを作成し、メッセージの保持期間を1日（86400秒）、可視性タイムアウトを30秒に設定しています。

さらに、SQSキューをLambda関数のイベントソースとして設定する場合の例も紹介します[¹](https://zenn.dev/voicy/articles/e8368c299d1de0):

```hcl
resource "aws_lambda_function" "example_lambda" {
  function_name = "example_lambda_function"
  handler       = "index.handler"
  runtime       = "nodejs14.x"
  role          = aws_iam_role.lambda_exec_role.arn
  filename      = "lambda_function_payload.zip"
}

resource "aws_lambda_event_source_mapping" "example_mapping" {
  event_source_arn = aws_sqs_queue.example_queue.arn
  function_name    = aws_lambda_function.example_lambda.arn
  batch_size       = 10
}
```

このスクリプトでは、`example_lambda_function`というLambda関数を作成し、`example_queue`からのイベントをトリガーとして設定しています。

[¹](https://zenn.dev/voicy/articles/e8368c299d1de0): [Zennの記事](https://zenn.dev/voicy/articles/e8368c299d1de0)

ソース: Copilot との会話、 2024/10/23
(1) SQSをイベントソースとしたLambdaをTerraformで定義する - Zenn. <https://zenn.dev/voicy/articles/e8368c299d1de0>.
(2) Terraformを使用したAWS SQSとLambdaの統合 - Qiita. <https://qiita.com/omitsuhashi/items/4e2c87a47ebd9f3f616a>.
(3) Terraform Registry. <https://registry.terraform.io/modules/terraform-aws-modules/sqs/aws/latest/examples/complete>.
(4) Amazon CloudWatch Logsのサブスクリプションフィルターを .... <https://qiita.com/neruneruo/items/db1e29386e036568acf0>.
(5) undefined. <https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/with-sqs.html>.
(6) undefined. <https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function>.
(7) undefined. <https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-handler.html>.
(8) undefined. <https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sqs_queue>.
(9) undefined. <https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>.
(10) undefined. <https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html>.
(11) undefined. <https://tech.uzabase.com/entry/2021/02/22/124454>.
(12) undefined. <https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_event_source_mapping>.
(13) undefined. <https://qiita.com/advent-calendar/2022/voicy>.
