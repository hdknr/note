Date: 2013-06-29 3:14
Title: Django:Admin: "View on site"リンク(サイト上で表示)
Type: post  
Excerpt:   

[Django Admin の View on site](https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/change_form.html#L35) リンク表示のテンプレート:


	{% if has_absolute_url %}
		<li>
			<a href="{% url 'admin:view_on_site' content_type_id original.pk %}" class="viewsitelink">{% trans "View on site" %}</a>
		</li>
	{% endif%}


[admin:view_on_site](https://github.com/django/django/blob/master/django/contrib/admin/sites.py#L235) のURLConf:

	url(r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$',
                wrap(contenttype_views.shortcut),
                name='view_on_site'),


[ContentTypeフレームワークのshortcut()が呼ばれている](https://github.com/django/django/blob/master/django/contrib/contenttypes/views.py#L9):


	def shortcut(request, content_type_id, object_id):

		#: モデルオブジェクト取得
		content_type = ContentType.objects.get(pk=content_type_id)
		obj = content_type.get_object_for_this_type(pk=object_id)
		
		#: モデルの絶対URLを取得
		get_absolute_url = obj.get_absolute_url
		absurl = get_absolute_url()
		
		#: httpで始まっていたらそのまま返す
		
		if absurl.startswith('http://') or absurl.startswith('https://'):
        	return http.HttpResponseRedirect(absurl)
        	
        #: そうじゃなかったら Siteオブジェクトをごにょごにょして、ドメイン名を取得してリダイレクトする
        protocol = 'https' if request.is_secure() else 'http'
        return http.HttpResponseRedirect('%s://%s%s'
                                         % (protocol, object_domain, absurl))
                                         
例えば、[Userモデルのget_absolute_url() ](https://github.com/django/django/blob/master/django/contrib/auth/models.py#L396): 

	    def get_absolute_url(self):
        	return "/users/%s/" % urlquote(self.username)
        	
と、/users/ユーザー名/ という決めになっているので、アプリケーションでURLConfとビューを用意すればいいということになります。

[get_absolute_url()に関するドキュメント](https://docs.djangoproject.com/en/dev/ref/models/instances/#get-absolute-url)


