## inotifywait

~~~bash
$ sudo apt-get install inotify-tools
~~~


~~~bash
$ inotifywait -m -e create -r media/exception                   
Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.




media/exception/ CREATE b
media/exception/ CREATE,ISDIR c
media/exception/c/ CREATE hoge.txt
~~~

## incron

~~~bash
$ sudo apt-get install incron
~~~

~~~bash
$ sudo /etc/init.d/incron status
● incron.service - file system events scheduler
   Loaded: loaded (/lib/systemd/system/incron.service; enabled; vendor preset: enabled)
   Active: active (running) since 土 2018-03-24 03:23:06 JST; 29s ago
 Main PID: 25401 (incrond)
   CGroup: /system.slice/incron.service
           └─25401 /usr/sbin/incrond

 3月 24 03:23:06 ip-172-20-2-196 systemd[1]: Starting file system events scheduler...
 3月 24 03:23:06 ip-172-20-2-196 incrond[25401]: loading system tables
 3月 24 03:23:06 ip-172-20-2-196 incrond[25401]: loading user tables
 3月 24 03:23:06 ip-172-20-2-196 incrond[25401]: ready to process filesystem events
 3月 24 03:23:06 ip-172-20-2-196 systemd[1]: Started file system events scheduler.
~~~

~~~bash
$ incrontab --help
incrontab - inotify cron table manipulator
(c) Lukas Jelinek, 2006, 2007, 208

usage: incrontab [<options>] <operation>
       incrontab [<options>] <FILE-TO-IMPORT>

<operation> may be one of the following:
  -?, --about                  gives short information about program
  -h, --help                   prints this help text
  -l, --list                   lists user table
  -r, --remove                 removes user table
  -e, --edit                   provides editing user table
  -t, --types                  list supported event types
  -d, --reload                 request incrond to reload user table
  -V, --version                prints program version


These options may be used:
  -u <USER>, --user=<USER>     overrides current user (requires root privileges)
  -f <FILE>, --config=<FILE>   overrides default configuration file  (requires root privileges)

For reporting bugs please use http://bts.aiken.cz
~~~

~~~bash
$ incrontab -e
user 'ubuntu' is not allowed to use incron
~~~

追加:

~~~bash
$ sudo cat /etc/incron.allow
root
ubuntu
~~~

~~~bash
$ incrontab -e
table updated

$ incrontab -l
/home/ubuntu/projects/club/web/media/exception IN_CREATE /home/ubuntu/projects/club/bin/exception.sh $@/$#
~~~

~~~bash
$ incrontab -d
requesting table reload for user 'ubuntu'...
request done
~~~

テスト:

~~~bash
$ cat ../bin/exception.sh
#!/bin/bash

echo $@ >> /tmp/exception.txt
~~~

~~~bash
$ touch media/exception/hoge.txt

$ cat /tmp/exception.txt

xxxxx
yyyy
/home/ubuntu/projects/club/web/media/exception/hoge.txt

$ mkdir media/exception/test
$ cat /tmp/exception.txt

xxxxx
yyyy
/home/ubuntu/projects/club/web/media/exception/hoge.txt
/home/ubuntu/projects/club/web/media/exception/test
~~~


## 記事

- [inotify-toolsでファイルやディレクトリを監視する](https://qiita.com/stc1988/items/464410382f8425681c20)
- [サーバの監視・運用まわりで使ってるツール類を少しだけ晒してみる](https://qiita.com/hiro32itou/items/7f276812409a33d7c340)
- [incronを使ってみた](https://qiita.com/k-suzuki/items/4a94ebeda9ec75fdad40)
- [ファイル/ディレクトリの変更を検知してコマンドを実行するincron](http://blog.glidenote.com/blog/2012/08/02/incron/)
- [Linux でファイルの変更を検出する(inotify/fanotify)](http://www.nminoru.jp/~nminoru/programming/file_change_notification.html)

## python

- https://github.com/seb-m/pyinotify
- [pythonでinotifyを使ってみる。](https://blanktar.jp/blog/2013/03/python-inotify.html)


## mac(fswatch)

- [ファイルの変更を検知してscpを実行するコマンド](https://qiita.com/suin/items/b35b6b35eed61724366b)
