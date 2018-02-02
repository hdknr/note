## dselect

- [ListInstalledPackages](https://wiki.debian.org/ListInstalledPackages)

~~~bash
$ dpkg --get-selections | tee packages.txt
~~~

~~~bash
$ sudo apt-get install dselect
$ sudo dpkg --set-selections < packages.txt
$ apt-get dselect-upgrade
~~~

~~~bash
$ aptitude install $(cat packages.txt | awk '{print $1}')
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
