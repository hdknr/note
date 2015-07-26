## ord  

~~~
>>> ord(u"あ")
12354
>>> hex(ord(u"あ"))
0x3042
>>> u"\u3042" == u"あ"
True
~~~

## unichr

~~~
>>> unichr(12354)
u"\u3042" 
~~~

## BOM

~~~
 UnicodeEncodeError: 'cp932' codec can't encode character u'\ufeff' 
 in position 0: illegal multibyte sequence
~~~

~~~py
import codecs
for line in codecs.open(path,"r",'utf-8-sig')
	pass
~~~

### unichr(65532)

- Windowsで作ったPDFをコピペしたとき、空白のコードが違うケース

~~~py
line = line.replace(unichr(65532), '').strip()    
~~~
	 

