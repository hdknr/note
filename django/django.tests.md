## Django Testing

- [Testing in Django](https://docs.djangoproject.com/en/1.8/topics/testing/)
- [Testing tools](https://docs.djangoproject.com/en/1.8/topics/testing/tools/)
- [Advanced testing topics](https://docs.djangoproject.com/en/1.8/topics/testing/advanced/)
- [Python Test cases](https://docs.python.org/3/library/unittest.html#test-cases)

### 実行

- [Writing and running tests](https://docs.djangoproject.com/en/1.8/topics/testing/overview/)

~~~
$ ./manage.py test
~~~


### `--keepdb` :データベースを削除させない

- 事前に test_{{ 実際のデータベース名 }} を作成する

~~~bash
$ python manage.py yourapp --keepdb
~~~


## Content Type fixture

- 作成

~~~
$ ./manage.py dumpdata contenttypes --indent 2
~~~

- content type なし

~~~
$ ./manage.py dumpdata --exclude contenttypes
~~~

## auth.permissionでハマるので

~~~
$ ./manage.py dumpdata --natural --exclude auth.permission --exclude contenttypes --indent 4  
~~~

## 負荷テスト

### locustio

- [locust](http://locust.io/)
- [locust docs](http://docs.locust.io/en/latest/index.html)

~~~
$ pip install locustio
~~~

- [Load testing django locustio](https://stackoverflow.com/questions/27261399/load-testing-django-locustio)

### Funkload

- [funkload](http://funkload.nuxeo.org/index.html)
