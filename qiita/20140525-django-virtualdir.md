Django: SCRIPT_NAMEについて


http://yoursite.com/apps を GunicornのDjangoにリバースプロキシさせる

# apacheの場合の設定
a2enmod proxy http_proxy headersしておく

```xml

        ProxyPass /apps/static !
        Alias /apps/static /home/system/apps/web/static
        ProxyPreserveHost On

        ProxyPreserveHost On
        <Location /apps/ >
        ProxyPass http://127.0.0.1:8000/apps/
        ProxyPassReverse http://127.0.0.1:8000/apps/
        RequestHeader set SCRIPT_NAME /apps
        
        RequestHeader set X-FORWARDED-PROTOCOL ssl    # for 443
        RequestHeader set X-FORWARDED-SSL on          # for 443
        </Location>

```

- Locationの名前を ProxyのURLにくっつける
- SCRIPT_NAME を Locationの名前       
- /apps/static はapacheに処理させる (manage.py collectstatic したパスをAliasする) 
- nginxの場合は[こんな感じ](http://lazylabs.org/blog/django-under-sub-url-powered-by-uwsgi-behind-nginx/)
    - ただし、ADMIN_MEDIA_PREFIXは廃止なので注意


# context processorを用意して STATIC_URLにパッチあてる

request.META['SCRIPT_NAME'] を settings.STATIC_URLの前に追加する。テンプレートのレンダリングまえにごにょる。

```py

    from django.core.urlresolvers import reverse
    from django.conf import settings

    def global_context(request):
        if all([
            request.META['SCRIPT_NAME'] ,
            not settings.STATIC_URL.startswith(request.META['SCRIPT_NAME'])]):
        settings.STATIC_URL = request.META['SCRIPT_NAME'] +  settings.STATIC_URL        
        
        return {}    #: 必要であればコンテキスト返す
```

テンプレートのタグのstaticがsetting.STATIC_URLをベースにファイルをリゾルブするので。アプリのHTMLはなんとでもなるが、adminのテンプレートはこうでもしないと。

    {% static "admin/css/base.css" %}
    

## コードを修正するとうまく行かない

- urls.pyとかviews.pyのコードを修正して gunicornをリスタートすると、context processorの処理が動かない(ことが多い？)
- 再度 conext processorの*.pyc を削除して、リスタートするとうまく行く   
- うまく行かない時もcontext processor はコールされているので、何らかの理由でstaticタグが、それを参照できていない、あるいはcontext processor が動く前にテンプレートタグが呼ばれているのかな？
    - ダメな場合は contextモジュールがテンプレートタグの処理の後に呼ばれています     


# ミドルウエアだったら大丈夫かも

大丈夫っぽい

```py

    from django.conf import settings
    
    class SettingsMiddleware(object):
        def process_request(self, request):
            prefix = request.META.get('SCRIPT_NAME')
            if all([
                prefix,
                not settings.STATIC_URL.startswith(prefix),]):
                settings.STATIC_URL = prefix + settings.STATIC_URL
    
    MIDDLEWARE_CLASSES += (
        'app.middleware.SettingsMiddleware',
    )
```

# admin_static テンプレートタグ

dajngo/contrib/admin/templatetags/admin_static.py。statifiles.staticが実際のadmin_staic タグを処理する:

```py

    if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
        from django.contrib.staticfiles.templatetags.staticfiles import static
    else:
        from django.templatetags.static import static

    static = register.simple_tag(static)
```

staticfilesがデフォルトで設定されているので、django/contrib/staticfiles/templatetags/staticfiles.py:

```py

    from django.contrib.staticfiles.storage import staticfiles_storage
    def static(path):
         return staticfiles_storage.url(path)

django/contrib/staticfiles/storage.py

    class ConfiguredStorage(LazyObject):
        def _setup(self):
            self._wrapped = get_storage_class(settings.STATICFILES_STORAGE)()

    staticfiles_storage = ConfiguredStorage()

```
    
django/core/files/storage.py:
    
```py

    from django.utils.module_loading import import_by_path
    def get_storage_class(import_path=None):
         return import_by_path(import_path or settings.DEFAULT_FILE_STORAGE)
```    

今の環境:

```py

    >>> from django.conf import settings
    >>> settings.STATICFILES_STORAGE
    'django.contrib.staticfiles.storage.StaticFilesStorage'
```
    
    
django/contrib/staticfiles/storage.py で、 StaticFilesStorageが引数無しで呼ばれるので、
base_urlがsettings.STATIC_URLをそのまま参照。settings.STATIC_URLにパッチ当たってないケースが:

```py

    from django.core.files.storage import FileSystemStorage
    ..

    class StaticFilesStorage(FileSystemStorage):
        """
        Standard file system storage for static files.
    
        The defaults for ``location`` and ``base_url`` are
        ``STATIC_ROOT`` and ``STATIC_URL``.
        """
        def __init__(self, location=None, base_url=None, *args, **kwargs):
            if location is None:
                location = settings.STATIC_ROOT
            if base_url is None:
                base_url = settings.STATIC_URL
            check_settings(base_url)
            super(StaticFilesStorage, self).__init__(location, base_url,
                                                     *args, **kwargs)
            # FileSystemStorage fallbacks to MEDIA_ROOT when location
            # is empty, so we restore the empty value.
            if not location:
                self.base_location = None
                self.location = None
```
                
#  SCRIPT_NAMEの扱い

django/core/handlers/wsgi.pyで２カ所

## 環境変数取得してrequest.METAにセットしている

```py

    class WSGIRequest(http.HttpRequest):
        def __init__(self, environ):
            script_name = base.get_script_name(environ)
            path_info = base.get_path_info(environ)
            if not path_info:
                # Sometimes PATH_INFO exists, but is empty (e.g. accessing
                # the SCRIPT_NAME URL without a trailing slash). We really need to
                # operate as if they'd requested '/'. Not amazingly nice to force
                # the path like this, but should be harmless.
                path_info = '/' 
            self.environ = environ
            self.path_info = path_info
            self.path = '%s/%s' % (script_name.rstrip('/'), path_info.lstrip('/'))
            self.META = environ
            self.META['PATH_INFO'] = path_info
            self.META['SCRIPT_NAME'] = script_name
            ....
        
```

## urlresovlersに渡している

これとは別にurlresovlersに現在のSCRIPT_NAMEを渡していて、reverseとか諸々の処理はそっちでよろしくやっている

```py

    from django.core.urlresolvers import set_script_prefix
    
    class WSGIHandler(base.BaseHandler):
        initLock = Lock()
        request_class = WSGIRequest
    
        def __call__(self, environ, start_response):
            # Set up middleware if needed. We couldn't do this earlier, because
            # settings weren't available.
            if self._request_middleware is None:
                with self.initLock:
                    try:
                        # Check that middleware is still uninitialised.
                        if self._request_middleware is None:
                            self.load_middleware()
                    except:
                        # Unload whatever middleware we got
                        self._request_middleware = None
                        raise
    
            set_script_prefix(base.get_script_name(environ))
            signals.request_started.send(sender=self.__class__)
            try:
                request = self.request_class(environ)
            except UnicodeDecodeError:
                logger.warning('Bad Request (UnicodeDecodeError)',
                    exc_info=sys.exc_info(),
                    extra={
                        'status_code': 400,
                    }
                )
                response = http.HttpResponseBadRequest()
            else:
                response = self.get_response(request)
    
            response._handler_class = self.__class__
    
            status = '%s %s' % (response.status_code, response.reason_phrase)
            response_headers = [(str(k), str(v)) for k, v in response.items()]
            for c in response.cookies.values():
                response_headers.append((str('Set-Cookie'), str(c.output(header=''))))
            start_response(force_str(status), response_headers)
            return response
                
```

# 正しいやり方

- settings ってimmutableな物だから動的に変更するってのはおかしいんじゃないか？とか
- 確実なのは、environにPREFIX定義して、settings.py:

        STATIC_URL = os.environ.get('PREFIX', '') + '/static/' 
        
- WSGIリクエスト毎に設定変更かえたいのであれば、ミドルウエアのprocess_requestの中でsettingsを修正するといいかも
- urlresolversみたいにそもそもその他のモジュールもSCRIPT_NAMEで判断するフック入れた方がいいんじゃないか
