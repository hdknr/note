Date: 2013-12-10  10:00
Title: Django: ５分でわかる Django REST Framework 
Type: post  
Excerpt:   

[quickstart](http://django-rest-framework.org/tutorial/quickstart)の写経です m(_ _)m

drf/app プロジェクト作成:

    (v16)hdknr@wzy:~/ve/v16/src$ mkdir drf
    (v16)hdknr@wzy:~/ve/v16/src$ django-admin.py startproject app drf

Django REST framework をインストール:

    (v16)hdknr@wzy:~/ve/v16/src$ pip install djangorestframework
    Downloading/unpacking djangorestframework
      Downloading djangorestframework-2.3.10.tar.gz (239kB): 239kB downloaded
      Running setup.py egg_info for package djangorestframework
        
    Installing collected packages: djangorestframework
      Running setup.py install for djangorestframework
        
    Successfully installed djangorestframework
    Cleaning up...

ストレージ初期化(sqlite3):

    (v16)hdknr@wzy:~/ve/v16/src$ cd drf/
    
    (v16)hdknr@wzy:~/ve/v16/src/drf$ python manage.py syncdb
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
    
    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'hdknr'): admin
    Email address: admin@admin.admin
    Password:  admin
    Password (again):  admin
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

users アプリケーション追加:

    (v16)hdknr@wzy:~/ve/v16/src/drf$ python manage.py startapp users
    
    (v16)hdknr@wzy:~/ve/v16/src/drf$ echo "INSTALLED_APPS += ('users',)" >> app/settings.py

usersアプリのシリアライザ作成。UserとGroupを配信:

    (v16)hdknr@wzy:~/ve/v16/src/drf$ cat << EOF > users/serializers.py

    > from django.contrib.auth.models import User, Group
    > from rest_framework import serializers
    > 
    > class UserSerializer(serializers.HyperlinkedModelSerializer):
    >     class Meta:
    >         model = User
    >         fields = ('url', 'username', 'email', 'groups')
    > 
    > class GroupSerializer(serializers.HyperlinkedModelSerializer):
    >     class Meta:
    >         model = Group
    >         fields = ('url', 'name')
    > 
    > EOF

userアプリにビューを追加:

    (v16)hdknr@wzy:~/ve/v16/src/drf$ cat << EOF >> users/views.py 

    > from django.contrib.auth.models import User, Group
    > from rest_framework import viewsets
    > from users.serializers import UserSerializer, GroupSerializer
    > 
    > class UserViewSet(viewsets.ModelViewSet):
    >     queryset = User.objects.all()
    >     serializer_class = UserSerializer
    > 
    > class GroupViewSet(viewsets.ModelViewSet):
    >     queryset = Group.objects.all()
    >     serializer_class = GroupSerializer
    > 
    > EOF
    
URLディスパッチャ追加:

    (v16)hdknr@wzy:~/ve/v16/src/drf$ cat << EOF >> app/urls.py 

    > from rest_framework import routers
    > from users import views
    > 
    > router = routers.DefaultRouter()
    > router.register(r'users', views.UserViewSet)
    > router.register(r'groups', views.GroupViewSet)
    > 
    > urlpatterns = patterns('',
    >     url(r'^admin/', include(admin.site.urls)),
    >     url(r'^', include(router.urls)),
    >     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    > )
    > 
    > EOF

settings.py に設定:

    (v16)hdknr@wzy:~/ve/v16/src/drf$ echo "INSTALLED_APPS += ('rest_framework',)" >> app/settings.py

    (v16)hdknr@wzy:~/ve/v16/src/drf$ cat << EOF >> app/settings.py

    > REST_FRAMEWORK = {
    >     'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    >     'PAGINATE_BY': 10
    > }
    > 
    > EOF

アプリ起動:

    (v16)hdknr@wzy:~/ve/v16/src/drf$ python manage.py runserver 0.0.0.0:9900
    Validating models...
    
    0 errors found
    December 10, 2013 - 01:07:38
    Django version 1.6, using settings 'app.settings'
    Starting development server at http://0.0.0.0:9900/
    Quit the server with CONTROL-C.


ホストOS(Mac）よりアクセス:

    Peeko:fabs hide$ curl -H 'Accept: application/json; indent=4' -u admin:admin http://wzy:9900/users/ 

    {
        "count": 1, 
        "next": null, 
        "previous": null, 
        "results": [
            {
                "url": "http://wzy:9900/users/1/", 
                "username": "admin", 
                "email": "admin@admin.admin", 
                "groups": []
            }
        ]
    }
    
    Peeko:fabs hide$ curl -H 'Accept: application/json; indent=4' -u admin:admin http://wzy:9900/users/1/
    {
        "url": "http://wzy:9900/users/1/", 
        "username": "admin", 
        "email": "admin@admin.admin", 
        "groups": []
    }
    
    Peeko:fabs hide$ curl  -I -H 'Accept: application/json; indent=4' -u admin:admin             http://wzy:9900/users/1/

    HTTP/1.0 200 OK
    Date: Tue, 10 Dec 2013 02:07:56 GMT
    Server: WSGIServer/0.1 Python/2.7.3
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN
    Content-Type: application/json; indent=4
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS