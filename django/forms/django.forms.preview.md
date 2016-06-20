## プレビューフォーム

- 基本的にはウィジェットをHiddenInputに変更
- 複数選択支の場合、MultipleHiddenInputに変更
- FileFieldの場合は難しい。ここでは一時ファイルに保存し、`_preview` に一時ファイル名をHiddenInputで回す

~~~py
def to_preview(the_form):
    '''
    フォームのアイテムを全てhiddeに変更する
        - ファイルアップロードのフィールドがあるとうまく行かないかも
    '''
    for k, f in the_form.fields.items():
        if str(type(f)).find('Multi') > 0:
            f.widget = forms.MultipleHiddenInput()

        elif isinstance(f, forms.fields.FileField):
            file_field = "{0}_preview".format(k)

            if the_form.cleaned_data[k] is False :
                # 削除
                the_form.fields[file_filed].widget = forms.HiddenInput(
                    attrs={'value':'delete',})

            elif the_form.cleaned_data[k] and k in the_form.changed_data:
                # アップロードがあったら、一時ファイルで保存
                file_data = getattr(the_form.instance, k, None)
                if file_data and file_data.name :
                    ext = os.path.splitext(file_data.name)[1]
                    file_data.name = the_form.cleaned_data.get(
                        file_field, create_preview_file_name())
                    with open(media_path(file_data.name), 'w') as out:
                        out.write(file_data.file.read())

                # ファイル名をプレビューフォームhiddenで保存
                # 次回「保存」した時には一時保存ファイルを実際に保存するようにする
                the_form.fields[file_field].widget = forms.HiddenInput(
                    attrs={'value':file_data.name,})
                the_form.fields[file_field].initial = file_data.name
            else:
                #  ファイルの指定が無い場合は、一時ファイルを削除する
                if the_form.cleaned_data.get(file_field):
                    os.remove(media_path(the_form.cleaned_data.get(file_filed))
                # 一時ファイル名フィールドを空にする
                the_form.fields[file_filed].widget = forms.HiddenInput(
                    attrs={'value':'',})
                the_form.fields[file_filed].initial= ''

            #: FileFiledをHidden化
            f.widget = forms.HiddenInput()

        elif not isinstance(f.widget, forms.HiddenInput):
            # それ以外は通常のHiddenInputに変更
            f.widget = forms.HiddenInput()
~~~

## ビューのパイプライン

- urls.py

~~~py
# Inquiry(問い合わせ)
url(r'inquiry/create',
    views.inquiry_create, name='inquiry_create'),
url(r'inquiry/confirm',
    views.inquiry_confirm, name='inquiry_confirm'),
url(r'inquiry/(?P<id>.+)',
    views.inquiry_detail, name='inquiry_detail'),
~~~

- views.py

~~~py
def inquiry_create(request):
    template_name = "inquiry/create.html"
    form = forms.InquiryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # 検証がとおったらプレビュー化して確認画面へ
        to_preview(form)
        template_name = "inquiry/confirm.html"

    context = {'form': form, }
    return TemplateResponse(request, template_name, context)
~~~

~~~py
def inquiry_confirm(request):
    if request.method == 'GET':
        # 直接アクセスがきたら編集からやりなおす
        url = reverse('inquiry_create')
        return HttpResponseRedirect(url)

    form = forms.InquiryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if request.POST['submit'] == u'送信':     
            # 送信ボタンでのみ確定
            form.save()
            url = reverse('inquiry_detail', kwargs={'id': form.instance.id})
            return HttpResponseRedirect(url)

    # 「送信」以外の場合は、もう一度編集画面
    template_name = "inquiry/create.html"
    context = {'form': form, }
    return TemplateResponse(request, template_name, context)
~~~    

- inquiry/create.html

~~~html
{# 通常のフォーム #}
<form method="post" action="{% url 'accounts_inquiry_create' %}" >{% csrf_token %}
    <table>
      {{ form.as_table }}
    </table>
    <input type="submit" name="submit" value="送信"/>
</form>
~~~

- inquiry/confirm.html

~~~html
<form method="post" action="{% url 'accounts_inquiry_confirm' %}">{% csrf_token %}
    {{ form }} {# これはユーザーにはみえない #}
    <table>
     {% for field in form %} {# ここでプレビューさせる #}
        <tr><td>{{field.label}}</td><td>{{ field.value }}</tr>
     {% endfor %}
    </table>
    <input type="submit" name="submit" value="送信"/> {# save & redirect #}
    <input type="submit" name="submit" value="修正"/> {# create.html #}
</form>
~~~
