## pbcopy/pbpaste (macOS)

~~~bash
$ echo 'Hello, World!' | pbcopy
~~~

~~~bash
$ pbpaste
Hello, World!
~~~


## xsel(Debian)


~~~bash
$ sudo apt-get install xsel
~~~

~~~bash
$ alias pbcopy='xsel --clipboard --input'
$ alias pbpaste='xsel --clipboard --output'
~~~


## clip (Windows)

- [［clip / pbcopy・pbpaste］クリップボードにコピー](https://xtech.nikkei.com/it/atcl/column/15/042000103/080400036/)
