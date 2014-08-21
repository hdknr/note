SPNEGO: apacheのmod_auth_kerbを使わずにDjangoの認証ミドルウエアで認証する

Ubuntu/DebianでKerberos関係パッケージいれる(libapache2-mod-auth-kerbいれたらいろいろ入る):

    $ sudo apt-get install krb5-user libkrb5-dev -y
    
python-gssapi をpipで入れる

    $ pip install python-gssapi
    
    
Djangoのプロジェクトに app/middleware.pyを作る:

```py

    from django.contrib import auth
    from django.contrib.auth.models import User
    from django.conf import settings
    from django.http import HttpResponse
    import uuid
    import gssapi
    import base64

    def create_user_from(peer_name):
        ''' peer_name がKerberosで帰って来た時にユーザーをロード
        もしくは作成するユーティリティ '''
        
        try:
            return User.objects.get(username=peer_name)

        except User.DoesNotExist:
            user = User.objects.create_user(
                username=peer_name,
                password=uuid.uuid1().hex,    # パスワード適当ランダム
                email=peer_name,)             
            return user
        return None
                

    class AuthMiddleware(object):
        ''' 認証ミドルウエア本体 '''
        
        def process_request(self, request):
            out_token = None

            if request.META.get('HTTP_AUTHORIZATION','').startswith('Negotiate '):
               
                # KDC/Domain ControllerとSPNで接続
                service_name = gssapi.Name(settings.SPN, gssapi.C_NT_HOSTBASED_SERVICE)
                server_cred = gssapi.Credential(service_name, usage=gssapi.C_ACCEPT)
                ctx = gssapi.AcceptContext(server_cred)

        　　　　　# Negotiateトークンを検証
                in_token = base64.b64decode(request.META['HTTP_AUTHORIZATION'][10:])
                out_token = ctx.step(in_token)

                if ctx.established:     # Negotiatedされた
                    
                    user = create_user_from(str(ctx.peer_name))    #:Djangoのローカルユーザー取得
                    
                    if user:
                        user.backend = 'django.contrib.auth.backends.ModelBackend' 
                        auth.login(request, user)                      # 認証
                        setattr(request, "spnego_token", out_token)    # Responseで使う
                        return None                                  　# 処理継続

            # ブラウザにKDC/Domain ControllerにNegatiateした結果を返してもらう
            response = HttpResponse(status = 401)
            response['WWW-Authenticate'] = 'Negotiate %s' % (
                out_token and base64.b64encode(out_token) or ''
            )
            return response
                

        def process_response(self, request, response):
            ''' トークンがあったらまたブラウザに運んでもらう '''
            out_token = getattr(request, "spnego_token", None)
            if out_token:
                response['WWW-Authenticate'] = 'Negotiate %s' % base64.b64encode(out_token)

            return response
                
```

settings.py:

```py

    import os
    
    INSTALLED_APPS += (
        'todo',
    )

    MIDDLEWARE_CLASSES += (
        'app.middleware.AuthMiddleware',
    )
    os.environ['KRB5_KTNAME'] = '/etc/hdknr.krb5.http.keytab'    #Keytabファイルを $KRB5_KTNAMEに設定
    SPN = 'HTTP@ubuntu.openid.local'                        　　　#サービスプリンシパル名
```

    
Active DirectoryでSPNとKeytabファイルの作り方とブラウザの設定は[こちらと同じ](http://qiita.com/hidelafoglia/items/00916344b6f314ae07b2)   


                
