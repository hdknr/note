- https://wkhtmltopdf.org/
- [wkhtmltopdf/wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)

## Ubuntu 17.10

~~~bash
$ sudo apt-get install xvfb
$ sudo apt-get install wkhtmltopdf
~~~

フォント:

~~~bash
$ sudo apt-get install fonts-takao-gothic
~~~

~~~bash
$ fc-list | grep takao
/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf: Takao Pゴシック,TakaoPGothic:style=Regular
/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf: Takaoゴシック,TakaoGothic:style=Regular
~~~

## 簡単な作成

カレントディレクトリにあるindex.html:

~~~
$ xvfb-run wkhtmltopdf index.html index.pdf
~~~

## python

~~~bash
$ pip install pyvirtualdisplay    
$ pip install EasyProcess
~~~
