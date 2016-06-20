## Cookbook

### クエリパラメータをアンカーに渡す

- django.core.context_processors.request が必要

setttings.py:

~~~py
TEMPLATES = [
    {   
        # ....
        'OPTIONS': {
            'context_processors': [
                # ....
                "django.template.context_processors.request",
            ],  
        },  
    },  
]

~~~

page/index.html:

~~~html
<a href="{% url 'page_detail' %}?{{ request.GET.urlencode }}">詳細</a>
~~~


### builtin:  `{% load %}` しなくてもタグ/フィルタを使う

- [built-in backend](https://docs.djangoproject.com/en/1.9/topics/templates/#module-django.template.backends.django)

~~~py
OPTIONS={
    'builtins': ['myapp.builtins'],
}
~~~
