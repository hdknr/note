
- [detach-volume](http://docs.aws.amazon.com/cli/latest/reference/ec2/detach-volume.html)

## 強制的にデタッチ

~~~bash
$ sudo aws ec2 detach-volume --volume-id vol-668537de --force
{
    "AttachTime": "2016-02-25T01:55:48.000Z",
    "InstanceId": "i-7897f3f7",
    "VolumeId": "vol-668537de",
    "State": "detaching",
    "Device": "/dev/sdf"
}
~~~bash

すでにデタッチされているとエラーが帰ります

~~~bash
$ sudo aws ec2 detach-volume --volume-id vol-668537de --force

A client error (IncorrectState) occurred when calling the DetachVolume operation:
Volume 'vol-668537de'is in the 'available' state.
~~~

[describe-volumes](http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html) で確認

~~~bash
$ sudo  aws ec2 describe-volumes --volume-ids vol-668537de | jq ".[][0]"
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

~~~bash
$ sudo aws ec2 detach-volume --filters Name=tag-key,Values="Name" Name=tag-value,Values="ApplicationStorage"  --force
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument --volume-id is required
~~~

~~~bash
$ export VOLID=$(aws ec2 describe-volumes --filters Name=tag-key,Values="Name" Name=tag-value,Values="ApplicationStorage" | jq '.[][0].VolumeId' -r)

$ sudo aws ec2 detach-volume --volume-id $VOLID --force
{
    "AttachTime": "2016-02-25T02:08:54.000Z",
    "InstanceId": "i-7897f3f7",
    "VolumeId": "vol-668537de",
    "State": "detaching",
    "Device": "/dev/sdf"
}
~~~
