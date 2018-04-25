## インストール

~~~bash
$ sudo apt-get install monit
~~~

~~~bash
$ sudo ps ax | grep monit
 1251 ?        Ss     0:00 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemonise --scan --syslog
11467 ?        S      0:00 /usr/bin/monit -c /etc/monit/monitrc
~~~

## /etc/monit/monitrc

~~~bash
$ sudo grep -v "^#" /etc/monit/monitrc

  set daemon 120            # check services at 2-minute intervals
  set logfile /var/log/monit.log
  set idfile /var/lib/monit/id
  set statefile /var/lib/monit/state


  set eventqueue
      basedir /var/lib/monit/events # set the base directory where events will be stored
      slots 100                     # optionally limit the queue size
   include /etc/monit/conf.d/*
   include /etc/monit/conf-enabled/*
~~~


## mysqld の自動起動 (/etc/monit/conf.d/mysql)

~~~bash
check process mysql with pidfile /var/run/mysqld/mysqld.pid
    start program = "/etc/init.d/mysql start"
    stop program = "/etc/init.d/mysql stop"
    if 5 restarts within 5 cycles then timeout
~~~

ログ:

~~~
$ suod tail /var/log/monit.log
[UTC Apr 25 05:38:35] error    : 'mysql' process is not running
[UTC Apr 25 05:38:35] info     : 'mysql' trying to restart
[UTC Apr 25 05:38:35] info     : 'mysql' start: /etc/init.d/mysql
~~~


## Action unmonitor not possible - monit http interface is not enabled, please add the 'set httpd' statement

~~~
$ sudo monit status
Status not available - monit http interface is not enabled, please add the 'set httpd' statement
~~~

/etc/monit/monitrc で httpd ポート監視を有効にする(コメントアウトする):

~~~
set httpd port 2812 and
    use address localhost  # only accept connection from localhost
    allow localhost        # allow localhost to connect to the server and
    allow admin:monit      # require user 'admin' with password 'monit'
~~~    


## 通知

起動した時にアラートを送るように, 起動スクリプトを変更:

~~~
check process mysql with pidfile /var/run/mysqld/mysqld.pid
     start program = "/bin/bash -c '/etc/init.d/mysql start && /home/ubuntu/bin/slert.py restart'"
     stop program = "/etc/init.d/mysql stop"
     if 1 restarts within 1 cycles then exec "/home/ubuntu/bin/slert.py error'"
     if 5 restarts within 5 cycles then timeout
~~~     

slert.py:

~~~py
#!/usr/bin/python3
'''pip install slackweb'''
import slackweb
URL='https://hooks.slack.com/services/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'
slack = slackweb.Slack(url=URL)
slack.notify(text="エラー")
~~~


## 考察

start プログラムにダミーのコマンドを指定してみる:

~~~
check process mysql with pidfile /var/run/mysqld/mysqld.pid
     start program = "/bin/bash -c '/home/ubuntu/bin/dummy.sh'"
     stop program = "/etc/init.d/mysql stop"
     if 1 restarts within 1 cycles then exec "/bin/bash -c '/etc/init.d/mysql start && /home/ubuntu/bin/slert.py'"  
     if 5 restarts within 5 cycles then timeout
~~~

mysqld をkillする

~~~bash
$ sudo killall mysqld
~~~

最初のサイクルで start プログラムを実行:

~~~
[UTC Apr 25 08:25:09] info     : 'mysql' trying to restart
[UTC Apr 25 08:25:09] info     : 'mysql' start: /bin/bash
[UTC Apr 25 08:25:39] error    : 'mysql' failed to start (exit status 0) -- no output
~~~

次のサイクルで `exec` され(startも実行されるがこれはダミー)て、mysqdが起動し、アラートも飛ぶ:

~~~
[UTC Apr 25 08:27:39] error    : 'mysql' service restarted 1 times within 1 cycles(s) - exec
[UTC Apr 25 08:27:39] info     : 'mysql' exec: /bin/bash
[UTC Apr 25 08:27:39] error    : 'mysql' process is not running

[UTC Apr 25 08:27:39] info     : 'mysql' trying to restart
[UTC Apr 25 08:27:39] info     : 'mysql' start: /bin/bash
[UTC Apr 25 08:27:40] info     : 'mysql' started
~~~

結局以下のようにすると１ cycleめで再起動させて成功したら次のサイクルで`exec`される:

~~~
check process mysql with pidfile /var/run/mysqld/mysqld.pid
     start program = "/etc/init.d/mysql start"
     stop program = "/etc/init.d/mysql stop"
     if does not exist then restart
     else if succeeded for 1 cycle then exec "/home/ubuntu/bin/slert.py restart"
     if 5 restarts within 5 cycles then timeout
~~~     

~~~
[UTC Apr 25 08:56:20] error    : 'mysql' process is not running
[UTC Apr 25 08:56:20] info     : 'mysql' trying to restart
[UTC Apr 25 08:56:20] info     : 'mysql' start: /etc/init.d/mysql


[UTC Apr 25 08:58:22] info     : 'mysql' process is running with pid 24467
[UTC Apr 25 08:58:22] info     : 'mysql' exec: /home/ubuntu/bin/slert.py
~~~

## 記事

- [
【Ubuntu】monit によるプロセス監視と Slack 通知【Webhook】](https://fisproject.jp/2017/07/slack-notification-from-monit/)
- [Debian 9 (Stretch) - Monit でプロセス監視！](https://www.mk-mode.com/octopress/2017/10/06/debian-9-monit-monitoring/)
