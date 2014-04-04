Django:入力アイテム数に応じて、子フォームの数を変動させる


入力された注文(Order)の数(units)だけ帯同者(Companion)の子フォームの数を変更させる。


やり方がよくわからんので、強引にやってみる。:

    if request.method == "POST":

          form = OrderForm(user=request.user,
                           ticket=ticket, data=request.POST)
          #: Order(注文)
          is_form_valid = form.is_valid()
  
          #: Companion (帯同者)
          formset = create_companion_formset(
              request, order=form.instance)            
          is_formset_valid = formset.is_valid()

          number = int(form.cleaned_data.get('units', 1)) 
          if number != len(formset.forms):
          
              #: 数に変更があったので、....
              is_formset_valid = False
              old = formset
              
              #: formset を新しい数で作りなおす
              formset = create_companion_formset(None, extra=number)
              
              #: コピーする
              for i in range(min(number, len(old.forms))):
                  formset.forms[i] = old.forms[i]
          
         if is_form_valid and is_forset_valid:
             form.save()
             formset.save()
             
         #:.....



追加された子フォームの入力を必須とする:

    class OrderCompanionFormset(BaseInlineFormSet):

        def clean(self):
            for i in range(self.total_form_count()):
                if not self.forms[i].has_changed():
                    _errs = self.forms[i].error_class(
                        [_("Form must be filled.")])
                    self.forms[i].errors['__all__'] = _errs 


フォームセットのファクトリ:

    def create_companion_formset(request, order=None, extra=1, *args, **kwargs):
        ''' Companion のフォームセットを作る '''
        kwargs['form'] = CompanionForm
        kwargs['can_delete'] = False
        kwargs['formset'] = OrderCompanionFormset
    
        #: 通常
        if request and request.method == "POST":
            formset = inlineformset_factory(
                Order, Companion,
                *args, **kwargs)(request.POST, instance=order)
    
        else:
            formset = inlineformset_factory(
                Order, Companion, extra=extra,
                *args, **kwargs)(instance=order)
    
        return formset                    
                    
_errs のメッセージは non_form_errosにでます:

    {% for form in formset %}
    <h4> 帯同者 </h4>
    {% if form.non_form_errors %}
    <div class="alert alert-error">{{ from.non_form_error.as_text }}</div>
    {% endif %}
	....
    {% endfor %}                                                                  
