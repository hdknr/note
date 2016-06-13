## Hours & Minutes : datetime.time

~~~py
In [1]: from datetime import time
In [2]: time(10, 0, 0)
Out[2]: datetime.time(10, 0)
~~~


## 現地時間

~~~bash
$ pip install python-dateutil
Collecting python-dateutil
  Downloading python_dateutil-2.4.2-py2.py3-none-any.whl (188kB)
    100% |████████████████████████████████| 192kB 1.7MB/s
Requirement already satisfied (use --upgrade to upgrade):
  six>=1.5 in /home/vagrant/.anyenv/envs/pyenv/versions/2.7.10/lib/python2.7/site-packages (from python-dateutil)
Installing collected packages: python-dateutil
Successfully installed python-dateutil-2.4.2
~~~

- 日付

~~~py
In [1]: from dateutil import parser
In [2]: dt = parser.parse('2016-2-1')

In [3]: dt
Out[3]: datetime.datetime(2016, 2, 1, 0, 0)
~~~

- ホノルル
~~~py
In [4]: import pytz
In [5]: honolulu = pytz.timezone('Pacific/Honolulu')
~~~

- ホノルル化

~~~py
In [6]: honolulu.localize(dt)
Out[6]: datetime.datetime(2016, 2, 1, 0, 0, tzinfo=<DstTzInfo 'Pacific/Honolulu' HST-1 day, 14:00:00 STD>)
~~~

- これをUTC 化

~~~py
In [8]: _.astimezone(pytz.UTC)
Out[7]: datetime.datetime(2016, 2, 1, 10, 0, tzinfo=<UTC>)
~~~


## combine:日付(date)と時刻(time) から日時(datetime)

~~~
>>> n = datetime.now()

>>> n
datetime.datetime(2015, 3, 28, 9, 55, 26, 953264)

>>> datetime.combine(n.date(), n.time())
datetime.datetime(2015, 3, 28, 9, 55, 26, 953264)
~~~



## TZ

- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
- [Current local time in Denpasar, Bali, Indonesia](http://www.timeanddate.com/worldclock/indonesia/denpasar)

- [Asia/Makassar](https://en.wikipedia.org/wiki/Asia/Makassar)
- [Pacific/Honolulu]
- [Pacific/Guam]

~~~py
>>> [tz for tz in pytz.all_timezones if tz.startswith('Asia')]

['Asia/Aden', 'Asia/Almaty',.....
~~~

~~~bash
$ date
2015年 12月20日 日曜日 13時57分56秒 JST
~~~

~~~python
In [1]: import pytz
In [2]: from datetime import datetime

In [3]: now = datetime.now()
In [4]: now
Out[4]: datetime.datetime(2015, 12, 20, 14, 1, 32, 57239)

In [5]: now.tzinfo == None
Out[5]: True

~~~

- 日時に対してタイムゾーンを設定する(日時が変わるのではない)

~~~
In [6]: tokyo = pytz.timezone('Asia/Tokyo')
In [7]: tokyo.localize(now)
Out[7]: datetime.datetime(2015, 12, 20, 14, 1, 32, 57239, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)

In [8]: honolulu = pytz.timezone('Pacific/Honolulu')
In [9]: honolulu.localize(now)
Out[9]: datetime.datetime(2015, 12, 20, 14, 1, 32, 57239, tzinfo=<DstTzInfo 'Pacific/Honolulu' HST-1 day, 14:00:00 STD>)
~~~

- タイムゾーンにおける現在時刻を取得

~~~py
In [10]: datetime.now(tokyo)
Out[10]: datetime.datetime(2015, 12, 20, 14, 4, 47, 820535, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)

In [11]: datetime.now(honolulu)
Out[11]: datetime.datetime(2015, 12, 19, 19, 4, 53, 709388, tzinfo=<DstTzInfo 'Pacific/Honolulu' HST-1 day, 14:00:00 STD>)
~~~
