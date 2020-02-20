
# インストール

## install: Mac Homebrew

~~~bash
$ brew install tmux
.
~~~

## install: CentOS

- [tmux: CentOS 6.3にインストール記録](https://github.com/hdknr/scriptogr.am/blob/master/posts/20140128-tmux-centos.md)

~~~bash
$ sudo yum groupinstall 'Development Tools'

$ mkdir src && cd src
$ wget https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz --no-check-certificate
$ tar zxvf libevent-2.0.21-stable.tar.gz
$ cd libevent-2.0.21-stable
$ cd /etc/ld.so.conf.d/
$ echo /usr/local/lib  |sudo tee -a libevent2.conf
/usr/local/lib
$ sudo ldconfig  
~~~

- tmux 2.0

~~~bash
$ cd && cd src
$ sudo yum install ncurses-devel
$ wget http://downloads.sourceforge.net/tmux/tmux-2.0.tar.gz
$ tar xvfz tmux-2.0.tar.gz
$ cd tmux-2.0
$ tmux -V
tmux 2.0
~~~

## install : Ubuntu LTS 14.04

- [ppa:pi-rho/dev](https://launchpad.net/~pi-rho/+archive/ubuntu/dev)

~~~bash
$ sudo apt-get update
$ sudo apt-get install -y python-software-properties software-properties-common
$ sudo add-apt-repository -y ppa:pi-rho/dev
$ sudo apt-get update
$ sudo apt-get install -y tmux
$ tmux -V
tmux 2.0
~~~