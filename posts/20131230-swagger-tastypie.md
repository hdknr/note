Date: 2013-12-30  5:50
Title: REST: Swagger UI でDjango TastypieのAPIドキュメンテーション自動生成
Type: post  
Excerpt:   



[Tastypiで作ったAPI](http://scriptogr.am/hdknr/post/django-10-tastypie)にSwagger UI でドキュメンテーションする。

インストール:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ pip install django-tastypie-swagger

    Downloading/unpacking django-tastypie-swagger
      Downloading django-tastypie-swagger-0.1.1.tar.gz (113kB): 113kB downloaded
      Running setup.py egg_info for package django-tastypie-swagger
        
    Installing collected packages: django-tastypie-swagger
      Running setup.py install for django-tastypie-swagger
        
    Successfully installed django-tastypie-swagger
    Cleaning up...
    
追加:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ vi app/settings.py
    
    
    INSTALLED_APPS += ( 
        'users',
        'tastypie',
        'tastypie_swagger',
    )


APIを再定義し、Swagger UI を追加:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ vi app/urls.py
   
   
    from users.api import UserResource
    from tastypie.api import Api 
    #
    users_api = Api( api_name='users' )
    users_api.register( UserResource() )
    #
    urlpatterns += patterns('',
       url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
       (r'', include(users_api.urls)),
    )


定義したAPIをSwaggerに設定:

    (v16)hdknr@wzy:~/ve/v16/src/pie$ vi app/settings.py

    TASTYPIE_SWAGGER_API_MODULE = 'app.urls.users_api'


http://wzy:9990/api/doc/ にアクセス:

<img src="https://www.evernote.com/shard/s302/sh/e8c2b7fd-7913-4c56-b3e1-eb2e72e34f94/9e08de630ce7a3a7d4ca7d2465157db9/res/65cc406e-de66-43c7-be6f-a01ada210104/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202013-12-30%205.36.01.png?resizeSmall&width=832">

<img src="https://www.evernote.com/shard/s302/sh/e8c2b7fd-7913-4c56-b3e1-eb2e72e34f94/9e08de630ce7a3a7d4ca7d2465157db9/res/3e3b0c1e-44dd-4fce-9269-59a125ff917a/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202013-12-30%205.36.09.png?resizeSmall&width=832">

<img src="https://www.evernote.com/shard/s302/sh/e8c2b7fd-7913-4c56-b3e1-eb2e72e34f94/9e08de630ce7a3a7d4ca7d2465157db9/res/b0e34ec7-05b6-4f5c-aac5-ddf036335835/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202013-12-30%205.37.32.png?resizeSmall&width=832">
