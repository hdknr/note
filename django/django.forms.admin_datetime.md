Django: FormのDateTimeFieldにAdminのJSを適用

## forms.py

~~~py
from django import forms    
from django.conf import settings                                                        
from django.contrib.admin.widgets import AdminSplitDateTime                         
from django.contrib.admin.templatetags.admin_static import static                   
~~~

- [ModelAdmin で要求されるmedia](https://github.com/django/django/blob/master/django/contrib/admin/options.py#L555) をコピる

~~~py
    def admin_media():
        extra = '' if settings.DEBUG else '.min'
        js = [
            'core.js',
            'admin/RelatedObjectLookups.js',
            'jquery%s.js' % extra,
            'jquery.init.js',
            'actions%s.js' % extra,
            'urlify.js',
            'prepopulate%s.js' % extra,
        ]
        return forms.Media(
        	js=[static('admin/js/%s' % url) for url in js])    
~~~

~~~py
class YouForm(forms.Form):                                                     

    send_at = forms.DateTimeField(                                                  
        required=False,                                                             
        widget=AdminSplitDateTime,)                                                 

    @property                                                                       
    def admin_media(self):                                                          
        return admin_media()     
~~~

### js のオーダー

- Form.Media.js に定義するとすべてのjsをform.media['js'] で参照できるようになるが、jsの依存関係があるので、分離して別途レンダリング出来た方がよいかな

~~~py
class YouForm(forms.Form):                                                     

    class Media:
    	js = admin_media()                                                                       
~~~

## テンプレート

~~~html
{% block extrahead %}
{{ block.super }}
<script type="text/javascript" src="{% url 'admin:jsi18n' %}"></script>
{{ form.admin_media }}		{# 先にインクルードしておく #}
{{ form.media.css }}		{# フォームで必要とされるCSS #}
{% endblock %}
~~~

~~~html
{% block content %}
...
<form method="post"> {% csrf_token %}
<table>
 {{ form.as_table }}
</table>
<input type="submit" value="Send" />

{{ form.media.js }}		{# フォームで必要とされるJS #}

</form>
</div>
{% endblock %}
~~~
                                                           
    
