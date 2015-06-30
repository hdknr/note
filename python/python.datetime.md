## combine:日付(date)と時刻(time) から日時(datetime)

~~~
>>> n = datetime.now()

>>> n
datetime.datetime(2015, 3, 28, 9, 55, 26, 953264)

>>> datetime.combine(n.date(), n.time())
datetime.datetime(2015, 3, 28, 9, 55, 26, 953264)
~~~