# pull

- pull = fetch + merge

## ブランチ指定で pull する

- branch指定( リモートにある br-remote1 ブランチを ローカルの br-local2 にpull)

~~~
$ git pull origin br-remote1:br-local2
~~~


## 不要なpullをしてしまったので、元のコードに戻す

~~~bash
$ git pull f003dca
~~~

## [サブモジュール](git.submodule.md)も丸ごと pull

~~~bash 
$ git pull --recurse-submodules
~~~
