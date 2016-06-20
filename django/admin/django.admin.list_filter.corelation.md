ModelAdmin.list_filter: 関連する条件で 絞り込む

- Permission 一覧を ContentType自体と、ContentType.app_labelで絞る
- ContentType.app_labelを指定したら、関連するContentTypeだけ選択肢に表示したい


## CorelatedFilter: 関連フィルター

- admin.RelatedFieldListFilterベース
- 関連フィールド(cofield)がクエリパラメータにあったら、 limit_choices_to を指定する

~~~py
from django.contrib import admin    


class CorelatedFilter(admin.RelatedFieldListFilter):                                

    def field_choices(self, field, request, model_admin):                           
        name = "{}__{}".format(field.name, self.cofield)                            
        covalue = request.GET.get(name, '')                                         
        if not covalue:                                                             
            return field.get_choices(include_blank=False)                           
        return field.get_choices(                                                   
            include_blank=False,                                                    
            limit_choices_to={self.cofield: covalue})                               
~~~

## PermissionAdmin

- コンテントタイプと、その app_label で絞る

~~~py
class PermissionAdmin(admin.ModelAdmin):                                         
    list_filter = [                                                              
        'content_type__app_label',                                               
        ('content_type',                                                         
         type('', (CorelatedFilter,), {'cofield': 'app_label'})),                
    ]                                                                            
~~~
