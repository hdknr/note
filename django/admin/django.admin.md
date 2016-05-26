## get_form(): フォームをカスタマイズ

~~~
class RentalAdmin(admin.ModelAdmin):                                                

    form = RentalAdminForm                                                          

    def get_form(self, request, obj=None, **kwargs):                                
		    # ここで何かする                                                                                    
        res = super(RentalAdmin, self).get_form(                                    
            request, obj, **kwargs)                                                 
        # さらに resに対して何かする                                                                                    
        return res  
~~~        

## フォームフィールドの初期化(get_changeform_initial_data)

- フォームフィールドの初期化であって、instanceに値がセットされるわけではない
- フォームフィールドを向こうにすると保存されません

~~~py
class AlumnusCsvAdmin(BaseModelAdmin):                                              
    def get_changeform_initial_data(self, request):                                 
        res = super(AlumnusCsvAdmin, self).get_changeform_initial_data(request)  
        res['user'] = request.user                                                  
        return res   
~~~

## フィードに値を設定(save_model)
  
~~~py
class AlumnusCsvAdmin(BaseModelAdmin):                                              
    def save_model(self, request, obj, form, change):                               
        obj.user = request.user                                                  
        super(AlumnusCsvAdmin, self).save_model(request, obj, form, change)         
~~~

## グルーピング

- [Group models from different app/object into one Admin block](https://stackoverflow.com/questions/10561091/group-models-from-different-app-object-into-one-admin-block)

## フィールドの横にテキスト

- [Django Admin: Add text at runtime next to a field](https://stackoverflow.com/questions/6304176/django-admin-add-text-at-runtime-next-to-a-field)


## ツール

- [django-grappelli](http://django-grappelli.readthedocs.org/en/latest/index.html)
- [django-adminactions](https://github.com/saxix/django-adminactions)


## Read Only

- [Readonly models in Django admin interface?](https://stackoverflow.com/questions/8265328/readonly-models-in-django-admin-interface)


## フィルター

- [modlinltd/django-advanced-filters](https://github.com/modlinltd/django-advanced-filters)


## 記事

- [Django 管理画面逆引きメモ](http://qiita.com/Fq4X/items/044c149d93db097cdaf8)
