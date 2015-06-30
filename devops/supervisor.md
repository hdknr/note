## その他

- [circus](http://circus.readthedocs.org/en/0.11.1/)
- [Linux daemonとsupervisordの美味しい関係](http://www.slideshare.net/KazushigeTakeuchi/linux-daemonsupervisord)

## インストール

- [Docs: Installing ](http://supervisord.org/installing.html)

~~~
# pip install supervisor
~~~

~~~
# which supervisorctl 
/root/.anyenv/envs/pyenv/shims/supervisorctl
~~~

### 設定ディレクトリ

~~~
# mkdir  /etc/supervisord.conf.d
~~~

### 設定ファイル

~~~
# echo_supervisord_conf > /etc/supervisord.conf
~~~

- 差分確認のため

~~~
# echo_supervisord_conf > /tmp/supervisord.conf.dist
~~~

-  Debianように編集

~~~
*** /tmp/supervisord.conf.dist  2015-04-02 07:35:29.000000000 +0900
--- /etc/supervisord.conf       2015-04-02 07:38:14.000000000 +0900
***************
*** 9,15 ****
--- 9,16 ----

  [unix_http_server]
! ;file=/tmp/supervisor.sock   ; (the path to the socket file)
! file=/var/run/supervisor.sock

***************
*** 21,31 ****
--- 22,34 ----

  [supervisord]
! ;logfile=/tmp/supervisord.log ; (main log file;default $CWD/supervisord.log)
! logfile=/var/log/supervisord.log

! ;pidfile=/tmp/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
! pidfile=/var/run/supervisord.pid ;

***************
*** 45,51 ****
--- 48,55 ----
  supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
  
  [supervisorctl]
! ;serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
! serverurl=unix:///var/run/supervisor.sock

***************
*** 139,141 ****
--- 143,146 ----
  
  ;[include]
  ;files = relative/directory/*.ini
+ files = /etc/supervisord.conf.d/*.ini

~~~

### debian: /etc/init.d/supervisord

- Debian sysvinit

~~~
# curl https://raw.githubusercontent.com/Supervisor/initscripts/master/debian-norrgard > supervisord
~~~

~~~
# chmod 755 supervisrod
~~~

- conf のパス. 以下の引数を修正

~~~
DAEMON_ARGS="--pidfile ${PIDFILE} -c /etc/supervisord.conf"
~~~

- deamon プログラムのパス

~~~
$ln -s $(which supervisord) /usr/bin/
~~~

- スクリプトパス

~~~
ln -s $(which supervisorctl ) /usr/bin/
~~~

## 起動

- [github initscripts](https://github.com/Supervisor/initscripts)
