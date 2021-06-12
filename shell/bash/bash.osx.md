## OSXの bash を 3(El Captain)から4にする

~~~bash
$ bash --version
GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin15)
Copyright (C) 2007 Free Software Foundation, Inc.
~~~

~~~bash
$ brew update && brew install bash
~~~

~~~bash
$ /usr/local/bin/bash
$ bash --version
GNU bash, バージョン 4.3.46(1)-release (x86_64-apple-darwin15.5.0)
Copyright (C) 2013 Free Software Foundation, Inc.
ライセンス GPLv3+: GNU GPL バージョン 3 またはそれ以降 <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
~~~

~~~bash
$ sudo chsh -s /usr/local/bin/bash hide
Changing shell for hide.
~~~
