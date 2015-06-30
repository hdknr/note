mod_macro: /$appname で gunicorn アプリを複数定義する

## macro.conf

~~~xml
<Macro App $appname $port $base >
	# Gunicorn アプリケーションを /$appname の apache Loctionで受ける
    <Location /$appname/ >
      ProxyPass http://127.0.0.1:$port/$appname/
      ProxyPassReverse http://127.0.0.1:$port/$appname/

	  # Gunicorn アプリに SCRIPT_NAME を渡す
      RequestHeader set SCRIPT_NAME /$appname

    # RequestHeader set X-FORWARDED-SSL "on"
    # RequestHeader set X-FORWARDED_PROTO "https"
    </Location>

	# Django /$appname/static ファイルはリバースプロキシしない
    <Location /$appname/static/ >
        ProxyPass !
    </Location>

	# /$appname/static をapacheで配信させる
    Alias /$appname/static $base/web/static

</Macro>


<Macro Site $base>
 # サイト全体の定義
 ServerAdmin admin@you.com

 ProxyPreserveHost On

 LogLevel warn
 ErrorLog  $base/web/etc/apache2/logs/apache.error.log
 CustomLog $base/web/etc/apache2/logs/apache.access.log combined

 <Location / >
    Require all granted
 </Location>
</Macro>

<Macro Certs $site>
# 証明書関連 : /etc/apache/ssl/$site にシンボリックリンク作っておくとか
SSLEngine on
SSLCACertificateFile /etc/apache2/ssl/$site/ca.cert.pem
SSLCertificateFile /etc/apache2/ssl/$site/cert.pem
SSLCertificateKeyFile  /etc/apache2/ssl/$site/key.pem
</Macro>
~~~

# you.com.conf

- 先に macro.conf が読み込まれていること
- ` sudo a2enmod macro proxy proxy_http rewrite headers`

~~~xml
<VirtualHost *:80>
   ServerName   https://you.com
   ServerAlias  you.com
   RewriteCond %{HTTPS} off

   Use Site /home/vagrant/projects/yoursite
   
	# ここからgunicornアプリごとの設定ファイル
   Include sites-enabled/app1.inc
   Include sites-enabled/app2.inc
</VirtualHost>

<VirtualHost *:443>
    ServerName   https://you.com
    ServerAlias  you.com
    SetEnv HTTPS ON

    Use Certs you.com
    Use Site /home/vagrant/projects/yoursite

    RequestHeader set X-FORWARDED-SSL "on"
    RequestHeader set X-FORWARDED_PROTO "https"

	# ここからgunicornアプリごとの設定ファイル
   Include sites-enabled/app1.inc
   Include sites-enabled/app2.inc
</VirtualHost>
~~~

## $appname.inc

- たとえば app1.inc
- TCP9000で gunicornで受ける
- /etc/apache2/sites-enabledにシンボリックリンクしておく

~~~
Use App app1 9000 /home/vagrant/projects/yoursite/app1
~~~

## gunicornアプリ

- supervisord.conf.d/app1.ini とか

~~~ini
[program:app1]

command=/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/bin/gunicorn -c /home/vagrant/projects/yoursite/web/app/gunicorn.py app.wsgi:application  -b 127.0.0.1:9000
user=vagrant
autostart=true
autorestart=true
redirect_stderr=true
process_name=app1
~~~

## django でSCRIPT_NAMEの対応
- ミドルウエアでsettingsにパッチする

- settings.py

~~~py
MIDDLEWARE_CLASSES += (
    'app.middleware.SettingsMiddleware',   
)
~~~

- middleware.py

~~~py
from django.conf import settings

URLS = [
    'STATIC_URL',
    'LOGIN_URL',
    'LOGOUT_URL',
    'LOGIN_REDIRECT_URL', ]


class SettingsMiddleware(object):
    def process_request(self, request):
        prefix = request.META.get('SCRIPT_NAME')

        if prefix:
            for i in URLS:
                val = getattr(settings, i, None)
                if val and not val.startswith(prefix):
                    setattr(settings, i, prefix + val)
~~~                    
