VirtualBox: /homeをLVMにして増やす

- Vagrant で作ったDebian Jessieの/homeを増やす

# VMDK -> VDI (VBoxManage clonehd)


~~~
Peeko:js1 hide$ cd ~/VirtualBox\ VMs/js1_default_1413703213140_69014/
~~~

~~~
Peeko:js1_default_1413703213140_69014 hide$ ls -al
total 1607640
drwx------+  6 hide staff        204 10 19 16:20 .
drwxr-xr-x+ 14 hide staff        476 10 19 16:20 ..
drwx------+  3 hide staff        102 10 19 16:20 Logs
-rw-------+  2 hide staff 1646198784 10 19 20:23 box-disk1.vmdk
-rw-------+  1 hide staff       9221 10 19 16:20 js1_default_1413703213140_69014.vbox
-rw-------+  1 hide staff       9220 10 19 16:20 js1_default_1413703213140_69014.vbox-prev
~~~

- VBoxManage clonehd

~~~
Peeko:js1_default_1413703213140_69014 hide$ VBoxManage clonehd box-disk1.vmdk box-disk1.vdi --format VDI
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Clone hard disk created in format 'VDI'. UUID: 03cfdd84-2dad-4a5b-8e37-d2c13b7142f4
~~~

~~~
Peeko:js1_default_1413703213140_69014 hide$ ls -al
total 3684376
drwx------+  7 hide staff        238 10 19 20:28 .
drwxr-xr-x+ 14 hide staff        476 10 19 16:20 ..
drwx------+  3 hide staff        102 10 19 16:20 Logs
-rw-------+  1 hide staff 2126512128 10 19 20:28 box-disk1.vdi
-rw-------+  2 hide staff 1646264320 10 19 20:28 box-disk1.vmdk
-rw-------+  1 hide staff       9221 10 19 20:28 js1_default_1413703213140_69014.vbox
-rw-------+  1 hide staff       9221 10 19 20:28 js1_default_1413703213140_69014.vbox-prev
~~~

- VBoxManage modifyhd

~~~
Peeko:js1_default_1413703213140_69014 hide$ VBoxManage modifyhd box-disk1.vdi --resize 30480
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

~~~

## VDIの内容(VboxManage showhdinfo)

~~~
Peeko:js1_default_1413703213140_69014 hide$ VboxManage showhdinfo  box-disk1.vdi
UUID:           03cfdd84-2dad-4a5b-8e37-d2c13b7142f4
Parent UUID:    base
State:          created
Type:           normal (base)
Location:       /Users/hide/VirtualBox VMs/js1_default_1413703213140_69014/box-disk1.vdi
Storage format: VDI
Format variant: dynamic default
Capacity:       30480 MBytes
Size on disk:   2028 MBytes
~~~

## VM一覧(VBoxManage list vms)

~~~
Peeko:js1_default_1413703213140_69014 hide$ VBoxManage  list vms
"SQZ" {e4a545b2-947d-4e11-9661-5bbb7cd58708}
"Wzy" {11b93b36-8bd5-4eb0-9f99-c058b47362df}
"Ubu" {d81e3ff2-5c79-4200-9e6a-465df999cec5}
"Ubu2" {a34a6016-98be-4365-a4e1-63dc50d97611}
"Ubu3" {4805e250-cbd4-413f-9d7a-55fe9a931e8c}
"Google Nexus 4 - 4.3 - API 18 - 768x1280" {01d925db-4bf5-4d0e-8ca0-321987c8c3a1}
"Google Nexus 10 - 4.3 - API 18 - 2560x1600" {43d543d9-1fab-4f28-9152-b0d07819ef7a}
"IE11 - Win8.1" {f1328962-97d7-4824-bbe5-ea755b5f9c12}
"js1_default_1413703213140_69014" {d3447ba2-0184-4b6a-ac79-a86a6362250f}

~~~

## ストレージコントローラ確認(VBoxManage showvminfo)

~~~
Peeko:js1_default_1413703213140_69014 hide$ VBoxManage showvminfo js1_default_1413703213140_69014 | GREP_OPTIONS='' grep "Storage"
Storage Controller Name (0):            IDE Controller
Storage Controller Type (0):            PIIX4
Storage Controller Instance Number (0): 0
Storage Controller Max Port Count (0):  2
Storage Controller Port Count (0):      2
Storage Controller Bootable (0):        on
Storage Controller Name (1):            SATA Controller
Storage Controller Type (1):            IntelAhci
Storage Controller Instance Number (1): 0
Storage Controller Max Port Count (1):  30
Storage Controller Port Count (1):      1
Storage Controller Bootable (1):        on

~~~


## ディスク変更(VBoxManage storageattach)

~~~
Peeko:js1_default_1413703213140_69014 hide$ VBoxManage storageattach js1_default_1413703213140_69014 --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium box-disk1.vdi

~~~

- 変更されています

~~~
Peeko:js1_default_1413703213140_69014 hide$ VBoxManage showvminfo js1_default_1413703213140_69014 | GREP_OPTIONS='' grep box-disk
SATA Controller (0, 0): /Users/hide/VirtualBox VMs/js1_default_1413703213140_69014/box-disk1.vdi (UUID: 03cfdd84-2dad-4a5b-8e37-d2c13b7142f4)

~~~


# 再起動(vagrant reload)

~~~
Peeko:js1 hide$ vagrant reload
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 => 2222 (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key

    default: Warning: Connection timeout. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /Users/hide/Documents/Boxes/js1
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: to force provisioning. Provisioners marked to run always will still run.

~~~

## ssh(vagrant ssh)

~~~
Peeko:js1 hide$ vagrant ssh
Linux 10 3.14-2-amd64 #1 SMP Debian 3.14.13-2 (2014-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Oct 19 07:20:38 2014 from 10.0.2.2
~~~

# ディスクサイズを拡大

## サイズが増えていることを確認(fdisk -l)

- 32.0 GBになっています

~~~
vagrant@10:~$ sudo fdisk -l

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19818494    20764671      473089    5  Extended
/dev/sda5        19818496    20764671      473088   82  Linux swap / Solaris
~~~

## /dev/sda2と/dev/sda5の再定義(fdisk)

- fidkインタラクティブ

~~~
vagrant@10:~$ sudo su -

root@10:~# fdisk /dev/sda
~~~~~

- 削除

~~~
Command (m for help): d
Partition number (1-5): 5

Command (m for help): d
Partition number (1-5): 2


~~~

- 拡張

~~~
Command (m for help): n
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): e
Partition number (1-4, default 2): 
Using default value 2
First sector (19816448-62423039, default 19816448): 
Using default value 19816448
Last sector, +sectors or +size{K,M,G} (19816448-62423039, default 62423039): 
Using default value 62423039
~~~

- 論理

~~~
CCommand (m for help): n
Partition type:
   p   primary (1 primary, 1 extended, 2 free)
   l   logical (numbered from 5)
Select (default p): l
Adding logical partition 5
First sector (19818496-62423039, default 19818496): 
Using default value 19818496
Last sector, +sectors or +size{K,M,G} (19818496-62423039, default 62423039): +500M
~~~

~~~
Command (m for help): n
Partition type:
   p   primary (1 primary, 1 extended, 2 free)
   l   logical (numbered from 5)
Select (default p): l
Adding logical partition 6
First sector (20844544-62423039, default 20844544): 
Using default value 20844544
Last sector, +sectors or +size{K,M,G} (20844544-62423039, default 62423039): 
Using default value 62423039
~~~


- 確認

~~~
CCommand (m for help): p

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19816448    62423039    21303296    5  Extended
/dev/sda5        19818496    20842495      512000   83  Linux
/dev/sda6        20844544    62423039    20789248   83  Linux
~~~

- /dev/sda5 -> Swap

~~~
Command (m for help): t
Partition number (1-6): 5
Hex code (type L to list codes): 82
Changed system type of partition 5 to 82 (Linux swap / Solaris)
~~~

- /dev/sda6 -> LVM

~~~
Command (m for help): t
Partition number (1-6): 6
Hex code (type L to list codes): 8e
Changed system type of partition 6 to 8e (Linux LVM)
~~~

- 確認

~~~
Command (m for help): p

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19816448    62423039    21303296    5  Extended
/dev/sda5        19818496    20842495      512000   82  Linux swap / Solaris
/dev/sda6        20844544    62423039    20789248   8e  Linux LVM

~~~

- 保存

~~~
Command (m for help): wq
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.
~~~

- 再起動

~~~
root@10:~# reboot
~~~

- 確認

~~~
vagrant@10:~$ sudo fdisk -l

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19816448    62423039    21303296    5  Extended
/dev/sda5        19818496    20842495      512000   82  Linux swap / Solaris
/dev/sda6        20844544    62423039    20789248   8e  Linux LVM
~~~

# LVM 設定

## lvm2

~~~
vagrant@10:~$ sudo apt-get update
~~~
~~~
vagrant@10:~$ sudo apt-get install lvm2
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libdevmapper-event1.02.1
Suggested packages:
  thin-provisioning-tools
The following NEW packages will be installed:
  libdevmapper-event1.02.1 lvm2
0 upgraded, 2 newly installed, 0 to remove and 14 not upgraded.
Need to get 687 kB of archives.
After this operation, 1,577 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
~~~


## 物理ボリューム作成(pvcrete)

- リブート後 pvcreate で作成

~~~
root@10:~# pvcreate /dev/sda6
  Physical volume "/dev/sda6" successfully created
~~~  

- pvscan 

~~~
root@10:~# pvscan
  PV /dev/sda6         lvm2 [19.83 GiB]
  Total: 1 [19.83 GiB] / in use: 0 [0   ] / in no VG: 1 [19.83 GiB]

~~~

- pvresize 

~~~
root@10:~# pvresize /dev/sda6
  Physical volume "/dev/sda6" changed
  1 physical volume(s) resized / 0 physical volume(s) not resized
~~~

- pvdisplay

~~~
root@10:~# pvdisplay -C
  PV         VG   Fmt  Attr PSize  PFree 
  /dev/sda6       lvm2 ---  19.83g 19.83g
~~~    

~~~
root@10:~# pvdisplay /dev/sda6
  "/dev/sda6" is a new physical volume of "19.83 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sda6
  VG Name               
  PV Size               19.83 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               euY5vu-P7nh-oKn6-inQj-A2Da-SXN4-D0e1Gd
  
~~~

## ボリュームグループ作成(vgcreate)

- PE(物理エクステント)を32Mbyteで作成

~~~
root@10:~# vgcreate -s32m vg6 /dev/sda6
  /proc/devices: No entry for device-mapper found
  Volume group "vg6" successfully created

~~~  

- 確認

~~~
root@10:~# vgdisplay -C
  VG   #PV #LV #SN Attr   VSize  VFree 
  vg6    1   0   0 wz--n- 19.81g 19.81g

~~~  

~~~
root@10:~# vgdisplay vg6
  --- Volume group ---
  VG Name               vg6
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               19.81 GiB
  PE Size               32.00 MiB
  Total PE              634
  Alloc PE / Size       0 / 0   
  Free  PE / Size       634 / 19.81 GiB
  VG UUID               sCvQgt-3z0r-LjsK-3fiP-ua5J-eWjK-3ifig0
~~~

## 論理ボリューム作成(lvcreate)

- 作成

~~~
root@10:~# lvcreate -l 100%FREE -n lv6 vg6
  Logical volume "lv6" created  
~~~  


- 確認

~~~
root@10:~# lvdisplay -C
  LV   VG   Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv6  vg6  -wi-a----- 19.81g
~~~

~~~
root@10:~# lvdisplay /dev/vg6/lv6 
  --- Logical volume ---
  LV Path                /dev/vg6/lv6
  LV Name                lv6
  VG Name                vg6
  LV UUID                fm21o4-Y3id-t7S5-bxin-Q0GW-N0nK-l3c9Tk
  LV Write Access        read/write
  LV Creation host, time 10, 2014-10-19 11:52:34 +0000
  LV Status              available
  # open                 0
  LV Size                19.81 GiB
  Current LE             634
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           254:0
    
~~~

~~~
root@10:~# lvscan
  ACTIVE            '/dev/vg6/lv6' [19.81 GiB] inherit
  
~~~

## ext3ファイルシステム


~~~
root@10:~# mkfs.ext3 /dev/vg6/lv6 

mke2fs 1.42.11 (09-Jul-2014)
Creating filesystem with 5193728 4k blocks and 1299984 inodes
Filesystem UUID: 992f464f-0473-494b-8b71-6d6b65769a55
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
        4096000

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done  


~~~      


# /home移動


## /mnt/home

~~~
root@10:~# mkdir /mnt/home
root@10:~# mount /dev/vg6/lv6 /mnt/home

~~~

~~~
root@10:~# df -H
Filesystem           Size  Used Avail Use% Mounted on
/dev/sda1            9.9G  1.3G  8.2G  14% /
udev                  11M     0   11M   0% /dev
tmpfs                422M  5.6M  417M   2% /run
tmpfs                1.1G     0  1.1G   0% /dev/shm
tmpfs                1.1G     0  1.1G   0% /sys/fs/cgroup
tmpfs                5.3M     0  5.3M   0% /run/lock
tmpfs                105M     0  105M   0% /run/user
none                 500G  442G   58G  89% /vagrant
/dev/mapper/vg6-lv6   21G   47M   20G   1% /mnt/home

~~~

## コピー

- cp -ax コマンドは、/home の内容を /mnt/newpart に繰り返しコピーして、すべてのファイル属性を保存し、どのマウント・ポイントも越えたりしないようにします。

~~~
root@10:~# cd /home

root@10:/home# cp -ax * /mnt/home
~~~

~~~
root@10:/home# ls -l /mnt/home/
total 20
drwx------ 2 root    root    16384 Oct 19 05:11 lost+found
drwxr-xr-x 3 vagrant vagrant  4096 Oct 19 00:34 vagrant
~~~



## 一度 /Usersで作る

- 新しいマウントポイント

~~~
root@10:~# mkdir /Users
~~~
 
- blkid で UUID 見つける

~~~
root@10:~# blkid | grep vg6
/dev/mapper/vg6-lv6: UUID="992f464f-0473-494b-8b71-6d6b65769a55" TYPE="ext3" 
~~~

- /etc/fstab

~~~
UUID=992f464f-0473-494b-8b71-6d6b65769a55 /Users ext3 defaults 0 0
~~~

- リブート

~~~
root@10:~# reboot
~~~

- 確認

~~~
vagrant@10:~$ df -H
Filesystem           Size  Used Avail Use% Mounted on
/dev/sda1            9.9G  1.3G  8.1G  14% /
udev                  11M     0   11M   0% /dev
tmpfs                422M  5.6M  417M   2% /run
tmpfs                1.1G     0  1.1G   0% /dev/shm
tmpfs                1.1G     0  1.1G   0% /sys/fs/cgroup
tmpfs                105M     0  105M   0% /run/user
tmpfs                5.3M     0  5.3M   0% /run/lock
/dev/mapper/vg6-lv6   21G   47M   20G   1% /Users
~~~

- vipw

~~~
vagrant:x:1000:1000:Vagrant User,,,:/Users/vagrant:/bin/bash
~~~

- リブートしてssh

~~~
Peeko:js1 hide$ vagrant ssh
Linux 10 3.14-2-amd64 #1 SMP Debian 3.14.13-2 (2014-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Oct 19 12:53:45 2014 from 10.0.2.2
vagrant@10:~$ pwd
/Users/vagrant
~~~

## /home にマウントし直す

- 一応バックアップとっておく

~~~
root@10:/# mv home home.old
root@10:/# mkdir home

~~~

- /etc/fstab

~~~
UUID=992f464f-0473-494b-8b71-6d6b65769a55 /home ext3 defaults 0 0
~~~

- vipw

~~~
vagrant:x:1000:1000:Vagrant User,,,:/home/vagrant:/bin/bash
~~~

- reboot

~~~
root@10:~# reboot
~~~

- ssh し直す

~~~
Peeko:js1 hide$ vagrant ssh
Linux 10 3.14-2-amd64 #1 SMP Debian 3.14.13-2 (2014-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Oct 19 12:55:48 2014 from 10.0.2.2
~~~
~~~
vagrant@10:~$ pwd
/home/vagrant
~~~

- df

~~~
vagrant@10:~$ df -H
Filesystem           Size  Used Avail Use% Mounted on
/dev/sda1            9.9G  1.3G  8.1G  14% /
udev                  11M     0   11M   0% /dev
tmpfs                422M  5.6M  417M   2% /run
tmpfs                1.1G     0  1.1G   0% /dev/shm
tmpfs                1.1G     0  1.1G   0% /sys/fs/cgroup
tmpfs                105M     0  105M   0% /run/user
tmpfs                5.3M     0  5.3M   0% /run/lock
/dev/mapper/vg6-lv6   21G   47M   20G   1% /home
~~~

# Box化しておく

~~~
Peeko:js1 hide$ vagrant package
==> default: Attempting graceful shutdown of VM...
==> default: Clearing any previously set forwarded ports...
==> default: Exporting VM...
==> default: Compressing package to: /Users/hide/Documents/Boxes/js1/package.box
~~~

