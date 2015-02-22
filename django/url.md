# スクリプトネーム(SCRIPT_NAME...)

- WSGIHandlerでWEBリクエストを処理するときにSCRIPT_NAMEを処理している

## django.core.urlresolvers

### set_script_prefix() / get_script_prefix()

~~~
_prefixes = local()
~~~

~~~
def set_script_prefix(prefix):
    if not prefix.endswith('/'):
        prefix += '/' 
    _prefixes.value = prefix
~~~


~~~
def get_script_prefix():

    return getattr(_prefixes, "value", '/')
~~~

## django.core.handlers.wsgi

~~~
from django.core.urlresolvers import set_script_prefix

...
class WSGIHandler(base.BaseHandler):
	...
    def __call__(self, environ, start_response):
		...
		set_script_prefix(get_script_name(environ))
		...

~~~

~~~
def get_script_name(environ):
    script_url = get_bytes_from_wsgi(environ, 'SCRIPT_URL', '')
    if not script_url:
        script_url = get_bytes_from_wsgi(environ, 'REDIRECT_URL', '')

    if script_url:
        path_info = get_bytes_from_wsgi(environ, 'PATH_INFO', '')
        script_name = script_url[:-len(path_info)]
    else:
        script_name = get_bytes_from_wsgi(environ, 'SCRIPT_NAME', '')

    return script_name.decode(UTF_8)
~~~

# reverse()

- get_script_prefix() を使って、SCRIPT_NAME を頭に設定して返す
- mange.py shell で操作すると SCRIPT_NAMEがなかったりするのでモデルいれたデータとマッチしなかったりとか
- この動作をオーバーライドするには、 prefix='/' を引数に指定する

~~~
reverse('accounts_password_change, prefix='/')
~~~