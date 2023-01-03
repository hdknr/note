# date

書式化:

~~~bash
$ echo $(date +%Y-%m-%d)
~~~




## 曜日

- Sunday = 0 , Saturday=6 の序数がいい
- dateコマンドのだけ 7の時に 0 に変える必要がある

- [javscriptは 0: Sunday](http://www.w3schools.com/jsref/jsref_getday.asp)

~~~js
> now = new Date();
Sat Dec 19 2015 23:07:31 GMT+0000 (UTC)
> now.getDay();
6
~~~

- date は 1:が月曜日、 7:日曜日

~~~bash
$ date
2015年 12月20日 日曜日 08時09分16秒 JST
$ date +"%u"
7
~~~


- .NET は 0 = Sunday

~~~csharp
csharp> DateTime.Now.DayOfWeek
Sunday
csharp> DateTime.Now.DayOfWeek.value__
0
~~~

- [python.datetime](http://docs.python.jp/2/library/datetime.html)

~~~py
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2015, 12, 19, 23, 13, 28, 601598)
~~~~

- weekday( 月曜日 = 1 , 日曜日 = 7 , dateコマンドと同じ)

~~~~py
>>> datetime.now().weekday()
5
~~~

- isoweekday( 月曜日 = 0 , 日曜日 = 6 )

~~~py
>>> datetime.now().isoweekday()
6
~~~

- isocalendar(日曜日 =0, 土曜日 =7)

~~~py
>>> datetime.now().isocalendar()
(2015, 51, 6)
~~~

- strftime "%w" は日曜日=0

~~~py
>>> datetime.now().strftime('%w %A')
'6 Saturday'
~~~

日付相対指定:

~~~bash
% date --date '7 days ago'
~~~

## 資料

- [date コマンドの日付指定頻出パターン](https://qiita.com/suzuki-kei/items/cb0a78a655fef37cb59d)
