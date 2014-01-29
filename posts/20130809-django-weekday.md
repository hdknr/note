Date: 2013-08-09  13:00
Title:   Django : 曜日
Type: post  
Excerpt:   

adate.strftime("%a") すると Friとかロケールを設定しなければいけなそうなので、

    from django.utils.dateformat import format
    
    format(adate,"Y/m/d(D)")
    
とかすると、Djagoのsettingsとかロケールの設定してくれるから日本語の曜日で表示できる。

OrderFormで、予約可能な日付けが 30日以下だったらリストボックス、１日だったらデータで埋める。それ以外だったら、手で入力してもらう:

    def __init__(self,user,id,oid=None,ordering_date=None,*args,**kwargs):
        #: 省略
        #:
        if self.start_date == self.end_date:
            # ticket.usedate_from == ticket.usedate_to だったら、データを埋める
            self.base_fields['usedate'].initial = self.start_date
        elif self.days <= 30: 
            # ticket.usedata_to != None で、選択可能日数が 30日以下だったらリストボックス
            choices=[]
            for i in range(self.days):
                d = self.start_date + timedelta(days=i)
                choices.append((d,format( d, "Y/m/d(D)")) )
            self.base_fields['usedate'].widget = forms.Select(choices=tuple(choices),)
        else:
            #:それ以外はYYYY-MM-DDで入力
            pass
            
        super(OrderForm,self).__init__(*args,**kwargs)    

テスト:

    <p><label for="id_usedate">利用日:</label> <select id="id_usedate" name="usedate">
    <option value="2013-08-19" selected="selected">2013/08/19(月)</option>
    <option value="2013-08-20">2013/08/20(火)</option>
    <option value="2013-08-21">2013/08/21(水)</option>
    <option value="2013-08-22">2013/08/22(木)</option>
    <option value="2013-08-23">2013/08/23(金)</option>
    <option value="2013-08-24">2013/08/24(土)</option>
    <option value="2013-08-25">2013/08/25(日)</option>
    <option value="2013-08-26">2013/08/26(月)</option>
    <option value="2013-08-27">2013/08/27(火)</option>
    <option value="2013-08-28">2013/08/28(水)</option>
    </select></p>
