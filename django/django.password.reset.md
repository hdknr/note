## パスワード関連フォーム

- リセット要求
- 新パスワード設定

### パスワードリセットフォーム

./contrib/auth/forms.py

- メールを入力させて確認する

~~~py

class PasswordResetForm(forms.Form):                                                
    email = forms.EmailField(label=_("Email"), max_length=254)                      
	...
~~~py

- 入力されたメールアドレスからユーザーを見つけます

~~~py
    def get_users(self, email):                                                     
        active_users = get_user_model()._default_manager.filter(                 
            email__iexact=email, is_active=True)                                 
        return (u for u in active_users if u.has_usable_password())              
~~~

- メールを送信します

~~~py
    def send_mail(self, subject_template_name, email_template_name,                 
                  context, from_email, to_email, html_email_template_name=None): 
        """                                                                         
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.              
        """                                                                         
        subject = loader.render_to_string(subject_template_name, context)  
                 
        # Email subject *must not* contain newlines                                 
        subject = ''.join(subject.splitlines())                                     
        body = loader.render_to_string(email_template_name, context)                
                                                                                    
        email_message = EmailMultiAlternatives(
        	subject, body, from_email, [to_email])
        	
        if html_email_template_name is not None:                                    
            html_email = loader.render_to_string(
            	html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')               
                                                                                    
        email_message.send()  
~~~

- save() がオーバーライドされていて、一連の処理が行われます

~~~py
    def save(self, domain_override=None,                                         
             subject_template_name='registration/password_reset_subject.txt',    
             email_template_name='registration/password_reset_email.html',       
             use_https=False, token_generator=default_token_generator,           
             from_email=None, request=None, html_email_template_name=None):      
                                                                 
        email = self.cleaned_data["email"]                                       
        for user in self.get_users(email):                                       
            if not domain_override:                                              
                current_site = get_current_site(request)                         
                site_name = current_site.name                                    
                domain = current_site.domain                                     
            else:                                                                
                site_name = domain = domain_override                             
            context = {                                                          
                'email': user.email,                                             
                'domain': domain,                                                
                'site_name': site_name,                                          
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),              
                'user': user,                                                    
                'token': token_generator.make_token(user),                       
                'protocol': 'https' if use_https else 'http',                    
            }                                                                    
                                                                                 
            self.send_mail(subject_template_name, email_template_name,           
                           context, from_email, user.email,                      
                           html_email_template_name=html_email_template_name)    

~~~

### 新パスワード設定

- パスワード１とパスワード２が必要です

~~~py
class SetPasswordForm(forms.Form):                                                  
    new_password1 = forms.CharField(label=_("New password"),                        
                                    widget=forms.PasswordInput)                     
    new_password2 = forms.CharField(label=_("New password confirmation"),           
                                    widget=forms.PasswordInput)                     
~~~

- パスワード１と２は一致しないとエラーです

~~~py
    def clean_new_password2(self):                                                  
        password1 = self.cleaned_data.get('new_password1')                          
        password2 = self.cleaned_data.get('new_password2')                       
        if password1 and password2:                                              
            if password1 != password2:                                           
                raise forms.ValidationError(                                     
                    self.error_messages['password_mismatch'],                    
                    code='password_mismatch',                                    
                )                                                                
        return password2                                                         
~~~

- save()するときにパスワードを更新します

~~~py
    def save(self, commit=True):                                                 
        self.user.set_password(self.cleaned_data['new_password1'])               
        if commit:                                                               
            self.user.save()                                                     
        return self.user 
~~~        


## パスワードリセット処理

./contrib/auth/views.py

~~~py
# 4 views for password reset:   
                                                    
# - password_reset sends 		: メールを送信する                                                   
# - password_reset_done 		: メール送信の完了                       
# - password_reset_confirm 	: リンクを踏んだ時に新しいパスワードを指定させる                                                    
# - password_reset_complete shows a success message for the above                   
~~~

### url

~~~py
urlpatterns = [                                                                     
    url(r'^password_reset/$', views.password_reset, name='password_reset'),         
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),               
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]                                                                                   

~~~

### リセット : メールを送信する
~~~py                                                                                
@csrf_protect                                                                       
def password_reset(request, is_admin_site=False,                                    
                   template_name='registration/password_reset_form.html',           
                   email_template_name='registration/password_reset_email.html', 
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,                           
                   token_generator=default_token_generator,                         
                   post_reset_redirect=None,                                        
                   from_email=None,                                                 
                   current_app=None,                                                
                   extra_context=None,                                              
                   html_email_template_name=None):  
~~~

- この処理が終わった時の画面のリダイレクトURLを決めます

~~~py
    if post_reset_redirect is None:                                                 
        post_reset_redirect = reverse('password_reset_done')                        
    else:                                                                           
        post_reset_redirect = resolve_url(post_reset_redirect)                      
~~~

- POSTバックしてきたらフォームの内容(email)を判定し、OKだったら save()します。
- save()したときにformからメールが送られます
- そのあとで先ほどのリダイレクトURLにリダイレクトします。

~~~py
    if request.method == "POST":                                                    
        form = password_reset_form(request.POST)                                    
        if form.is_valid():                                                         
            opts = {                                                                
                'use_https': request.is_secure(),                                   
                'token_generator': token_generator,                                 
                'from_email': from_email,                                           
                'email_template_name': email_template_name,                         
                'subject_template_name': subject_template_name,                     
                'request': request,                                                 
                'html_email_template_name': html_email_template_name,               
            }                                                                       
            form.save(**opts)                                                       
            return HttpResponseRedirect(post_reset_redirect)                        
~~~

- GETできたらフォームをつくって表示させます
- POSTでフォームがOKじゃない時も表示です

~~~py
    else:                                                                           
        form = password_reset_form()                                                
    context = {                                                                     
        'form': form,                                                               
        'title': _('Password reset'),                                               
    }       
    ....
    return TemplateResponse(request, template_name, context)                     
                                                                                                                                                         
~~~


### メール送信の完了

~~~py
def password_reset_done(request,                                                 
                        template_name='registration/password_reset_done.html',   
                        current_app=None, extra_context=None):                   
    context = {                                                                  
        'title': _('Password reset sent'),                                       
    }                                                                            
    if extra_context is not None:                                                
        context.update(extra_context)                                            
                                                                                 
    if current_app is not None:                                                  
        request.current_app = current_app                                        
                                                                                 
    return TemplateResponse(request, template_name, context)                     
~~~

### ユーザーがリンクを踏んで新パスワードを受ける

~~~py
@sensitive_post_parameters()                                                     
@never_cache                                                                     
def password_reset_confirm(request, uidb64=None, token=None,                     
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,              
                           set_password_form=SetPasswordForm,                    
                           post_reset_redirect=None,                             
                           current_app=None, extra_context=None):                

~~~

- ユーザーモデルクラスを取得します
- `uidb64` と `token` は必須です

~~~py
    UserModel = get_user_model()                                                 
    assert uidb64 is not None and token is not None  # checked by URLconf        
~~~

- 処理完了時のリダイレクトURLを判定します

~~~py
    if post_reset_redirect is None:                                              
        post_reset_redirect = reverse('password_reset_complete')                 
    else:                                                                        
        post_reset_redirect = resolve_url(post_reset_redirect)    
~~~

- uidをデコードして、Userモデルインスタンスを探します

~~~py
    try:                                                                         
        # urlsafe_base64_decode() decodes to bytestring on Python 3              
        uid = force_text(urlsafe_base64_decode(uidb64))                          
        user = UserModel._default_manager.get(pk=uid)                            
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):       
        user = None  
~~~

- userがみつかって、トークンが正しい時に処理が進みます

~~~py
    if user is not None and token_generator.check_token(user, token):            
        validlink = True                                                         
        title = _('Enter new password')  
~~~


- ポストバックしてきたら、パスワード設定の内容が正しいことを確認し、パスワードを保存します
- その後先ほど決めたリダイレクトURLにリダイレクトさせます
- GETだと新パスワード設定フォームを出します

~~~py
        if request.method == 'POST':                                             
            form = set_password_form(user, request.POST)                         
            if form.is_valid():                                                  
                form.save()                                                      
                return HttpResponseRedirect(post_reset_redirect)       
        else:                                                                    
            form = set_password_form(user)                            
~~~        
               
- ユーザーがいないか、あるいはURLが不正だと処理がつづけられません

~~~py
    else:                                                                        
        validlink = False                                                        
        form = None                                                              
        title = _('Password reset unsuccessful')   
~~~

- 画面表示します

~~~py
    if extra_context is not None:                                                
        context.update(extra_context)                                            
                                                                                 
    if current_app is not None:                                                  
        request.current_app = current_app                                        
                                                                                 
    return TemplateResponse(request, template_name, context)                     
~~~                        

### リセット処理の完了

~~~py
def password_reset_complete(request,                                             
                            template_name='registration/password_reset_complete.html',
                            current_app=None, extra_context=None):               
    context = {                                                                  
        'login_url': resolve_url(settings.LOGIN_URL),                            
        'title': _('Password reset complete'),                                   
    }                                                                            
    if extra_context is not None:                                                
        context.update(extra_context)                                            
                                                                                 
    if current_app is not None:                                                  
        request.current_app = current_app                                        
                                                                                 
    return TemplateResponse(request, template_name, context)     
~~~    

                   
