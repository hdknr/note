Date: 2013-09-30  10:00
Title: Django:Csrfミドルウェア とセッションキー
Type: post  
Excerpt:   



# django Csrfミドルウェア #

django.middleware.csrf.CsrfViewMiddleware で標準的にCSRFプロテクションを実装しています。

    MIDDLEWARE_CLASSES = ( 
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    
# csrf_processing_done #


ビューの処理の前にCSRFトークンのチェックしている。([process_view](https://docs.djangoproject.com/en/dev/topics/http/middleware/#process-view)).

        if getattr(request, 'csrf_processing_done', False):
            return None

なので、process_requestの際に、csrf_processing_done=Trueにセットしてやれば通すかな？

    class SessionMiddleware(RootSessionMiddleware):
        def process_request(self, request):
            setattr(request,'csrf_processing_done',True)        #:強制的に処理済にする
            :
            :

とやれば {% csrf_token %}入れなくても 403でません。

# CSRFトークンのサニタイズ #

COOKIESに入っているCSRF_COOKIE_NAME ([デフォルトはcsrftoken](https://github.com/django/django/blob/master/django/conf/global_settings.py#L551) )
の値を[サニタイズします](https://github.com/django/django/blob/master/django/middleware/csrf.py#L62) 。:

    csrf_token = _sanitize_token(
        request.COOKIES[settings.CSRF_COOKIE_NAME])
    request.META['CSRF_COOKIE'] = csrf_token    

(ここで例外がおきると、新規にCSRFクッキーを request.META['CSRF_COOKIE']に[新規にクッキーを振ります](https://github.com/django/django/blob/master/django/middleware/csrf.py#L36) )


# csrf_exempt (免除) # 

REST呼び出しとか用にCSRFトークンをビューがわで免除したい時には csrf_exempt をたてると、ミドルウェアでCSRFトークンの検証をしません。
なので、免除したいビューの前に[デコレータ]( https://github.com/django/django/blob/stable/1.5.x/django/views/decorators/csrf.py#L69 )を入れるとビューの属性にestf_exempt=Trueを建ててくれます。

    from django.views.decoratros.csrf import csrf_exempt

    @csrf_exempt
    def article_post(request):
        # 
        #

# _dont_enforce_csrf_checks #

テストランナーなどが_dont_enforce_csrf_checksを建てているとCSRFトークンのチェックを無視してくれます。
テストの設定がめんどくさくないように。


# SSLの場合 #

## リファラがないリクエストはエラーとします ##

request.META['HTTP_REFERER']が設定されていないと403です。

## リファラと同じオーソリティじゃないとエラーとします(Same Origin)##

[same_origin]( https://github.com/django/django/blob/stable/1.5.x/django/utils/http.py#L224 ) チェックが通らないと403です。



# リクエストに埋められているトークンと一致しているかを確認します #

下記のどちらかに埋められているトークンがrequest.META['CSRF_COOKIE'] に一致すれば 403は出ません。

# 1. request.POST['csrfmiddlewaretoken'] #

フォームに入れられたパラメータからトークンを取得します。{% csrf_token %}でHIDDENで埋められているでしょう。

# 2. request.META['HTTP_X_CSRFTOKEN'] #

あるいは、JavascriptとかでHTTPのリクエストヘッダーに埋める場合も許すようです。



# process_response の処理 #

   
## CSRFトークンを処理しないケースがあります ##

### response.csrf_processing_done =True だと処理しません ###

アプリケーションで独自に処理したいとかの場合、これをセットするとミドルウェアは何もしません。


### request.META['CSRF_COOKIE'] == Noneだと処理しません ###

別のミドルウエアがリダイレクとしているときとか。

### request.META['CSRF_COOKIE_USED'] == Trueだと処理しません ###

テストの時とか？
    

##  それ以外はSetCookieします  ##

settings.CSRF_COOKIE_NAME クッキーにrequest.META["CSRF_COOKIE"] の値を適切に設定します。


# ちなみにセッションキーに関して #

django.contrib.auth.login で指定したユーザーでログインさせますが、ログイン前のセッション
(匿名ユーザー、あるいは別のクレデンシャル)で割り当てられていたセッションデータの
[SESSION_KEY](https://github.com/django/django/blob/stable/1.5.x/django/contrib/auth/__init__.py#L8)
が異なっていたら、セッションを[再構築](https://github.com/django/django/blob/stable/1.5.x/django/contrib/sessions/backends/base.py#L256)して、
おなじだったら[セッションキーを再利用](https://github.com/django/django/blob/stable/1.5.x/django/contrib/sessions/backends/base.py#L265)するようです。SESSION_KEYはサーバーの永続データの中のキーで「セッションキー(session.session_key)」はブラウザにSet-Cookieするときのキーの事なので注意。


    def login(request, user):
        if user is None:
            user = request.user
    
        if SESSION_KEY in request.session:
            if request.session[SESSION_KEY] != user.pk:
                # To avoid reusing another user's session, create a new, empty
                # session if the existing session corresponds to a different
                # authenticated user.
                request.session.flush()
        else:
            request.session.cycle_key()
        request.session[SESSION_KEY] = user.pk
        request.session[BACKEND_SESSION_KEY] = user.backend
        if hasattr(request, 'user'):
            request.user = user
        rotate_token(request)
        user_logged_in.send(sender=user.__class__, request=request, user=user)
