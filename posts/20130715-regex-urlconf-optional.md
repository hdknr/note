Date: 2013-07-15  13:00
Title:  Python : 正規表現のオプションパターン
Type: post  
Excerpt: 

 
いつも忘れる:

    from django.conf.urls import patterns, include, url 
    from views import *

    urlpatterns = patterns('',
        url(r'(?P<id>\d+)/(?P<command>.+)(?:/(?P<oid>\d+))?',command,name="tickets_command",),


reverse()させてみる:     

    >>> from django.core.urlresolvers import reverse

    >>> reverse('tickets_command',kwargs = {'id':3,'command':'cancel','oid':7} )
    '/tickets/3/cancel/7'
    
    >>> reverse('tickets_command',kwargs = {'id':3,'command':'cancel',} )                                                                                                          
    '/tickets/3/cancel'


(?: )が非格納グループ(Non Captureing Groups):

    >>> re.search(r"(http|ftp)://([^/]+)(/[^/]*)?","http://hdknr.com/").groups()

    ('http', 'hdknr.com', '/')
    
    >>> re.search(r"(?:http|ftp)://([^/]+)(/[^/]*)?","http://hdknr.com/").groups()

    ('hdknr.com', '/')


1st,2nd,3rd,4th….:

    >>> map(lambda x : re.search(r"([0-9]+)(st|nd|rd|th)",x).groups(),["1st","2nd","3rd","4th","5th"])
    
    [('1', 'st'), ('2', 'nd'), ('3', 'rd'), ('4', 'th'), ('5', 'th')]


    >>> map(lambda x : re.search(r"([0-9]+)(st|nd|rd|th)",x).groups(),["1st","2nd","3rd","4th","5th","1","2","3","4","5",])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 1, in <lambda>
    AttributeError: 'NoneType' object has no attribute 'groups'
    
数字の後をオプショナル(?)にする:

    >>> map(lambda x : re.search(r"([0-9]+)(st|nd|rd|th)?",x).groups(),["1st","2nd","3rd","4th","5th","1","2","3","4","5",])
    
    [('1', 'st'), ('2', 'nd'), ('3', 'rd'), ('4', 'th'), ('5', 'th'), ('1', None), ('2', None), ('3', None), ('4', None), ('5', None)]
    
非格納にするとキャプチャされなくなるので、 5th == 5 となる:

    >>> map(lambda x : re.search(r"([0-9]+)(?:st|nd|rd|th)?",x).groups(),["1st","2nd","3rd","4th","5th","1","2","3","4","5",])

    [('1',), ('2',), ('3',), ('4',), ('5',), ('1',), ('2',), ('3',), ('4',), ('5',)]

    
URLConfも「非格納」しなくていいんじゃないの？：

        urlpatterns = patterns('',
        url(r'(?P<id>\d+)/(?P<command>.+)(?:/(?P<oid>\d+))?',command,name="tickets_command",),

oid を指定しないと問題ない:

    >>> reverse('tickets_command',kwargs = {'id':3,'command':'cancel',} )
    '/tickets/3/cancel'
    
が、指定されるとだめです。:

    >>> reverse('tickets_command',kwargs = {'id':3,'command':'cancel','oid':7} )

    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "/home/hdknr/ve/slu/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 496, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
      File "/home/hdknr/ve/slu/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 416, in _reverse_with_prefix
    "arguments '%s' not found." % (lookup_view_s, args, kwargs))
    NoReverseMatch: Reverse for 'tickets_command' with arguments '()' and keyword arguments '{'oid': 7, 'command': 'cancel', 'id': 3}' not found.

逆に、オプショナルの?を外すと:

    url(r'(?P<id>\d+)/(?P<command>.+)(?:/(?P<oid>\d+))',command,name="tickets_command",),
    
oidを指定すると問題ない:

    >>> reverse('tickets_command',kwargs = {'id':3,'command':'cancel','oid':7} )

    '/tickets/3/cancel/7'

が、指定しないとエラー(必須だからそうだろう):

    >>> reverse('tickets_command',kwargs = {'id':3,'command':'cancel',} )
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "/home/hdknr/ve/slu/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 496, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
      File "/home/hdknr/ve/slu/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 416, in _reverse_with_prefix
    "arguments '%s' not found." % (lookup_view_s, args, kwargs))
    NoReverseMatch: Reverse for 'tickets_command' with arguments '()' and keyword arguments '{'command': 'cancel', 'id': 3}' not found.
   
    
なので、DjangoのURLConfのパラメータをオプショナルにするには、1)オプショナル()? した上で、 2)非格納にする。
     
    