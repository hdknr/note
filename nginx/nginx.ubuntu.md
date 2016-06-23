## Install

~~~
$ sudo apt-get install nginx
~~~

## upstart

- [Ubuntu Upstart](https://www.nginx.com/resources/wiki/start/topics/examples/ubuntuupstart/)


-  /etc/init/nginx.conf

~~~
# nginx

description "nginx http daemon"
author "George Shammas <georgyo@gmail.com>"

start on (filesystem and net-device-up IFACE=lo)
stop on runlevel [!2345]

env DAEMON=/usr/sbin/nginx
env PID=/var/run/nginx.pid

expect fork
respawn
respawn limit 10 5
#oom never

pre-start script
        $DAEMON -t
        if [ $? -ne 0 ]
                then exit $?
        fi
end script

exec $DAEMON
~~~

~~~
# initctl reload-configuration
# initctl list | grep nginx
# initctl start nginx
~~~
