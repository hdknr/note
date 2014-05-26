Django: inlineformset_factory で フォームセットの各フォームに初期値を与える


例えばイベント参加者を指定するフォーム:

```py

    class CompanionForm(forms.ModelForm):
        def __init__(self, event=None, *args, **kwargs):
            # アルコールが出るイベントに参加する同行者は年齢を入力しないといけない
            if event.with_alcoholic_drink:
                self.base_fields['age'] = forms.TextInput(required=True)
                
            super(CompanionForm, self).__init__(*args, **kwargs)

```

申し込みの同行者が複数いるので、inlineformset_factoryで、複数のCompanionFormを作成したい。

が、inlineformset_factoryで生成したフォームセットクラスには、インラインフォームに渡す引数を指定できない。

inlineformset_factory はフォームセットインスタンスを作成したら、インライン入力するフォームのクラスを"form"フィールドにセットするので、これを引数をCurry化したstaticmethodでリプレースしてやると、

フォームセットインスタンスの__init__()の中のどこかで呼ばれる、

```
    self.form(**initial_parameter) 
```
 
で各インラインフォームを作る時に実際のインラインフォームを初期化する時にパラメータを指定してくれるようになる。


ヘルパーを作って対応

```py

    class OrderCompanionFormset(BaseInlineFormSet):
        # ... Order-Companion の関係モデルのフォームセットをごにょごにょする

    from django.utils.functional import curry

    def create_companion_formset(request, event, order, initial={})
        formset = inlineformset_factory(
            Order, Companion,
            form=CompanionForm,
            fromset=OrderCompanionFormset )
            
        # form を event引数でcurry化
        formset.form = staticmethod(curry(formset.form, event=event))
        
        ...
        return formset(data=request.POST or None
                       instance=order, initial=initial{})
        
```
