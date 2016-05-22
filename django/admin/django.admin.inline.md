# 親モデルに応じてインラインの選択肢を絞る

## models.py

- 複数の路線の乗り換え駅になっている駅が地域に存在する


~~~py

class Region(BaseModel):
  ''' 地域 '''
  ....

class Line(BaseModel):
  ''' 路線 '''
  region = models.ForeignKey(Region)
  ...

class Station(BaseModel):
  ''' 駅 '''
  region = models.ForeignKey(Region)
  ...

class LineStation(BaseModel):
  ''' 停車駅 '''
  line = models.ForeignKey(Line)
  station = models.ForeignKey(Station)
  ....
~~~


## admin.py

- LineStation のインライン定義
- `get_formset()` をオーバーライド
- obj(Line) のインスタンスを formset.form に持たせる

~~~py
class LineStationAdminInline(admin.TabularInline):
    model = models.LineStation
    form = LineStationAdminInlineForm

    def get_formset(self, request, obj=None, **kwargs):
        res = super(
            LineStationAdminInline,
            self).get_formset(request, obj=None, **kwargs)

        # Lineインスタンスをフォームクラスに持たせる
        res.form.line = obj
        return res
~~~

- LineStationのフォーム
- LineStationのインラインでフォームにLineのインスタンスがセットされているはず
- `station` を Line.region に含まれるもののみに絞る

~~~py
class LineStationAdminInlineForm(forms.ModelForm):
    class Meta:
        model = models.LineStation

    def __init__(self, *args, **kwargs):
        if 'station' in self.base_fields and self.line:
            # Region中の Stationのみに限定する
            self.base_fields['station'].queryset = \
                self.line.region.station_set
        super(LineStationAdminInlineForm,
              self).__init__(*args, **kwargs)
~~~
