# ECS

- [環境変数の取得](ECS.environ.md)
- [SSH接続](../../docker/docker.ssh.md)

ログ:

- [CloudWatch Logs](ECS.awslogs.md)


## サービスのタスクを再起動

- [AWS ECS restart Service with the same task definition and image with no downtime](https://stackoverflow.com/questions/42735328/aws-ecs-restart-service-with-the-same-task-definition-and-image-with-no-downtime)
- 強制更新して、新規のタスクが起動するので、古いタスクを手動で削除する

サービス名: `djdocker`, クラスタ名: `services`

~~~bash
aws ecs update-service --force-new-deployment --service djdocker --cluster services --profile spindd
~~~ 
