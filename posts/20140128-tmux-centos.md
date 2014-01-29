Date: 2014-01-28  11:25
Title: tmux: CentOS 6.3にインストール記録
Type: post  
Excerpt:   


インストールログ:
  
    $ wget https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz --no-check-certificate
    $ tar zxvf libevent-2.0.21-stable.tar.gz
    $ cd libevent-2.0.21-stable
    $ ./configure && make && sudo make install
    $ cd /etc/ld.so.conf.d/
    $ echo /usr/local/lib  |sudo tee -a libevent2.conf
    $ sudo ldconfig  
    $ ldconfig -p | grep libevent
          libevent_pthreads-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent_pthreads-2.0.so.5
          libevent_extra-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent_extra-2.0.so.5
          libevent_extra-1.4.so.2 (libc6,x86-64) => /usr/lib64/libevent_extra-1.4.so.2
          libevent_core-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent_core-2.0.so.5
          libevent_core-1.4.so.2 (libc6,x86-64) => /usr/lib64/libevent_core-1.4.so.2
          libevent-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent-2.0.so.5
          libevent-1.4.so.2 (libc6,x86-64) => /usr/lib64/libevent-1.4.so.2
  
    $ wget http://downloads.sourceforge.net/tmux/tmux-1.8.tar.gz
    $ tar xvfz tmux-1.8.tar.gz
    $ cd tmux-1.8
    $ ./configure && make && sudo make install
    $ tmux -V
    tmux 1.8
