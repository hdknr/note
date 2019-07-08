##  /etc/fstab

~~~bash
# cat /etc/fstab

LABEL=cloudimg-rootfs   /        ext4   defaults,discard        0 0
~~~

## /etc/mtab

- mount/umout コマンドで更新

~~~
cat /etc/mtab

/dev/xvda1 / ext4 rw,discard 0 0
proc /proc proc rw,noexec,nosuid,nodev 0 0
sysfs /sys sysfs rw,noexec,nosuid,nodev 0 0
none /sys/fs/cgroup tmpfs rw 0 0
none /sys/fs/fuse/connections fusectl rw 0 0
none /sys/kernel/debug debugfs rw 0 0
none /sys/kernel/security securityfs rw 0 0
udev /dev devtmpfs rw,mode=0755 0 0
devpts /dev/pts devpts rw,noexec,nosuid,gid=5,mode=0620 0 0
tmpfs /run tmpfs rw,noexec,nosuid,size=10%,mode=0755 0 0
none /run/lock tmpfs rw,noexec,nosuid,nodev,size=5242880 0 0
none /run/shm tmpfs rw,nosuid,nodev 0 0
none /run/user tmpfs rw,noexec,nosuid,nodev,size=104857600,mode=0755 0 0
none /sys/fs/pstore pstore rw 0 0
binfmt_misc /proc/sys/fs/binfmt_misc binfmt_misc rw,noexec,nosuid,nodev 0 0
systemd /sys/fs/cgroup/systemd cgroup rw,noexec,nosuid,nodev,none,name=systemd 0 0
~~~

## mount -v

~~~bash
# mount -v

/dev/xvda1 on / type ext4 (rw,discard)
proc on /proc type proc (rw,noexec,nosuid,nodev)
sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
none on /sys/fs/cgroup type tmpfs (rw)
none on /sys/fs/fuse/connections type fusectl (rw)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
udev on /dev type devtmpfs (rw,mode=0755)
devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
none on /run/shm type tmpfs (rw,nosuid,nodev)
none on /run/user type tmpfs (rw,noexec,nosuid,nodev,size=104857600,mode=0755)
none on /sys/fs/pstore type pstore (rw)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,noexec,nosuid,nodev)
systemd on /sys/fs/cgroup/systemd type cgroup (rw,noexec,nosuid,nodev,none,name=systemd)
~~~~


##  /proc/mounts

~~~bash
cat /proc/mounts

rootfs / rootfs rw 0 0
sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0
proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
udev /dev devtmpfs rw,relatime,size=289508k,nr_inodes=72377,mode=755 0 0
devpts /dev/pts devpts rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000 0 0
tmpfs /run tmpfs rw,nosuid,noexec,relatime,size=60272k,mode=755 0 0
/dev/disk/by-label/cloudimg-rootfs / ext4 rw,relatime,discard,data=ordered 0 0
none /sys/fs/cgroup tmpfs rw,relatime,size=4k,mode=755 0 0
none /sys/fs/fuse/connections fusectl rw,relatime 0 0
none /sys/kernel/debug debugfs rw,relatime 0 0
none /sys/kernel/security securityfs rw,relatime 0 0
none /run/lock tmpfs rw,nosuid,nodev,noexec,relatime,size=5120k 0 0
none /run/shm tmpfs rw,nosuid,nodev,relatime 0 0
none /run/user tmpfs rw,nosuid,nodev,noexec,relatime,size=102400k,mode=755 0 0
none /sys/fs/pstore pstore rw,relatime 0 0
binfmt_misc /proc/sys/fs/binfmt_misc binfmt_misc rw,nosuid,nodev,noexec,relatime 0 0
systemd /sys/fs/cgroup/systemd cgroup rw,nosuid,nodev,noexec,relatime,name=systemd 0 0
~~~


## df -T

~~~bash
# df -aT
Filesystem                         Type        1K-blocks    Used Available Use% Mounted on
sysfs                              sysfs               0       0         0    - /sys
proc                               proc                0       0         0    - /proc
udev                               devtmpfs       289508      12    289496   1% /dev
devpts                             devpts              0       0         0    - /dev/pts
tmpfs                              tmpfs           60272     196     60076   1% /run
/dev/disk/by-label/cloudimg-rootfs ext4        123723748 1723652 116866780   2% /
none                               tmpfs               4       0         4   0% /sys/fs/cgroup
none                               fusectl             0       0         0    - /sys/fs/fuse/connections
none                               debugfs             0       0         0    - /sys/kernel/debug
none                               securityfs          0       0         0    - /sys/kernel/security
none                               tmpfs            5120       0      5120   0% /run/lock
none                               tmpfs          301344       0    301344   0% /run/shm
none                               tmpfs          102400       0    102400   0% /run/user
none                               pstore              0       0         0    - /sys/fs/pstore
binfmt_misc                        binfmt_misc         0       0         0    - /proc/sys/fs/binfmt_misc
systemd                            cgroup              0       0         0    - /sys/fs/cgroup/systemd
~~~


## パーティションテーブル: fdisk  -l

~~~bash
# fdisk -l

Disk /dev/xvda1: 128.8 GB, 128849018880 bytes
255 heads, 63 sectors/track, 15665 cylinders, total 251658240 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/xvda1 doesn't contain a valid partition table
'
~~~

## カーネルが認識しているパーティションテーブル: /proc/partitions

~~~
# cat /proc/partitions
major minor  #blocks  name

 202        1  125829120 xvda1
~~~


## カーネルが利用可能なファイルシステム : /proc/filesystem

~~~bash
# cat /proc/filesystems
nodev   sysfs
nodev   rootfs
nodev   ramfs
nodev   bdev
nodev   proc
nodev   cgroup
nodev   cpuset
nodev   tmpfs
nodev   devtmpfs
nodev   debugfs
nodev   securityfs
nodev   sockfs
nodev   pipefs
nodev   anon_inodefs
nodev   devpts
        ext3
        ext2
        ext4
nodev   hugetlbfs
        vfat
nodev   ecryptfs
        fuseblk
nodev   fuse
nodev   fusectl
nodev   pstore
nodev   mqueue
        iso9660
nodev   binfmt_misc
~~~

##  ファイルシステムのパラメータ: /sbin/tune2fs -l

~~~bash
# /sbin/tune2fs -l  /dev/disk/by-label/cloudimg-rootfs
tune2fs 1.42.9 (4-Feb-2014)
Filesystem volume name:   cloudimg-rootfs
Last mounted on:          /
Filesystem UUID:          65977fbb-0696-4828-b4df-66f9cfa7bbc0
Filesystem magic number:  0xEF53
Filesystem revision #:    1 (dynamic)
Filesystem features:      has_journal ext_attr resize_inode dir_index filetype needs_recovery extent flex_bg sparse_super large_file huge_file uninit_bg dir_nlink extra_isize
Filesystem flags:         signed_directory_hash
Default mount options:    user_xattr acl
Filesystem state:         clean
Errors behavior:          Continue
Filesystem OS type:       Linux
Inode count:              7864320
Block count:              31457280
Reserved block count:     1279233
Free blocks:              30500113
Free inodes:              7762609
First block:              0
Block size:               4096
Fragment size:            4096
Reserved GDT blocks:      504
Blocks per group:         32768
Fragments per group:      32768
Inodes per group:         8192
Inode blocks per group:   512
Flex block group size:    16
Filesystem created:       Wed Mar 25 15:53:02 2015
Last mount time:          Wed Feb 24 10:30:14 2016
Last write time:          Wed Mar 25 15:53:44 2015
Mount count:              5
Maximum mount count:      -1
Last checked:             Wed Mar 25 15:53:02 2015
Check interval:           0 (<none>)
Lifetime writes:          1133 MB
Reserved blocks uid:      0 (user root)
Reserved blocks gid:      0 (group root)
First inode:              11
Inode size:               256
Required extra isize:     28
Desired extra isize:      28
Journal inode:            8
Default directory hash:   half_md4
Directory Hash Seed:      1be9be8f-ddec-4da2-bbee-92bf0534e50b
Journal backup:           inode blocks
~~~

## ドライブのパラメータ:  hdparm -v

~~~bash
#  hdparm -v   /dev/disk/by-label/cloudimg-rootfs

/dev/disk/by-label/cloudimg-rootfs:
 HDIO_DRIVE_CMD(identify) failed: Invalid argument
 readonly      =  0 (off)
 readahead     = 256 (on)
 geometry      = 15665/255/63, sectors = 251658240, start = 0
~~~
