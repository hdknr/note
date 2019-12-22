# [vagrant package](https://www.vagrantup.com/docs/cli/package.html)

## 仮想マシンの移動

- [VirtualBox - 仮想マシンのエクスポート（別のPCへ移動・移行）](https://pc-karuma.net/virtualbox-export-vm-appliance/) 
- [Vagrantでexportした環境(box)を取り込む方法](https://qiita.com/kon_yu/items/ac7fb2c5af1cc0844225)

パッケージ化する:

~~~bash
$ vagrant package 4331eef --output centos7dev.box
.
~~~

移動先で追加する:

~~~bash
$ vagrant box add centos7dev centos7dev.box
.
~~~

初期化する:

~~~bash
$ vagrant init centos7dev
.
~~~

設定ファイルを変更する

~~~bash
$ vim Vagrantfile
.
~~~
