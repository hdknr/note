
- [Git submodule の基礎](http://qiita.com/sotarok/items/0d525e568a6088f6f6bb)
- [git submodule 使い方](http://transitive.info/article/git/command/submodule/)

~~~
git-submodule - Initialize, update or inspect submodules
~~~


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

### deinit

~~~       
       git submodule [--quiet] deinit
       			     [-f|--force] [--] <path>...
~~~

### update

~~~       
       git submodule [--quiet] update
       			     [--init] [--remote] [-N|--no-fetch]
                     [-f|--force]
                     [--rebase|--merge]
                     [--reference <repository>]
                     [--depth <depth>]
                     [--recursive] [--]
                     [<path>...]
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
