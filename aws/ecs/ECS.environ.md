# ECS: パラメータストアから環境変数を設定する

## 方法

1. タスク定義に明示的に定義
2. S3に置いた.envファイル
3. パラメータストア/Secrets Managerからインポート

## Sysmtem Manager に環境情報を設定する

1. [AmazonECSTaskExecutionRolePolicy:Amazon ECS タスク実行 IAM ロールポリシー](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_execution_IAM_role.html)  

- 追加されているはず
  
2. ecsTaskExecuteionRoleロールにポリシーを追加すること

`ECS-SecretsManager-Permission.json`:

~~~json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "secretsmanager:GetSecretValue",
                "ssm:GetParameters"
            ],
            "Resource": [
                "arn:aws:kms:ap-northeast-1:696600128753:key/10d2672b-8fdf-46f5-a561-7614433ab6d9",
                "arn:aws:secretsmanager:ap-northeast-1:696600128753:secret:dev/DockerHubSecret-5Z0abn",
                "arn:aws:secretsmanager:ap-northeast-1:696600128753:secret:djdocker-database-params",
                "arn:aws:ssm:*:696600128753:parameter/*"
            ]
        }
    ]
}
~~~

3. パラメータストアに変数を定義する

-  AWS System Manager > アプリケーション管理 > パラメータストア
-  `名前`: 環境変数が参照する名称 (`docker-database-params` とか)
-  `KMSキーソース`:  `現在のアカウント`
-  `KMSキーID`: `alias/aws/ssm` もしくは選択
-  `タイプ`: `SecureString`
-  `値`: 環境変数が参照する実際の値 (`{"user": "useri1", "password": "pwd@wreq"}` とか)

4. タスク定義に`環境変数`を設定する

- `ValueFrom` としてアプリケーションから参照する環境変数名を`Key`として定義する( `DATABASE_PARAMS`とか)
- `Value` には、パラメータストアに定義した`名前` を入れる(`docker-database-params`とか)


## 資料

- [コンテナへの環境変数の受け渡し](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/taskdef-envfiles.html)
