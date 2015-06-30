
## 不要なファイル削除

```
hg addremove
```

```
hg remove --after
hg remove -A
```

## ブランチ作成

```
Peeko:connectsharp hide$ hg branch study0

marked working directory as branch study0
(branches are permanent and global, did you want a bookmark?)
```

```
Peeko:connectsharp hide$ hg branch
study0
```

```
Peeko:connectsharp hide$ hg ci -m "Study0, as of Nov, 2014"

committed changeset 79:e6e329fe286b
```

```

Peeko:connectsharp hide$ hg parents

changeset:   79:e6e329fe286b
branch:      study0
tag:         tip
user:        hdknr <gmail@hoge.com>
date:        Mon Nov 17 10:05:24 2014 +0900
description:
Study0, as of Nov, 2014
```

```
Peeko:connectsharp hide$ hg push --new-branch

pushing to ssh://hg@bitbucket.org/harajukutech/connectsharp
running ssh hg@bitbucket.org 'hg -R harajukutech/connectsharp serve --stdio'
searching for changes
6 changesets found
remote: adding changesets
remote: adding manifests
remote: adding file changes
remote: added 6 changesets with 11 changes to 8 files (+1 heads)
```


## TortoisHG: Windowsでsshを使えるようにする

- $HOME/.hgrc (あるいはMercurial.ini)で tortoiseplink.exe コマンドを ssh に指定しておくとよい

```
[ui]
ssh = tortoiseplink.exe -ssh -i "C:\Users\hdknr\Documents\Share\ssh\blacky.win8.ppk"
```

##  ブランチ間 diff

~~~
$ hg branches
spnego                       149:e5f805debc06
composer                     130:5387bfca7e8a
default                      147:687f440ffe67 (非アクティブ)
~~~

~~~
$ hg diff -r spnego:composer
~~~


## フォーク元からマージ

- フォーク元を origin として追加

~~~
$ vim .hg/hgrc 
~~~

~~~
[paths]
default = ssh://hg@bitbucket.org/hdknr/code
origin = ssh://hg@bitbucket.org/hide/code
~~~

- gitだとコマンドで追加

~~~
$ git remote add hides ssh://git@github.com/hide/code
~~~

- フォーク元からpull

~~~
$ hg pull origin
~~~

- merge

~~~
$ hg merge
~~~

- コンフリクトファイルの修正

~~~
$ vim some_file.php
$ hg resolve --mark
~~~

- commit & push

~~~
$ hg commit -m "merge behinds"
$ hg push
~~~


## TortoisHG

## sshの設定

- .hgrc の ssh に記載する

```
C:\>cd Users
C:\Users>cd hdknr

C:\Users\hdknr>more .hgrc

[ui]
ssh = tortoiseplink.exe -ssh -i "C:\Users\hdknr\Documents\mykey.ppk"

```

## SubRepository

- [Subrepository](http://mercurial.selenic.com/wiki/Subrepository)

- [Is there a way to use a Mercurial repository as Git submodule?](https://stackoverflow.com/questions/9067283/is-there-a-way-to-use-a-mercurial-repository-as-git-submodule)

- [Mercurial でのサブリポジトリの利用](http://d.hatena.ne.jp/flying-foozy/20120526/1338047861)

- [リポジトリホスティング使用時の .hgsub 記述](http://d.hatena.ne.jp/flying-foozy/20140109/1389234412)


