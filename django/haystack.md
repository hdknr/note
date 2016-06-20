- [Welcome to Haystack!](http://django-haystack.readthedocs.io/en/v2.4.1/)
- [django-haystack/django-haystack](https://github.com/django-haystack/django-haystack)
- [Django製サイトにSphinx製ドキュメントを導入する方法](http://d.hatena.ne.jp/hirokiky/20120707/1341645096)
- [Implementing Search In Django Site Using HayStack And Xapian / Whoosh](http://www.nitinh.com/2009/10/implementing-search-in-django-site-using-haystack-and-xapian-whoosh/)


# Whoosh

- https://bitbucket.org/mchaput/whoosh/overview
- [RTD](http://whoosh.readthedocs.io/en/latest/)
- [pythonのwhooshで全文検索してみる](http://blanktar.jp/blog/2013/04/python-woosh.html)
- [whooshで日本語検索](http://takaki-web.media-as.org/blog/w6f01k/)
- [Whoosh用の日本語トークナイザ(IgoTokenizer)](http://hideaki-t.blogspot.jp/2011/02/whooshigotokenizer.html)
- [[Python] Python純正の全文検索ライブラリ、Whooshを使ってみた](http://tdoc.info/test/2011/04/20/2011-04-20.html)

## IgoTokenizer

- https://pypi.python.org/pypi/whoosh-igo



# Elasticsearch

- [Elasticsearch](elasticsearch.md)
- [haystack](haystack.md)


# Command

- haystack_info

~~~bash
$ python manage.py haystack_info
Number of handled 1 index(es).
  - Model: Note by Index: <blog.search_indexes.NoteIndex object at 0x7f9c92ae8668>
~~~  

# SearchQuerySet API

- [SearchQuerySet API](http://django-haystack.readthedocs.io/en/v2.4.1/searchqueryset_api.html#ref-searchqueryset-api)

~~~py
In [1]: from haystack.query import SearchQuerySet
In [2]: all_results = SearchQuerySet().all()
In [3]: type(all_results)
Out[3]: haystack.query.SearchQuerySet
In [4]: all_results.count()
Out[4]: 2
~~~

~~~py
In [9]: SearchQuerySet().filter(text=u'東京五輪').count()
Out[9]: 1

In [10]: SearchQuerySet().filter(text=u'東京五輪')[0]
Out[10]: <SearchResult: blog.note (pk=u'2')>

In [12]: res.model
Out[12]: blog.models.Note

In [14]: print res.text[:10]
東京五輪期間中、国学

In [15]: res.object
Out[15]: <Note: 東京五輪期間中、国学院高、都立青山高の一部も駐車場に借用か>

In [17]: print res.object.body[:10]
２０２０年東京五輪
~~~
