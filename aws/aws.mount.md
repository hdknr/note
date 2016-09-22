## ツール

~~~bash
$ sudo apt-get update
$ sudo apt-get install jq python-pip tree -y
$ sudo pip install awscli
~~~

~~~bash
$ sudo aws configure
~~~

## アタッチするスクリプト

- [awslabs/aws-quickstart](https://github.com/awslabs/aws-quickstart/blob/master/sap/scripts/create-attach-volume.sh)

~~~
#!/bin/bash
# Booting Insntace ID
export INSTANCE_ID=$(wget -q -O - http://169.254.169.254/latest/meta-data/instance-id)

# Wait
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

export VOLUME_ID=$(aws ec2 describe-volumes --filters \
    Name=tag-key,Values="Name" \
    Name=tag-value,Values="AppDisk" \
    Name=status,Values="available"  | jq ".Volumes[].VolumeId")

if [ "$VOLUME_ID" == "" ]; then
    echo "No Available Volume"
    exit
fi

export VOLUME_ID=$(eval "echo $VOLUME_ID")

# Attach
aws ec2 attach-volume  --volume-id $VOLUME_ID --instance-id $INSTANCE_ID --device /dev/sdf

# Wait
aws ec2 wait volume-available  --volume-ids $VOLUME_ID

~~~

- デバイスが利用可能になるまでまつbash関数

~~~bash
wait_for_attach_volume () {
   local volumeid="$1"
    while true; do
		status=$(aws ec2 describe-volumes --volume-ids ${volumeid}  | \
				${JQ_COMMAND} '.Volumes[].Attachments[].State' )
		echo ${volumeid}:${status}
        case "$status" in
			*attached* ) break;;
        esac
		sleep 10
	done
	log ${volumeid}:"attached"
}
~~~

## パーティション作成

- [Amazon EBS ボリュームを使用できるようにする](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ebs-using-volumes.html)
- /dev/sdb で作成したボリュームをインスタンスにアタッチ

~~~bash
# fdisk /dev/xvdf

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x36d6905d.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-209715199, default 2048):
Last sector, +sectors or +size{K,M,G,T,P} (2048-209715199, default 209715199):

Created a new partition 1 of type 'Linux' and of size 100 GiB.

Command (m for help): p

Disk /dev/xvdf: 100 GiB, 107374182400 bytes, 209715200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x36d6905d

Device     Boot Start       End   Sectors  Size Id Type
/dev/xvdf1       2048 209715199 209713152  100G 83 Linux

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.


~~~

~~~bash
# file -s /dev/xvdf
/dev/xvdf: DOS/MBR boot sector; partition 1 : ID=0x83, start-CHS (0x0,32,33), end-CHS (0x2fe,42,44), startsector 2048, 209713152 sectors, extended partition table (last)
~~~

## フォーマット

~~~
# mkfs -t ext4 /dev/xvdf1
mke2fs 1.42.9 (4-Feb-2014)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
6553600 inodes, 26214144 blocks
1310707 blocks (5.00%) reserved for the super user
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

## マウント

~~~bash
#!/bin/bash

mkdir -p /vagrant
chown ubuntu:ubuntu /vagrant
cat >>/etc/fstab <<EOF
/dev/xvdf1 /vagrant ext4 defaults 1 1
EOF

mount -a
~~~

-  確認

~~~

# df -H
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1      127G  1.2G  121G   1% /
none            4.1k     0  4.1k   0% /sys/fs/cgroup
udev            298M   13k  298M   1% /dev
tmpfs            62M  201k   62M   1% /run
none            5.3M     0  5.3M   0% /run/lock
none            309M     0  309M   0% /run/shm
none            105M     0  105M   0% /run/user
/dev/xvdf1      106G   63M  101G   1% /vagrant
~~~
