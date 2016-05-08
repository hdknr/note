from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'(?P<path>.*)', views.publish, name='docs_publish'),
]
