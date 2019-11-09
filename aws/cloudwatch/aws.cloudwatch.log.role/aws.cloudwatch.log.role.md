# `AWSサービス` ロール作成

![サービス選択](role.1.png)
![権限ポリシー選択](role.2.png)
![ロール名](role.3.png)
![作成](role.4.png)

## 「インランポリシーの追加」

![インラインポリシー](role.5.png)

## JSONをコピペ

![](role.6.policy.png)

~~~json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
    ],
      "Resource": [
        "arn:aws:logs:*:*:*"
    ]
  }
 ]
}
~~~

## 保存

![ポリシー名/許可サービス/許可権限](role.7.policy.png)
![作成](role.8.policy.png)
