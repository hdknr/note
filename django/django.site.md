## shortcuts.get_current_site

- [shortcuts.get_current_site(request)](https://docs.djangoproject.com/ja/1.9/ref/contrib/sites/#get-current-site-shortcut)
- [現在のサイトを返す](https://github.com/hdknr/annotated-django/commit/128931bf66b68ee8d3c685e7e6dcc8c8fec367c1)

- settings.py で SITE_ID をコメントアウトする

~~~py
# SITE_ID = 1       
~~~

- requestのホスト名みて現在のサイトが帰る

~~~py
from django.contrib.sites import shortcuts    


def publish(request, path):                                                         
    current_site = shortcuts.get_current_site(request)                         
    ....
~~~

- ただし、`request.get_host()` に対応する [Site](https://docs.djangoproject.com/ja/1.9/ref/contrib/sites/#django.contrib.sites.models.Site) が存在しないと例外が発生します
