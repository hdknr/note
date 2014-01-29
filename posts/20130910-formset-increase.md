Date: 2013-09-10  14:00
Title: Django: Formsetのフォームの数を増減させる
Type: post  
Excerpt:   


親モデルで子モデルのインスタンス数を指定するシナリオ。
入力したインスタンス数がFormsetのフォームの数と合わない場合は新規フォームセットを作って、コピるというやり方。
入力したチケットの枚数だけの個人情報を入力させる例：

    @login_required
    def order(request,id):
        dc=device_class(request)
        subcommand = "begin"    
        if request.method == "POST":
            form = OrderForm(user=request.user,id=id,data=request.POST)
            formset = None
            if form.is_valid():
                number = int( form.cleaned_data['units'])
                formset = create_companion_formset(request)
                
                if number != len(formset.forms):         #:数が合わない
                    old = formset
                    formset = create_companion_formset(None,extra=number)
                    for i in range(min(number,len(old.forms))):
                        formset.forms[i] = old.forms[i]    #:ポストバックフォームをコピー
                               
                elif formset.is_valid(number):
                    subcommand = "complete"
                    form.save()
                    for f in formset.forms:
                        f.instance.order =form.instance
                        f.save()
            else:
                formset = create_companion_formset(request,extra=form.instance.units)
        else:
            form = OrderForm(user=request.user,id=id, )
            formset = create_companion_formset(request,extra=form.instance.units) #:初期値
                
        return render_to_response( '%s/tickets/order_%s.html' % ( dc,subcommand ),
            {'form':form,'formset':formset, },
            context_instance=template.RequestContext(request),)

フォームセットを作るヘルパ：

    def create_companion_formset(request,order=None,*args,**kwargs):
        kwargs['form'] = CompanionForm
        kwargs['can_delete'] = False
        kwargs['formset'] = OrderCompanionFormset
    #
        if request and request.method =="POST":
            return inlineformset_factory( Order, Companion,
                        *args,**kwargs)(request.POST,instance=order)
        
        return inlineformset_factory( Order, Companion,
                        *args,**kwargs)(instance=order)
