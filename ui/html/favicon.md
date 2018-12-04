# favicon

## パス指定

ICO形式 : [ICO (file format) - Wikipedia](https://en.wikipedia.org/wiki/ICO_%28file_format%29):

~~~html
<link rel="icon" type="image/x-icon" href="{% static 'yoursite/images/favicon.ico' %}" />
~~~

PNG:

~~~html
<link rel="icon" type="image/png" href="{% static 'yoursite/images/favicon.ico' %}" />
~~~

IE8:

~~~html
<link rel="shortcut icon" type="image/x-icon" href="{% static 'yoursite/images/favicon.jpg' %}" />
~~~

## Django リダイレクト

[python - WARNING Not Found: /favicon.ico - Stack Overflow](https://stackoverflow.com/questions/9371378/warning-not-found-favicon-ico):

urls.py:

~~~py
from django.views.generic import RedirectView

url_patterns=[
    ...

    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
~~~


## 記事

- [正しいfaviconの設定方法を対応ブラウザ別にまとめる | Glatch（グラッチ） – 夫婦で活動するフリーランスWeb制作ユニット](https://glatchdesign.com/blog/web/coding/943)
- [【2018年版】ホームページのタブ画像(favicon/touch-icon)作成と設定方法まとめ – 新宿のWeb制作会社Btiesが教える！ホームページ制作のすべて](https://homepagenopro.com/html/favicon.html)
