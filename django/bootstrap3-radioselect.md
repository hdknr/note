django: RadioSelectの選択アイテムを fontawesome でラベル化

# anyenv : pyenv + ndenv

## anyenv.bash

~~~
export PATH="$HOME/.anyenv/bin:$PATH"
eval "$(anyenv init -)"
 
for D in `\ls $HOME/.anyenv/envs`; do
    export PATH="$HOME/.anyenv/envs/$D/shims:$PATH"
done
 
function ANYENV_PLUGIN()
{
    mkdir -p $(anyenv root)/plugins;
    git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update;
}

function ANYENV_PYENV_VIRTUALENV()
{
	git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.anyenv/envs/pyenv/plugins/pyenv-virtualenv
}
~~~


## install anyenv

~~~
$ git clone https://github.com/riywo/anyenv ~/.anyenv
~~~
~~~
$ source ~/anyenv.bash
~~~

##  install ndenv + node.js

~~~
$ anyenv install ndenv
$ source ~/bin/env/anyenv.bash
~~~

~~~
$ ndenv install 0.12.0
$ ndenv global 0.12.0
$ source ~/bin/env/anyenv.bash
~~~

## install bower

~~~
$ npm install bower -g
$ source ~/bin/env/anyenv.bash
~~~


## install pyenv , python

~~~
$ anyenv install pyenv
$ source ~/bin/env/anyenv.bash
$ pyenv  install 2.7.8
$ pyenv global 2.7.8
$ pip install django 
~~~

## install django ...

- requirements.txt
- [django-bootstrap3](http://django-bootstrap3.readthedocs.org/en/latest/)
- [bambu-bootstrap](http://bambu-bootstrap.readthedocs.org/en/latest/)
- [django-bower](https://django-bower.readthedocs.org/en/latest/)

~~~
Django
bambu-bootstrap
beautifulsoup4
django-bootstrap3
django-bower
...
~~~

~~~
$ pip install -r requirements.txt
~~~

# Django アプリケーション設定

## settings.py : bootstrap3 の設定

- django のプロジェクト作成すみ
- settings.py 

~~~py
from django.conf import global_settings

MEDIA_ROOT = os.path.join(BASE_DIR, 'medias/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
INSTALLED_APPS += (
    'bootstrap3',   	# django-bootstrap3
    'djangobower',  	# django-bower
    'bambu_bootstrap',  # bambu
)
STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + (
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components/')
BOWER_INSTALLED_APPS = (
    'bootstrap',
    'fontawesome',
    'jquery-ui',
    'lightbox2',
)
~~~

## Bootstrap 関連インストール

~~~
$ python manage.py bower install
~~~

~~~
$ python manage.py collectstatic
~~~

# forms.py

## IconModelChoiceField

- Roleモデルの symbol フィールドにfontawesomeのclassを入れてる

~~~py

>>> [ r.symbol for r in Role.objects.all()]
[u'fa-building-o', u'fa-smile-o', u'fa-user', u'fa-users']
~~~

- Role をModelChoiceFieldで参照するフォームでのレンダリングを派生クラスで

~~~py

class IconModelChoiceField(forms.ModelChoiceField):   
                             
    def __init__(self, *args, **kwargs):                                            
        kwargs['widget'] = forms.RadioSelect()                                      
        kwargs['empty_label'] = mark_safe(                                          
            '<i class="fa fa-question fa-1x" title=""></i>')                        
        super(IconModelChoiceField, self).__init__(*args, **kwargs)                 
                                                                                    
    def label_from_instance(self, obj):                                             
        if isinstance(obj, models.Role):                                            
            return mark_safe('<i class="fa {0} fa-1x" title="{1}"></i>'.format(  
                obj.symbol, obj.__unicode__().encode('utf8')))                      
                                                                                    
        return super(IconModelChoiceField, self).label_from_instance(obj)           
~~~

## ActionForm

- Roleを選択させます

~~~py

class ActionForm(forms.ModelForm):                                                     

    initiator_role = IconModelChoiceField(                                       
        label=_('Initiator Role'), required=True,                                
        queryset=models.Role.objects.all(),)                                     
~~~

# action_edit.html

- form

~~~html

  <div class="form-group">
    <label class="col-md-2 control-label" for="id_initiator_role">
    {{ form.initiator_role.label }}
    </label>
    <div class="col-md-4">
        {{ form.initiator_role}}
    </div>
  </div>

~~~

- javascript

~~~js

<script>
  $(function() {
    $("ul#id_initiator_role li").addClass("btn btn-default btn-xs");
  });
</script>

~~~

- レンダリング

![](https://github.com/hdknr/scriptogr.am/raw/master/django/bootstrap3-radioselect.1.png)

# こんな面倒くさいことしなくても...

## forms.py

- 標準のRadioSelect

~~~py

class ActionForm(forms.ModelForm):                                                  
                                                                                    
    class Meta:                                                                     
         _STAKEHOLDER = {'class': 'stakeholder-selection', }                         
        model = models.Action                                                       
        widgets = dict(                                                             
            initiator=forms.RadioSelect(attrs=_STAKEHOLDER),                        
            target=forms.RadioSelect(attrs=_STAKEHOLDER),                           
        ) 
~~~

## tamplate.html

~~~js
  
  // ul.btn-group ui.btn.btn-default
  $.each(
    ['{{ form.initiator.auto_id }}',
     '{{ form.target.auto_id }}' ], 
    function(i, id){ 
        $('ul#'+id).addClass('btn-group');
        $('ul#'+id+ ' li').addClass('btn btn-default');
    }
  );

  // 未選択を'?'アイコン
  elm = $('.stakeholder-selection[value=""]:radio');
  elm.parent().html(
    document.getElementById(elm.attr('id')).outerHTML + 
    '<i style="margin-left:10px" class="fa fa-question"></i>');

　 // 選択肢はモデルに定義されているアイコン化
  {% for stakeholder in action.usecase.assessment.stakeholder_set.all %}
    elm = $('.stakeholder-selection[value="{{ stakeholder.id }}"]:radio');
    elm.parent().html(
        document.getElementById(elm.attr('id')).outerHTML + 
        '<i style="margin-left:10px" class="fa {{ stakeholder.role.symbol }}"></i>');
  {% endfor %} 
~~~

# bootstrap-select: アイコン付きドロップダウンの方がよくないか？

- settings.py

~~~py

BOWER_INSTALLED_APPS = (
	...
    'bootstrap-select',     # option/select
)
~~~

~~~
$ python manage.py bower install
$ python manage.py collectstatic
~~~

- forms.py

~~~py

class ActionForm(forms.ModelForm):                                               
                                                                                 
    class Meta:                                                                  
        _STAKEHOLDER = {'class': 'selectpicker stakeholder-selection', }         
        model = models.Action                                                    
        exclude = ['description', 'diagram_text', ]                              
        widgets = dict(      
            initiator=forms.Select(attrs=_STAKEHOLDER),                          
            target=forms.Select(attrs=_STAKEHOLDER),                             
        )                                                                        


~~~

- templatehtml

~~~html
<link href="{{ STATIC_URL }}bootstrap-select/dist/css/bootstrap-select.min.css" rel="stylesheet">
<script src="{{ STATIC_URL }}bootstrap-select/js/bootstrap-select.js"></script>
~~~
~~~js

  {% for stakeholder in action.usecase.assessment.stakeholder_set.all %}
   $('.selectpicker.stakeholder-selection option[value="{{ stakeholder.id }}"]').attr(
    'data-content', '<i class="fa {{ stakeholder.role.symbol }}"></i> {{ stakeholder}}');
  {% endfor %} 

~~~

![](https://raw.githubusercontent.com/hdknr/scriptogr.am/35165bff32bb2273057b988e76d5da932ef47e75/django/bootstrap3-radioselect.dropdown.png)
