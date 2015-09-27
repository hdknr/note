## Reverse URL

- [Getting Django admin url for an object](https://stackoverflow.com/questions/694477/getting-django-admin-url-for-an-object)

~~~
{% url 'admin:index' %}
{% url 'admin:polls_choice_add' %}
{% url 'admin:polls_choice_change' choice.id %}
{% url 'admin:polls_choice_changelist' %}
~~~


## テンプレートカスタマイズ

### カスタマイズ可能

- [Templates which may be overridden per app or model](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#templates-which-may-be-overridden-per-app-or-model)

- app_index.html
- change_form.html
- change_list.html
- delete_confirmation.html
- object_history.html


## モデルレベル

- emailqueueアプリの `Mail` モデルのカスタマイズ

~~~
$ tree emailqueue/templates/
emailqueue/templates/
└── admin
    └── emailqueue
        └── mail
            └── change_form.html

3 directories, 1 file
~~~

- `./django/contrib/admin/templates/admin/change_form.html` をコピーしてカスタマイズする。
- あるいは extends する。以下のようにすると "Mailを変更" の下にリストをだす。

~~~
{% extends "admin/change_form.html" %}

{% block content %}
<div>
  <ul>
    <li> aaaa
    <li> bbbb
    <li> ccc
  </ul>
</div>
{{ block.super }}
{% endblock %}
~               
~~~

### メニュー追加

- `{% block object-tools-items %}` をオーバーライドして、`<li><a href="__url__">メニューリンク</a></li>` を追加していく。

~~~
{% extends "admin/change_form.html" %}

{% block object-tools-items %}
<li><a href="#">aaaa</a></li>
<li><a href="#">bbbb</a></li>
{{ block.super }}
{% endblock %}
~~~

## 変数(django/contrib/admin/options.py)

- [github master](https://github.com/django/django/blob/master/django/contrib/admin/options.py)

~~~
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        opts = self.model._meta                                                      
        app_label = opts.app_label                                                   
        preserved_filters = self.get_preserved_filters(request)                      
        form_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, form_url)
        view_on_site_url = self.get_view_on_site_url(obj)                            
        context.update({                                                             
            'add': add,                                                              
            'change': change,                                                        
            'has_add_permission': self.has_add_permission(request),                  
            'has_change_permission': self.has_change_permission(request, obj),   
            'has_delete_permission': self.has_delete_permission(request, obj),   
            'has_file_field': True,  # FIXME - this should check if form or formsets have a FileField,
            'has_absolute_url': view_on_site_url is not None,                        
            'absolute_url': view_on_site_url,                                        
            'form_url': form_url,                                                    
            'opts': opts,                                                            
            'content_type_id': get_content_type_for_model(self.model).pk,            
            'save_as': self.save_as,                                                 
            'save_on_top': self.save_on_top,                                         
            'to_field_var': TO_FIELD_VAR,                                            
            'is_popup_var': IS_POPUP_VAR,                                            
            'app_label': app_label,                                                  
        })                                                                           
        if add and self.add_form_template is not None:                               
            form_template = self.add_form_template                                   
        else:                                                                        
            form_template = self.change_form_template                                

        request.current_app = self.admin_site.name                                   

        return TemplateResponse(request, form_template or [                          
            "admin/%s/%s/change_form.html" % (app_label, opts.model_name),           
            "admin/%s/change_form.html" % app_label,                                 
            "admin/change_form.html"                                                 
        ], context)                                                                  
~~~

~~~
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    	...
        adminForm = helpers.AdminForm(                                               
            form,                                                                    
            list(self.get_fieldsets(request, obj)),                                  
            self.get_prepopulated_fields(request, obj),                              
            self.get_readonly_fields(request, obj),                                  
            model_admin=self)

        media = self.media + adminForm.media

        inline_formsets = self.get_inline_formsets(
        	request, formsets, inline_instances, obj)
        for inline_formset in inline_formsets:                                       
            media = media + inline_formset.media                                     

        context = dict(self.admin_site.each_context(request),                        
            title=(_('Add %s') if add else _('Change %s')) % force_text(opts.verbose_name),
            adminform=adminForm,                                                     
            object_id=object_id,                                                     
            original=obj,                                                            
            is_popup=(IS_POPUP_VAR in request.POST or                                
                      IS_POPUP_VAR in request.GET),                                  
            to_field=to_field,                                                       
            media=media,                                                             
            inline_admin_formsets=inline_formsets,                                   
            errors=helpers.AdminErrorList(form, formsets),                           
            preserved_filters=self.get_preserved_filters(request),                   
        )                                                                            

        context.update(extra_context or {})                                          

        return self.render_change_form(
        	request, context, add=add,
        	change=not add, obj=obj, form_url=form_url)

~~~

### media

- テンプレートに渡るメディア : `modelAdmin.media +  adminForm.media + [fs.media for ms in inline_formsets]`

~~~
from django.contrib.admin.templatetags.admin_static import static
from django import forms  
~~~
~~~
class ModelAdmin(BaseModelAdmin):  
	...                                              
    @property                                                                        
    def media(self):                                                                 
        extra = '' if settings.DEBUG else '.min'                                     
        js = [                                                                       
            'core.js',                                                               
            'admin/RelatedObjectLookups.js',                                         
            'jquery%s.js' % extra,                                                   
            'jquery.init.js'                                                         
        ]                                                                            
        if self.actions is not None:                                                 
            js.append('actions%s.js' % extra)

        if self.prepopulated_fields:                                                 
            js.extend(['urlify.js', 'prepopulate%s.js' % extra])

        return forms.Media(
        	js=[static('admin/js/%s' % url) for url in js])           
~~~

~~~
>>> from bs4 import BeautifulSoup as Soup
>>> from django import forms
>>> print Soup(forms.Media(js=['hoge.js',]).render()).prettify()
<html>
 <head>
  <script src="/static/hoge.js" type="text/javascript">
  </script>
 </head>
</html>
~~~

- テンプレート

~~~
{{ form.media }}
{{ form.media.js }}
{{ form.media.css }}
~~~

### mediaに追加する

- [How can I override the “media” property of Django's ModelAdmin and make it dynamic?](https://stackoverflow.com/questions/23302175/how-can-i-override-the-media-property-of-djangos-modeladmin-and-make-it-dynam)


~~~

from django.contrib import admin
class MyModelAdmin(admin.ModelAdmin):
    model = MyModel
    ...

    @property
    def media(self):
        media = super(MyModelAdmin, self).media
        css = {
            "all": (
                "my/css/file1.css",
                "my/css/file2.css",
            )
        }
        js = [
            "my/js/file1.js",
            "my/js/file2.js",
        ]
        if whatever_condition_I_want:
            js.append("my/js/file3.js")
        media.add_css(css)
        media.add_js(js)
        return media
~~~        

## レスポンシブ

- [django-admin-bootstrap/django-admin-bootstrap](https://github.com/django-admin-bootstrap/django-admin-bootstrap)

~~~
$ pip install bootstrap-admin
~~~

### CSS, JSなどを追加

~~~html
{% extends "admin/change_list.html" %}
{% load i18n %}

{% block content %}
<div class="local-menu" style="padding-bottom:5px" >
<a href="{% url 'bulletins_default' %}" class="button">戻る</a>
</div>

{{ block.super }}
{% endblock %}

{% block extrahead %}
{{ block.super  }}
<script src="{{ STATIC_URL }}theme/js/jquery-1.11.1.min.js"></script>
<script src="{{ STATIC_URL }}theme/jqui/jquery-ui.min.js"></script>
<script type="text/javascript" charset="utf-8">
$(function(){
 $("a.button").button();
});
</script>
{% endblock %}


{% block extrastyle %}
  {{ block.super }}
<link href="{{ STATIC_URL }}theme/css/font-awesome.min.css" rel="stylesheet">
<link href="{{ STATIC_URL }}theme/jqui/jquery-ui.min.css" rel="stylesheet">
<style type="text/css">
</style>
{% endblock %}
~~~
