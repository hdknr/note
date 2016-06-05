## datetimeフィールドの日付で件数を出す
- [extra](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.extra) で `last` (date) を追加する

~~~py
>>> Profile.objects.extra({'last': "date(updated)"})[0].last
datetime.date(2015, 2, 10)
>>> Profile.objects.extra(select={'last': "date(updated)"})[0].last
datetime.date(2015, 2, 10)
~~~

~~~py
>>> type(Profile.objects.extra(select={'last': 'date(updated)'}))
<class 'django.db.models.query.QuerySet'>
~~~


- dateはMySQL(sqliteも)の関数

~~~
mysql> select date(updated) as last from accounts_profile limit 1;
+------------+
| last       |
+------------+
| 2015-02-10 |
+------------+
1 row in set (0.00 sec)
~~~

- ValueQuerySet

~~~py
>>> type(Profile.objects.extra(select={'last': 'date(updated)'}).values('last'))
<class 'django.db.models.query.ValuesQuerySet'>
~~~

- ValueQuerSetを件数で集約する
- `last` で descソートする

~~~py
>>> from django.db.models import Count
>>> Profile.objects.extra({'last': "date(updated)"}).values('last').annotate(count=Count('id')).order_by('-last')
>>> c = _
>>> for i in c:
...     print i['last'], i['count']
...
2015-09-25 7096
2015-06-16 198
2015-05-01 1
~~~
