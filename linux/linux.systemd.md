## systemctl

### daemon-reload

- init.d スクリプトを修正したら `daemon-reload` が必要なのかな？

~~~~

# /etc/init.d/apache2 restart
[....] Restarting apache2 (via systemctl): apache2.serviceWarning: Unit file of apache2.service changed on disk, 'systemctl daemon-reload' recommended.
. ok 
root@caramel:/etc/init.d# lsof -i:80
COMMAND   PID     USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
apache2 31347     root    4u  IPv6 1385969      0t0  TCP *:http (LISTEN)
apache2 31351 www-data    4u  IPv6 1385969      0t0  TCP *:http (LISTEN)
apache2 31352 www-data    4u  IPv6 1385969      0t0  TCP *:http (LISTEN)
apache2 31353 www-data    4u  IPv6 1385969      0t0  TCP *:http (LISTEN)
apache2 31354 www-data    4u  IPv6 1385969      0t0  TCP *:http (LISTEN)
apache2 31355 www-data    4u  IPv6 1385969      0t0  TCP *:http (LISTEN)
~~~

### list-units

~~~
# systemctl list-units --type=service | grep super

supervisord.service                loaded active running LSB: Starts supervisord - see http://supervisord.org
~~~