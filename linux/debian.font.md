## Debian にIPAのTrueTypeを導入

- [IPAフォント(Debian)のインストール](http://symfoware.blog68.fc2.com/blog-entry-1505.html)
- [IPAフォント](http://ipafont.ipa.go.jp/ipafont/download.html)

~~~
$ wget -O IPAfont00303.zip  http://ipafont.ipa.go.jp/ipafont/IPAfont00303.php  

--2015-01-26 04:54:31--  http://ipafont.ipa.go.jp/ipafont/IPAfont00303.php
Resolving ipafont.ipa.go.jp (ipafont.ipa.go.jp)... 192.218.88.244
Connecting to ipafont.ipa.go.jp (ipafont.ipa.go.jp)|192.218.88.244|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: http://dl.ipafont.ipa.go.jp/IPAfont/IPAfont00303.zip [following]
--2015-01-26 04:54:37--  http://dl.ipafont.ipa.go.jp/IPAfont/IPAfont00303.zip
Resolving dl.ipafont.ipa.go.jp (dl.ipafont.ipa.go.jp)... 192.218.88.241
Connecting to dl.ipafont.ipa.go.jp (dl.ipafont.ipa.go.jp)|192.218.88.241|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 20088137 (19M) [application/zip]
Saving to: ‘IPAfont00303.zip’

  

2015-01-26 04:54:56 (1018 KB/s) - ‘IPAfont00303.zip’ saved [20088137/20088137]
~~~

~~~
$ unzip IPAfont00303.zip -d /tmp
Archive:  IPAfont00303.zip
  inflating: /tmp/IPAfont00303/IPA_Font_License_Agreement_v1.0.txt  
  inflating: /tmp/IPAfont00303/ipag.ttf  
  inflating: /tmp/IPAfont00303/ipagp.ttf  
  inflating: /tmp/IPAfont00303/ipam.ttf  
  inflating: /tmp/IPAfont00303/ipamp.ttf  
  inflating: /tmp/IPAfont00303/Readme_IPAfont00303.txt  
~~~

~~~
$ sudo mv /tmp/IPAfont00303 /usr/share/fonts/truetype/
~~~  

~~~
$ sudo fc-cache

$ sudo fc-list | grep ipa

/usr/share/fonts/truetype/IPAfont00303/ipagp.ttf: IPAPGothic,IPA Pゴシック:style=Regular
/usr/share/fonts/truetype/IPAfont00303/ipamp.ttf: IPAPMincho,IPA P明朝:style=Regular
/usr/share/fonts/truetype/IPAfont00303/ipag.ttf: IPAGothic,IPAゴシック:style=Regular
/usr/share/fonts/truetype/IPAfont00303/ipam.ttf: IPAMincho,IPA明朝:style=Regular
~~~

## コマンド

- fc-cache
- fc-list