## django-pagnation

- [ericflo/django-pagination](https://github.com/ericflo/django-pagination)

インストール

~~~bash
$ pip install django-pagination
~~~

設定(settings.py)

~~~py
INSTALLED_APPS += ('pagination', )
MIDDLEWARE_CLASSES += ('pagination.middleware.PaginationMiddleware', )
TEMPLATE_CONTEXT_PROCESSORS += (
    "django.core.context_processors.request",
)
~~~

ビュー(特に変わりなく):

~~~py
def index(request):
    instances = models.AlumnusMaster.objects.filter()
    return TemplateResponse(
        request, 'alumni/index.html',
        dict(request=request, instances=instances,))   
~~~        


テンプレート

~~~~html
{% load pagination_tags %}

現在のページ : {{ request.page }}
{% autopaginate instances 30 as object_list %}
{% for instance in object_list %}
    <tr>
        <td>{{ instance.full_name }}</td>
        <td>{{ instance.full_name_kana }}</td>
        <td>{{ instance.grad_year|to_wareki }}</td>
        <td>{{ instance.dept.name }}</td>      
    </tr>
{% endfor %}

{% paginate %} {# pagination/pagination.html テンプレートのイクルードタグ #}
~~~~

### TODO

- パジネーションテンプレートの動的変更

## django-filter

- [alex/django-filter](https://github.com/alex/django-filter) ([doc](https://django-filter.readthedocs.org/en/latest/))

### 基本的な使い方

フィルター定義

~~~py
import django_filters                                                               
import models

class AlumnusFilter(django_filters.FilterSet):                                

    class Meta:                                                                     
        model = models.Alumnus
        fields = {                                                                  
            'full_name': ['contains', ],                                            
        }
~~~        

ビュー

~~~py
import filters

def index(request):                                                                 
    instances = filters.AlumnusMasterFilter(request.GET)                             
    return TemplateResponse(                                                        
        request, 'alumni/index.html',                                               
        dict(request=request, instances=instances,))  
~~~        

テンプレート

~~~html
{% load pagination_tags %} {# パジネーション #}

<div class="container-fluid">
<form action="" method="get">
 {{ instances.form.as_p }}
 <input type="submit" />
</form>

<div class="row">
    <div class="col-md-12">
        <table class="table table-striped table-hover container">
            <tbody>
            {% autopaginate instances.qs 30 as object_list %}
            {% for instance in object_list %}
                <tr>
                    <td>{{ instance.full_name }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
</div><!-- /container-fluid -->

{% paginate %}
~~~

### オーダー

- Meta に　order_by を指定できる

~~~py
  class Meta:
      order_by = ['js_number', '-js_number', 'full_name', 'full_name_kana', ]
~~~

- フォームにChoiceで表示されるので選択できる

- get_order_by で指定されたオーダーを修正できる

~~~py
def get_order_by(self, order_value):                                            
    # order_value を修正する
    return super(AlumnusMasterFilter, self).get_order_by(order_value)
~~~

### その他

- リクストをクエリ文字列に (self.data にGETが保存されている)

~~~html
<a href="?{{ filterset.data.urlencode }}">{% trans 'Full Name' %}</a>
~~~
