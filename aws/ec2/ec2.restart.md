# EC2 リスタート

## boto3

[reboot_instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/reboot-instances.html)

```py
import boto3

ec2 = boto3.client('ec2')
response = ec2.reboot_instances(InstanceIds=['string'])
```

## 記事

- [【習作】EC2 を起動してステータスチェックに失敗したらリトライするスクリプトを書いた](https://dev.classmethod.jp/articles/check-instance-status-script/)
- [How to Auto Shutdown and Start Amazon EC2 Instance](https://saturncloud.io/blog/how-to-auto-shutdown-and-start-amazon-ec2-instance/)
