# apt 関連

## dselect

- [ListInstalledPackages](https://wiki.debian.org/ListInstalledPackages)
- [What does the "apt-get dselect-upgrade" command do? - Ask Ubuntu](https://askubuntu.com/questions/585273/what-does-the-apt-get-dselect-upgrade-command-do)

~~~bash
$ dpkg --get-selections | tee packages.txt
~~~

~~~bash
$ sudo apt-get install dselect
$ sudo dpkg --set-selections < packages.txt
$ apt-get dselect-upgrade
~~~

[apt - dpkg --get-selections shows packages marked "deinstall" - Ask Ubuntu](https://askubuntu.com/questions/165951/dpkg-get-selections-shows-packages-marked-deinstall)

### dselect を使わない

~~~bash
$ sudo apt install $(grep -v deinstall  packages.txt | awk '{print $1}')
.
~~~

## dist-upgrade

どのパッケージが新規インストール、アップグレード、削除なのかなどが表示:

~~~bash 
$ sudo apt-get -s dist-upgrade
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています       
状態情報を読み取っています... 完了
アップグレードパッケージを検出しています... 完了
アップグレード: 0 個、新規インストール: 0 個、削除: 0 個、保留: 0 個。
~~~

## apt-get update が404

- [Ubuntu で apt-get update が404になる問題](https://qiita.com/nyanchu/items/a8cfc5cf627d70d798bf)

~~~bash
$ sudo rm -rf /var/lib/apt/lists/*
~~~

## 不要パッケージの削除

~~~bash 
$ sudo apt-get autoremove
~~~