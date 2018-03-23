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

- [incronを使ってみた](https://qiita.com/k-suzuki/items/4a94ebeda9ec75fdad40)

## 記事

- [inotify-toolsでファイルやディレクトリを監視する](https://qiita.com/stc1988/items/464410382f8425681c20)
- [サーバの監視・運用まわりで使ってるツール類を少しだけ晒してみる](https://qiita.com/hiro32itou/items/7f276812409a33d7c340)

## python

- https://github.com/seb-m/pyinotify
- [pythonでinotifyを使ってみる。](https://blanktar.jp/blog/2013/03/python-inotify.html)


## mac(fswatch)

- [ファイルの変更を検知してscpを実行するコマンド](https://qiita.com/suin/items/b35b6b35eed61724366b)
