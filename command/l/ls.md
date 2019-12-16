# ls 

## 時刻表示

~~~bash
$ ls -l --full-time | grep file

-rw------- 1 vagrant vagrant         0 2015-10-31 00:13:43.930947104 +0000 fileDgEWcL
-rw------- 1 vagrant vagrant         0 2015-10-31 00:13:57.787184541 +0000 filefOkexg
~~~

## サイズ表示 (`-h`)

`-h`: 人が読めるフォーマット

## サイズソート

-l: 詳細, -S: ソート (降順), -r: 逆順

~~~bash
$ ls -lhSr
.
~~~

## 日付順にソート(`ls -lt`)

~~~bash
$ ls -alt *.tsv | head -n 3
-rw------- 1 system users  748082  4月 15 15:57 tmpVl_0X7.tsv
-rw------- 1 system users  750174  3月 22 20:47 tmpCbWA3m.tsv
-rw------- 1 system users  699387  2月 17 09:59 tmpbwOKRi.tsv
~~~

- 古い順 (`ls -lrt`)

~~~bash
$ ls -alrt *.tsv | head -n 3
-rw------- 1 system users      46  3月 10  2015 tmpJb5ZqR.tsv
-rw------- 1 system users       0  3月 10  2015 tmp2apieB.tsv
-rw------- 1 system users      46  3月 10  2015 tmp5jcPte.tsv
~~~

## リンク

- [【 ls 】 ファイルやディレクトリの情報を表示する](http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230820/)
