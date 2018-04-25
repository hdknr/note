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


## mysqld の監視 (/etc/monit/conf.d/mysql.conf)

bitnamiのMySQL監視:

~~~bash
check process mysql with pidfile /var/run/mysqld/mysqld.pid
    start program = "/etc/init.d/mysql start"
    stop program = "/etc/init.d/mysql stop"
    if failed port 3306 then restart
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

## 記事

- [
【Ubuntu】monit によるプロセス監視と Slack 通知【Webhook】](https://fisproject.jp/2017/07/slack-notification-from-monit/)
