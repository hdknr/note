Date: 2013-10-02  9:00
Title: libpam-python : Django のユーザー認証を使ってみた  
Type: post  
Excerpt:   

Djangoとpysqlite(やMySQL-python)はvirtualenvじゃなくてsystemにインストール済。Djangoのプロジェクトを作る

    $ mkdir web ; django-admin.py startproject app web

app/setttings.py でDB設定修正:

    DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3', } } 
 

同じくadmin追加:

    INSTALLED_APPS += ('django.contrib.admin',)    
    
app/urls.py でadmin UI 有効：

    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
    
syncdb でDB初期化、管理者追加:        

    $ python manage.py syncdb        

runserverしてadmin UIでユーザーを追加:

    >>> from django.contrib.auth.models import User
    >>> [u.username for u in User.objects.all()]
    [u'admin', u'hdknr']        
    

dj_pam.py を用意：

    import os,sys,syslog
    from getpass import getuser, getpass
    #   
    NAME="DJ_AUTH"
    sys.path.insert(0,"/usr/local/lib/python2.7")
    sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages")
    #   
    # Djangoプロジェクトのパス追加
    PRJ_PATH= os.path.dirname( os.path.abspath(__file__))
    sys.path.insert(0, PRJ_PATH )
    sys.path.insert(0, os.path.join(PRJ_PATH ,'app'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
    #   
    def pam_sm_authenticate(pamh, flags, argv):
      from django.contrib.auth import authenticate
      #:現在のユーザーに対してパスワードを要求、Djangoに認証させる
      user = authenticate(username=getuser(),password=getpass() )
      if user:
          syslog.syslog("%s: %s is authenticated." % ( NAME,user.username) )
      return pamh.PAM_SUCCESS if user else pamh.PAM_AUTH_ERR 

chshに追加してみる:

    $ sudo vi /etc/pam.d/chsh      
    
    auth required pam_python.so /home/hdknr/ve/sandbox/src/any_auth/web/dj_auth.py
    
実行：

    $ chsh
    Password: (Djangoに登録した時のパスワード)
    Changing the login shell for hdknr
    Enter the new value, or press ENTER for the default
    	Login Shell [/bin/bash]: /bin/bash    
    	

syslog:

    $ sudo tail -f /var/log/syslog
    
    Oct  2 08:53:00 ubt3 DJ_AUTH[2518]: DJ_AUTH: hdknr is authenticated.
    Oct  2 08:53:02 ubt3 DJ_AUTH[2518]: changed user 'hdknr' shell to '/bin/bash'