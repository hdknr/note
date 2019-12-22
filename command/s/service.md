# service

- [Linux service関連　基本コマンドメモ - Qiita](https://qiita.com/manjiroukeigo/items/2b217ffbb50b119d5f58)

~~~bash
$ sudo service --status-all | grep php
 [ + ]  php7.0-fpm
 [ - ]  php7.3-fpm
~~~

~~~bash
$ sudo systemctl list-units | grep php
phpsessionclean.timer                             loaded active waiting   Clean PHP session files every 30 mins
~~~

- [startup - How to install an init.d script? - Ask Ubuntu](https://askubuntu.com/questions/335242/how-to-install-an-init-d-script)

## 関連

- [update-rc.d](../u/update-rc.d.md)
