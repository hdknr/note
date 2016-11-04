## ディレクトリ指定

~~~bash
$ git --git-dir=$PWD/myrepo/.git push
~~~


## 新しいブランチをpush

~~~bash
$ git push origin centos
Password:  *******
Counting objects: 3, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 229 bytes, done.
Total 2 (delta 1), reused 0 (delta 0)
To https://hdknr@github.com/hdknr/bin.git
 * [new branch]      centos -> centos
~~~



##  branch名指定

~~~
$ git push origin br1
~~~

## default = upstream (追跡関係のみ)

~~~
$ git config --global push.default upstream
$ git push
~~~

## default = current (現在のブランチ)

~~~
$ git config --global push.default current
$ git push
~~~

## default = simple (カレントブランチと同名のリモートブランチが存在する場合のみ)

~~~
$ git config --global push.default simple
$ git push
~~~


## その他

- [引数なしのgit pushは危険なので気をつけましょう](http://dqn.sakusakutto.jp/2012/10/git_push.html)
