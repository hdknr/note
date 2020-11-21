# nkf

- [iconv](../i/iconv.md)
- https://stackoverflow.com/questions/42896807/how-to-parse-xml-from-local-file-or-url-with-lxml
- https://lxml.de/index.html
- https://lxml.de/xpathxslt.html

In [4]: from lxml import etree as ET                                                                                                                                                                                                       
## SQL Server: トレースXML

~~~py
import sys
from lxml import etree as ET

e = ET.parse(sys.argv[1])
ns = {'ns': 'http://tempuri.org/TracePersistence.xsd'}
path = '//ns:Event[@name="SQL:BatchStarting"]/ns:Column[@id="1"]/text()'
#
for i in e.xpath(path, namespaces=ns):
    print(i)
~~~


## リンク


- [文字コード変換コマンドの nkfの使い方と実例をまとめました。](http://takuya-1st.hatenablog.jp/entry/20100511/12735859530)

## --overwrite : 置き換え

~~~
$ nfk -w --overwirte hoge.php
~~~


## urlencode

~~~bash
$ echo 'テスト' | nkf -WwMQ | tr = %
%E3%83%86%E3%82%B9%E3%83%88
~~~

~~~bash
$ echo %E3%83%86%E3%82%B9%E3%83%88 | nkf -w --url-input
テスト
~~~
