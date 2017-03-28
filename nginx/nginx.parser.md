nginxparser: Pythonでnginxの設定ファイルを解析してみる

## nginxparser

-  https://github.com/fatiherikli/nginxparser
-  [pyparsing](http://pyparsing.wikispaces.com/)使ってる
-  https://github.com/peakwinter/python-nginx

### その他パーサ

- [Rubyのやつ](https://github.com/will3942/nginxparser)
- [PHPのやつ](https://github.com/jorisros/nginxparser)


## install

```
$ pip install -e git+https://github.com/fatiherikli/nginxparser#egg=nginxparser
Obtaining nginxparser from git+https://github.com/fatiherikli/nginxparser#egg=nginxparser
  Cloning https://github.com/fatiherikli/nginxparser to /home/vagrant/.pyenv/versions/wordpress/src/nginxparser
Collecting pyparsing>=1.5.5 (from nginxparser)
  Downloading pyparsing-2.0.3-py2.py3-none-any.whl
Installing collected packages: pyparsing, nginxparser

  Running setup.py develop for nginxparser
    Creating /home/vagrant/.pyenv/versions/wordpress/lib/python2.7/site-packages/Nginxparser.egg-link (link to .)
    Adding Nginxparser 0.2 to easy-install.pth file
    Installed /home/vagrant/.pyenv/versions/wordpress/src/nginxparser
Successfully installed nginxparser pyparsing-2.0.3

```

## やってみる

```
>>> from nginxparser import load
>>> conf = load(open('nginx.conf'))
>>> type(conf)
<type 'list'>
```

## locationのmodifireが対応されていないみたい
- [プルリクエストしてみました](https://github.com/fatiherikli/nginxparser/pull/14)
- [とっくに指摘されていた...](https://github.com/fatiherikli/nginxparser/pull/13)(> <)

## nginx.py

- nginx.confを Deibanパッケージのnginxで有効/無効にする
- [pycommand](https://github.com/hdknr/pycommand)というしょぼいargparseのラッパー使ってみた


```py

#!/usr/bin/env python                                                               
from nginxparser import load                                                        
import os                                                                           
from pycommand.command import Command, SubCommand                                   
                                                                                    
                                                                                    
def server_name(file):                                                              
    for i in load(open(file)):                                                      
        for j in (i[0] == ['server']) and i[1] or []:                               
            if j[0] == 'server_name':                                               
                return j[1]                                                         
    return None                                                                     
                                                                                    
                                                                                    
ARGS = [                                                                            
    (('file', ), dict(nargs='?', default='nginx.conf')),                            
]                                                                                   
                                                                                    
                                                                                    
class NginxCommand(Command):                                                        
                                                                                    
    class Enable(SubCommand):                                                       
        args = ARGS                                                                 
                                                                                    
        def run(self, param, **options):                                            
            cname = server_name(param.file)                                         
            print "sudo ln -s {0} /etc/nginx/site-enable/{1}".format(               
                os.path.abspath(param.file), cname)   
            print "mkdir run"                                                       
            print "mkdir logs"                                               
                                                                                    
    class Disable(SubCommand):                                                      
        args = ARGS                                                                 
                                                                                    
        def run(self, param, **options):                                            
            cname = server_name(param.file)                                         
            print "sudo unlink /etc/nginx/site-enable/{0}".format(cname)            
                                                                                    
if __name__ == '__main__':                                                          
    NginxCommand().run()                                    
```    
