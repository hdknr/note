## ソースからインストール
- gettext, autoconf は必要

~~~bash
    # wget https://github.com/git/git/archive/master.zip
    # unzip master
    # cd git-master/
    # autoconf
    # ./configure --prefix=$HOME/local --with-curl=/usr/local --with-expat
    # make all
    # make install
    # ~/local/bin/git --version
~~~

- /usr/local いれるなら
-
~~~
$ sudo make prefix=/usr/local install
~~~

## fatal: Unable to find remote helper for 'https'

~~~
$ sudo apt-get install libcurl4-openssl-dev
$ autoconf
$ ./configure  --with-expat --with-curl
$ make && sudo make prefix=/usr/local install
~~~

## error setting certificate verify locations

~~~
fatal: unable to access 'https://github.com/riywo/anyenv/': error setting certificate verify locations:
  CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: none
~~~

とりあえず無視する

~~~  
$ export GIT_SSL_NO_VERIFY=true  
~~~
