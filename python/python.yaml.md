## XMLをYAMLに変換
- [OrderedDict](http://docs.python.jp/2/library/collections.html#ordereddict) を処理できないので

~~~py
import xmltodict                                                                    
import yaml                                                                         
import json                                                                         
import sys                                                                          

doc = xmltodict.parse(open(sys.argv[1]).read())                                     
doc = json.loads(json.dumps(doc))                                                   

print yaml.safe_dump(doc, allow_unicode=True)  
~~~
