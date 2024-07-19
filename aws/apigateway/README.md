# API Gateway

## HTTP/2 429

スロットリングの問題:

```tf
resource "aws_apigatewayv2_stage" "this" {
  name          = "${var.symbol.prefix}-this-stage"
  api_id        = aws_apigatewayv2_api.kb.id
  deployment_id = aws_apigatewayv2_deployment.kb.id
  default_route_settings {
    detailed_metrics_enabled = false
    throttling_burst_limit   = 10 # 必ずしていすること！(デフォルト0)
    throttling_rate_limit    = 10 # 必ずしていすること！(デフォルト0)
  }
  tags = {}

}
```

## 記事

- [AWS API Gateway の Websocket サーバを Terraform で書いてみた](https://qiita.com/taniyk/items/9f2d55ee95e4da31f909)
- [Deploy serverless applications with AWS Lambda and API Gateway](https://developer.hashicorp.com/terraform/tutorials/aws/lambda-api-gateway)
- [落とし穴にハマるな！AWS Lambda を利用するときの 6 つの注意点](https://www.skyarch.net/column/aws-lambda-important-point/)
