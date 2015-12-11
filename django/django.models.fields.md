## OneToOneFieldの指定されているかの判定

- `hasattr` でチェックする

~~~py
In [20]: hasattr(User.objects.first(), 'profile')
Out[20]: False

In [21]: hasattr(User.objects.filter()[400], 'profile')
Out[21]: True
~~~


## 派生フィールドクラスのマイグレーションタイプにDjangoのクラスを使う

- [Emulating built-in field types](https://docs.djangoproject.com/en/1.7/howto/custom-model-fields/#emulating-built-in-field-types)

~~~
class AlumniField(models.CharField):                                                
    def __init__(self, *args, **kwargs):                                            
        super(AlumniField, self).__init__(*args, **kwargs)                          

    def get_internal_type(self):                                                    
        return 'CharField'     
~~~        
