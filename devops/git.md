## 削除してしまったファイルを戻す

```
$ git checkout HEAD --  ../language/ja_jp.lang.py
```


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