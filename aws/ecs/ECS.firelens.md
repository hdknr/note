# ECS Firelens

- Kinesis Data Firehose でログシッピングする

## タスクロール

FargateFireosePolicy:

~~~json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "firehose:PutRecordBatch",
            "Resource": "*"
        }
    ]
}
~~~

## タスク定義

作成した Kinesis Data Firehose 名を `djdocker-s3` とする

アプリケーション:

~~~json
    "logConfiguration": {
        "logDriver":"awsfirelens",
        "options": {
            "Name": "firehose",
            "region": "ap-northeast-1",
            "delivery_stream": "djdocker-s3"
        }
    }
~~~


## `log_router`  コンテナ

- アプリケーションのログドライバを `firehose` にすると追加される

