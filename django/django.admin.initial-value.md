Django:Admin: 追加フォームに初期値を設定する

Ticket-Orderのモデル

## admin.py: OrderAdminForm

- 通常のモデルフォーム

~~~py
class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []
~~~        

## admin.py: OrderAdmin

- OrderAdminFormを使うようにする
- get_form()
- URIのクエリにいれた ticket_id からTicketオブジェクトを取得
- base_fields['ticket'].initialにセットする

~~~y
class OrderAdmin(admin.ModelAdmin):

    form = OrderAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form_class = super(OrderAdmin, self).get_form(request, obj, **kwargs)
  	    ticket_id = request.REQUEST.get('ticket_id', None)
        form_class.base_fields['ticket'].initial = ticket_id and Ticket.objects.get(id=ticket_id)
        return form_class
~~~

## templates/admin/tickets/ticket/change_form.html

- Django の標準テンプレートをコピる
- Ticketの編集画面で、Orderの追加画面へのアンカーを追加する
- `<a href="history/">{% trans "History" %}</a>` の隣とか

~~~html
<a href="{% url 'admin:tickets_order_add' %}?ticket_id={{ object_id }}">注文 </a>
~~~

## こんなことをしなくても ?ticket={{ticket.id}} を加えればやってくれる


~~~html
<a href="{% url 'admin:tickets_order_add' %}?ticket={{ object_id }}">注文 </a>
~~~
