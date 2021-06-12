転送メールアドレス設定

- input[type=radio] を水平に並べる
- 選択されたドメインをメールアドレス入力の右横に表示させる

## horizontal フォーム

- [django-bootstrap3: Template tags and filters](https://django-bootstrap3.readthedocs.org/en/latest/templatetags.html)

~~~html
<form method="post"
  action="{% url 'accounts_email_forward_add' id=profile.id command='preview' %}"
  class="form-horizontal"> {# これを指定しないと、radio-inline の１つ目の水平が崩れる #}
  {% csrf_token %}
  {% bootstrap_form_errors form  %}

  {% bootstrap_field form.domain layout="horizontal" %}

  {# INPUT が大きすぎるのでfield_class で幅を小さくする #}
  {% bootstrap_field form.user layout="horizontal" field_class="col-md-3" %}      
  {% bootstrap_field form.forward layout="horizontal" field_class="col-md-5" %}

  <div class="form-group">
    {# offset-3 でラベルの幅分、インデントさせる #}
    <div class="col-md-offset-3 col-md-9">
    <button type="submit" class="btn btn-primary">
    {% trans 'Submit Form' %}
    </button>
    <a class="btn btn-warning"
      href="{{ profile.get_absolute_url }}">{% trans 'Cancel Form'%}</a>
    </div>
  </div>
</form>
~~~

### form クラス

~~~py
class EmailForwardForm(forms.Form, PreviewMixin):                                        
    user = forms.CharField( required=True)
    domain = forms.ChoiceField(
        choices=tuple((i, i) for i in DOMAINS),                                     
        widget=forms.RadioSelect, required=True)
    forward = forms.EmailField(required=True)
~~~        

## ドメインを選択したら表示を変える

~~~javascript
<script>
$(function(){

  // Radioボタンを水平方向に並べる
  $("input[type=radio]").parent('label').parent('div').addClass('radio-inline');

  // 転送先メールのドメインが変わった時の表記の切り替え
  function reset_domain(){
    v = $("input[name=domain]:checked").val();
    if (v == undefined)
      return;
    $("input[name=user]").parent('div').after(
        '<div class="col-md-2 domain-name"><a href="#" class="btn btn-info">@' + v + '</a></div>');
  }

  if( $("input[name=domain]").val() != ''){
    // POSTバックしてきた時のデフォルト表記
    reset_domain();
  }

  $("input[name=domain]:radio").change(function(){
    // ラジオボタンの選択が変わったら
    $("input[name=user]").parent('div').nextAll().remove();   // 一旦HTMLを削除
    reset_domain();   // 表示させる
  });
});
</script>
~~~

## 表示

![](./bootstrap.form.email.png)
