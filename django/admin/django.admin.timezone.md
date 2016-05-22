
## Add, Change の際に強制的にタイムゾーンを変更する

### Regionモデル : tz フィールドにタイムゾーンを持っている

~~~py
class Region(BaseModel):
    tz = models.CharField(default='Asia/Tokyo', max_length=30)

    @property
    def timezone(self):
        return self.tz and pytz.timezone(self.tz)
~~~

### RegionモデルをForeginKeyで参照しているモデルの

~~~py
from django.utils import timezone

class RegionChildAdmin(admin.OSMGeoAdmin):

    def set_current_timezone(self, region):
        if region and region.timezone:
            timezone.activate(region.timezone)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.set_current_timezone(
            models.Region.objects.filter(announce__id=object_id).first())

        return super(RegionChildAdmin, self).change_view(
            request, object_id, form_url=form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        region = request.POST.get(
            'region', request.GET.get('region', None))
        if region:
            self.set_current_timezone(
                models.Region.objects.filter(id=region).first())

        return super(RegionChildAdmin, self).add_view(
            request, form_url=form_url, extra_context=extra_context)
~~~            
