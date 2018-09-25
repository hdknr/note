# jq 

- [github](https://stedolan.github.io/jq/)

## install

### Mac Homebrew

```
$ brew install jq
```
```
==> Installing jq dependency: bison
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/bison-3.0.2.yosemite.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring bison-3.0.2.yosemite.bottle.1.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

Mac OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

Some formulae require a newer version of bison.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/bison/lib

==> Summary
🍺  /usr/local/Cellar/bison/3.0.2: 37 files, 2.0M
==> Installing jq
==> Downloading http://stedolan.github.io/jq/download/source/jq-1.4.tar.gz
######################################################################## 100.0%
==> ./configure --disable-silent-rules --prefix=/usr/local/Cellar/jq/1.4
==> make install
🍺  /usr/local/Cellar/jq/1.4: 15 files, 720K, built in 15 seconds
```

## Tutorial

### pretty print ( jq ".")

- デフォルトです

~~~bash
curl -s https://accounts.google.com/.well-known/openid-configuration | jq "."
~~~

### Wordpress API

`id` と `title` を表示 (`-r` (raw) でダブルクオートを表示しない)

~~~bash
curl -s http://192.168.56.54:8080/wp-json/wp/v2/posts/ | jq '.[] | "\(.id) , \(.title.rendered)"' -r
~~~


## 関連

- [curl](curl.md)
- [pup](pup.md) - HTMLのパーサー