## フィンガープリント

~~~
$ ssh-keygen  -lf ~/.ssh/id_rsa.pub 

2049 26:fb:4d:82:b2:53:2e:3c:b0:fa:0e:12:a1:b3:1d:85 /home/vagrant/.ssh/id_rsa.pub (RSA)
~~~


## RSA 4096ビット

~~~
$ ssh-keygen -t rsa -b 4096
~~~

## known_hosts

- [ssh-keygen コマンド](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh-keygen.1?query=ssh-keygen&sec=1)
- [SSHのknown_hostsをスマートに更新する
](http://qiita.com/kawaz/items/20983ec286088a1ae5c7)


- 探す

~~~
$ ssh-keygen  -F  myserver.com
~~~

- 削除

~~~
$ ssh-keygen -R myserver.com

# myserver.com found: line 13 type RSA
/Users/hide/.ssh/known_hosts updated.
Original contents retained as /Users/hide/.ssh/known_hosts.old
~~~