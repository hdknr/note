Django :Yet Another Class-Based View


- URLConf をビューのメソッドベースでつくる
- メソッドには、 url(正規表現), order(URLConf中の順番)を属性に加える
- これをデコレータでやる
- ビュークラスにはモデルをバインドさせて、nameを生成する


## ビューデコレータ: handler

~~~py
from functools import wraps


def handler(url='', order=0):
    def _hander(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.url = url         # url 正規表現
        wrapper.order = order     # urlの並び
        return classmethod(wrapper)

    return _handler

~~~


## ベースクラス :View

~~~py
from django.conf import urls
from operator import itemgetter


class View(object):

    @classmethod
    def urls(cls):
        '''URLConf をつくる '''
        base = "{}_{}".format(
            cls.Meta.models._meta.app_label,
            cls.Meta.models._meta.model_name, )

        funcs = []
        for name in cls.__dict__:
            obj = getattr(cls, name)
            if hasattr(obj, 'url'):
                funcs.append((name, obj.order, obj))

        # メソッドに指定した order で並べ替え、それぞれに url を作成する
        return [
            urls.url(func.url, func, name="{}_{}".format(base, name))
            for name, _, func in sorted(funcs, key=itemgetter(1))
        ]

~~~

## 実際のビュークラス: CommunityView

~~~py
from django.contrib.auth import decorators as authdeco
from django.utils.decorators import method_decorator


# パーミッション
permission_required = method_decorator(
    authdeco.permission_required('communities.list_community'))


class CommunityView(View):
    class Meta:
        # バインドするモデル
        models = models.Community

    @handler(url=r'^community/(?P<id>.+)/edit(?:/(?P<command>.*))?', order=0)
    @permission_required
    def edit(cls, request, id, command=''):
        # .....
        return TemplateResponse(
            request,
            'communities/community/edit{0}.html'.format(name),
            dict(request=request, form=form))

    @handler(url=r'^community/(?P<id>.+)', order=1)
    @permission_required
    def detail(cls, request, id, *args, **kwargs):
        # .....
        return TemplateResponse(
            request,
            'communities/community/detail.html',
            dict(request=request, instance=instance, form=form))

    @handler(url=r'^community', order=2)
    @permission_required
    def index(cls, request):
        # ...
        return TemplateResponse(
            request,
            'communities/community/index.html',
            dict(request=request, instances=instances))
~~~

## urls.py


~~~
from django.conf.urls import url    
from . import views

urlpatterns = [        
  # その他のURLConf
  # ....
] + views.CommunityView.urls()
~~~

## 確認

~~~py
In [4]: for url in CommunityView.urls():
   ...:     print url
   ...:     
<RegexURLPattern communities_community_edit ^community/(?P<id>.+)/edit(?:/(?P<command>.*))?>
<RegexURLPattern communities_community_detail ^community/(?P<id>.+)>
<RegexURLPattern communities_community_index ^community>
~~~
