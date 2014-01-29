Date: 2013-10-10  17:30
Title: Django:GenericTabularInlineの新規追加するときの初期値を指定する  
Type: post  
Excerpt:   

TaggedItem モデルが GenericForeignKeyで実装されていて、さらにForeignKeyでTagモデルを参照している場合、TaggedItemをGenericForeingKey先のモデルの編集画面で、TaggedItemの追加/編集するときに新規のTagが必要な場合。 Tagのフォームがポップアップするがそれに初期値を与えたい。

Tagモデル。タグ名とどのモデルに対するタグか、を持っている。:

    class Tag(models.Model):
        content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
        name = models.CharField(_(u'Name'),max_length=100,db_index=True,)

TaggedItemモデル。実際にあるモデルに付与するタグ:

    class TaggedItem(models.Model):
        tag = models.ForeignKey(Tag,verbose_name=_(u'Tag'))
        content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
        object_id = models.PositiveIntegerField()
        content_object = generic.GenericForeignKey('content_type', 'object_id')
        user = models.ForeignKey(User,verbose_name=_(u'Creator'))

TicketモデルのAdmin UIでTaggedItemのカスタムフォームを指定。
このフォームの中でwidgetのrender() をカスタムのメソッド(custom_render)で入れ替える。
ウィジェットは django.contrib.admin.widgets.RelatedFieldWidgetWrapper なハズ :

    import new 

    class TicketTaggedItemForm(forms.ModelForm):
        def __init__(self,*args,**kwargs):
            super(TicketTaggedItemForm,self).__init__(*args,**kwargs)
            self.fields['tag'].queryset = Tag.objects.filter(
                            content_type = ContentType.objects.get_for_model(Ticket))
    
            #: renderを入れ替えて URL に添付するquery parameter 指定する
            self.fields['tag'].widget.render = new.instancemethod( custom_render,
                                    self.fields['tag'].widget,None)
            self.fields['tag'].widget.query_param = 'content_type=%d' %  ContentType.objects.get_for_model(Ticket).id

このフォームの中でwidgetのrender() をカスタムのメソッド(custom_render)で入れ替える。
入れ替えたさきでJavascriptでポップアップされるURLにクエリパラメータを入れる。:

    def custom_render(self, name, value, *args, **kwargs):
        rel_to = self.rel.to
        info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
        self.widget.choices = self.choices
        output = [self.widget.render(name, value, *args, **kwargs)]
        if self.can_add_related:
            related_url = reverse('admin:%s_%s_add' % info, current_app=self.admin_site.name)
    
            #:--- ここから:widgetにquery_paramがあればURLに添付する
            query_parameter =  getattr(self,'query_param','')
            if query_parameter:
                related_url = related_url + "?" + query_parameter
            #:--- ここまで追加
        
            # TODO: "add_id_" is hard-coded here. This should instead use the
            # correct API to determine the ID dynamically.
            output.append('<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> '
                          % (related_url, name))
            output.append('<img src="%s" width="10" height="10" alt="%s"/></a>'
                          % (static('admin/img/icon_addlink.gif'), _('Add Another')))
        return mark_safe(''.join(output)) 


これでポップアップされるURLのパラメータに content_type=48 が渡されるので、DjangoのAdminのフォームがリレーションフィールドのウィジェット(プルダウンセレクト)を適切に初期化してくれます。

