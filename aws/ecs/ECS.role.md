# ロール

２つのロール:

| **ロール**       | **内容**                                                                                                                       | 用途                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| タスクロール     | [タスク用の IAM ロール](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task-iam-roles.html)                 | コンテナで使用できる IAM ロール                 |
| タスク実行ロール | [Amazon ECS コンテナエージェント](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ECS_agent.html) が利用する | AmazonECSTaskExecutionRolePolicy を設定すること |


## タスク実行ロール

ecsTaskExecutionRole:

- マネジメントコンソールで ECS のタスク定義を作成するときに、タスク実行ロールで「新しいロールの作成」を選択すると、AmazonECSTaskExecutionRolePolicy がアタッチされた ecsTaskExecutionRole が作成されます 


### System Managerのパラメータストアを参照して 環境変数にセットする

全てのリージョン, アカウント番号=695590128999, 全てのパラメータ  で、パラメータ取得を許す

- SecureString:  `arn:aws:secretsmanager:*:695590128999:secret:*` 
- String: `arn:aws:ssm:*:695590128999:parameter/*` 

SecureStringのデコードのためにキーのアクセスを許す:

- SecureString を使用するときに生成されたキー: `arn:aws:kms:ap-northeast-1:695590128999:key/10d2672b-7abc-46f5-a561-7614433ab6d9`

ECS-SecretsManager-Permissionポリシー: 

~~~bash
% aws iam get-role-policy --role-name ecsTaskExecutionRole --policy-name ECS-SecretsManager-Permission --profile spindd
~~~

~~~json
{
    "RoleName": "ecsTaskExecutionRole",
    "PolicyName": "ECS-SecretsManager-Permission",
    "PolicyDocument": {
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
                    "arn:aws:kms:ap-northeast-1:695590128999:key/10d2672b-7abc-46f5-a561-7614433ab6d9",
                    "arn:aws:secretsmanager:*:695590128999:secret:*",
                    "arn:aws:ssm:*:695590128999:parameter/*"
                ]
            }
        ]
    }
}
~~~



## 記事

- [ECSのタスクロールとタスク実行ロールの違い](https://www.karakaram.com/difference-between-ecs-task-role-and-task-execution-role/)
