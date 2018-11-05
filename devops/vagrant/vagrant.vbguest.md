# Vbguest

~~~bash 
$ vagrant plugin install vagrant-vbguest

Installing the 'vagrant-vbguest' plugin. This can take a few minutes...
Fetching: micromachine-2.0.0.gem (100%)
Fetching: vagrant-vbguest-0.16.0.gem (100%)
Installed the plugin 'vagrant-vbguest (0.16.0)'!
~~~

~~~bash 
$ vagrant vbguest --status
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.1.28
Going on, assuming VBoxService is correct...
[default] GuestAdditions versions on your host (5.2.18) and guest (5.1.28) do not match.
~~~

## 更新

~~~bash 
$ vagrant vbguest

Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.1.28
Going on, assuming VBoxService is correct...
[default] GuestAdditions versions on your host (5.2.18) and guest (5.1.28) do not match.
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.1.28
Going on, assuming VBoxService is correct...
パッケージリストを読み込んでいます...
依存関係ツリーを作成しています...
状態情報を読み取っています...
linux-headers-4.15.0-24-generic はすでに最新バージョン (4.15.0-24.26) です。
linux-headers-4.15.0-24-generic は手動でインストールしたと設定されました。
dkms はすでに最新バージョン (2.3-3ubuntu9.2) です。
アップグレード: 0 個、新規インストール: 0 個、削除: 0 個、保留: 3 個。
Copy iso file /Applications/VirtualBox.app/Contents/MacOS/VBoxGuestAdditions.iso into the box /tmp/VBoxGuestAdditions.iso
Mounting Virtualbox Guest Additions ISO to: /mnt
mount: /mnt: WARNING: device write-protected, mounted read-only.
Installing Virtualbox Guest Additions 5.2.18 - guest version is 5.1.28
Verifying archive integrity... All good.
Uncompressing VirtualBox 5.2.18 Guest Additions for Linux........
VirtualBox Guest Additions installer
Removing installed version 5.1.28 of VirtualBox Guest Additions...
Copying additional installer modules ...
Installing additional modules ...
VirtualBox Guest Additions: Building the VirtualBox Guest Additions kernel modules.  This may take a while.
VirtualBox Guest Additions: Running kernel modules will not be replaced until the system is restarted
VirtualBox Guest Additions: Starting.
An error occurred during installation of VirtualBox Guest Additions 5.2.18. Some functionality may not work as intended.
In most cases it is OK that the "Window System drivers" installation failed.
Unmounting Virtualbox Guest Additions ISO from: /mnt
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.2.18
Going on, assuming VBoxService is correct...
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.2.18
Going on, assuming VBoxService is correct...
~~~

## 記事

- [VagrantのboxのGuest Additionsのアップデート方法 - Qiita](https://qiita.com/isaoshimizu/items/e217008b8f6e79eccc85)
