~~~~
Xen Minimal OS!
  start_info: 0xae2000(VA)
    nr_pages: 0x26700
  shared_inf: 0x7de11000(MA)
     pt_base: 0xae5000(VA)
nr_pt_frames: 0x9
    mfn_list: 0x9ae000(VA)
   mod_start: 0x0(VA)
     mod_len: 0
       flags: 0x0
    cmd_line: root=/dev/sda1 ro 4
  stack:      0x96d840-0x98d840
MM: Init
      _text: 0x0(VA)
     _etext: 0x7dc7d(VA)
   _erodata: 0x9a000(VA)
     _edata: 0x9fce0(VA)
stack start: 0x96d840(VA)
       _end: 0x9ade40(VA)
  start_pfn: af1
    max_pfn: 26700
Mapping memory range 0xc00000 - 0x26700000
setting 0x0-0x9a000 readonly
skipped 0x1000
MM: Initialise page allocator for c1f000(c1f000)-26700000(26700000)
MM: done
Demand map pfns at 26701000-2026701000.
Heap resides at 2026702000-4026702000.
Initialising timer interface
Initialising console ... done.
gnttab_table mapped at 0x26701000.
Initialising scheduler
Thread "Idle": pointer: 0x2026702050, stack: 0x26660000
Thread "xenstore": pointer: 0x2026702800, stack: 0x26670000
xenbus initialised on irq 1 mfn 0xf572f9
Thread "shutdown": pointer: 0x2026702fb0, stack: 0x26680000
Dummy main: start_info=0x98d940
Thread "main": pointer: 0x2026703760, stack: 0x26690000
"main" "root=/dev/sda1" "ro" "4"
vbd 2049 is hd0
******************* BLKFRONT for device/vbd/2049 **********


backend at /local/domain/0/backend/vbd/7090/2049
Failed to read /local/domain/0/backend/vbd/7090/2049/feature-barrier.
Failed to read /local/domain/0/backend/vbd/7090/2049/feature-flush-cache.
251658240 sectors of 512 bytes
**************************
vbd 2128 is hd1
******************* BLKFRONT for device/vbd/2128 **********


backend at /local/domain/0/backend/vbd/7090/2128
Failed to read /local/domain/0/backend/vbd/7090/2128/feature-barrier.
Failed to read /local/domain/0/backend/vbd/7090/2128/feature-flush-cache.
209715200 sectors of 512 bytes
**************************
[H[J  Booting 'Ubuntu 14.04.2 LTS, kernel 3.13.0-48-generic'

root  (hd0)
 Filesystem type is ext2fs, using whole disk
kernel  /boot/vmlinuz-3.13.0-48-generic root=LABEL=cloudimg-rootfs ro console=h
vc0
initrd  /boot/initrd.img-3.13.0-48-generic

============= Init TPM Front ================
Tpmfront:Error Unable to read device/vtpm/0/backend-id during tpmfront initialization! error = ENOENT
Tpmfront:Info Shutting down tpmfront
close blk: backend=/local/domain/0/backend/vbd/7090/2049 node=device/vbd/2049
close blk: backend=/local/domain/0/backend/vbd/7090/2128 node=device/vbd/2128
[    0.000000] Initializing cgroup subsys cpuset
[    0.000000] Initializing cgroup subsys cpu
[    0.000000] Initializing cgroup subsys cpuacct
[    0.000000] Linux version 3.13.0-48-generic (buildd@orlo) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #80-Ubuntu SMP Thu Mar 12 11:16:15 UTC 2015 (Ubuntu 3.13.0-48.80-generic 3.13.11-ckt16)
[    0.000000] Command line: root=LABEL=cloudimg-rootfs ro console=hvc0
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] ACPI in unprivileged domain disabled
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] Xen: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] Xen: [mem 0x00000000000a0000-0x00000000000fffff] reserved
[    0.000000] Xen: [mem 0x0000000000100000-0x0000000026efffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] DMI not present or invalid.
[    0.000000] No AGP bridge found
[    0.000000] e820: last_pfn = 0x26f00 max_arch_pfn = 0x400000000
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] init_memory_mapping: [mem 0x00000000-0x000fffff]
[    0.000000] init_memory_mapping: [mem 0x26400000-0x265fffff]
[    0.000000] init_memory_mapping: [mem 0x24000000-0x263fffff]
[    0.000000] init_memory_mapping: [mem 0x00100000-0x23ffffff]
[    0.000000] init_memory_mapping: [mem 0x26600000-0x26efffff]
[    0.000000] RAMDISK: [mem 0x02403000-0x03860fff]
[    0.000000] NUMA turned off
[    0.000000] Faking a node at [mem 0x0000000000000000-0x0000000026efffff]
[    0.000000] Initmem setup node 0 [mem 0x00000000-0x26efffff]
[    0.000000]   NODE_DATA [mem 0x266fb000-0x266fffff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x00001000-0x00ffffff]
[    0.000000]   DMA32    [mem 0x01000000-0xffffffff]
[    0.000000]   Normal   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x00001000-0x0009ffff]
[    0.000000]   node   0: [mem 0x00100000-0x26efffff]
[    0.000000] SFI: Simple Firmware Interface v0.81 http://simplefirmware.org
[    0.000000] smpboot: Allowing 1 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.000000] e820: [mem 0x26f00000-0xffffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on Xen
[    0.000000] Xen version: 3.4.3.amazon (preserve-AD)
[    0.000000] setup_percpu: NR_CPUS:256 nr_cpumask_bits:256 nr_cpu_ids:1 nr_node_ids:1
[    0.000000] PERCPU: Embedded 28 pages/cpu @ffff880026000000 s82368 r8192 d24128 u2097152
[10831492.013407] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 156878
[10831492.013409] Policy zone: DMA32
[10831492.013412] Kernel command line: root=LABEL=cloudimg-rootfs ro console=hvc0
[10831492.015079] PID hash table entries: 4096 (order: 3, 32768 bytes)
[10831492.015128] Checking aperture...
[10831492.024381] No AGP bridge found
[10831492.027252] Memory: 578984K/637564K available (7385K kernel code, 1145K rwdata, 3408K rodata, 1336K init, 1444K bss, 58580K reserved)
[10831492.027357] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[10831492.027381] Hierarchical RCU implementation.
[10831492.027383] 	RCU dyntick-idle grace-period acceleration is enabled.
[10831492.027384] 	RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=1.
[10831492.027385] 	Offload RCU callbacks from all CPUs
[10831492.027388] 	Offload RCU callbacks from CPUs: 0.
[10831492.027398] NR_IRQS:16640 nr_irqs:256 16
[10831492.027553] Console: colour dummy device 80x25
[10831492.027679] console [tty0] enabled
[10831492.027888] console [hvc0] enabled
[10831492.028321] allocated 2621440 bytes of page_cgroup
[10831492.028328] please try 'cgroup_disable=memory' option if you don't want memory cgroups
[10831492.028371] installing Xen timer for CPU 0
[10831492.028414] tsc: Detected 1795.672 MHz processor
[10831492.028424] Calibrating delay loop (skipped), value calculated using timer frequency.. 3591.34 BogoMIPS (lpj=7182688)
[10831492.028434] pid_max: default: 32768 minimum: 301
[10831492.028748] Security Framework initialized
[10831492.028785] AppArmor: AppArmor initialized
[10831492.028790] Yama: becoming mindful.
[10831492.029101] Dentry cache hash table entries: 131072 (order: 8, 1048576 bytes)
[10831492.029438] Inode-cache hash table entries: 65536 (order: 7, 524288 bytes)
[10831492.029575] Mount-cache hash table entries: 2048 (order: 2, 16384 bytes)
[10831492.029590] Mountpoint-cache hash table entries: 2048 (order: 2, 16384 bytes)
[10831492.029903] Initializing cgroup subsys memory
[10831492.029919] Initializing cgroup subsys devices
[10831492.029925] Initializing cgroup subsys freezer
[10831492.029930] Initializing cgroup subsys blkio
[10831492.029935] Initializing cgroup subsys perf_event
[10831492.029941] Initializing cgroup subsys hugetlb
[10831492.030020] CPU: Physical Processor ID: 0
[10831492.030026] CPU: Processor Core ID: 7
[10831492.030037] Last level iTLB entries: 4KB 512, 2MB 0, 4MB 0
[10831492.030037] Last level dTLB entries: 4KB 512, 2MB 32, 4MB 32
[10831492.030037] tlb_flushall_shift: 5
[10831492.168083] Freeing SMP alternatives memory: 32K (ffffffff81e6e000 - ffffffff81e76000)
[10831492.170140] ftrace: allocating 28562 entries in 112 pages
[10831492.190624] cpu 0 spinlock event irq 17
[10831492.204656] Performance Events: unsupported p6 CPU model 45 no PMU driver, software events only.
[10831492.206616] x86: Booted up 1 node, 1 CPUs
[10831492.206695] NMI watchdog: disabled (cpu0): hardware events not enabled
[10831492.206799] devtmpfs: initialized
[10831492.211384] EVM: security.selinux
[10831492.211391] EVM: security.SMACK64
[10831492.211395] EVM: security.ima
[10831492.211398] EVM: security.capability
[10831492.212534] pinctrl core: initialized pinctrl subsystem
[10831492.212571] xen:grant_table: Grant tables using version 1 layout
[10831492.212588] Grant table initialized
[10831492.212639] regulator-dummy: no parameters
[10831492.232512] RTC time: 165:165:165, date: 165/165/65
[10831492.232569] NET: Registered protocol family 16
[10831492.233726] PCI: setting up Xen PCI frontend stub
[10831492.234675] bio: create slab <bio-0> at 0
[10831492.234835] ACPI: Interpreter disabled.
[10831492.234850] xen:balloon: Initialising balloon driver
[10831492.235898] xen_balloon: Initialising balloon driver
[10831492.236103] vgaarb: loaded
[10831492.236313] SCSI subsystem initialized
[10831492.236410] usbcore: registered new interface driver usbfs
[10831492.236426] usbcore: registered new interface driver hub
[10831492.236453] usbcore: registered new device driver usb
[10831492.236572] PCI: System does not support PCI
[10831492.236580] PCI: System does not support PCI
[10831492.236674] NetLabel: Initializing
[10831492.236681] NetLabel:  domain hash size = 128
[10831492.236685] NetLabel:  protocols = UNLABELED CIPSOv4
[10831492.236704] NetLabel:  unlabeled traffic allowed by default
[10831492.236785] Switched to clocksource xen
[10831492.242529] AppArmor: AppArmor Filesystem Enabled
[10831492.242556] pnp: PnP ACPI: disabled
[10831492.244175] NET: Registered protocol family 2
[10831492.244398] TCP established hash table entries: 8192 (order: 4, 65536 bytes)
[10831492.244463] TCP bind hash table entries: 8192 (order: 5, 131072 bytes)
[10831492.244497] TCP: Hash tables configured (established 8192 bind 8192)
[10831492.244542] TCP: reno registered
[10831492.244552] UDP hash table entries: 512 (order: 2, 16384 bytes)
[10831492.244565] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
[10831492.244626] NET: Registered protocol family 1
[10831492.244705] Trying to unpack rootfs image as initramfs...
[10831492.272878] Freeing initrd memory: 20856K (ffff880002403000 - ffff880003861000)
[10831492.273037] platform rtc_cmos: registered platform RTC device (no PNP device found)
[10831492.273128] microcode: CPU0 sig=0x206d7, pf=0x1, revision=0x70d
[10831492.273189] microcode: Microcode Update Driver: v2.00 <tigran@aivazian.fsnet.co.uk>, Peter Oruba
[10831492.273197] Scanning for low memory corruption every 60 seconds
[10831492.273492] Initialise system trusted keyring
[10831492.273561] audit: initializing netlink socket (disabled)
[10831492.273584] type=2000 audit(1456305653.763:1): initialized
[10831492.308480] HugeTLB registered 2 MB page size, pre-allocated 0 pages
[10831492.309534] zbud: loaded
[10831492.309735] VFS: Disk quotas dquot_6.5.2
[10831492.309786] Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[10831492.310272] fuse init (API version 7.22)
[10831492.310354] msgmni has been set to 1171
[10831492.310419] Key type big_key registered
[10831492.310691] Key type asymmetric registered
[10831492.310697] Asymmetric key parser 'x509' registered
[10831492.310737] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
[10831492.310775] io scheduler noop registered
[10831492.310780] io scheduler deadline registered (default)
[10831492.310809] io scheduler cfq registered
[10831492.310869] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
[10831492.310889] pciehp: PCI Express Hot Plug Controller Driver version: 0.4
[10831492.369011] ipmi message handler version 39.2
[10831492.369360] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[10831492.370471] Linux agpgart interface v0.103
[10831492.371729] brd: module loaded
[10831492.372399] loop: module loaded
[10831492.390236] blkfront: xvda1: barrier or flush: disabled; persistent grants: disabled; indirect descriptors: disabled;
[10831492.399581] libphy: Fixed MDIO Bus: probed
[10831492.399684] tun: Universal TUN/TAP device driver, 1.6
[10831492.399690] tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
[10831492.399745] PPP generic driver version 2.4.2
[10831492.399785] xen_netfront: Initialising Xen virtual ethernet driver
[10831492.401495] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[10831492.401508] ehci-pci: EHCI PCI platform driver
[10831492.401521] ehci-platform: EHCI generic platform driver
[10831492.401547] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[10831492.401556] ohci-pci: OHCI PCI platform driver
[10831492.401573] ohci-platform: OHCI generic platform driver
[10831492.401587] uhci_hcd: USB Universal Host Controller Interface driver
[10831492.401644] i8042: PNP: No PS/2 controller found. Probing ports directly.
[10831493.407564] i8042: No controller found
[10831493.407807] mousedev: PS/2 mouse device common for all mice
[10831493.467566] rtc_cmos rtc_cmos: rtc core: registered rtc_cmos as rtc0
[10831493.467647] rtc_cmos: probe of rtc_cmos failed with error -38
[10831493.467748] device-mapper: uevent: version 1.0.3
[10831493.467835] device-mapper: ioctl: 4.27.0-ioctl (2013-10-30) initialised: dm-devel@redhat.com
[10831493.467848] ledtrig-cpu: registered to indicate activity on CPUs
[10831493.467988] TCP: cubic registered
[10831493.468093] NET: Registered protocol family 10
[10831493.468348] NET: Registered protocol family 17
[10831493.468369] Key type dns_resolver registered
[10831493.468498] Loading compiled-in X.509 certificates
[10831493.469775] Loaded X.509 cert 'Magrathea: Glacier signing key: 4eb2de249917cbf39cb85692e54cebade594d680'
[10831493.469803] registered taskstats version 1
[10831493.474194] Key type trusted registered
[10831493.482099] Key type encrypted registered
[10831493.482112] AppArmor: AppArmor sha1 policy hashing enabled
[10831493.482119] IMA: No TPM chip found, activating TPM-bypass!
[10831493.514120] blkfront: xvdf: barrier or flush: disabled; persistent grants: disabled; indirect descriptors: disabled;
[10831493.591970]  xvdf: xvdf1
[10831493.680840] regulator-dummy: incomplete constraints, leaving on
[10831493.680922]   Magic number: 1:252:3141
[10831493.680971] /build/buildd/linux-3.13.0/drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
[10831493.681027] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[10831493.681033] EDD information not available.
[10831493.682004] Freeing unused kernel memory: 1336K (ffffffff81d20000 - ffffffff81e6e000)
[10831493.682014] Write protecting the kernel read-only data: 12288k
[10831493.686660] Freeing unused kernel memory: 796K (ffff880001739000 - ffff880001800000)
[10831493.687141] Freeing unused kernel memory: 688K (ffff880001b54000 - ffff880001c00000)
Loading, please wait...
[10831493.727944] systemd-udevd[94]: starting version 204
Begin: Loading essential drivers ... done.
Begin: Running /scripts/init-premount ... done.
Begin: Mounting root file system ... Begin: Running /scripts/local-top ... done.
Begin: Running /scripts/local-premount ... done.
[10831495.630833] EXT4-fs (xvda1): INFO: recovery required on readonly filesystem
[10831495.630846] EXT4-fs (xvda1): write access will be enabled during recovery
[10831497.270015] random: nonblocking pool is initialized
[10831503.956235] EXT4-fs (xvda1): orphan cleanup on readonly fs
[10831504.643324] EXT4-fs (xvda1): 10 orphan inodes deleted
[10831504.643338] EXT4-fs (xvda1): recovery complete
[10831504.677510] EXT4-fs (xvda1): mounted filesystem with ordered data mode. Opts: (null)
Begin: Running /scripts/local-bottom ... done.
done.
Begin: Running /scripts/init-bottom ... done.
 * Stopping adjust system clock and timezone[74G[ OK ]
 * Starting Mount filesystems on boot[74G[ OK ]
 * Starting Fix-up sensitive /proc filesystem entries[74G[ OK ]
 * Starting Populate /dev filesystem[74G[ OK ]
 * Starting Populate and link to /run filesystem[74G[ OK ]
 * Stopping Fix-up sensitive /proc filesystem entries[74G[ OK ]
 * Stopping Populate /dev filesystem[74G[ OK ]
 * Stopping Populate and link to /run filesystem[74G[ OK ]
 * Stopping Track if upstart is running in a container[74G[ OK ]
[10831516.553269] EXT4-fs (xvda1): re-mounted. Opts: discard
 * Starting Signal sysvinit that the rootfs is mounted[74G[ OK ]
 * Starting Clean /tmp directory[74G[ OK ]
 * Starting Initialize or finalize resolvconf[74G[ OK ]
 * Stopping Clean /tmp directory[74G[ OK ]
[10831523.931348] EXT4-fs (xvdf1): mounted filesystem with ordered data mode. Opts: (null)
 * Stopping Read required files in advance (for other mountpoints)[74G[ OK ]
Cloud-init v. 0.7.5 running 'init-local' at Wed, 24 Feb 2016 09:21:29 +0000. Up 36.24 seconds.
cloud-init-nonet[39.28]: waiting 10 seconds for network device
 * Starting Signal sysvinit that virtual filesystems are mounted[74G[ OK ]
 * Starting Signal sysvinit that virtual filesystems are mounted[74G[ OK ]
 * Starting Bridge udev events into upstart[74G[ OK ]
 * Starting Signal sysvinit that remote filesystems are mounted[74G[ OK ]
 * Starting device node and kernel event manager[74G[ OK ]
 * Starting load modules from /etc/modules[74G[ OK ]
 * Starting cold plug devices[74G[ OK ]
 * Starting log initial device creation[74G[ OK ]
 * Stopping load modules from /etc/modules[74G[ OK ]
 * Starting Uncomplicated firewall[74G[ OK ]
 * Starting configure network device security[74G[ OK ]
 * Starting configure network device security[74G[ OK ]
 * Starting Mount network filesystems[74G[ OK ]
 * Stopping Mount network filesystems[74G[ OK ]
 * Starting Bridge socket events into upstart[74G[ OK ]
 * Starting configure network device[74G[ OK ]
 * Starting Mount network filesystems[74G[ OK ]
 * Stopping Mount network filesystems[74G[ OK ]
 * Starting configure network device[74G[ OK ]
cloud-init-nonet[43.72]: static networking is now up
Cloud-init v. 0.7.5 running 'init' at Wed, 24 Feb 2016 09:21:37 +0000. Up 44.12 seconds.
 * Stopping cold plug devices[74G[ OK ]
ci-info: ++++++++++++++++++++++++++Net device info+++++++++++++++++++++++++++
ci-info: +--------+------+--------------+---------------+-------------------+
ci-info: | Device |  Up  |   Address    |      Mask     |     Hw-Address    |
ci-info: +--------+------+--------------+---------------+-------------------+
ci-info: |   lo   | True |  127.0.0.1   |   255.0.0.0   |         .         |
ci-info: |  eth0  | True | 172.31.12.39 | 255.255.240.0 | 0a:57:5c:34:4e:fd |
ci-info: +--------+------+--------------+---------------+-------------------+
ci-info: +++++++++++++++++++++++++++++++Route info+++++++++++++++++++++++++++++++
ci-info: +-------+-------------+------------+---------------+-----------+-------+
ci-info: | Route | Destination |  Gateway   |    Genmask    | Interface | Flags |
ci-info: +-------+-------------+------------+---------------+-----------+-------+
ci-info: |   0   |   0.0.0.0   | 171.32.0.1 |    0.0.0.0    |    eth0   |   UG  |
ci-info: |   1   |  171.32.0.0 |  0.0.0.0   | 255.255.240.0 |    eth0   |   U   |
ci-info: +-------+-------------+------------+---------------+-----------+-------+
 * Stopping log initial device creation[74G[ OK ]
 * Starting enable remaining boot-time encrypted block devices[74G[ OK ]
Generating public/private rsa key pair.
Your identification has been saved in /etc/ssh/ssh_host_rsa_key.
Your public key has been saved in /etc/ssh/ssh_host_rsa_key.pub.
The key fingerprint is:
d1:ff:8e:fc:22:82:66:d7:de:84:67:0c:3f:b0:89:a1 root@ip-171-32-13-40
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|         .       |
|        . .      |
|         . .     |
|        S o .    |
|       . o O .   |
|      E...+ B .  |
|      + o o*.+   |
|     o . o..+oo  |
+-----------------+
Generating public/private dsa key pair.
Your identification has been saved in /etc/ssh/ssh_host_dsa_key.
Your public key has been saved in /etc/ssh/ssh_host_dsa_key.pub.
The key fingerprint is:
8e:fd:67:e4:a9:5a:9b:a7:c3:b2:04:de:8f:88:19:c2 root@ip-171-32-13-40
The key's randomart image is:
+--[ DSA 1024]----+
|                 |
|                 |
|                 |
|                 |
|      . S        |
| .   . *    .    |
|  E . o =..o .   |
|   . + o.=oo*    |
|    o . ++BB     |
+-----------------+
Generating public/private ecdsa key pair.
Your identification has been saved in /etc/ssh/ssh_host_ecdsa_key.
Your public key has been saved in /etc/ssh/ssh_host_ecdsa_key.pub.
The key fingerprint is:
eb:e8:cc:8b:3c:3d:ed:0c:f5:02:31:75:07:c1:00:10 root@ip-171-32-13-40
The key's randomart image is:
+--[ECDSA  256]---+
|    Eo..oo+o.    |
|       . ...     |
|      o          |
|       o         |
|      . S        |
|       o o       |
|     ...o .      |
|   ..+o=..       |
|    oo*++        |
+-----------------+
Generating public/private ed25519 key pair.
Your identification has been saved in /etc/ssh/ssh_host_ed25519_key.
Your public key has been saved in /etc/ssh/ssh_host_ed25519_key.pub.
The key fingerprint is:
70:19:b8:7b:23:68:0a:c2:1c:8d:0a:04:dc:52:e0:c3 root@ip-171-32-13-40
The key's randomart image is:
+--[ED25519  256--+
|+.+.   ..        |
|o+ .  .  o       |
|.E+   ..o        |
|.o..  .o         |
|= .  . .S        |
|+o  o o o        |
|.. o   o .       |
|  .              |
|                 |
+-----------------+~~~- ssh 接続できない場合は、以下のログがでていない~~~
 * Starting Signal sysvinit that local filesystems are mounted[74G[ OK ] * Starting configure network device security[74G[ OK ]
 * Stopping Mount filesystems on boot[74G[ OK ]
 * Starting flush early job output to logs[74G[ OK ]
 * Stopping Failsafe Boot Delay[74G[ OK ]
 * Starting System V initialisation compatibility[74G[ OK ]
 * Stopping flush early job output to logs[74G[ OK ]
 * Starting configure virtual network devices[74G[ OK ]
 * Starting Enabling additional executable binary formats[74G[ OK ]
 * Starting Seed the pseudo random number generator on first boot[74G[ OK ]
 * Stopping Seed the pseudo random number generator on first boot[74G[ OK ]
 * Starting Bridge file events into upstart[74G[ OK ]
 * Starting D-Bus system message bus[74G[ OK ]
 * Starting SystemD login management service[74G[ OK ]
 * Starting early crypto disks...       [80G [74G[ OK ]
 * Starting system logging daemon[74G[ OK ]
 * Starting Handle applying cloud-config[74G[ OK ]

Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
Cloud-init v. 0.7.5 running 'modules:config' at Wed, 24 Feb 2016 09:21:43 +0000. Up 49.83 seconds.

 * Starting AppArmor profiles       [80G [74G[ OK ]
 * Setting up X socket directories...       [80G [74G[ OK ]
 * Stopping System V initialisation compatibility[74G[ OK ]
 * Starting System V runlevel compatibility[74G[ OK ]
 * Starting ACPI daemon[74G[ OK ]
 * Starting regular background program processing daemon[74G[ OK ]
 * Starting deferred execution scheduler[74G[ OK ]
 * Starting automatic crash report generation[74G[ OK ]
 * Stopping CPU interrupts balancing daemon[74G[ OK ]
 * Starting OpenSSH server[74G[ OK ]

Generating locales...
  en_US.UTF-8... up-to-date
Generation complete.
open-vm-tools: not starting as this is not a VMware VM
landscape-client is not configured, please run landscape-config.
 * Restoring resolver state...       [80G [74G[ OK ] * Stopping System V runlevel compatibility[74G[ OK ]

Cloud-init v. 0.7.5 running 'modules:final' at Wed, 24 Feb 2016 09:21:54 +0000. Up 60.62 seconds.
ci-info: +++++Authorized keys from /home/ubuntu/.ssh/authorized_keys for user ubuntu++++++
ci-info: +---------+-------------------------------------------------+---------+---------+
ci-info: | Keytype |                Fingerprint (md5)                | Options | Comment |
ci-info: +---------+-------------------------------------------------+---------+---------+
ci-info: | ssh-rsa | 4c:43:a8:22:1b:b5:a2:18:98:7d:aa:02:28:0c:35:b3 |    -    | vagrant |
ci-info: +---------+-------------------------------------------------+---------+---------+
ec2:
ec2: #############################################################
ec2: -----BEGIN SSH HOST KEY FINGERPRINTS-----
ec2: 1024 8e:fd:67:e4:a9:5a:9b:a7:c3:b2:04:de:8f:88:19:c2  root@ip-171-32-13-40 (DSA)
ec2: 256 eb:e8:cc:8b:3c:3d:ed:0c:f5:02:31:75:07:c1:00:10  root@ip-171-32-13-40 (ECDSA)
ec2: 256 70:19:b8:7b:23:68:0a:c2:1c:8d:0a:04:dc:52:e0:c3  root@ip-171-32-13-40 (ED25519)
ec2: 2048 d1:ff:8e:fc:22:82:66:d7:de:84:67:0c:3f:b0:89:a1  root@ip-171-32-13-40 (RSA)
ec2: -----END SSH HOST KEY FINGERPRINTS-----
ec2: #############################################################
-----BEGIN SSH HOST KEY KEYS-----
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKhCvi7WQ2WEX9caT0RJPkmInGWEmPFaQkYf4ozCMbH8Mef2P+BpD++xjNEfgx4EIEauiojiUjOQcTz0ApU5jac= root@ip-171-32-13-40
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFToVL5pbHpyW9yWPPUjqqONo1PxR7VwgQN3R8YnRmpL root@ip-171-32-13-40
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDTo5HotCWeMQNaLMCJqXYB+pFOgN4zAcgvK9anCG3KBLEMQV6jOfPfAi7E0OS1kC1vQvFkZk+4IZ/NUI2Zh9gPNvCgBjl5Klnp0N1g0WUkRCJTynpl18D7bw+GNYvKufGUsg04vKedroIWiGAOJu9M8HgUV7+vg+O0JLWbjWbJbfb99g/59M91hP7RSg67GjkocPzLODNzC6xLk3PVcSZuAT8ZVjHPG6GsKO7kSjCoPf+yXyNqS2p4hV8KHR1kmYB4rWYb8MOCwACHTCxZ7F5NeLiRnOTyGW108NVouk9tHeLpDhDFjLIAx+nr5BWIse7nlIkMwZ4+bPb0s+955pXZ root@ip-171-32-13-40
-----END SSH HOST KEY KEYS-----
Cloud-init v. 0.7.5 finished at Wed, 24 Feb 2016 09:21:54 +0000. Datasource DataSourceEc2.  Up 61.11 seconds~~~
