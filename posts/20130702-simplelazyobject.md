Date: 2013-07-02  18:00
Title: Django: SimpleLazyObjectで軽くハマる
Type: post  
Excerpt:   

request.userは 
[AuthenticationMiddleWareがUserをSimpleLazyObjectをかえす](https://github.com/django/django/blob/4a71b842662162e0892a9269179421ff2191adba/django/contrib/auth/middleware.py#L18)のでした。

	class PublishForm(forms.ModelForm):
		def __init__(self,user,*args,**kwargs):
			self.user = user        #:作成ユーザー
			assert self.user != None
			assert any([type(self.user) ==User, type(self.user._wrapped) == User ] ) #:_wrapped : SimpleLazyObject
			

[callabelを _wrapped でラップ](https://github.com/django/django/blob/fd961941cc1c9e7e1384af527792801f8f897d9f/django/utils/functional.py#L278)する。 
[親クラスのLazyObjectで__getattr__がオーバーライドされていて](https://github.com/django/django/blob/fd961941cc1c9e7e1384af527792801f8f897d9f/django/utils/functional.py#L233)、属性がアクセスされた時に実際に[評価されたオブジェクト](https://github.com/django/django/blob/fd961941cc1c9e7e1384af527792801f8f897d9f/django/utils/functional.py#L297)に対してgettattr()で属性が返される。