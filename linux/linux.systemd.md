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


## リンク

- [Writing systemd service files](http://patrakov.blogspot.jp/2011/01/writing-systemd-service-files.html)
- [watchdogs, systemd for Administrators, Part XV](http://0pointer.de/blog/projects/watchdog.html)
- [「Systemd」を理解する ーシステム起動編ー](http://equj65.net/tech/systemd-boot/)
- [CentOS7 + Systemd でMinecraftサーバーの起動/自動起動/自動再起動](http://qiita.com/nownabe/items/ca45bb4829d75460b31e) (Restart=always)
