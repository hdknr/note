## proxy：キャッシュしない

~~~py
from django.views.decorators.cache import patch_cache_control
  from functools import wraps
~~~

- デコレータ

~~~py
def never_ever_cache(decorated_function):

    @wraps(decorated_function)
    def wrapper(*args, **kwargs):

        # オリジナル関数
        response = decorated_function(*args, **kwargs)

        # キャッシュさせないようにする
        patch_cache_control(
            response, no_cache=True, no_store=True, must_revalidate=True,
            max_age=0)
        # no-cache
        response['Pragma'] = 'no-cache'

        return response
    return wrapper
~~~    

- プロキシ

~~~py
import requests

@never_ever_cache
def proxy(request):
    cookies = request.META.get('HTTP_COOKIE', '')
    url = create_url(request)
    # Access Google Analytics
    requests.get(
        url, cookies=parse_cookie(cookies),
        headers={
            'User-Agent': request.META.get('HTTP_USER_AGENT', 'Unknown'),
            'Accepts-Language:': request.META.get("HTTP_ACCEPT_LANGUAGE", ''),
        },)
    return HttpResponse(GIF_DATA, content_type='image/gif')
~~~
