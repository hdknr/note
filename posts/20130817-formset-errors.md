Date: 2013-08-17 10:00 
Title: Django: FormSetのis_validをオーバーライド   
Type: post  
Excerpt:  


is_valid()で個別フォームのバリデーションが終わったあとの関連性チェックをしたい。
フォームセットファクトリの中で強引にメソッドを入れ替える:

    def entry_formset(request,queryset=None,prefix='entry',
                    initial=None,extra=3,
                    *args,**kwargs):

        formset = None
        if request == None or request.method=='GET':
            formset = modelformset_factory(Entry,form=EntryForm ,
                            extra=extra,
                            )(queryset=queryset,prefix=prefix,initial=initial,*args,**kwargs)
        else:
            formset = modelformset_factory(Entry,form=EntryForm,
                            extra=extra,
                            )(request.POST,request.FILES,
                              queryset=queryset,prefix=prefix,initial=initial,*args,**kwargs)

        default_is_valid = formset.is_valid
         
        def override_is_valid(self,*args,**kwargs):
            #:ここでいろいろチェックしてエラーをかえす
            return False

        #: import new  をしておく
        formset.is_valid= new.instancemethod(override_is_valid,formset,type(formset))
        return formset

これだとエラーを出せない。ので、FormSetのカスタムクラスを定義して ValidationErrorを出した方がいいよ。:
        
    class EntriesFormSet(BaseModelFormSet):
        def clean(self):
            if not any(self.errors):        #:すでの各フォームでエラーが起きていない時だけチェック
                if anything_is_happen:
                    raise forms.ValidationError(u'何か起きました')
   
    
    def entry_formset(request,queryset=None,prefix='entry',
                    initial=None,extra=3,
                    *args,**kwargs):
        
        formset = None
        if request == None or request.method=='GET':
            formset = modelformset_factory(Entry,form=EntryForm ,formset=EntriesFormSet,
                            extra=extra,
                            )(queryset=queryset,prefix=prefix,initial=initial,*args,**kwargs)
        else:
            formset = modelformset_factory(Entry,form=EntryForm,formset=EntriesFormSet,
                            extra=extra,
                            )(request.POST,request.FILES,
                              queryset=queryset,prefix=prefix,initial=initial,*args,**kwargs)
        
        return formset
        
フォームセットのclean()でraiseした例外は、non_form_errors()で参照します:

    if request.method == 'POST' and formset.is_valid():
        formset.save() #:保存
    else:
        print formset.non_form_errors()          
        