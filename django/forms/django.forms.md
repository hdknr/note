# Django Form


## ModelForm のエラー処理

### 1. フィールドエラー

- clean_{{フィールド名}} メソッドの中で問題があったらforms.ValidationErrorを出す

~~~
    def clean_units(self):
        value = self.cleaned_data['units']
        your_max = self.ticket.orderable_units(self.user)
        if value <= your_max:
            return value
        raise forms.ValidationError(
        	u"{0} ({1} > {2})".format(
				_(u"Too many units"), value, your_max))
~~~

- テンプレートでは {{フィールド名}}.errors を使う

~~~
{% if form.units.errors %}
<font color="red">{{ form.units.errors }}</font>
{% endif %}
~~~

### 2. フォーム全体のエラー

- is_valid()でFalseを返す
- ¥_errors[forms.forms.NON_FIELD_ERRORS] にエラークラス(error_classタイプ)インスタンスをセットする

~~~
from django import forms

class OrderForm(froms.ModelForm):
	...
    def is_valid(self):
        ret = super(OrderForm, self).is_valid()

        if ret and Order.objects.has_repeated_order(self.ticket, self.user):
            # 繰り返し注文の確認
            self._errors[forms.forms.NON_FIELD_ERRORS] = self.error_class(
                [u"繰り返し注文です"],
            )
            return False
		....
~~~

- テンプレートでは non_field_errors を使う

~~~
{% if form.non_field_errors %}
<font color="red"> {{ form.non_field_errors }} </font>
{% endif %}
~~~

## フィールド

- [MultiValueField](https://github.com/hdknr/annotated-django/commit/2cead7bfa850c14b51496738f1bf5e134b93e850)

## テンプレート

### すべての hidden フィールド

~~~
{% for hidden in form.hidden_fields %}
{{ hidden }}
{% endfor %}
~~~

### フィールドの値の参照

- [value()](https://github.com/hdknr/annotated-django/commit/71aff2e8215d92800dafb21f0f2cec7fce2f3ec1)

~~~js
var phone_time = {{ form.phone_time.value }};
if( phone_time == 0 ){
  $("input[name=phone_time_from]").closest(".form-group").toggle();}
}
~~~
