## `AWSサービス` ロール作成

![](role.1.png)
![](role.2.png)
![](role.3.png)
![](role.4.png)

## 「インランポリシーの追加」
![](role.5.png)

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

![](role.7.policy.png)
![](role.8.policy.png)