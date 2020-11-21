# cron

## /etc/crontab

- [Debian](http://manpages.debian.org/cgi-bin/man.cgi?query=crontab&sektion=5)

`EDITOR` 変数:

~~~bash
$ export EDITOR=vim
.
~~~

~~~bash
$ crontab -e

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
~~~

5分ごとに実行:

~~~bash
*/5  * * * * /home/ubuntu/bin/every5.bash
~~~

## /etc/anacrontab

- [Centos](http://www.unix.com/man-page/centos/5/anacrontab/)

~~~bash
# /etc/anacrontab: configuration file for anacron

# See anacron(8) and anacrontab(5) for details.

SHELL=/bin/sh
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
# the maximal random delay added to the base delay of the jobs
RANDOM_DELAY=45
# the jobs will be started during the following hours only
START_HOURS_RANGE=3-22

#period in days   delay in minutes   job-identifier   command
1       5       cron.daily              nice run-parts /etc/cron.daily
7       25      cron.weekly             nice run-parts /etc/cron.weekly
@monthly 45     cron.monthly            nice run-parts /etc/cron.monthly
~~~

## うごかない？

### cron 自体が動いているか確認

毎分実行される：

~~~bash
*/1 * * * * /usr/bin/env > /tmp/output
~~~

Ubuntu([How to check cron logs in Ubuntu - Server Fault](https://serverfault.com/questions/136461/how-to-check-cron-logs-in-ubuntu)):

~~~bash
$ sudo grep CRON /var/log/syslog
May 14 07:30:01 ip-172-31-42-253 CRON[12150]: (ubuntu) CMD (/home/ubuntu/projects/myweb/bin/ignorelogs.bash )
~~~

### PATHがおかしい

cronで動くシェルの場合、 binのみ。

~~~bash
PATH=/usr/bin:/bin
~~~

### SHELL を明示的に指定してみる

シェルスクリプトコードが特定のシェルに依存しているとか。

~~~bash
SHELL=/bin/bash
...
~~~

## ログファイル

- [Where is the cron / crontab log?](https://askubuntu.com/questions/56683/where-is-the-cron-crontab-log)

Ubuntu:

~~~bash
$ sudo zless /var/log/syslog* | grep CRON
~~~

## 記事


- [Cronの使い方とテクニックと詰まったところ](https://qiita.com/UNILORN/items/a1a3f62409cdb4256219)
