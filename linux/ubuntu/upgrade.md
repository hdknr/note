## 17.04 -> 17.10

- [Upgrading from Ubuntu 17.04](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes#Upgrading_from_Ubuntu_17.04)

/etc/apt/sources.list:

~~~
deb http://old-releases.ubuntu.com/ubuntu/ zesty main universe
deb-src http://old-releases.ubuntu.com/ubuntu/ zesty main universe
deb http://old-releases.ubuntu.com/ubuntu/ zesty-security main universe
deb http://old-releases.ubuntu.com/ubuntu/ zesty-updates main universe
deb http://old-releases.ubuntu.com/ubuntu/ zesty-proposed main universe
deb http://old-releases.ubuntu.com/ubuntu/ zesty-backports main universe
deb-src http://old-releases.ubuntu.com/ubuntu/ zesty-security main universe
deb-src http://old-releases.ubuntu.com/ubuntu/ zesty-updates main universe
deb-src http://old-releases.ubuntu.com/ubuntu/ zesty-proposed main universe
deb-src http://old-releases.ubuntu.com/ubuntu/ zesty-backports main universe
~~~

~~~bash
$ sudo apt-get update && sudo apt-get upgrade
~~~

~~~bash
$ sudo apt-get install update-manager-core

パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています       
状態情報を読み取っています... 完了
update-manager-core はすでに最新バージョン (1:17.04.8) です。
アップグレード: 0 個、新規インストール: 0 個、削除: 0 個、保留: 3 個
~~~

`normall`:

~~~bash
$ grep -v "^#" /etc/update-manager/release-upgrades

[DEFAULT]
Prompt=normal
~~~

~~~bash
$ sudo do-release-upgrade
~~~

~~~bash
$ sudo lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 17.10
Release:        17.10
Codename:       artful
~~~

全バージョンがZ(zesty)だったので、A(artful)になる:

~~~bash
$ grep -v "^#"  /etc/apt/sources.list

deb http://jp.archive.ubuntu.com/ubuntu artful main universe
deb-src http://jp.archive.ubuntu.com/ubuntu artful main universe

deb http://jp.archive.ubuntu.com/ubuntu artful-security main universe
deb http://jp.archive.ubuntu.com/ubuntu artful-updates main universe
deb http://jp.archive.ubuntu.com/ubuntu artful-proposed main universe
deb http://jp.archive.ubuntu.com/ubuntu artful-backports main universe
deb-src http://jp.archive.ubuntu.com/ubuntu artful-security main universe
deb-src http://jp.archive.ubuntu.com/ubuntu artful-updates main universe
deb-src http://jp.archive.ubuntu.com/ubuntu artful-proposed main universe
deb-src http://jp.archive.ubuntu.com/ubuntu artful-backports main universe
~~~
