[describe-volumes](http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html)

## EC2 に接続できない

~~~bash
$ /usr/bin/aws ec2 describe-volumes

HTTPSConnectionPool(host='ec2.ap-northeast-1a.amazonaws.com', port=443):
Max retries exceeded with url: /
(Caused by NewConnectionError('<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7f1d1c5c4278>:
Failed to establish a new connection: [Errno -2] Name or service not known',)
~~~

これは、リージョン名が間違っている。

- `ap-northeast-1a` は `ゾーン名`
- `ap-northeast-1` が `リージョン名`


## ストレージ名で検索


~~~
# aws ec2 describe-volumes --filters Name=tag-key,Values="Name" Name=tag-value,Values="ApplicationStorage" | jq ".[]"
[
  {
    "Size": 100,
    "CreateTime": "2016-02-25T01:55:48.781Z",
    "SnapshotId": "snap-6996c955",
    "AvailabilityZone": "ap-northeast-1c",
    "Attachments": [
      {
        "Device": "/dev/sdf",
        "DeleteOnTermination": false,
        "State": "attaching",
        "VolumeId": "vol-668537de",
        "InstanceId": "i-7897f3f7",
        "AttachTime": "2016-02-25T02:08:54.000Z"
      }
    ],
    "Tags": [
      {
        "Key": "Name",
        "Value": "ApplicationStorage"
      }
    ],
    "Encrypted": false,
    "VolumeType": "gp2",
    "VolumeId": "vol-668537de",
    "State": "in-use",
    "Iops": 300
  }
]
~~~

## 利用可能なストレージ

- 利用可能なボリューム

~~~bash
$ aws ec2 describe-volumes --filters Name=status,Values="available"
$ aws ec2 describe-volumes --filters Name=status,Values="available"  | jq ".Volumes[].VolumeId"
"vol-79ad2586"
~~~


## ボリューム一覧

~~~bash
$ aws ec2 describe-volumes | jq ".Volumes[].VolumeId"
"vol-4ff179b0"
"vol-79ad2586"
"vol-56bb259f"
~~~
