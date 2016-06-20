django-filter: order_by に複数指定可能にする

- [alex/django-filter](https://github.com/alex/django-filter) ([doc](https://django-filter.readthedocs.org/en/latest/))
- ソート条件を複数指定できるようにする

~~~
/events?o=opening_on&o=-title
/events?o=-presenter&o=-opening_on&o=title
~~~

## フィルターセット:get_ordering_field / get_order_by

~~~py
class EventFilter(django_filters.FilterSet):
    class Meta:
        model = models.Event
        order_by = [
            '-opening_on', 'opening_on',
            '-title', 'title',
            'presenter', '-presenter' ]

    def get_ordering_field(self):
        '''
        - デフォルトで１つ(フォームフィールドが ChoiceField)
        - 複数変数を受けるようにMultipleChoiceField化する
        '''
        field = super(EventFilter, self).get_ordering_field()
        return forms.MultipleChoiceField(choices=field.choices, required=False)

    def get_order_by(self, order_choice):
        ''' リストが来たらそのまま帰す '''
        if isinstance(order_choice, (list, tuple)):
            return order_choice
        return [order_choice]
~~~          

## テンプレートタグ: ordering

- `query` でクエリ文字列を返す
- `direction` に `asc` / `desc` を返す

~~~py
@register.assignment_tag(takes_context=True)                                        
def ordering(context, field, key='o'):                                              
    qdict = context.get('request').GET.copy()                                              
    rfield = '-' + field                                                            
    q = qdict.getlist(key)                                                            
    if rfield in q:                                                                 
        q.remove(rfield)                                                            
        direction = "asc"                                                           
    else:                                                                           
        if field in q:                                                              
            q.remove(field)                                                         
        field = rfield                                                              
        direction = "desc"                                                          

    q = [field] + q                                                                 
    qdict.setlist(key, q)                                                             
    return dict(query=qdict.urlencode(), direction=direction)   
~~~  

テンプレート:

~~~html
{% load mytags %}

<thead>
  <tr>
    <th>
      {% ordering 'opening_on' as opening_on_order %}
      <a href="?{{ opening_on_order.query }}">
        <span class="sort-{{ opening_on_order.direction }}">{% trans 'Opening On' %}</span></a></th>

    <th>
      {% ordering 'title' as title_order %}
      <a href="?{{ title_order.query }}">
        <span class="sort-{{ title_order.direction }}">{% trans 'Event Title' %}</span></a></th>
  </tr>
</thead>

~~~

スタイル:

~~~html
<style>
.sort-asc:after{content: "↓"}
.sort-desc:after{content: "↑"}
</style>
~~~
