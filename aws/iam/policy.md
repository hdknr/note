# ポリシー


## ロールポリシーの表示 (`get-role-policy`)

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
                    "arn:aws:kms:ap-northeast-1:695590128999:key/10d2672b-8fdf-37e4-a561-7614433ab6d9",
                    "arn:aws:secretsmanager:ap-northeast-1:695590128999:secret:*",
                    "arn:aws:ssm:*:695590128999:parameter/*"
                ]
            }
        ]
    }
}
~~~