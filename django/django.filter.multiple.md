Django: django-filter でモデルフィールドの検索指定を２つ以上のフィールドに分ける

- [alex/django-filter](https://github.com/alex/django-filter) ([doc](https://django-filter.readthedocs.org/en/latest/))

## やりたいこと

- 複数選択指定であるフィールドを検索する(タグとか)
- 選択肢はデータベースから(ModelMultipleChoiceFilter)
- 選択肢が多すぎるので、よく使われる選択支だけを最初だして、「もっと」をクリックしたら追加の選択肢を提示する

## 検索対象テーブルの選択支を二つに割る

- メジャーな選択肢が disp=1, それ以外は disp=0のDepartmentテーブルから選択肢を引いてくる

~~~py
class AlumnusFilter(django_filters.FilterSet):                                

    depts = django_filters.ModelMultipleChoiceFilter(                               
        queryset=models.Department.objects.filter(disp=1),                          
        widget=forms.widgets.CheckboxSelectMultiple,                                
    )                                                                               

    depts_ex = django_filters.ModelMultipleChoiceFilter(                            
        queryset=models.Department.objects.filter(disp=0),                          
        widget=forms.widgets.CheckboxSelectMultiple,                                
    )                                                                               

    class Meta:
      model = models.Alumnus
~~~

## フィルター関数を指定

- 関数を指定しないとモデルのQuerySetにフィルターかけてエラーになるので`__init__`で指定する
- depts, depts_ex のフィルターとして filter_deptsメソッドを使う
- filter_deptsに `field` 引数を追加し、 functools.partialでこれを部分適用して設定することで１つのフィルターにまとめる
- self.dept_items にrequest.GETにデータが存在するフィールド名一覧する(最後のフィルターを判定するフラグ)
- self.dept_values は空のlistで初期化しておく

~~~py
def __init__(self, data, *args, **kwargs):                                   
    self.depts_items = {}                                                    
    self.depts_values = []                                                   

    for i in ['depts', 'depts_ex', ]:                                        
        self.base_filters[i].filter = partial(self.filter_depts, field=i)    
        if data.get(i, None):                                                
            self.depts_items[i] = i                                          

    super(AlumnusFilter, self).__init__(data, *args, **kwargs)         
~~~

## フィルター関数

- valueが指定されたら、 Department.code のリストに変換する
- リストは self.depts_valuesに貯める
- 変換したら自分を self.depts_itemsから抜く
- deptsに関して処理すべきフィルターの最後だったら、querysetをフィルターする。最後でなかったらquersetをそのまま返す。
- deptsを判定するフイールドが３個あるのでORでクエリを組み立てる

~~~py
def filter_depts(self, queryset, value, field=None):                         
    if value:                                                                
        del self.depts_items[field]                                          
        self.depts_values += [i.code for i in value]                         

    if not self.depts_items:                                                 
        return queryset.filter(                                              
            Q(dept_code_1__in=self.depts_values) |                      
            Q(dept_code_2__in=self.depts_values) |                      
            Q(dept_code_2__in=self.depts_values))                       

    return queryset  
~~~    

## 追加選択肢の表示/非表示を切り替えるチェックボックス

- JavascriptのUIのトリガー用のチェックボックス
- クエリのフィルターとは関係ないのでフォームとしてフィールドを用意する
- メタクラスの form パラメータにフォームを定義するとよい

~~~py
class Meta:                                                                  
    form = type('BaseForm', (forms.Form,), dict(                             
        depts_ex_on=forms.BooleanField(label=_('Dept Ex On'))                
    ))
~~~    
