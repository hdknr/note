## ハードディスクのパーティション情報: fdisk -l {{ device}}

~~~bash
# fdisk -l /dev/disk/by-label/cloudimg-rootfs

Disk /dev/disk/by-label/cloudimg-rootfs: 128.8 GB, 128849018880 bytes
255 heads, 63 sectors/track, 15665 cylinders, total 251658240 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/disk/by-label/cloudimg-rootfs doesn't contain a valid partition table
'
~~~
