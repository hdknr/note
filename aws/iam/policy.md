# ポリシー


## ポリシー一覧(`list-policies`)

~~~bash
% env $(cat .env|xargs) aws iam list-policies --scope Local --only-attached  | jq -r ".Policies[]|[.PolicyName,.Arn]|@tsv" | grep legacy
~~~


## ポリシードキュメント(`get-policy-version`)

~~~bash
POLICY=our-policy
ARN=$(aws iam list-policies --scope Local --only-attached  | jq -r '.Policies[]|select(.PolicyName == "'$POLICY'")|.Arn')
aws iam get-policy-version \
  --policy-arn $ARN \
  --version-id $(aws iam get-policy --policy-arn $ARN | jq -r '.Policy.DefaultVersionId') | jq -r '.PolicyVersion.Document' 
~~~

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

## 資料

- [aws-cliで効率よくIAMのポリシードキュメント更新を行ってみた](https://dev.classmethod.jp/articles/iam-policy-document-update-on-terminal/)


