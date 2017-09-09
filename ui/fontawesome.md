## fontawesome animation

- [Font Awesome Animation](https://l-lin.github.io/font-awesome-animation/) ([github](https://github.com/l-lin/font-awesome-animation))
- [sample](https://l-lin.github.io/font-awesome-animation/demo/partials/usage.html)

### djanog-bower

~~~
BOWER_INSTALLED_APPS = (                                                            
    'fontawesome',                                                                  
    'font-awesome-animation',                                                       
)  
~~~
~~~
$ python manage.py bower install
$ python manage.py collectstatic
~~~

~~~
<link href="{{ STATIC_URL }}fontawesome/css/font-awesome.css" rel="stylesheet">
<link href="{{ STATIC_URL }}font-awesome-animation/dist/font-awesome-animation.min.css" rel="stylesheet">
~~~

## CSS

- [fontawesomeのアイコンをcssの:before/:afterで挿入する](http://qiita.com/ttskch/items/741a272794cff9e72e27)

~~~css
h1:before {
  content: "\f14a";   // fa-check-square のアイコン
  font-family: FontAwesome;
}
~~~

アイコンの後に空白を入れる:
- [Unicode 空白文字等調査](http://d.hatena.ne.jp/s_hiiragi/20110111/1294755929)
- [Unicode spaces](https://www.cs.tut.fi/~jkorpela/chars/spaces.html)
- [Chapter 6 Writing Systems and Punctuation](http://www.unicode.org/versions/Unicode9.0.0/ch06.pdf)

~~~css
.fa-download:after {content:  "\2003"; }
~~~
