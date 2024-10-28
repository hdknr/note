# ステータスチェック

- [ステータスチェックに失敗した Amazon EC2 Linux インスタンスをトラブルシューティングする](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/TroubleshootingInstances.html#system-log-errors-linux)
- [Amazon EC2 インスタンスのステータスチェック](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/TroubleshootingInstances.html#system-log-errors-linux)

## ステータスチェック情報の確認

- メモリ不足: プロセスの終了 ((`Out of memory: kill process...`))
- エラー: mmu_update failed (メモリ管理の更新に失敗しました) (`ERROR: mmu_update failed with rc=-22` (`Amazon Linux`))
- I/O エラー (ブロックデバイス障害) (`end_request: I/O error, dev sde, sector 52428288`) (`EBS`に問題あり)
- I/O エラー: ローカルでもリモートディスクでもありません (破損した分散ブロックデバイス) (`block drbd1: IO ERROR: neither local nor remote disk`)
- request_module: runaway loop modprobe (古い Linux バージョンでレガシーカーネル modprobe がループしている) (`request_module: runaway loop modprobe binfmt-464c` 古いカーネル)
- 「FATAL: kernel too old」および「fsck: No such file or directory while trying to open /dev」 (カーネルと AMI の不一致) (`FATAL: kernel too old` カーネルに互換性がない)
- 「FATAL: Could not load /lib/modules」または「BusyBox」 (カーネルモジュールの欠如) (`FATAL: Could not load /lib/modules/..` RAMディスク,rootボリューム問題)
- エラー: 無効のカーネル (EC2 と互換性のないカーネル)(`ERROR Invalid kernel: elf_xen_note_check: ERROR:...` GRUBサポートなし)
fsck: No such file or directory while trying to open..。(ファイルシステムが見つからない。) (`fsck.ext3: No such file or directory while trying to open /dev/sdh...` : `fstab` 問題, ドライブ問題)
- General error mounting filesystems (マウント失敗) (`General error mounting filesystems....` EBSボリュームに問題、 RAMディスクとAMIの不一致)
- VFS: Unable to mount root fs on unknown-block (ルートファイルシステム不一致) (`Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(8,1)` : ルートデバイス、ファイルシステムのフォーマット、カーネルが古い)
- Error: Unable to determine major/minor number of root device..。(ルートファイルシステム/デバイス不一致)(`ERROR: Unable to determine major/minor number of root device '/dev/xvda1'.` ... `[ramfs /]#` : 仮装BLOCK DEVICEドライバがない、設定がおかしい, デバイス列挙競合)
- XENBUS: Device with no driver..。(`ERROR: Unable to determine major/minor number of root device '/dev/xvda1'.` ... `[ramfs /]#` : 仮装BLOCK DEVICEドライバがない、設定がおかしい, デバイス列挙競合)
- ... days without being checked, check forced (ファイルシステムのチェックが必要です) (`/dev/sda1 has gone 361 days without being checked, check forced` fsckが必要)
- fsck died with exit status..。(デバイスが見つからない) (`fsck died with exit status 8` ドライブが見つからない/fsck中/ドライブエラー/ドライブがデタッチ)
- GRUB プロンプト (grubdom>) (`grubdom>`: `GRUB` に問題あり)
- Bringing up interface eth0: Device eth0 has different MAC address than expected, ignoring。(ハードコードされた MAC アドレス) (`Bringing up interface eth0:  Device eth0 has different MAC address than expected, ignoring.  [FAILED]`)
- SELinux ポリシーを読み込めません。Machine is in enforcing mode。Halting now。(SELinux の誤設定) (`Unable to load SELinux Policy.` SELinuxが有効になっている)
- XENBUS: Timeout connecting to devices (Xenbus タイムアウト) (`XENBUS: Timeout connecting to devices!`: ブロックデバイスがインスタンスに接続されていない, 古いインスタンスカーネル)
