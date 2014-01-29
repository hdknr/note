Date: 2013-09-30 15:00
Title: Django:認証ミドルウエアはユーザーをキャッシュする
Type: post  
Excerpt: 


[django.contrib.auth.middleware.AuthenticationMiddleware](https://github.com/django/django/blob/stable/1.5.x/django/contrib/auth/middleware.py#L14) では事前になにかしらのセッションミドルウエア(標準的には[django.contrib.sessions.middleware.SessionMiddleware](https://github.com/django/django/blob/stable/1.5.x/django/contrib/sessions/middleware.py#L8))がrequestオブジェクトにsessionオブジェクトをsetattrしている事を前提としています。

そして、そのsessionオブジェクトから情報を復元してdjango.contrib.auth.models.Userオブジェクトをrequestにsetattrするのですが、実際は遅延関数get_user()で _cached_userにセットしてそのそれを返しています。


    def get_user(request):
        if not hasattr(request, '_cached_user'):
            request._cached_user = auth.get_user(request)
        return request._cached_user
    
    
    class AuthenticationMiddleware(object):
        def process_request(self, request):
            request.user = SimpleLazyObject(lambda: get_user(request))
  


ので、一旦このミドルウェアの処理をしてしまったあとにさらにセッションの処理をしてget_userしても１つ前のセッションみどるウェアの処理でget_user()されてしまったキャッシュが帰ってしまいます。

ので、ミドルウェアのパイプラインの後ろにあるセッションミドルウェアなどで強制的に再度get_user()する場合は、


        delattr( request, '_cached_user' ) #:ログインユーザーをチャラパーにする
        AuthenticationMiddleware().process_request(request)

とかすればいいと思います。

ちなみに、auth.get_user(request)の実装は、

    def get_user(request):
        from django.contrib.auth.models import AnonymousUser
        try:
            user_id = request.session[SESSION_KEY]
            backend_path = request.session[BACKEND_SESSION_KEY]
            backend = load_backend(backend_path)
            user = backend.get_user(user_id) or AnonymousUser()
        except KeyError:
            user = AnonymousUser()
        return user

ということで、認証バックエンドのget_user( request.session["_auth_user_id"])でデータを戻しています。
