Date: 2013-06-27  10:30
Title: upstart : イベント起動のデーモンも自動自動再起動します
Type: post  
Excerpt:   


supervisordをupstartで動かしている。MySQLが動いてから起動するようにしてます。

    system@wheezy:~$ more /etc/init/supervisord.conf 

    description "supervisord"
         
    start on mysqlready
    stop on runlevel [!2345]
         
    respawn
    script 
       exec /usr/local/bin/supervisord -n -c /etc/supervisord.conf
    end script

supervisor確認

    system@wheezy:~$ ps ax | grep supervisor
     1522 ?        Ss     0:12 /usr/bin/python /usr/local/bin/supervisord -n -c /etc/supervisord.conf

強制停止

    system@wheezy:~$ sudo kill -9 1522

再度supervisord 確認

    system@wheezy:~$ sudo ps ax | grep super
       14 ?        S      0:00 [sync_supers]
    15090 ?        Ss     0:00 /usr/bin/python /usr/local/bin/supervisord -n -c /etc/supervisord.conf


syslog確認

	system@wheezy:~$ sudo tail /var/log/syslog


	Jun 27 10:28:29 wheezy kernel: [65128.391657] init: supervisord main process (1522) killed by KILL signal
	Jun 27 10:28:29 wheezy kernel: [65128.391708] init: supervisord main process ended, respawning