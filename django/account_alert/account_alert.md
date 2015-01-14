Django: 期限がきたらアラート画面に飛ばす

- パスワードのリセットの強制とか


# アカウントアラートモデル

~~~py
from django.db import models                                                        
from django.contrib.auth.models import User                                         
                                                                                    
                                                                                    
class AccountAlert(models.Model):                                                   
    user = models.ForeignKey(User)                                                  
    url = models.CharField(max_length=200, db_index=True)                           
    text = models.TextField(null=True, default=None, blank=True)                    
    force = models.BooleanField(default=False)                                      
    due_on = models.DateTimeField(null=True, blank=True, default=None)              
    executed_at = models.DateTimeField(null=True, blank=True, default=None)         
                                                                                    
    class Meta:                                                                     
        ordering = ['-due_on']                                                      
~~~

# アラート確認ミドルウェア

## accounts/middleware.py

- ログインユーザーに強制(force=True) のアラートが追加があったらurlにリダイレクトする。
- アラートが処理されていたら(executed_at != None) スルー。
- 期限前だったらスルー。
- リダイレクトループを起こさないように。

~~~py
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.timezone import now


class AccountAlertMiddleware(object):

    def process_request(self, request):
        if getattr(request, 'user', None) and request.user.is_authenticated():
            alerts = request.user.accountalert_set.filter(
                force=True,
                executed_at=None,
                due_on__lt=now()).exclude(url=request.path)

            if alerts.count() > 0:
                return HttpResponseRedirect(alerts[0].url)
~~~

## app/settings.py

~~~py
MIDDLEWARE_CLASSES += (
    'accounts.middleware.AccountAlertMiddleware',
)
~~~


# UseCase 1. パスワードリセットアラート

- /accounts/password/change/ させるアラート

~~~py
>>> from django.utils.timezone import now
>>> from accounts.models import AccountAlert
>>> from django.contrib.auth.models import User
>>> AccountAlert(user=User.objects.get(username='admin'), url='/accounts/password/change/', force=True, due_on=now()).save()

~~~

## パスワードリセットビュー

- パスワード変更が終わってリダイレクトする前に、処理済みとする(executed_at=now())
- パスワードリセットは djangoの実装を使う(django.contrib.auth)

~~~py
from django.contrib.auth import views as django_views                            
from django.contrib.auth import forms 

@sensitive_post_parameters()                                                        
@csrf_protect                                                                       
@login_required                                                                     
def password_change(request): 
                                                      
    res = django_views.password_change(                                             
        request,                                                                    
        template_name='accounts/password_change.html',                              
        post_change_redirect=reverse('accounts_password_change_done'),              
        password_change_form=forms.PasswordChangeForm,                              
        current_app=None,                                                           
        extra_context=None)                                                         
                                                                                    
    try:                                                                            
        if type(res) == HttpResponseRedirect:                                       
            request.user.accountalert_set.filter(                                   
                executed_at=None, url=reverse('accounts_password_change'),          
            ).update(executed_at=now())                                             
                                                                                    
    except Exception, ex:                                                           
        print ex                                                                    
                                                                                    
    return res                   
~~~ 

# UseCase 2. 汎用的に通知を読ませる

- 既読チェックしたら消し込む

~~~py
  @sensitive_post_parameters()                                                     
  @csrf_protect                                                                    
  @login_required                                                                  
  def alert(request):                                                          
      alerts = request.user.accountalert_set.filter(                               
          force=True,                                                              
          url=request.path,                                                        
          executed_at=None,                                                        
          due_on__lt=now())                                                        
                                                                                   
      # formset でチェックが入ったAccountAlert を消す                              
      #  ....                                                                      
                                                                                   
      return TemplateResponse(                                                     
          request,                                                                 
          'accounts/alert.html',                                                   
          dict(request=request), )                                                   
	
~~~

~~~py
>>> AccountAlert(user=User.objects.get(username='admin'), 
url='/accounts/alert/', 
force=True, due_on=now(), 
text=u".......").save()
~~~
