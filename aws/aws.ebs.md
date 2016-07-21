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


## ボリューム一覧

~~~bash
$ aws ec2 describe-volumes | jq ".Volumes[].VolumeId"
"vol-4ff179b0"
"vol-79ad2586"
"vol-56bb259f"
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

# デバイス名

- [Linux でボリュームを使用できるようにする](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ebs-using-volumes.html)

- デバイス名が異なる

~~~bash
# lsblk
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
xvda    202:0    0     8G  0 disk
└─xvda1 202:1    0     8G  0 part /
xvdb    202:16   0   100G  0 disk
~~~

- data だけが表示された場合、デバイスにはファイルシステムが存在していないので、ファイルシステムを作成する必要があります。

~~~bash
# file -s /dev/xvdb
/dev/xvdb: data
~~~

- 作成

~~~bash
# mkfs -t ext4 /dev/xvdb
mke2fs 1.42.9 (4-Feb-2014)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
6553600 inodes, 26214400 blocks
1310720 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=4294967296
800 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
	4096000, 7962624, 11239424, 20480000, 23887872

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done   
~~~

~~~bash
# file -s /dev/xvdb
/dev/xvdb: Linux rev 1.0 ext4 filesystem data, UUID=f1babc5d-3254-4f92-ba4c-381c3a748c2b (extents) (large files) (huge files)
~~~

~~~bash
# mkdir /home/system
# mount /dev/xvdb /home/system
~~~




# 記事

- [[AWS] EC2インスタンスにEBSボリュームをアタッチする/デタッチする](http://qiita.com/white_aspara25/items/270c7253e5fe58bd5d86)
