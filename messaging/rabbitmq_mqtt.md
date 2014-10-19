RabbitMQ

- [MQTT コトハジメ](https://gist.github.com/voluntas/8238751)

# Debian Jessie Install

~~~
vagrant@10:~$ sudo apt-get install rabbitmq-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  erlang-asn1 erlang-base erlang-corba erlang-crypto erlang-diameter erlang-edoc erlang-eldap
  erlang-erl-docgen erlang-eunit erlang-ic erlang-inets erlang-mnesia erlang-nox erlang-odbc erlang-os-mon
  erlang-parsetools erlang-percept erlang-public-key erlang-runtime-tools erlang-snmp erlang-ssh erlang-ssl
  erlang-syntax-tools erlang-tools erlang-webtool erlang-xmerl libodbc1 libsctp1 libsystemd0 lksctp-tools
Suggested packages:
  erlang erlang-manpages erlang-doc xsltproc fop erlang-ic-java erlang-observer libmyodbc odbc-postgresql
  tdsodbc unixodbc-bin
The following NEW packages will be installed:
  erlang-asn1 erlang-base erlang-corba erlang-crypto erlang-diameter erlang-edoc erlang-eldap
  erlang-erl-docgen erlang-eunit erlang-ic erlang-inets erlang-mnesia erlang-nox erlang-odbc erlang-os-mon
  erlang-parsetools erlang-percept erlang-public-key erlang-runtime-tools erlang-snmp erlang-ssh erlang-ssl
  erlang-syntax-tools erlang-tools erlang-webtool erlang-xmerl libodbc1 libsctp1 libsystemd0 lksctp-tools
  rabbitmq-server
0 upgraded, 31 newly installed, 0 to remove and 290 not upgraded.
Need to get 24.0 MB of archives.
After this operation, 39.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
~~~

~~~
Adding group `rabbitmq' (GID 111) ...
Done.
Adding system user `rabbitmq' (UID 106) ...
Adding new user `rabbitmq' (UID 106) with group `rabbitmq' ...
Not creating home directory `/var/lib/rabbitmq'.
Job for rabbitmq-server.service failed. See 'systemctl status rabbitmq-server.service' and 'journalctl -xn' for details.
invoke-rc.d: initscript rabbitmq-server, action "start" failed.
dpkg: error processing package rabbitmq-server (--configure):
 subprocess installed post-installation script returned error exit status 1
Processing triggers for libc-bin (2.19-7) ...
Errors were encountered while processing:
 rabbitmq-server
E: Sub-process /usr/bin/dpkg returned an error code (1)
~~~

## Debian Hostname 変更

~~~
vagrant@10:~$ hostname
10
~~~

~~~
vagrant@10:~$ sudo hostname js1
vagrant@10:~$ hostname
js1
~~~


~~~
vagrant@10:~$ sudo vim /etc/hosts


127.0.1.1       js1   
~~~

~~~
vagrant@10:~$ sudo /etc/init.d/hostname.sh restart
~~~

## rabbitmq restart

~~~
vagrant@10:~$ sudo /etc/init.d/rabbitmq-server start
Starting rabbitmq-server (via systemctl): rabbitmq-server.service.
~~~

# mqtt plugin

~~~

vagrant@10:~$ sudo rabbitmq-plugins enable rabbitmq_mqtt
The following plugins have been enabled:
  amqp_client
  rabbitmq_mqtt
Plugin configuration has changed. Restart RabbitMQ for changes to take effect.
vagrant@10:~$ sudo /etc/init.d/rabbitmq-server start
Starting rabbitmq-server (via systemctl): rabbitmq-server.service.
~~~

## management plugin

~~~
root@js1:~# rabbitmq-plugins enable rabbitmq_management
The following plugins have been enabled:
  mochiweb
  webmachine
  rabbitmq_web_dispatch
  rabbitmq_management_agent
  rabbitmq_management
Plugin configuration has changed. Restart RabbitMQ for changes to take effect.
~~~

## /etc/rabbitmq/rabbitmq.config

- [3.3 は guest/guestは ローカルホストからのみアクセスできる](http://www.rabbitmq.com/access-control.html)

~~~
root@js1:~# zcat /usr/share/doc/rabbitmq-server/rabbitmq.config.example.gz  | sudo tee -a /etc/rabbitmq/rabbitmq.config
~~~

- 編集:  erlangのコメントアウト(%%)、リストの最後のアイテムは ","で終われないみたいなので注意。

~~~
root@js1:~# vi /etc/rabbitmq/rabbitmq.config 
~~~
~~~
{loopback_users, []}         %%, 
~~~

- 再起動

~~~
root@js1:~# sudo /etc/init.d/rabbitmq-server restart
Restarting rabbitmq-server (via systemctl): rabbitmq-server.service.
~~~

# mqtt 設定

- [こちら](http://www.rabbitmq.com/mqtt.html)


~~~
[{rabbit,        [{tcp_listeners,    [5672]}]},
 {rabbitmq_mqtt, [{default_user,     <<"guest">>},
                  {default_pass,     <<"guest">>},
                  {allow_anonymous,  true},
                  {vhost,            <<"/">>},
                  {exchange,         <<"amq.topic">>},
                  {subscription_ttl, 1800000},
                  {prefetch,         10},
                  {ssl_listeners,    []},
                  %% Default MQTT with TLS port is 8883
                  %% {ssl_listeners,    [8883]}
                  {tcp_listeners,    [1883]},
                  {tcp_listen_options, [binary,
                                        {packet,    raw},
                                        {reuseaddr, true},
                                        {backlog,   128},
                                        {nodelay,   true}]}]}
].
~~~

~~~
root@js1:~# lsof -i:1883
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
beam    5651 rabbitmq   15u  IPv6  25954      0t0  TCP *:1883 (LISTEN)
~~~

# paho-mqtt 


~~~
(sandbox)Peeko:messaging hide$ pip install paho-mqtt
Downloading/unpacking paho-mqtt
  Downloading paho-mqtt-1.0.tar.gz (40Kb): 40Kb downloaded
  Running setup.py egg_info for package paho-mqtt
    
Installing collected packages: paho-mqtt
  Running setup.py install for paho-mqtt
    
Successfully installed paho-mqtt
Cleaning up...
~~~

## publisher/subscriber

- [MQTT コトハジメ](https://gist.github.com/voluntas/8238751)のpahoのコードで動いた

~~~
(sandbox)Peeko:messaging hide$ for i in $(seq 1 10); do python paho_pub.py ;done
~~~

~~~
(sandbox)Peeko:messaging hide$ python paho_sub.py 
rc: 0
Subscribed: 1 (0,)
Subscribed: 2 (0,)

my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
my/topic/string 0 Hello Mon Oct 20 00:17:05 2014
~~~

## RabbitMQのマネージャから送信


~~~
my/topic/string 0 ほげほげ
~~~
