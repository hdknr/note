## パスワード生成

- CentOS  : [CentOSでランダムなパスワードを生成する](http://nullpopopo.blogcube.info/2008/01/memo-centos.html)
- [パスワードに使えるランダム文字列を生成するコマンド](http://qiita.com/speg03/items/ec404c217e417160e2d5)

~~~bash
$ sudo yum install -y expect
$ mkpasswd
37[OenkmF
~~~


##  pwgen

~~bash
$ pip install pwgen
~~~

~~~bash
$ pwgen --help
usage: pwgen [-h] [--capitalize] [--no-capitalize] [--numerals]
             [--no-numerals] [--symbols] [--ambiguous] [-1]
             [pw_length]

random PassWord GENerator

positional arguments:
  pw_length            Password length

optional arguments:
  -h, --help           show this help message and exit
  --capitalize, -c     Include at least one capital letter in the password
  --no-capitalize, -A  Don't include capital letters in the password
  --numerals, -n       Include at least one number in the password
  --no-numerals, -0    Don't include numbers in the password
  --symbols, -y        Include at least one special symbol in the password
  --ambiguous, -B      Don't include ambiguous characters in the password
  -1                   Don't print the generated passwords in columns
~~~
