# Auto Scaling 起動設定

- aws に作成

~~~
$ aws autoscaling create-launch-configuration --launch-configuration-name ec2_lc_test1 --image-id ami-e54e648b --key-name vagrant --security-groups development --instance-type t1.micro
~~~

- 確認

~~~
$ aws autoscaling describe-launch-configurations
{
    "LaunchConfigurations": [
        {
            "UserData": "",
            "EbsOptimized": false,
            "LaunchConfigurationARN": "arn:aws:autoscaling:ap-northeast-1:757103751050:launchConfiguration:6fec9df6-e4ed-4782-90e6-b593ec067d03:launchConfigurationName/ec2_lc_test1",
            "InstanceMonitoring": {
                "Enabled": true
            },
            "ClassicLinkVPCSecurityGroups": [],
            "CreatedTime": "2015-12-15T05:45:07.574Z",
            "BlockDeviceMappings": [],
            "KeyName": "vagrant",
            "SecurityGroups": [
                "development"
            ],
            "LaunchConfigurationName": "ec2_lc_test1",
            "KernelId": "",
            "RamdiskId": "",
            "ImageId": "ami-f548629b",
            "InstanceType": "t1.micro"
        }
    ]
}
~~~

- [ec2_lc - Create or delete AWS Autoscaling Launch Configurations](http://docs.ansible.com/ansible/ec2_lc_module.html)

# Auto Scaling グループ

~~~bash
$ aws autoscaling create-auto-scaling-group --auto-scaling-group-name ec2_asg_test1 --launch-configuration-name ec2_lc_test1 --min-size 1 --max-size 1 --availability-zones ap-northeast-1a
~~~

- [ec2_asg - Create or delete AWS Autoscaling Groups](http://docs.ansible.com/ansible/ec2_asg_module.html)


~~~bash
仮想化タイプ 'hvm' を使用する Windows 以外の AMI は現在、クラスターコンピューティングインスタンスタイプでのみ使用できます。EC2 インスタンスの起動に失敗しました。

原因: HVM 仮想化を使用する Linux AMI は、クラスターコンピューティング以外のインスタンスの起動には使用できません。
解決策:
クラスターコンピューティング以外のインスタンスを起動するには、準仮想化の仮想化タイプを使用する AMI を使用して、起動設定を作成します。
update-auto-scaling-group コマンドを使用して、新しい起動設定を使用するように Auto Scaling グループを更新します。
~~~

# ロードバランシング

~~~bash
TODO:
~~~
