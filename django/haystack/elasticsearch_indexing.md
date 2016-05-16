elasticsearch backendによるインデックス作成


# update_index コマンドの動作

~~~py
In [1]: from haystack import connections as haystack_connections

In [2]: haystack_connections.connections_info.keys()
Out[2]: ['default']
In [3]: backends = _

In [4]: from haystack.utils.app_loading import haystack_load_apps                                                                                              
In [5]: haystack_load_apps()
Out[5]: ['admin', 'auth', 'contenttypes', 'sessions', u'haystack', 'blog']
In [6]: apps = _

In [7]: haystack_connections[backends[0]].get_backend()
Out[7]: <haystack.backends.elasticsearch_backend.ElasticsearchSearchBackend at 0x7f9132d5d790>
In [8]: backend = _

In [11]: haystack_connections[backends[0]].get_unified_index()
Out[11]: <haystack.utils.loading.UnifiedIndex at 0x7f9132d2f210>
In [12]: unified_index = _


In [15]: label = apps[5]
In [16]: label
Out[16]: 'blog'


In [21]: from haystack.utils.app_loading import haystack_get_models
In [22]: haystack_get_models(label)
Out[22]: <generator object get_models at 0x7f9132d59dc0>
In [23]: model = _.next()
In [24]: model
Out[24]: blog.models.Note

In [25]: index = unified_index.get_index(model)
In [26]: index
Out[26]: <blog.search_indexes.NoteIndex at 0x7f9132cbf188>

In [27]: using = backends[0]
In [28]: index.build_queryset(using=using)
Out[28]: [<Note: 平清盛の死因はインフルエンザか 謎の高熱に苦しんだ描写>, <Note: 東京五輪期間中、国学院高、都立青山高の一部も駐車場に借用か>]
In [29]: qs = _

In [33]: current_qs = qs[0:2]
In [34]: current_qs
Out[34]: [<Note: 平清盛の死因はインフルエンザか 謎の高熱に苦しんだ描写>, <Note: 東京五輪期間中、国学院高、都立青山高の一部も駐車場に借用か>]

In [35]: type(backend)
Out[35]: haystack.backends.elasticsearch_backend.ElasticsearchSearchBackend
In [36]: type(index)
Out[36]: blog.search_indexes.NoteIndex
In [37]: backend.update(index, current_qs)
~~~

# backend.update の実装

~~~py
In [20]: obj = current_qs[0]
In [21]: prepped_data = index.full_prepare(obj)
In [22]: type(prepped_data)
Out[22]: dict
In [23]: prepped_data.keys()
Out[23]: [u'django_id', 'author', 'text', u'django_ct', 'pub_date', u'id']

In [24]: backend.conn
Out[24]: <Elasticsearch([{u'host': '127.0.0.1', u'scheme': 'http', u'port': 9200}])>

In [25]: backend.index_name
Out[25]: 'haystack'

In [28]: final_data = dict((key, backend._from_python(value)) for key, value in prepped_data.items())
In [29]: final_data
Out[29]:
{'author': u'vagrant',
 u'django_ct': u'blog.note',
 u'django_id': u'1',
 u'id': u'blog.note.1',
 'pub_date': '2016-05-10T07:54:49+00:00',
 'text': u'\u5e73\u6e05\u76db\u306e\u6b7b...
}

In [32]: from haystack.constants import ID
In [33]: final_data['_id'] = final_data[ID]

In [34]: prepped_docs = [final_data]

In [35]: from elasticsearch.helpers import bulk


In [36]: bulk(backend.conn, prepped_docs, index=backend.index_name, doc_type='modelresult')
Out[36]: (1, [])

~~~

# use_template: テンプレートをつかってインデックス対象のテキストを作る

~~~py
In [1]: from blog.search_indexes import NoteIndex
In [2]: n = NoteIndex()
In [3]: qs = n.build_queryset(n.get_model())
In [4]: prepped_data = n.full_prepare(qs[0])
~~~
