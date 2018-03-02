## データベースディレクトリを移動したら動かない

~~~bash
$ sudo service mysql restart

Job for mysql.service failed because the control process exited with error code.
See "systemctl status mysql.service" and "journalctl -xe" for details.
~~~

~~~bash
$ sudo tail -n 100 /var/log/mysql/error.log

2018-03-01T10:07:24.762519Z 0 [Warning] Changed limits: max_open_files: 1024 (requested 5000)
2018-03-01T10:07:24.762557Z 0 [Warning] Changed limits: table_open_cache: 431 (requested 2000)
2018-03-01T10:07:24.922321Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
2018-03-01T10:07:24.922525Z 0 [Warning] Can't create test file /data/mysql/ip-172-50-10-211.lower-test
2018-03-01T10:07:24.922561Z 0 [Note] /usr/sbin/mysqld (mysqld 5.7.21-0ubuntu0.16.04.1) starting as process 2183 ...
2018-03-01T10:07:24.925007Z 0 [Warning] Can't create test file /data/mysql/ip-172-50-10-211.lower-test
2018-03-01T10:07:24.925077Z 0 [Warning] Can't create test file /data/mysql/ip-172-50-10-211.lower-test
2018-03-01T10:07:24.927116Z 0 [Note] InnoDB: PUNCH HOLE support available
2018-03-01T10:07:24.927134Z 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
2018-03-01T10:07:24.927139Z 0 [Note] InnoDB: Uses event mutexes
2018-03-01T10:07:24.927145Z 0 [Note] InnoDB: GCC builtin __atomic_thread_fence() is used for memory barrier
2018-03-01T10:07:24.927154Z 0 [Note] InnoDB: Compressed tables use zlib 1.2.8
2018-03-01T10:07:24.927158Z 0 [Note] InnoDB: Using Linux native AIO
2018-03-01T10:07:24.927384Z 0 [Note] InnoDB: Number of pools: 1
2018-03-01T10:07:24.927484Z 0 [Note] InnoDB: Using CPU crc32 instructions
2018-03-01T10:07:24.928884Z 0 [Note] InnoDB: Initializing buffer pool, total size = 128M, instances = 1, chunk size = 128M
2018-03-01T10:07:24.936249Z 0 [Note] InnoDB: Completed initialization of buffer pool
2018-03-01T10:07:24.938219Z 0 [Note] InnoDB: If the mysqld execution user is authorized, page cleaner thread priority can be changed. See the man page of setpriority().
2018-03-01T10:07:24.948413Z 0 [ERROR] InnoDB: The innodb_system data file 'ibdata1' must be writable
2018-03-01T10:07:24.948430Z 0 [ERROR] InnoDB: The innodb_system data file 'ibdata1' must be writable
2018-03-01T10:07:24.948435Z 0 [ERROR] InnoDB: Plugin initialization aborted with error Generic error
2018-03-01T10:07:25.549502Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
2018-03-01T10:07:25.549534Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
2018-03-01T10:07:25.549540Z 0 [ERROR] Failed to initialize builtin plugins.
2018-03-01T10:07:25.549543Z 0 [ERROR] Aborting
~~~

~~~bash
$ sudo journalctl -xe
~~~
~~~
-- Unit mysql.service has begun starting up.
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.752:178): apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/proc/3969/status" pid=3969 comm=
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/proc/3969/status" pid=3969 comm="mysqld" requested_mask="r" denied_
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/sys/devices/system/node/" pid=3969 comm="mysqld" requested_mask="r"
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/proc/3969/status" pid=3969 comm="mysqld" requested_mask="r" denied_
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.756:179): apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/sys/devices/system/node/" pid=39
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.756:180): apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/proc/3969/status" pid=3969 comm=
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="mknod" profile="/usr/sbin/mysqld" name="/data/mysql/ip-172-50-10-211.lower-test" pid=3969 comm="mysqld" req
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="mknod" profile="/usr/sbin/mysqld" name="/data/mysql/ip-172-50-10-211.lower-test" pid=3969 comm="mysqld" req
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="mknod" profile="/usr/sbin/mysqld" name="/data/mysql/ip-172-50-10-211.lower-test" pid=3969 comm="mysqld" req
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.920:181): apparmor="DENIED" operation="mknod" profile="/usr/sbin/mysqld" name="/data/mysql/ip-172-50-10-211.low
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.920:182): apparmor="DENIED" operation="mknod" profile="/usr/sbin/mysqld" name="/data/mysql/ip-172-50-10-211.low
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.920:183): apparmor="DENIED" operation="mknod" profile="/usr/sbin/mysqld" name="/data/mysql/ip-172-50-10-211.low
Mar 01 19:15:57 ip-172-50-10-211 audit[3969]: AVC apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/data/mysql/ibdata1" pid=3969 comm="mysqld" requested_mask="wr" deni
Mar 01 19:15:57 ip-172-50-10-211 kernel: audit: type=1400 audit(1519899357.948:184): apparmor="DENIED" operation="open" profile="/usr/sbin/mysqld" name="/data/mysql/ibdata1" pid=3969 com
Mar 01 19:15:58 ip-172-50-10-211 systemd[1]: mysql.service: Main process exited, code=exited, status=1/FAILURE
lines 23
~~~

### AppArmor 問題

- [MySQL won't start because of AppArmor?](https://askubuntu.com/questions/916009/mysql-wont-start-because-of-apparmor)


~~~bash
$ sudo vim /etc/apparmor.d/usr.sbin.mysqld
~~~

追加:
~~~
  /data/mysql/ r,
  /data/mysql/** rwk,  
  /proc/*/status r,
  /sys/devices/system/node/ r,
  /sys/devices/system/node/node0/meminfo r,
~~~

~~~bash
$ sudo /etc/init.d/apparmor restart

[ ok ] Restarting apparmor (via systemctl): apparmor.service.
~~~

~~~bash
$ sudo /etc/init.d/mysql restart

[ ok ] Restarting mysql (via systemctl): mysql.service.
~~~

## `aa-status` で確認

~~~bash
$ sudo /usr/sbin/aa-status
apparmor module is loaded.
15 profiles are loaded.
15 profiles are in enforce mode.
   /sbin/dhclient
   /usr/bin/lxc-start
   /usr/lib/NetworkManager/nm-dhcp-client.action
   /usr/lib/NetworkManager/nm-dhcp-helper
   /usr/lib/connman/scripts/dhclient-script
   /usr/lib/lxd/lxd-bridge-proxy
   /usr/lib/snapd/snap-confine
   /usr/lib/snapd/snap-confine//mount-namespace-capture-helper
   /usr/lib/snapd/snap-confine//snap_update_ns
   /usr/sbin/mysqld
   /usr/sbin/tcpdump
   lxc-container-default
   lxc-container-default-cgns
   lxc-container-default-with-mounting
   lxc-container-default-with-nesting
0 profiles are in complain mode.
2 processes have profiles defined.
2 processes are in enforce mode.
   /sbin/dhclient (1004)
   /usr/sbin/mysqld (3628)
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
~~~

## 参照

- [gitlab:apparmor/apparmor](https://gitlab.com/apparmor/apparmor)
- [gitlab wiki](https://gitlab.com/apparmor/apparmor/wikis/home/)
- [AppArmor wikipedia](https://ja.wikipedia.org/wiki/AppArmor)
- [AppArmor をおおまかに理解する](http://www.usupi.org/sysad/220.html)
- [AppArmorをDebianでもデフォルトに!? ―Tails開発者が提言](http://gihyo.jp/admin/clip/01/linux_dt/201709/25)
