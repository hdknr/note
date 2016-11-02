- http://qiita.com/nbtakusaito/items/bdd338bdb581b602cc1e
- http://tech.pjin.jp/blog/2015/12/15/%E3%80%90%E7%AC%AC5%E5%9B%9E%E3%80%91%E3%80%8Cangularjs%E3%80%8D%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F%E3%81%84%EF%BC%81%E3%80%80%EF%BD%9Ehtml%E3%83%86%E3%83%B3%E3%83%97/
- http://www.slideshare.net/muneakinishimura/angularjs-3734265  8
- http://www.spiceworks.co.jp/blog/?p=6470
- http://qiita.com/nbtakusaito/items/bdd338bdb581b602cc1e
- https://angularjs.org/
- http://angular-js.net/qa/

- http://glynjackson.org/weblog/tutorial-using-angularjs-django/
- http://stackoverflow.com/questions/8302928/angularjs-with-django-conflicting-template-tags
- https://thinkster.io/django-angularjs-tutorial

# ui-grid

- https://github.com/angular-ui/ui-grid
- http://qiita.com/s_edward/items/a36734836f8baba2b11d

- http://www.jeasyui.com/documentation/treegrid.php
- http://study-upup.blogspot.jp/2014/03/jqueryjquery.html
- http://stackoverflow.com/questions/26565518/angularjs-repeat-with-table-and-rowspan
- http://stackoverflow.com/questions/29878928/angularjs-ng-repeat-colspan-rowspan-issue

# jquery

- http://stackoverflow.com/questions/22275590/how-to-apply-jquery-after-angularjs-partial-template-is-loadedk
- http://dev.classmethod.jp/client-side/javascript/angularjsandjquery/

# ng-repeat

- http://stackoverflow.com/questions/15412897/how-to-obtain-previous-item-in-ng-repeat
- http://stackoverflow.com/questions/27776855/how-to-compare-values-inside-ng-repeat

# ng-app

- ng-app ディレクティブを付けたタグの中が、 AngularJS のテンプレートとして処理される。


# 日付

- http://iwb.jp/angularjs-date-japanese/
- http://js.studio-kingdom.com/angularjs/ng_filter/date

## date フィルター

- [日付／時刻データを整形するには？（date）](http://www.buildinsider.net/web/angularjstips/0027)

~~~html
{{updated_at | date: 'yyyy年M月d日（EEE）a hh時mm分ss秒'}}
~~~

# テンプレート

## ng-bind

- [ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)

~~~html
<span ng-bind="name"></span>
~~~

## django `verbatim`

~~~html
{% verbatim %}
    {{ name }}
{% endverbatim %}
~~~

# CORS

~~~py
response = HttpResponse(json.dumps(output), content_type="application/json")
response["Access-Control-Allow-Origin"] = "*"
response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
response["Access-Control-Max-Age"] = "1000"
response["Access-Control-Allow-Headers"] = "*"
return response
~~~
