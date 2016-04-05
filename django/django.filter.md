## ヘルプテキストを消す


~~~js
$(function(){
 $(".form-group .help-block").toggle();
});
~~~

## 文字列検索を全て部分一致にする

~~~py
class ForumFilter(django_filters.FilterSet):

    class Meta:
        model = models.Forum

    def __init__(self, *args, **kwargs):
        super(ForumFilter, self).__init__(*args, **kwargs)

        # CharfFilter を defaultのexact からcontainsに変更
        for i in self.filters:
            if isinstance(self.filters[i],  django_filters.CharFilter):
                self.filters[i].lookup_type = u'contains'
~~~
