##  選択肢をプルダウンからラジオボタンに変更する

~~~python
class OrderForm(forms.ModelForm):                                     
    class Meta:                                                                     
        model = models.Order                                                        
        exclude = ['ordinal', 'amount', 'user', ]                                   
        # ウィジェット切り替え
        widgets = {                                                                 
            'payment': forms.RadioSelect(),                                         
            'contact_by': forms.RadioSelect(),                                      
        }                                                                           

    def __init__(self, *args, **kwargs):                                            
        super(OrderForm, self).__init__(*args, **kwargs)                            

        # choices から 空の選択肢を抜く
        for name in self.fields:                                                    
            field = self.fields.get(name)                                           
            if field and getattr(field, 'choices', None):                           
                if type(field.choices) == list:                                     
                    field.choices = field.choices[1:]                               
                else:                                                               
                    # django.forms.models.ModelChoiceIterator とか
                    field.empty_label = None    
~~~

## Bootstrapフォーム で水平表示

~~~html

<form method="post"
  class="form-horizontal"> {# これを指定しないと、radio-inline の１つ目の水平が崩れる #}
  {% csrf_token %}
  <!---   ..... -->
</form>
~~~

## jQueryでクラス変更

~~~javascript
$("input[type=radio]").parent('label').parent('div').addClass('radio-inline');
~~~
