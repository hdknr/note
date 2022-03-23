# ECS howto

## ulimits: IOError: [Errno 24] Too many open files

- [タスク定義](ECS.task_definition.md) で設定する

~~~tf
locals {
  container_definitions = [
    {
      name   = "my_container"
      image  = "nginx"
      cpu    = 1024
      memory = 2048
      ulimits = [
        {
          name      = "nofile"
          hardLimit = 65535
          softLimit = 65535
        }
      ]
    }
  ]
}

resource "aws_ecs_task_definition" "this" {
  container_definitions = jsonencode(local.container_definitions)
}
~~~
