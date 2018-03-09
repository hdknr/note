## サーバーからエラーを返す

- 400

~~~py
from django.http import HttpResponseBadRequest
...

def upload_image(request):
  ...

  if form.cleaned_data['photo'].size > IMAGE_LIMIT:
      return HttpResponseBadRequest(_('Image size is too large'))
  ...
~~~
