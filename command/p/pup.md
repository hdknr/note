- https://github.com/ericchiang/pup
- http://brewformulas.org/Pup

## インストール

Debian/golang([goenv](https://github.com/hdknr/scriptogr.am/blob/master/go/goenv.md)):

~~~bash
$ go get github.com/ericchiang/pup
~~~


macOS:

~~~bash
$ brew install pup
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (caskroom/cask).
No changes to formulae.

==> Downloading https://homebrew.bintray.com/bottles/pup-0.4.0.sierra.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring pup-0.4.0.sierra.bottle.1.tar.gz
🍺  /usr/local/Cellar/pup/0.4.0: 5 files, 3.9MB
~~~

## 例

H1を抜く:

~~~bash 
$ curl -s http://yoursite.com/ | pup h1 text{}
~~~

## 記事

- [curl と pup と jq を使って、コマンドラインで wikipedia からデータを取り出す](https://qiita.com/osd/items/a94aba111b5c7717bd22)
- [html をコマンドラインからパースするなら pup が便利](https://mattn.kaoriya.net/software/20140916103411.htm)
