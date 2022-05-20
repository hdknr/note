# 定期実行

- [Amazon EventBridge](https://docs.aws.amazon.com/ja_jp/eventbridge/latest/userguide/eb-what-is.html) で ECSタスクを定期実行する

## 定義

CRONで実行するECSの一覧を定義:

~~~tf
locals {
  cronjobs = flatten([
    for name, defs in var.ecs_app_confs : [
      for cron in defs.cronjobs : {
        name     = "${var.name}-${var.environment}-cron-${name}-${cron.name}" # key
        app      = name
        container_def = local.container_definitions[name] 
        schedule = cron.schedule
        command  = cron.command
      }
    ]
  ])

}
~~~

~~~tf
# 1.イベントルール 
#
# cronjobsに key = { schedue=CRON書式 } で定義している。 
resource "aws_cloudwatch_event_rule" "this" {
  for_each = { for cron in local.cronjobs : "${cron.name}" => cron }
  # 
  name                = each.key
  schedule_expression = each.value.schedule     # CRON書式
}


# 2. イベントターゲット(ECSタスク)の定義
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target
resource "aws_cloudwatch_event_target" "this" {
  for_each = { for cron in local.cronjobs : "${cron.name}" => cron }
  #
  target_id = "${each.key}-target"
  rule      = aws_cloudwatch_event_rule.this[each.key].name     # 1.イベントルールで定義したルール(aws_cloudwatch_event_ruleのnameがキー)
  arn       = aws_ecs_cluster.this[each.value.app].arn          # appの名前で識別されるECSのクラスタター
  role_arn  = aws_iam_role.task.arn                             # ECSタスクロール
  #
  input = jsonencode({
    containerOverrides = [
      {
        name    = each.value.container_def.name                 # コンテナ定義
        command = each.value.command                            # 実行コマンド
      }
    ]
  })

  # 実行するECSの内容
  ecs_target {
    // リビジョンなしで渡すことで常に最新のバージョンを使用するようにする
    launch_type         = "FARGATE"
    task_definition_arn = replace(aws_ecs_task_definition.this[each.value.app].arn, "/:\\d+$/", "")
    task_count          = 1
    network_configuration {
      security_groups  = var.sg_set         # タスクが動作するセキュリティグループ
      subnets          = var.subnets        # タスクが動作するネットワーク
      assign_public_ip = true
    }
  }
}

~~~

## 実行の確認

必要なメトリックを探す:

~~~bash
aws cloudwatch list-metrics
~~~

metric-query.jsonに記載する(タスク起動(Invocations)):

~~~json
[{
    "Id": "m1",
    "MetricStat": {
        "Metric": {
            "Namespace": "AWS/Events",
            "MetricName": "Invocations",
            "Dimensions": [{
                "Name": "RuleName",
                "Value": "task-schedule-name"
            }]
        },
        "Period": 3600,
        "Stat": "Sum",
        "Unit": "Count"
    }
}]
~~~

~~~bash
aws cloudwatch get-metric-data \
    --metric-data-queries file://./modules/ecs/bin/metric-query.json  \
    --start-time '2022-05-10T00:00:00Z' \ 
    --end-time '2022-05-20T00:00:00Z'
~~~

~~~json
{
    "MetricDataResults": [
        {
            "Id": "m1",
            "Label": "Invocations",
            "Timestamps": [
                "2022-05-19T20:00:00+00:00",
                "2022-05-18T20:00:00+00:00",
                ...
            ],
            "Values": [
                1.0,
                1.0,
                ...
            ],
            "StatusCode": "Complete"
        }
    ],
    "Messages": []
}
~~~
