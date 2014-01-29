Date: 2014-01-23  17:00
Title: Python : 匿名クラス  
Type: post  
Excerpt:   


type('',(),{})() で作成できるそうです :

    >>> import requests
    >>> url = 'http://op.dev:4000/.well-known/openid-configuration'
    >>> meta = type('',(object,), requests.get(url).json )()
    >>> dir(meta)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', 
     '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', 
     '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
     u'authorization_endpoint', u'claims_supported', u'grant_types_supported', 
     u'id_token_signing_alg_values_supported', u'issuer', u'jwks_uri', 
     u'registration_endpoint', u'request_object_signing_alg_values_supported', 
     u'response_types_supported', u'scopes_supported', u'subject_types_supported', 
     u'token_endpoint', u'token_endpoint_auth_methods_supported', u'userinfo_endpoint']

基底クラスを作る

    >>> class ProviderMeta(object):
    ...    authorization_endpoint = None
    ...    def authzep(self):
    ...       return self.authorization_endpoint
    ... 

基底クラスのサブクラスで作成:

    >>> meta = type('',(ProviderMeta,), requests.get(url).json )()

メソッド継承されている:

    >>> meta.authzep()
    u'http://op.dev:4000/authorizations/new'
    
同じ型のインスタンスをもう一つ:

    >>> meta2 = type(meta)()
    >>> type(meta2)
    <class '__main__.'>

元がプロトタイプになっている:

    >>> meta2.authorization_endpoint == meta.authorization_endpoint
    True

もちろん別々のインスタンス:

    >>> meta2.authorization_endpoint ='http://google.com'
    >>> meta2.authzep()
    'http://google.com'
    >>> meta2.authorization_endpoint == meta.authorization_endpoint
    False
