## 互換コード
- [Six: Python 2 and 3 Compatibility Library](https://pythonhosted.org/six/)
- [Cheat Sheet: Writing Python 2-3 compatible code](http://python-future.org/compatible_idioms.html)


## いろいろ

~~~
from __future__ import print_function
~~~

## unicode_literals

~~~python
from __future__ import unicode_literals
~~~

- [Should I import unicode_literals?](http://python-future.org/unicode_literals.html)

## basestring

- python3にはありません

~~~py
>>> import six
>>> isinstance('aaa', (str, six.text_type))
True
~~~

~~~py
>>> sys.version
'3.4.3 (default, Sep 10 2015, 06:57:28) \n[GCC 4.9.2]'
>>> six.text_type
<class 'str'>
~~~

~~~py
>>> sys.version
'2.7.9 (default, Apr 24 2015, 02:28:37) \n[GCC 4.9.2]'
>>> six.text_type
<type 'unicode'>
~~~

## ord

~~~py
>>> sys.version
'2.7.9 (default, Apr 24 2015, 02:28:37) \n[GCC 4.9.2]'
>>> six.b('xxx')[0]
'x'
>>> type(six.b('xxx')[0])
<type 'str'>
~~~

~~~py
>>> sys.version
'3.4.3 (default, Sep 10 2015, 06:57:28) \n[GCC 4.9.2]'
>>> six.b('xxx')[0]
120
>>> type(six.b('xxx')[0])
<class 'int'>
~~~

## `TypeError: ord() expected string of length 1, but int found`

~~~py
>>> x = b'a'
>>> x[0]
97
>>> ord(x[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected string of length 1, but int found
~~~

- python3

~~~py
>>> x = b'abc'
>>> type(x[1:2])
<class 'bytes'>
>>> type(x[1])
<class 'int'>
~~~

- これはどちらでも動く

~~~py
>>> x[:1]
b'a'
>>> ord(x[:1])
97
~~~

## 文字列 -> バイト列

~~~py
from __future__ import print_function                                               
'''                                                                                 
python 2:                                                                           

    six.string_types: (<type 'basestring'>,)
    six.text_type: <type 'unicode'>
    six.binary_type: <type 'str'>

python 3:
    six.string_types: (<class 'str'>,)
    six.text_type: <class 'str'>
    six.binary_type: <class 'bytes'>

'''                                                                                 
import six


def to_bytes(src, enc='utf8'):                                                      
    return isinstance(src, six.text_type) and src.encode(enc) or src                

for i in ['a', u'a', b'a']:                                                         
    assert type(to_bytes(i)) == six.binary_type   
~~~
