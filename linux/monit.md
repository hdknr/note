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

起動スクリプトを変更:

~~~
check process mysql with pidfile /var/run/mysqld/mysqld.pid
     start program = "/bin/bash -c '/etc/init.d/mysql start && /home/ubuntu/bin/slert.py'"
     stop program = "/etc/init.d/mysql stop"
     if 5 restarts within 5 cycles then timeout
~~~     

slert.py:

~~~py
#!/usr/bin/python3
import slackweb
URL='https://hooks.slack.com/services/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'
slack = slackweb.Slack(url=URL)
slack.notify(text="エラー")
~~~

## 記事

- [
【Ubuntu】monit によるプロセス監視と Slack 通知【Webhook】](https://fisproject.jp/2017/07/slack-notification-from-monit/)
- [Debian 9 (Stretch) - Monit でプロセス監視！](https://www.mk-mode.com/octopress/2017/10/06/debian-9-monit-monitoring/)
