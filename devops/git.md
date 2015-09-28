## git

- 戻す: [reset](./git.reset.md)

### checkout: 削除してしまったファイルを戻す

~~~bash
$ git checkout HEAD --  ../language/ja_jp.lang.py
~~~

~~~bash
$ git checkout -f
~~~
~~~bash
$ git checkout -f ../lib
~~~

## fatal: cannot do a partial commit during a merge.

~~~bash
$ git commit -a my_filename
~~~

~~~bash
$ git commit -i file.txt -m "Merging file.txt"
~~~


## Cannot get remote repository information.

- gitが古すぎる (> <)

~~~
$ git clone https://github.com/hdknr/bin.git
Initialized empty Git repository in /home/ubuntu/bin/.git/
Cannot get remote repository information.
Perhaps git-update-server-info needs to be run there?

$ git --version
git version 1.5.4.3

$ git clone git://github.com/hdknr/bin.git
Initialized empty Git repository in /home/ubuntu/bin/.git/
remote: Counting objects: 641, done.
remote: Total 641 (delta 0), reused 0 (delta 0), pack-reused 641
Receiving objects: 100% (641/641), 77.96 KiB, done.
Resolving deltas: 100% (344/344), done.
~~~

## ソースからインストール
- gettext, autoconf は必要

~~~bash
    # wget https://github.com/git/git/archive/master.zip
    # unzip master
    # cd git-master/
    # autoconf
    # ./configure --prefix=$HOME/local --with-curl=/usr/local --with-expat
    # make all
    # make install
    # ~/local/bin/git --version
~~~

- /usr/local いれるなら
-
~~~
$ sudo make prefix=/usr/local install
~~~

## fatal: Unable to find remote helper for 'https'

~~~
$ sudo apt-get install libcurl4-openssl-dev
$ autoconf
$ ./configure  --with-expat --with-curl
$ make && sudo make prefix=/usr/local install
~~~

## error setting certificate verify locations

~~~
fatal: unable to access 'https://github.com/riywo/anyenv/': error setting certificate verify locations:
  CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: none
~~~

とりあえず無視する

~~~  
$ export GIT_SSL_NO_VERIFY=true  
~~~

## ブランチ作成 + push

- [参考](http://sessan.hatenablog.com/entry/2012/06/20/205036)

- clone してくる

```
(myproj)sugar@wzy:~/myproj.clean$ git clone git@bitbucket.org:hidelafoglia/myproj.git repo
Cloning into 'repo'...
remote: Counting objects: 5534, done.
remote: Compressing objects: 100% (2519/2519), done.
remote: Total 5534 (delta 3738), reused 4546 (delta 2851)
Receiving objects: 100% (5534/5534), 39.07 MiB | 4.45 MiB/s, done.
Resolving deltas: 100% (3738/3738), done.
```

- beta1 作成

```
(myproj)sugar@wzy:~/myproj.clean$ cd repo
(myproj)sugar@wzy:~/myproj.clean/repo$ git branch beta1
```

- beta1の状態にする

```
(myproj)sugar@wzy:~/myproj.clean/repo$ git checkout beta1

Switched to branch 'beta1'

(myproj)sugar@wzy:~/myproj.clean/repo$ git branch

  master
* beta1
```

- 修正後コミットする

```
(myproj)sugar@wzy:~/myproj.clean/repo$ git commit -a -m "beta1 ブランチ"
[beta1 a553dc3] beta1 ブランチ
 1 file changed, 2 insertions(+)
```

- beta1をpushする

```
(myproj)sugar@wzy:~/myproj.clean/repo$ git push origin beta1
Counting objects: 5, done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 372 bytes, done.
Total 3 (delta 2), reused 0 (delta 0)
To git@bitbucket.org:hidelafoglia/myproj.git
 * [new branch]      beta1 -> beta1

```

## 削除したファイルを取り除く

- [参考](http://www.commandlinefu.com/commands/view/1246/git-remove-files-which-have-been-deleted)

```
$ git rm $(git ls-files --deleted)
```


## リンク

- [サルでもわかるGit入門](http://www.backlog.jp/git-guide/)


## github

- [コミットメッセージにIssueのリンクを入れる](https://stackoverflow.com/questions/1687262/link-to-github-issue-number-with-commit-message)


## push

- [引数なしのgit pushは危険なので気をつけましょう](http://dqn.sakusakutto.jp/2012/10/git_push.html)


- branch名指定

~~~
$ git push origin br1
~~~

- default = upstream (追跡関係のみ)

~~~
$ git config --global push.default upstream
$ git push
~~~

- default = current (現在のブランチ)

~~~
$ git config --global push.default current
$ git push
~~~

- default = simple (カレントブランチと同名のリモートブランチが存在する場合のみ)

~~~
$ git config --global push.default simple
$ git push
~~~

## pull

- pull = fetch + merge
- branch指定( リモートにある br-remote1 ブランチを ローカルの br-local2 にpull)

~~~
$ git pull origin br-remote1:br-local2
~~~
