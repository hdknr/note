- うまく行っていない...

# VMDK -> VDI (VBoxManage clonehd)

~~~
Peeko:~ hide$ cd ~/VirtualBox\ VMs/jssie1_default_1413678798477_55336/
~~~

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ ls -al
total 1426392
drwx------+  6 hide staff        204 10 19 09:53 .
drwxr-xr-x+ 14 hide staff        476 10 19 09:33 ..
drwx------+  4 hide staff        136 10 19 09:53 Logs
-rw-------+  2 hide staff 1460600832 10 19 10:17 box-disk1.vmdk
-rw-------+  1 hide staff       9227 10 19 09:53 jssie1_default_1413678798477_55336.vbox
-rw-------+  1 hide staff       9226 10 19 09:53 jssie1_default_1413678798477_55336.vbox-prev
~~~

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ VBoxManage clonehd box-disk1.vmdk box-disk1.vdi --format VDI

0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Clone hard disk created in format 'VDI'. UUID: 0976d403-5b1c-46e6-9a98-b08028d2ee99
~~~

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ ls -al
total 3318744
drwx------+  7 hide staff        238 10 19 10:21 .
drwxr-xr-x+ 14 hide staff        476 10 19 09:33 ..
drwx------+  4 hide staff        136 10 19 09:53 Logs
-rw-------+  1 hide staff 1937768448 10 19 10:21 box-disk1.vdi
-rw-------+  2 hide staff 1460600832 10 19 10:20 box-disk1.vmdk
-rw-------+  1 hide staff       9227 10 19 10:21 jssie1_default_1413678798477_55336.vbox
-rw-------+  1 hide staff       9227 10 19 10:20 jssie1_default_1413678798477_55336.vbox-prev
~~~

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ VBoxManage modifyhd box-disk1.vdi --resize 30480
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
~~~

## VDIの内容(VboxManage showhdinfo)

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ VboxManage showhdinfo  box-disk1.vdi

UUID:           0976d403-5b1c-46e6-9a98-b08028d2ee99
Parent UUID:    base
State:          created
Type:           normal (base)
Location:       /Users/hide/VirtualBox VMs/jssie1_default_1413678798477_55336/box-disk1.vdi
Storage format: VDI
Format variant: dynamic default
Capacity:       30480 MBytes
Size on disk:   1848 MBytes

~~~

## VM一覧(VBoxManage list vms)

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ VBoxManage  list vms

"SQZ" {e4a545b2-947d-4e11-9661-5bbb7cd58708}
"Wzy" {11b93b36-8bd5-4eb0-9f99-c058b47362df}
"Ubu" {d81e3ff2-5c79-4200-9e6a-465df999cec5}
"Ubu2" {a34a6016-98be-4365-a4e1-63dc50d97611}
"Ubu3" {4805e250-cbd4-413f-9d7a-55fe9a931e8c}
"Google Nexus 4 - 4.3 - API 18 - 768x1280" {01d925db-4bf5-4d0e-8ca0-321987c8c3a1}
"Google Nexus 10 - 4.3 - API 18 - 2560x1600" {43d543d9-1fab-4f28-9152-b0d07819ef7a}
"IE11 - Win8.1" {f1328962-97d7-4824-bbe5-ea755b5f9c12}
"jssie1_default_1413678798477_55336" {357d560e-d9cf-436b-973d-22ba75be0322}
~~~

## ストレージコントローラ確認(VBoxManage showvminfo)

~~~
Peeko:jssie1_default_1413678798477_55336 hide$ VBoxManage showvminfo jssie1_default_1413678798477_55336 | GREP_OPTIONS='' grep "Storage"

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
Peeko:jssie1_default_1413678798477_55336 hide$ VBoxManage storageattach jssie1_default_1413678798477_55336 --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium box-disk1.vdi
~~~

- 変更されています

~~~
Peeko:jssie1 hide$ VBoxManage showvminfo jssie1_default_1413678798477_55336 | GREP_OPTIONS='' grep box-disk

SATA Controller (0, 0): /Users/hide/VirtualBox VMs/jssie1_default_1413678798477_55336/box-disk1.vdi (UUID: 0976d403-5b1c-46e6-9a98-b08028d2ee99)
~~~


# 再起動(vagrant reload)

~~~
Peeko:jssie1 hide$ vagrant reload
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
    default: /vagrant => /Users/hide/Documents/Boxes/jssie1
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: to force provisioning. Provisioners marked to run always will still run.
~~~

## ssh(vagrant ssh)

~~~
Peeko:jssie1 hide$ vagrant ssh
Linux 10 3.14-2-amd64 #1 SMP Debian 3.14.13-2 (2014-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Oct 19 00:54:02 2014 from 10.0.2.2
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
vagrant@10:~$ sudo fdisk /dev/sda
~~~

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
Command (m for help): n
Partition type:
   p   primary (1 primary, 1 extended, 2 free)
   l   logical (numbered from 5)
Select (default p): l
Adding logical partition 5
First sector (19818496-62423039, default 19818496): 
Using default value 19818496
Last sector, +sectors or +size{K,M,G} (19818496-62423039, default 62423039): 
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
/dev/sda5        19818496    62423039    21302272   83  Linux
~~~

- /dev/sda5 -> LVM

~~~
Command (m for help): t
Partition number (1-5): 5
Hex code (type L to list codes): 8e
Changed system type of partition 5 to 8e (Linux LVM)

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
/dev/sda5        19818496    62423039    21302272   8e  Linux LVM
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
vagrant@10:~$ sudo shutdown -r now
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
/dev/sda5        19818496    62423039    21302272   8e  Linux LVM
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

## ボリューム無い？

~~~
vagrant@10:~$ sudo pvscan
  No matching physical volumes found
~~~

~~~
vagrant@10:~$ sudo lvscan
  No volume groups found
~~~

~~~
root@10:~# pvs --all
  PV         VG   Fmt Attr PSize PFree
  /dev/sda1           ---     0     0 
  /dev/sda5           ---     0     0 
~~~

# 作り直し

~~~
root@10:~# fdisk /dev/sda
~~~

~~~
Command (m for help): n
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): p
Partition number (1-4, default 2): 
Using default value 2
First sector (19816448-62423039, default 19816448): 
Using default value 19816448
Last sector, +sectors or +size{K,M,G} (19816448-62423039, default 62423039): 
Using default value 62423039

Command (m for help): p

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19816448    62423039    21303296   83  Linux
~~~

~~~
Command (m for help): t
Partition number (1-4): 2
Hex code (type L to list codes): 8e
Changed system type of partition 2 to 8e (Linux LVM)

Command (m for help): p

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19816448    62423039    21303296   8e  Linux LVM
~~~

~~~
Command (m for help): wq
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.
~~~

## 物理ボリューム作成(pvcrete)

- リブート後 pvcreate で作成

~~~
root@10:/var/log# pvcreate /dev/sda2
  Physical volume "/dev/sda2" successfully created
~~~  

- pvscan 

~~~
root@10:/var/log# pvscan
  PV /dev/sda2         lvm2 [20.32 GiB]
  Total: 1 [20.32 GiB] / in use: 0 [0   ] / in no VG: 1 [20.32 GiB]
~~~

~~~
root@10:/var/log# fdisk -l

Disk /dev/sda: 32.0 GB, 31960596480 bytes
255 heads, 63 sectors/track, 3885 cylinders, total 62423040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x5cdfd35b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    19816447     9907200   83  Linux
/dev/sda2        19816448    62423039    21303296   8e  Linux LVM
~~~

- pvresize 

~~~
root@10:/var/log# pvresize /dev/sda2 
  Physical volume "/dev/sda2" changed
  1 physical volume(s) resized / 0 physical volume(s) not resized
~~~

- pvdisplay

~~~
root@10:/var/log# pvdisplay -C
  PV         VG   Fmt  Attr PSize  PFree 
  /dev/sda2       lvm2 ---  20.32g 20.32g
~~~    

~~~
root@10:/var/log# pvdisplay /dev/sda2
  "/dev/sda2" is a new physical volume of "20.32 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sda2
  VG Name               
  PV Size               20.32 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               kLMMR5-UXuL-fV9m-sSIr-HfhV-2d0J-Ztxs2v
~~~

## ボリュームグループ作成(vgcreate)

- PE(物理エクステント)を32Mbyteで作成

~~~
root@10:/var/log# vgcreate -s32m vg2 /dev/sda2

  Volume group "vg2" successfully created
~~~  

- 確認

~~~
root@10:/var/log# vgdisplay -C

  VG   #PV #LV #SN Attr   VSize  VFree 
  vg2    1   0   0 wz--n- 20.31g 20.31g
~~~  

~~~
root@10:/var/log# vgdisplay vg2

  --- Volume group ---
  VG Name               vg2
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
  VG Size               20.31 GiB
  PE Size               32.00 MiB
  Total PE              650
  Alloc PE / Size       0 / 0   
  Free  PE / Size       650 / 20.31 GiB
  VG UUID               2qY3tI-IJV7-BzlW-3AHo-IQNB-PKSW-QrGWfu
~~~

## 論理ボリューム作成(lvcreate)
- 作成

~~~
root@10:/var/log# lvcreate -l 100%FREE -n lv2 vg2
WARNING: swap signature detected on /dev/vg2/lv2. Wipe it? [y/n]: n
  Aborted wiping of swap signature.
  Logical volume "lv2" created
~~~  


- 確認

~~~
root@10:/var/log# lvdisplay -C
  LV   VG   Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv2  vg2  -wi-a----- 20.31g   
~~~

~~~
root@10:/var/log# lvdisplay /dev/vg2/lv2 
  --- Logical volume ---
  LV Path                /dev/vg2/lv2
  LV Name                lv2
  VG Name                vg2
  LV UUID                Mkg0Ao-PbDR-qJjD-uGao-LfN3-0Epu-KUMF3N
  LV Write Access        read/write
  LV Creation host, time 10, 2014-10-19 04:59:18 +0000
  LV Status              available
  # open                 0
  LV Size                20.31 GiB
  Current LE             650
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           254:0
~~~

~~~
root@10:/var/log# lvscan
  ACTIVE            '/dev/vg2/lv2' [20.31 GiB] inherit
~~~

# ext3ファイルシステム


~~~
root@10:~# mkfs.ext3  /dev/vg2/lv2 

mke2fs 1.42.11 (09-Jul-2014)
Creating filesystem with 5324800 4k blocks and 1332688 inodes
Filesystem UUID: 5f27b5dc-1afc-477a-a936-02526263c722
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
root@10:~# mount /dev/vg2/lv2 /mnt/home/
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
/dev/mapper/vg2-lv2   22G   47M   21G   1% /mnt/home
~~~

## コピー

- cp -ax コマンドは、/home の内容を /mnt/newpart に繰り返しコピーして、すべてのファイル属性を保存し、どのマウント・ポイントも越えたりしないようにします。

~~~
root@10:/home# cp -ax * /mnt/home
~~~

~~~
root@10:/home# ls -l /mnt/home/
total 20
drwx------ 2 root    root    16384 Oct 19 05:11 lost+found
drwxr-xr-x 3 vagrant vagrant  4096 Oct 19 00:34 vagrant
~~~


## /etc/fstab

~~~
root@10:/# more /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=709046e9-c297-4dd7-8e6a-757c2a821a32 /               ext3    errors=remount-ro 0       1
# swap was on /dev/sda5 during installation
UUID=483004ef-568a-4d50-92a4-a6b15d431d1d none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0
/dev/sr1        /media/cdrom1   udf,iso9660 user,noauto     0       0
/dev/lv2/vg2    /home 1 2
~~~

~~~
root@10:/# mv /home/ /home.old
root@10:/# mkdir /home
~~~