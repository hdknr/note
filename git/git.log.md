## 個別ファイルの変更ログ( `-p` オプション)

diff で確認

~~~
$ git log --follow -p filename
~~~

~~~
$ git log -p filename
~~~


## グラフ表示

[git log を見やすくする](https://qiita.com/takasianpride/items/842a785af610025a2030)

~~~bash 
$ git log --graph --all --format="%x09%an%x09%h %d %s"

*       hdknr   2bfe83b  (HEAD -> master) feature2->temp->master
| *     hdknr   605851d  (temp) feature2 -> temp
|/  
*       hdknr   b2b97b4  feature1 -> temp -> master
| *     hdknr   422d76d  (feature2) readme
| *     hdknr   fe08b2d  feature2: goodbye() was implemented
|/  
| *     hdknr   486bc32  (feature1) feature1: hello() was implemented
|/  
*       hdknr   1203d78  start
~~~

~~~bash 
$ git config --global alias.tree 'log --graph --all --format="%x09%C(cyan bold)%an%Creset%x09%C(yellow)%h%Creset %C(magenta reverse)%d%Creset %s"'
~~~

~~~bash 
$ git tree
...
~~~