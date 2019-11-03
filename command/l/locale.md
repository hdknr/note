# locale

~~~bash
$ locale
LANG=ja_JP.UTF-8
LANGUAGE=ja_JP:ja
LC_CTYPE="ja_JP.UTF-8"
LC_NUMERIC="ja_JP.UTF-8"
LC_TIME="ja_JP.UTF-8"
LC_COLLATE="ja_JP.UTF-8"
LC_MONETARY="ja_JP.UTF-8"
LC_MESSAGES="ja_JP.UTF-8"
LC_PAPER="ja_JP.UTF-8"
LC_NAME="ja_JP.UTF-8"
LC_ADDRESS="ja_JP.UTF-8"
LC_TELEPHONE="ja_JP.UTF-8"
LC_MEASUREMENT="ja_JP.UTF-8"
LC_IDENTIFICATION="ja_JP.UTF-8"
LC_ALL=
~~~

~~~bash
$ locale -a

C
C.UTF-8
POSIX
en_US.utf8
ja_JP.utf8
~~~

## localectl

- [【 localectl 】コマンド――ロケール設定の確認と変更：Linux基本コマンドTips（262） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1811/30/news060.html)

日本語化(Ubuntu)：

~~~bash
$ sudo apt install language-pack-ja-base language-pack-ja
$ sudo localectl set-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"
.
~~~

- [【 localectl 】 システムのロケールやキーボードレイアウトを管理する 【 Linuxコマンドまとめ 】 | LFI](https://linuxfan.info/localectl)

バーチャルコンソールで日本語が化ける場合の回避策:

~~~bash
[[ $TERM == 'linux' ]] && export LC_ALL=en_US.utf8
~~~
