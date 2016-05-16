django-haystack + elasticsearch サンプル

＃ Debianパッケージインストール

~~~bash
$ cat debian.txt  | while read pkg ; do sudo apt-get install $pkg -y ;done
~~~

## Redis 確認

~~~bash
$ echo "info" | redis-cli  | grep port

tcp_port:6379
~~~

## Elasticsearch 確認

- [Elasticsearch](../elasticsearch.md)

# PYPI パッケージ

~~~bash
$ pip install -r requirements.txt
~~~

# Django プロジェクト初期化

~~~bash
$ django-admin statproject app web; cd web
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py startapp blog
~~~

## 設定

- settings.py

~~~python
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
INSTALLED_APPS += [
    'haystack',
    'blog',
]
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',  # NOQA
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
~~~

# モデル作成

- blog/models.py

~~~py
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
~~~

- マイグレーション

~~~bash
$ python manage.py makemigrations blog
$ python manage.py migrate blog
~~~

# 検索インターフェース

- app/search_indexes.py

~~~py
import datetime
from haystack import indexes
from blog.models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(
            pub_date__lte=datetime.datetime.now())
~~~

## 検索テンプレート

~~~bash
$ mkdir -p blog/templates/search/indexes/blog/
~~~

- blog/templates/search/search.html

~~~html
{% extends 'base.html' %}

{% block content %}
    <h2>Search</h2>

    <form method="get" action=".">
        <table>
            {{ form.as_table }}
            <tr>
                <td>&nbsp;</td>
                <td>
                    <input type="submit" value="Search">
                </td>
            </tr>
        </table>

        {% if query %}
            <h3>Results</h3>

            {% for result in page.object_list %}
                <p>
                    <a href="{{ result.object.get_absolute_url }}">{{ result.object.title }}</a>
                </p>
            {% empty %}
                <p>No results found.</p>
            {% endfor %}

            {% if page.has_previous or page.has_next %}
                <div>
                    {% if page.has_previous %}<a href="?q={{ query }}&amp;page={{ page.previous_page_number }}">{% endif %}&laquo; Previous{% if page.has_previous %}</a>{% endif %}
                    |
                    {% if page.has_next %}<a href="?q={{ query }}&amp;page={{ page.next_page_number }}">{% endif %}Next &raquo;{% if page.has_next %}</a>{% endif %}
                </div>
            {% endif %}
        {% else %}
            {# Show some example queries to run, maybe query syntax, something else? #}
        {% endif %}
    </form>
{% endblock %}
~~~

~~~bash
$ cat blog/templates/search/indexes/blog/note_text.txt
{{ object.title }}
{{ object.user.get_full_name }}
{{ object.body }}
~~~

# URLConf

- app/urls.py

~~~py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
]
~~~

# インデックス作成

- /admin/blog/note/ でデータ登録

- 再インデックス

~~~bash
$ python manage.py rebuild_index
~~~

- 更新

~~~bash
$ python manage.py update_index
~~~

# アクセス

- /search/?q={{ word }} で検索


# レイアウト

~~~
haystack
├── README.md
├── debian.txt
├── requirements.txt
└── web
    ├── app
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── search_indexes.py
    │   ├── templates
    │   │   ├── base.html
    │   │   └── search
    │   │       ├── indexes
    │   │       │   └── blog
    │   │       │       └── note_text.txt
    │   │       └── search.html
    │   ├── tests.py
    │   └── views.py
    ├── db.sqlite3
    └── manage.py

8 directories, 21 files
~~~

# その他

- [elasticsearchをつかったインデクシンング](elasticsearch_indexing.md)
- [celery-haystackでジョブキューでインデクシング](celery-haystack.md)
