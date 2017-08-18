## グローバル

~~~bash
$ git config --global core.excludesfile ~/.gitignore_global
~~~

~~~bash
$ more ~/.gitconfig
[user]
        email = gmail@hdknr.com
        name = hdknr
[core]
        excludesfile = /home/vagrant/.gitignore_global
~~~        

~~~bash
$ cat ~/.gitignore_global
.DS_Store
~~~

## リソース

- https://github.com/github/gitignore
