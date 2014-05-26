Mezzanine:ガラケ対応

[Mezzanine](http://mezzanine.jupo.org/)をガラケ対応してみる。

settings.DEVICE_USER_AGENTSにエージェントを登録.

mezzanine.core.middleware.TemplateForDeviceMiddlewareで、

```py

    tuple('デバイス', tuple('エージェント1', 'エージェント2',..))
```

 をループで判別して、現在のデバイスを判定し、判定した'デバイス/'を指定された
 テンプレート名の頭に挿入してリストを返す(mezzanine.utils.device.templates_for_device())。

例えば、サイトルートがアクセスされると、テンプレートリストは以下になるので、:

```py

    [u'pages/index.html', u'pages/index/richtextpage.html', u'pages/richtextpage.html', u'pages/page.html']
```

ミドルウェアは、

```py

    [u'デバイス/pages/index.html', u'pages/index.html', u'デバイス/pages/index/richtextpage.html', 
    u'pages/index/richtextpage.html', u'デバイス/pages/richtextpage.html', u'pages/richtextpage.html', 
    u'デバイス/pages/page.html', u'pages/page.html']
```

を返します。

デバイスの判定は、'エージェントn' の文字列が request.META["HTTP_USER_AGENT"].lower() の文字列にふく
まれ手いるかどうかだけで判定するので、 スマホの判定をガレケの判定の前にいれないと、DoCoMoのAndroidが
ガラケ扱いされてしまうこともある。

phone アプリを Mezzaineに追加し、:

    python manage.py startapp phone

settins.py:

    INSTALLED_APPS += (
        'phone',
    )


mezzanine.mobile.templatesとmezzanine.mobile.staticをコピってHTMLを作成。
extends のパスを "phone/" にするなどして修正:

    sample
    ├── phone
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── models.py
    │   ├── models.pyc
    │   ├── static
    │   │   ├── css
    │   │   │   ├── global-mobile.css
    │   │   │   └── mobile.rtl.css
    │   │   └── img
    │   │       ├── icon-home.png
    │   │       └── mobile-bg.gif
    │   └── templates
    │       └── phone
    │           ├── 404.html
    │           ├── 500.html
    │           ├── base.html
    │           ├── blog
    │           │   ├── blog_post_detail.html
    │           │   └── blog_post_list.html
    │           ├── includes
    │           │   ├── footer_scripts.html
    │           │   ├── pagination.html
    │           │   └── search.html
    │           ├── index.html
    │           ├── pages
    │           │   ├── form.html
    │           │   ├── index.html
    │           │   ├── menus
    │           │   │   └── phone.html
    │           │   ├── page.html
    │           │   └── richtextpage.html
    │           └── search_results.html

    
local_settings.pyにDEVICE_USER_AGENTSを作成:

```py

    DEVICE_USER_AGENTS = ( 
        ("mobile", ("Android", "BlackBerry",
                    "iPhone", "iPad", "iPod", "Windows Phone")),
        ("phone", ('DoCoMo', 'SoftBank', 'KDDI', 'Vodafone',
                   'Nokia', 'MOT-', 'J-PHONE', 'BlackBerry', 'Symbian',)),
    )
```


サイトテーマ使うならば、

    sample/static/テーマ名/phone/...
    sample/templates/テーマ名/phone/...

のパスに作れば良さそう。
