Bootstrap3: フォーム項目を水平方向に並べる

## やりたいこと

### djang-bootstrap3

- [django-filter](https://django-filter.readthedocs.org/en/latest/index.html)のフォームアイテムを [django-bootstrap3](https://github.com/dyve/django-bootstrap3)で整形
- grad_year は MultiWidget/RangeWidget
- eraはRadioSelect

~~~html
{% load bootstrap3 %}
{% bootstrap_field filter.form.grad_year %}
{% bootstrap_field filter.form.era %}  
~~~

### よくない

![](https://github.com/hdknr/scriptogr.am/blob/e345d9840903683d6015e5d8a17f568c7aa7736f/django/bootstrap3.input.horizontal.bad.png?raw=true)

### こうしたい

![](https://github.com/hdknr/scriptogr.am/blob/e345d9840903683d6015e5d8a17f568c7aa7736f/django/bootstrap3.input.horizontal.good.png?raw=true)


## RadioSelect : jQueryでclassを変える

- `radio` -> `radio-inline` に修正

~~~js
  $("#id_era").children('div.radio').each(function(i){
    $(this).addClass('radio-inline'); 
    $(this).removeClass('radio'); 
  });
~~~


## MultiWidget は置き換える

### BootstrapRangeWidget

-  input のclassのデフォルトを `form-control` に
- レンダリングの修正
- 単純に `-` で連結したたものを `span.input-group-addon` でラップして連結する
- 全体を `div.input-group` でラップする
- あとはbootstrap3 に任せる

~~~py
from django import (forms, template) 

class BootstrapRangeWidget(forms.MultiWidget):
    def __init__(self, attrs={'class': 'form-control'}):
        widgets = (forms.TextInput(attrs=attrs), forms.TextInput(attrs=attrs))
        super(BootstrapRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        return template.Template('''
        <div class="input-group">
        {{w.0}} <span class="input-group-addon">-</span> {{ w.1 }}
        </div>
        ''').render(template.Context(
            dict(w=rendered_widgets, c=self)))
~~~

### フィルターにWidgetを指定

~~~py
import django_filters

class AlumnusFilter(django_filters.FilterSet):                                         
    grad_year = django_filters.RangeFilter(widget=BootstrapRangeWidget,)  
    ....
~~~
