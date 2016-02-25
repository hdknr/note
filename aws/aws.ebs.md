#  EBSはいつ in-use から available になるか？

- EC2インスタンスをおとしただけだと、attached されているEBSは in-use のまま
- 削除すると available に変わる


#  describe-volumes

## ストレージ名で検索

[describe-volumes](http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html)

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


# detach-valume

- [detach-volume](http://docs.aws.amazon.com/cli/latest/reference/ec2/detach-volume.html)

強制的にデタッチ

~~~
# aws ec2 detach-volume --volume-id vol-668537de --force
{
    "AttachTime": "2016-02-25T01:55:48.000Z",
    "InstanceId": "i-7897f3f7",
    "VolumeId": "vol-668537de",
    "State": "detaching",
    "Device": "/dev/sdf"
}
~~~

すでにデタッチされているとエラーが帰ります

~~~
# aws ec2 detach-volume --volume-id vol-668537de --force

A client error (IncorrectState) occurred when calling the DetachVolume operation:
Volume 'vol-668537de'is in the 'available' state.
~~~

[describe-volumes](http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html) で確認

~~~
# aws ec2 describe-volumes --volume-ids vol-668537de | jq ".[][0]"
{
  "Size": 100,
  "CreateTime": "2016-02-25T01:55:48.781Z",
  "AvailabilityZone": "ap-northeast-1c",
  "Attachments": [],
  "Encrypted": false,
  "VolumeType": "gp2",
  "VolumeId": "vol-668537de",
  "State": "available",
  "Iops": 300,
  "SnapshotId": "snap-6996c955"
}
~~~

## `volume-id` は必須

~~~
# aws ec2 detach-volume --filters Name=tag-key,Values="Name" Name=tag-value,Values="ApplicationStorage"  --force
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument --volume-id is required
~~~

~~~
# export VOLID=$(aws ec2 describe-volumes --filters Name=tag-key,Values="Name" Name=tag-value,Values="ApplicationStorage" | jq '.[][0].VolumeId' -r)

# aws ec2 detach-volume --volume-id $VOLID --force
{
    "AttachTime": "2016-02-25T02:08:54.000Z",
    "InstanceId": "i-7897f3f7",
    "VolumeId": "vol-668537de",
    "State": "detaching",
    "Device": "/dev/sdf"
}
~~~

# 記事

- [[AWS] EC2インスタンスにEBSボリュームをアタッチする/デタッチする](http://qiita.com/white_aspara25/items/270c7253e5fe58bd5d86)