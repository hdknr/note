## ECS タスク定義

- [terraform:aws_ecs_task_definition](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition)
- [ulimits](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definition_parameters.html)

## コマンドの上書き

| ディレティブ | 内容                                                   | 注意             |
| ------------ | ------------------------------------------------------ | ---------------- |
| ENTRYPOINT   | docker runのパラメータがそのままENTRYPOINTのパラメータ |                  |
| CMD          | docker runのパラメータをCMD自体として扱う              | **コマンドの上書き** で指定するもの |
## 資料

- [ulimits](../../command/u/ulimits.md)
- [【AWS ECS】Fargateの「コマンドの上書き」](https://qiita.com/akihiko_sugiyama/items/bc1628230e7ac58e09d1)
