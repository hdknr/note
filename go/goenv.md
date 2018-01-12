## goenv インストール

~~~bash
$ anyenv install goenv
/tmp/goenv.20180112104835.23550 /vagrant/projects
Cloning https://github.com/syndbg/goenv.git...
Cloning into 'goenv'...
remote: Counting objects: 12816, done.
remote: Total 12816 (delta 0), reused 0 (delta 0), pack-reused 12816
Receiving objects: 100% (12816/12816), 2.25 MiB | 777.00 KiB/s, done.
Resolving deltas: 100% (8883/8883), done.
/vagrant/projects

Install goenv succeeded!
Please reload your profile (exec $SHELL -l) or open a new session.
~~~

~~~bash
$ goenv install 1.9.2
Downloading go1.9.2.linux-amd64.tar.gz...
-> https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz
Installing Go Linux 64bit 1.9.2...
Installed Go Linux 64bit 1.9.2 to /home/vagrant/.anyenv/envs/goenv/versions/1.9.2

~~~

~~~bash
$ goenv global 1.9.2
$ which go
/home/vagrant/.anyenv/envs/goenv/shims/go
$ go version
go version go1.9.2 linux/amd64
~~~

~~~bash
$ mkdir /vagrant/projects/go
$ export GOPATH=/vagrant/projects/go
$ export PATH=$PATH:$GOPATH/bin
~~~


[go get](http://cuto.unirita.co.jp/gostudy/post/command-go-get/)

~~~bash
$ go get github.com/ericchiang/pup
~~~

~~~bash
curl http://www.google.com | pup
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                Dload  Upload   Total   Spent    Left  Speed
100   271  100   271    0     0   3914      0 --:--:-- --:--:-- --:--:--  3927
<html>
<head>
 <meta http-equiv="content-type" content="text/html;charset=utf-8">
 <title>
  302 Moved
 </title>
</head>
<body>
 <h1>
  302 Moved
 </h1>
 The document has moved
 <a href="http://www.google.co.jp/?gfe_rd=cr&amp;dcr=0&amp;ei=Lh5YWs_2OOzZ8AeTlZSYCA">
  here
 </a>
 .
</body>
</html>
~~~

## 記事

- [Goの開発環境に思いを馳せる](https://qiita.com/mi-bear/items/8662c16a2b4917157eb1)
- [GOPATH は適当に決めて問題ない](https://qiita.com/yuku_t/items/c7ab1b1519825cc2c06f)
