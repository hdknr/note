## CakePHP3: cake console

~~~bash
$ web/bin/cake console

Welcome to CakePHP v3.2.9 Console
---------------------------------------------------------------
App : src
Path: /vagrant/projects/researchdb/web/src/
PHP : 7.0.6
---------------------------------------------------------------
You can exit with `CTRL-C` or `exit`

Psy Shell v0.7.2 (PHP 7.0.6 — cli) by Justin Hileman
>>>
~~~



## app/venders/shellsのラッパー

- "-app パス" や cake のパスを指定するの面倒くさいので
- ディレクトリ構成

~~~
.
├── app
│   ├── vendors
│   │   └── shells
│
├── cake
│   ├── console
~~~

- スクリプト

~~~
#!/bin/bash
BASEDIR=$(readlink -f $0 | xargs dirname | xargs dirname | xargs dirname | xargs dirname)
COMMAND=${1%.*}			# 拡張子を抜く
ARGS=${@:2}				# $2以降を全て
#
$BASEDIR/cake/console/cake -app $BASEDIR/app $COMMAND $ARGS
~~~
