# OGP

- OGP リクエスト(と思われる) 場合、OGPを返すPHPにリダイレクトする

~~~py
import json
import re
from urllib.parse import parse_qs, urlencode


ogp_ua = [
    re.compile(r'Twitterbot'),
    re.compile(r'facebookexternalhit'),
]

url_maps = {
    re.compile(r'^/ariticle/(?P<id>.\d+)$'): '/ogp/article.php',
}

def is_ogp_request(ua):
    for p in ogp_ua:
        if p.search(ua):
            return True
    return False

def get_ua(request):
    uas = request['headers'].get('user-agent', [])
    return uas[0]['value'] if len(uas) > 0 else ''

def qs_to_dict(querystring):
    return {k : v[0] for k, v in parse_qs(querystring).items()}

def dict_to_qs(params):
    return urlencode(params)

def map_uri(uri, querystring):
    params = qs_to_dict(querystring)
    for p, f in url_maps.items():
        ma = p.search(uri)
        q = ma and ma.groupdict()
        if q:
            params.update(q)
            return (f.format(**q), dict_to_qs(q))
    return (None, None)

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']

    ua = get_ua(request)
    (uri, qs) = map_uri(request.get('uri', ''), request.get('querystring', ''))

    if is_ogp_request(ua) and uri:
        request['headers']['x-ogp-request'] = [{'value': 'on'}]
        request['uri'] = uri or request.get('uri', '/')
        request['querystring'] = qs or request.get('querystring', None)

    return request
~~~
