## get_form(): フォームをカスタマイズ

~~~
class RentalAdmin(admin.ModelAdmin):                                                

    form = RentalAdminForm                                                          
                                                                                    
    def get_form(self, request, obj=None, **kwargs):                                
		#  ここで何かする                                                                                    
        res = super(RentalAdmin, self).get_form(                                    
            request, obj, **kwargs)                                                 
		# さらに resに対して何かする                                                                                    
        return res  
~~~        

## グルーピング

- [Group models from different app/object into one Admin block](https://stackoverflow.com/questions/10561091/group-models-from-different-app-object-into-one-admin-block)

## フィールドの横にテキスト

- [Django Admin: Add text at runtime next to a field](https://stackoverflow.com/questions/6304176/django-admin-add-text-at-runtime-next-to-a-field)


## ツール

- [django-grappelli](http://django-grappelli.readthedocs.org/en/latest/index.html)
- [django-adminactions](https://github.com/saxix/django-adminactions)