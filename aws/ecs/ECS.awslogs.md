# ECS: CloudWatch Logs へのログシッピング


- [AWS> ドキュメント> Amazon ECS> 開発者ガイド> awslogs ログドライバーを使用する](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/using_awslogs.html)

awslogs ドライバ:

- デフォルトでは、 `/dev/stdout` , `/dev/stderr`  のキャプチャを  CloudWatch Logsにシップする


## 例 Django: ログを `/dev/stdout` にストリームする

- [Centralized Logging with Django, Docker, and CloudWatch](https://testdriven.io/blog/django-logging-cloudwatch/)

loggings.py でログを `/dev/stdout` に流す:

~~~py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
~~~

## 資料

Docker Log:

- [View logs for a container or service](https://docs.docker.com/config/containers/logging/)
