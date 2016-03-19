# QuerySet メソッド

## QuerSetを返すメソッド

- filter
- exclude
- annotate
- order_by
- reverse
- distinct
- values ( ValuesQuerySet )
- values_list (tuple)
- dates
- datetimes
- none
- all
- select_related
- prefetch_related
- extra
- defer
- only
- using
- select_for_update
- raw

## QuerySetを返さない

### インスタンス

- get
- first /  last
- latest / earliest
- in_bulk


### 生成

- [create](https://docs.djangoproject.com/en/1.7/ref/models/querysets/#create)
- get_or_create
- update_or_create
- bulk_create

### 一括削除更新

- delete
- update

### 状態

- count
- exists


### その他

- iterator (イタレータで返す)
- aggregate (集約)
- as_manager (Managerクラス生成)

## フィールド検索条件

- [exact](https://docs.djangoproject.com/en/1.7/ref/models/querysets/#exact) / iexact
- contains / icontains
- in
- gt /  gte/  lt / lte
- startswith / istartswith / endswith / iendswith
- range
- year / month / day / week_day / hour/ minute/ second
- isnull
- search
- regex /  iregex


## 集約

- Avg
- Count
- Max
- Min
- StdDev
- Sum
- Variance

## Length

- [django filter on the basis of text length](http://stackoverflow.com/questions/12314168/django-filter-on-the-basis-of-text-length)

~~~
from django.db.models.functions import Length
qs = MyModel.objects.annotate(text_len=Length('text')).filter(
    text_len__gt=10)
~~~

## 記事

- [SQLのSELECT文を、DjangoのQuerySet APIで書いてみた](http://thinkami.hatenablog.com/entry/2015/09/04/235841)
