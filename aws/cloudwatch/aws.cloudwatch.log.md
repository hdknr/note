
# CloudWatch Logs エージェント

## Ubuntuにインストール

[クイックスタート: 実行中の EC2 Linux インスタンスに CloudWatch Logs エージェントをインストールして設定する](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html) 

~~~bash 
$ curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -O
~~~

~~~bash
$ sudo python ./awslogs-agent-setup.py --region ap-northeast-1

Launching interactive setup of CloudWatch Logs agent ... 

Step 1 of 5: Installing pip ...libyaml-dev does not exist in system DONE

Step 2 of 5: Downloading the latest CloudWatch Logs agent bits ... DONE

Step 3 of 5: Configuring AWS CLI ... 
AWS Access Key ID [None]: XKIAIA4YIP9UFBYLMRA
AWS Secret Access Key [None]: Ki7cail6Coo2aengeu4lieN2avoSee2v
Default region name [ap-northeast-1]: 
Default output format [None]: 

Step 4 of 5: Configuring the CloudWatch Logs Agent ... 
Path of log file to upload [/var/log/syslog]: /var/log/nginx/myapp.access.ltsv.log
Destination Log Group name [/var/log/nginx/myapp.access.ltsv.log]: nginx

Choose Log Stream name:
  1. Use EC2 instance id.
  2. Use hostname.
  3. Custom.
Enter choice [1]: 1

Choose Log Event timestamp format:
  1. %b %d %H:%M:%S    (Dec 31 23:59:59)
  2. %d/%b/%Y:%H:%M:%S (10/Oct/2000:13:55:36)
  3. %Y-%m-%d %H:%M:%S (2008-09-08 11:52:54)
  4. Custom
Enter choice [1]: 3

Choose initial position of upload:
  1. From start of file.
  2. From end of file.
Enter choice [1]: 1
More log files to configure? [Y]: N

Step 5 of 5: Setting up agent as a daemon ...DONE


------------------------------------------------------
- Configuration file successfully saved at: /var/awslogs/etc/awslogs.conf
- You can begin accessing new log events after a few moments at https://console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logs:
- You can use 'sudo service awslogs start|stop|status|restart' to control the daemon.
- To see diagnostic information for the CloudWatch Logs Agent, see /var/log/awslogs.log
- You can rerun interactive setup using 'sudo python ./awslogs-agent-setup.py --region ap-northeast-1 --only-generate-config'
------------------------------------------------------
~~~

~~~bash
$ sudo ps ax  | grep aws
.
26755 ?        S      0:00 /bin/sh /var/awslogs/bin/awslogs-agent-launcher.sh
26758 ?        SNl    0:01 /var/awslogs/bin/python /var/awslogs/bin/aws logs push --config-file /var/awslogs/etc/awslogs.conf --additional-configs-dir /var/awslogs/etc/config
~~~

## インスタンスにロールを割り当てる

[IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role)

~~~bash 
$ aws ec2 associate-iam-instance-profile --instance-id $(wget -q -O - http://169.254.169.254/latest/meta-data/instance-id) --iam-instance-profile Name="AppServer"
.
~~~

## 設定ファイル

~~~bash
$ sudo grep -v "^#" /var/awslogs/etc/awslogs.conf | grep -v "^$"
.
~~~

~~~ini
[general]
state_file = /var/awslogs/state/agent-state

[/var/log/nginx/myapp.access.ltsv.log]
datetime_format = %Y-%m-%d %H:%M:%S
file = /var/log/nginx/myapp.access.ltsv.log
buffer_duration = 5000
log_stream_name = {instance_id}
initial_position = start_of_file
log_group_name = nginx

[/var/log/mysql/error.log]
datetime_format = %Y-%m-%d %H:%M:%S
file = /var/log/mysql/error.log
buffer_duration = 5000
log_stream_name = {instance_id}
initial_position = start_of_file
log_group_name = mysql
~~~

## フィルターパターン

スペース区切りファイルのパターン指定

~~~
[time, remote_addr, request_method, request_length, request_uri, https, uri, query_string, status=*5*, bytes_sent, body_bytes_sent, referer, useragent, forwarderedfor, request_time, upstream_response_time]
~~~


##　資料

~~~python
[time, remote_addr, request_method, request_length, request_uri, https, uri, query_string, status=*5*, bytes_sent, body_bytes_sent, referer, useragent, forwarderedfor, request_time, upstream_response_time]
~~~

##　資料

- [CloudWatch Logs エージェントのリファレンス](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/logs/AgentReference.html)
