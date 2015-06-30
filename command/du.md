## サイズの上位10の一覧

~~~
$ du -k / | sort -n | tail -10
~~~


~~~
$ find . -type f -size +1000000k -exec ls -lh {} \; | awk '{ print $8 ": " $5 }'
~~~

~~~
$ sudo find . -type f -size +50000k -exec ls -lh {} \;
~~~