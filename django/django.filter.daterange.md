django-filter: DateField のレンジ検索

- [alex/django-filter](https://github.com/alex/django-filter) ([doc](https://django-filter.readthedocs.org/en/latest/))
- YYYY-MM も受け付ける。Fromはその月の初日、 To はその月の最終日。

## フォームフィールド

- django_filters.widgets.RangeWidget をそのまま使って From , To の入力フィールドを出す
- フィールドはforms.CharField

~~~python
from django import forms
from django_filters.widgets import RangeWidget
from datetime import date, timedelta
import re


class DateRangeField(forms.MultiValueField):
    widget = RangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
        )
        super(DateRangeField, self).__init__(fields, *args, **kwargs)

    def find_date(self, datestr, find_last=False):
        if not datestr:
            return None
        year, month, day = [
            i and int(i) for i in
            (re.split(r'\D+', datestr) + [None, None, None])[:3]]
        if not year or not month:
            return None
        month = min(12, max(1, month))
        year = min(9999, max(1, year))
        any_day = date(year, month, day or 1)
        if find_last and not day:
            # dayが指定されていなくて最終日を探す
            any_day = (
                any_day.replace(day=1) + timedelta(days=32)
            ).replace(day=1) - timedelta(days=1)
        return any_day

    def compress(self, data_list):
        ''' 必須: slice(start_date, stop_date)を返す
        '''
        if data_list:
            start = self.find_date(data_list[0])
            if data_list[1]:
                stop = self.find_date(data_list[1], True)
            else:
                stop = None
            return slice(start, stop)
        return None
~~~        


## フィールドフィルター

~~~python
import django_filters
from . import fields

class DateRangeFilter(django_filters.RangeFilter):
    field_class = fields.DateRangeField
~~~


## モデル & モデルフィルター

~~~python
class Bulletin(BaseModel):
    issued_at = models.DateField(
        null=True, default=None, blank=True)
    ....
~~~

~~~python
class BulletinFilter(django_filters.FilterSet):
    issued_at = DateRangeFilter()

    class Meta:
        model = models.Bulletin
~~~
