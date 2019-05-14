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