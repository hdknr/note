## attach-volume

-  [インスタンス起動時にEBSをアタッチしてマウントする](ebs.attach-volume.md)

## describe-volumes

-  [EC2 に接続できない](ebs.describe-volumes.md)
- ボリューム一覧
- 利用可能なボリューム
- ストレージ名で検索

## [detach-volume.md](ebs.detach-volume.md)

- 強制的にデタッチ


##  EBSはいつ in-use から available になるか？

- EC2インスタンスをおとしただけだと、attached されているEBSは in-use のまま
- 削除すると available に変わる


## デバイス名

- [Linux でボリュームを使用できるようにする](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ebs-using-volumes.html)

  `このような場合、各デバイス名の末尾の文字は同じ規則で変更されます。たとえば、/dev/sdb が /dev/xvdf になり、/dev/sdc が /dev/xvdg に変更されます。`

- デバイス名が異なる `lsblk` ( list block devices) で確認

~~~bash
$ sudo lsblk
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
xvda    202:0    0     8G  0 disk
└─xvda1 202:1    0     8G  0 part /
xvdb    202:16   0   100G  0 disk
~~~

- data だけが表示された場合、デバイスにはファイルシステムが存在していないので、ファイルシステムを作成する必要があります。

~~~bash
$ sudo file -s /dev/xvdb
/dev/xvdb: data
~~~

## ファイルシステム作成

~~~bash
$ sudo mkfs -t ext4 /dev/xvdb

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
$ sudo file -s /dev/xvdb
/dev/xvdb: Linux rev 1.0 ext4 filesystem data, UUID=f1babc5d-3254-4f92-ba4c-381c3a748c2b (extents) (large files) (huge files)
~~~


## マウント

~~~bash
$ sudo mkdir /home/system
$ sudo mount /dev/xvdb /home/system

$ sudo lsblk
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
xvda    202:0    0     8G  0 disk
└─xvda1 202:1    0     8G  0 part /
xvdb    202:16   0   100G  0 disk /home/system
~~~

## /etc/fstab


~~~
LABEL=cloudimg-rootfs	/	 ext4	defaults,discard	0 0
/var/swap/swap0 swap swap defaults 0 0
/dev/xvdf1	/vagrant  ext4    defaults	0    0
~~~


~~~bash 
$ sudo file -s /dev/xvdf1
/dev/xvdf1: Linux rev 1.0 ext4 filesystem data, UUID=7da175a4-ed10-4c74-af46-4d233d433a3b (needs journal recovery) (extents) (large files) (huge files)
~~~

~~~bash 
$ sudo lsblk
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
xvdf    202:80   0   100G  0 disk 
└─xvdf1 202:81   0   100G  0 part /vagrant
xvda1   202:1    0   120G  0 disk /
~~~


## 記事

- [[AWS] EC2インスタンスにEBSボリュームをアタッチする/デタッチする](http://qiita.com/white_aspara25/items/270c7253e5fe58bd5d86)
