Date: 2013-12-10  10:30
Title: Django: 10分でわかる Tastypie  
Type: post  
Excerpt:   

[Tastypie](http://tastypieapi.org/) を動かしてみる。

django-tastypieインストール:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ pip install django-tastypie
    Downloading/unpacking django-tastypie
      Downloading django-tastypie-0.11.0.tar.gz (727kB): 727kB downloaded
      Running setup.py egg_info for package django-tastypie
        
        warning: no files found matching 'VERSION'
    Downloading/unpacking python-mimeparse>=0.1.4 (from django-tastypie)
      Downloading python-mimeparse-0.1.4.tar.gz
      Running setup.py egg_info for package python-mimeparse
        
    Downloading/unpacking python-dateutil>=1.5,!=2.0 (from django-tastypie)
      Downloading python-dateutil-2.2.tar.gz (259kB): 259kB downloaded
      Running setup.py egg_info for package python-dateutil
        
    Requirement already satisfied (use --upgrade to upgrade): six in /home/hdknr/ve/v16/lib/python2.7/site-packages (from python-dateutil>=1.5,!=2.0->django-tastypie)
    Installing collected packages: django-tastypie, python-mimeparse, python-dateutil
      Running setup.py install for django-tastypie
        
        warning: no files found matching 'VERSION'
      Running setup.py install for python-mimeparse
        
      Running setup.py install for python-dateutil
        
    Successfully installed django-tastypie python-mimeparse python-dateutil
    Cleaning up...


プロジェクト作成:

    (v16)hdknr@wzy:~/ve/v16/src$ mkdir pie
    (v16)hdknr@wzy:~/ve/v16/src$ django-admin.py startproject app pie
    (v16)hdknr@wzy:~/ve/v16/src$ cd pie/


users アプリ追加:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ python manage.py startapp users


usersのApi作成:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ vi users/api.py

    from django.contrib.auth.models import User,Group
    from tastypie.resources import ModelResource
    
    class UserResource(ModelResource):
        class Meta:
            queryset = User.objects.all()
            resource_name = 'user'

URLConf に追加:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ vi app/urls.py 
    
    #
    from users.api import UserResource
    user_resource = UserResource()
    urlpatterns += patterns('',
        (r'^users/', include(user_resource.urls)),
    )

settings.py にアプリ追加:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ vi app/settings.py
    
    INSTALLED_APPS += ( 
        'users',
        'tastypie',
    )


ストレージ初期化:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ python manage.py syncdb
    Creating tables ...
    Creating table django_admin_log
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_groups
    Creating table auth_user_user_permissions
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table tastypie_apiaccess
    Creating table tastypie_apikey
    
    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'hdknr'): admin
    Email address: admin@admin.admin
    Password: 
    Password (again): 
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)


アプリ起動:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ python manage.py runserver 0.0.0.0:9900
    Validating models...
    
    0 errors found
    December 10, 2013 - 01:30:42
    Django version 1.6, using settings 'app.settings'
    Starting development server at http://0.0.0.0:9900/
    Quit the server with CONTROL-C.


アクセス :

    Peeko:fabs hide$ curl  -H 'Accept: application/json'  http://wzy:9900/users/user/

    {"meta": 
        {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1}, 
     "objects": [
        {"date_joined": "2013-12-10T01:30:25.410285", 
            "email": "admin@admin.admin", 
            "first_name": "", 
            "id": 1, 
            "is_active": true, 
            "is_staff": true, 
            "is_superuser": true, 
            "last_login": "2013-12-10T01:30:25.410285", 
            "last_name": "", 
            "password": "pbkdf2_sha256$12000$WLuzYyPv4T6T$McayMCAe6Ll9Ud0lEf+2hAqAUe8Sjn+2Oymiq+wmF3U=", 
            "resource_uri": "/users/user/1/", 
            "username": "admin"}]}


    }
    
    Peeko:fabs hide$ curl  -H 'Accept: application/json'  http://wzy:9900/users/user/1/

    {"date_joined": "2013-12-10T01:30:25.410285", 
         "email":"admin@admin.admin", 
         "first_name": "", 
         "id": 1, 
         "is_active": true, 
         "is_staff": true, 
         "is_superuser": true, 
         "last_login": "2013-12-10T01:30:25.410285", 
         "last_name": "", 
         "password": "pbkdf2_sha256$12000$WLuzYyPv4T6T$McayMCAe6Ll9Ud0lEf+2hAqAUe8Sjn+2Oymiq+wmF3U=", 
         "resource_uri": "/users/user/1/", 
         "username": "admin"}
         
         
    Peeko:fabs hide$ curl  -I -H 'Accept: application/json'  http://wzy:9900/users/user/1/

    HTTP/1.0 405 METHOD NOT ALLOWED
    Date: Tue, 10 Dec 2013 02:23:38 GMT
    Server: WSGIServer/0.1 Python/2.7.3
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html; charset=utf-8
    Allow: GET,POST,PUT,DELETE,PATCH         