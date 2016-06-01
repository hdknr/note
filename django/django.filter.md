django-filter

## Resource

- [alex/django-filter](https://github.com/alex/django-filter) ([doc](https://django-filter.readthedocs.org/en/latest/))
- [readthedocs](https://django-filter.readthedocs.io/en/latest/)

## ヘルプテキストを消す


~~~js
$(function(){
 $(".form-group .help-block").toggle();
});
~~~

## 文字列検索を全て部分一致にする

~~~py
class ForumFilter(django_filters.FilterSet):

    class Meta:
        model = models.Forum

    def __init__(self, *args, **kwargs):
        super(ForumFilter, self).__init__(*args, **kwargs)

        # CharfFilter を defaultのexact からcontainsに変更
        for i in self.filters:
            if isinstance(self.filters[i],  django_filters.CharFilter):
                self.filters[i].lookup_type = u'contains'
~~~

## ソートオーダー

- フィールドを Meta.`order_by` で選択可能フィールドを指定する
- 降順であればマイナスをつける

~~~python
class EventFilter(django_filters.FilterSet):                                        
    class Meta:                                                                     
        model = models.Event                                                        
        order_by = [                                                                
            '-opening_on', 'opening_on', 'presenter', '-presenter']   
~~~            

### ORDER_BY_FIELD

- デフォルトのクエリ変数は `o` 。変更は可能。

~~~py
class BaseFilterSet(object):                                                        
    order_by_field = ORDER_BY_FIELD       #  o です
    ...
~~~

###  ordering_field

- `def get_ordering_field(self)` でオーバーライド可能
- デフォルトでは`order_by` のリストからchoices を作ってChoiceFieldを返す。

### get_order_by

- `queryset.order_by(*self.get_order_by(values))`

~~~py
def get_order_by(self, order_choice):                                        
    return [order_choice]                                                    
~~~

## デフォルトの検索条件を与える(`queryset`)

~~~py
def alumnus_list(request):
    queryset = models.Alumnus.objects.filter(full_name__gt='')             
    results = filters.AlumnusFilter(request.GET or None, queryset=queryset)  
    ...
~~~
