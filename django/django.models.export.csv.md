## CSV出力

### UnicodeWriteを用意

~~~py
class UnicodeWriter(object):
    def __init__(
        self, 
        stream, 	# HttpResponseかOSファイル
        dialect=None, encoding=None, errors="strict", **kwds
    ):
        self.writer = csv.writer(stream, dialect=dialect or csv.excel, **kwds)
        self.encoding = encoding or settings.DEFAULT_CHARSET
        self.errors = errors

    def writerow(self, row):
        self.writer.writerow(
            map(lambda s: force_text(s).encode(self.encoding), row))

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
~~~

### CsvReponseを用意

~~~py
class CSVResponse(HttpResponse):
    def __init__(
        self, content='', mimetype=None, status=None,
        content_type='application/octet-stream',
        filename=None, *args, **kwargs
    ):
        super(CSVResponse, self).__init__(
            content, mimetype, status, content_type)

        if filename:
			# Content-Dispositionに設定しないと結果がブラウザに帰る    
            self.set_filename(filename)

    def set_filename(self, filename):
        self['Content-Disposition'] = 'attachment; filename=%s' % filename
~~~

### CsvQuerySet を用意

~~~py
class CsvQuerySet(models.QuerySet):

    def export(self,
               stream, excludes=[], **kwargs):

        writer = UnicodeWriter(stream, **kwargs)
        names = tuple(
            (field.name, ugettext(field.verbose_name))
            for field in self.model._meta.fields
            if field.name not in excludes
        )

        writer.writerow([name[1] for name in names])
        for row in self.all():
            writer.writerow([getattr(row, name[0]) for name in names])
~~~

###  モデルにCsvQuerSetをマネージャとして追加

~~~py
class Application(Profile, BaseModel):
	...

    objects = models.Manager()		# デフォルトマネージャ
    csvs = CsvQuerySet.as_manager()	# CSVマネージャ
~~~

### ダウンロードビューを用意する

~~~py
@staff_member_required
def application_export(request):
    response = CSVResponse(filename="application.csv")
    models.Application.csvs.export(response, encoding="cp932")
    return response
~~~  

### ダウンロードビューをAdmin UIの右上メニューに追加

- キャンペーンアプリ(campaign)
- campaign/templates/admin/campaign/application/change_list.html

~~~html
{% extends "admin/change_list.html" %}
{% load i18n admin_urls admin_static admin_list %}

{% block object-tools-items %}
  {{ block.super }}
  <li>
    <a href="{% url 'campaign_application_export' %}">CSV出力</a>
  </li>
{% endblock %}
~~~                      