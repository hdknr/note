# [git-submodule - Initialize, update or inspect submodules](https://git-scm.com/docs/git-submodule)

## SYNOPSIS

### add

~~~
       git submodule [--quiet] add
       				 [-b <branch>]
       				 [-f|--force]
       				 [--name <name>]
                     [--reference <repository>]
                     [--depth <depth>]
                     [--] <repository>
                     [<path>]
~~~

~~~bash
$ git submodule add https://github.com/jquery/jquery.git asset/jquery
Cloning into 'asset/jquery'...
remote: Counting objects: 37144, done.
remote: Compressing objects: 100% (58/58), done.
remote: Total 37144 (delta 24), reused 0 (delta 0), pack-reused 37086
Receiving objects: 100% (37144/37144), 22.68 MiB | 2.50 MiB/s, done.
Resolving deltas: 100% (26185/26185), done.
Checking connectivity... done.

$ git add .gitmodules
$ git add asset/jquery/

$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   .gitmodules
        new file:   asset/jquery


$ git commit -a -m "add jquery"
[master (root-commit) 2d7829d] add jquery
 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 asset/jquery

~~~

### status

~~~                     
       git submodule [--quiet] status
       			    [--cached]
       			    [--recursive]
       			    [--] [<path>...]
~~~

~~~bash
$ git submodule
 aabe94edb4880c75eeebc5b5b5d66a9ad17008fe asset/jquery (2.1.0-beta1-517-gaabe94e)
~~~

~~~
$ git config -l | grep -v "user"
push.default=simple
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
submodule.asset/jquery.url=https://github.com/jquery/jquery.git
~~~


### init

~~~       			    
       git submodule [--quiet] init
       				 [--] [<path>...]
~~~

### deinit  削除

~~~
git submodule [--quiet] deinit
          [-f|--force] [--] <path>...
~~~

~~~bash
git submodule deinit -f client
git rm -f client
~~~

### update 更新

~~~man
git submodule [--quiet] update
    [--init]
    [--remote]
    [-N|--no-fetch]
    [--[no-]recommend-shallow]
    [-f|--force]
    [--checkout|--rebase|--merge]
    [--reference <repository>]
    [--depth <depth>]
    [--recursive]
    [--jobs <n>]
    [--]
    [<path>...]
~~~

### 再帰的に更新

~~~bash
$ git submodule update --recursive --remote
.
~~~

### summary

~~~                     
       git submodule [--quiet] summary
       				 [--cached|--files]
       				 [(-n|--summary-limit) <n>]
                     [commit] [--] [<path>...]
~~~

###  foreach

~~~                     
       git submodule [--quiet] foreach [--recursive] <command>
~~~

### sync

~~~       
       git submodule [--quiet] sync [--recursive] [--] [<path>...]
~~~

## URL の変更

- [submodule の向き先 url を変更する](http://qiita.com/8mamo10/items/fd11d8c7a2d928b39173)

~~~bash
$ vim .gitmodules
.
~~~

~~~bash
$ git submodule sync && git submodule update
.
~~~

## 記事

- [gitサブモジュールの追加/削除/再追加 - Qiita](https://qiita.com/uma8/items/f6d625c92bb355ccc409)
- [Git submodule の基礎](http://qiita.com/sotarok/items/0d525e568a6088f6f6bb)
- [git submodule 使い方](http://transitive.info/article/git/command/submodule/)