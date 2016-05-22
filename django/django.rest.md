## REST Framework

- http://www.django-rest-framework.org/
- [tomchristie/django-rest-framework](https://github.com/tomchristie/django-rest-framework)

## doac

- https://github.com/Rediker-Software/doac


## REST Framework OAuth

- [REST Framework OAuth](http://jpadilla.github.io/django-rest-framework-oauth/)
- [jpadilla/django-rest-framework-oauth](https://github.com/jpadilla/django-rest-framework-oauth)


## フィールドデータをオーバーライド

- [SerializerMethodField](http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield)


~~~py
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    ''' get_{{ シリアライザーフィールド名 }} のメソッドを用意すること'''

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
~~~        

- GIS フィールドの場合

~~~py
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

class BusSerializer(serializers.ModelSerializer):
    location = gis_serializers.GeometrySerializerMethodField()

    def get_location(self, obj):
        return obj.gps_location        

    class Meta:
        model = Bus
~~~


## Django

- http://stackoverflow.com/questions/21925671/convert-django-model-object-to-dict-with-all-of-the-fields-intact
