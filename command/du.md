## du と df

- dfとは、ディスク容量の表示。
- duとは、ファイル容量を表示。

### (deleted)

- [duで見つからないファイルはlsofで探そう - 見えないファイルにディスクが圧迫されてる時とかね](http://qiita.com/nntsugu@github/items/3e492f1ea164568ae259)

~~~bash
$ sudo lsof -nP | grep '(deleted)'

vmtoolsd   2482      root    3u      REG      253,0     4837   17139075 /tmp/vmware-root/vmware-apploader-2482.log (deleted)
hald-addo  3473 haldaemon  txt       REG      253,0    13472    4635881 /usr/libexec/hald-addon-keyboard.#prelink#.HWCYFW (deleted)
yum-updat  4036      root  txt       REG      253,0     5708    4637381 /usr/bin/python.#prelink# (deleted)
~~~

~~~bash
$ sudo find /proc/*/fd -ls | grep  '(deleted)'

162693123    0 lrwx------   1 root     root           64  7月 28 11:55 /proc/2482/fd/3 -> /tmp/vmware-root/vmware-apploader-2482.log\ (deleted)
find: /proc/self/fd/4: そのようなファイルやディレクトリはありません
~~~


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