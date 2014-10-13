~~~
$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 16108
max locked memory       (kbytes, -l) 32
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 10240
cpu time               (seconds, -t) unlimited
max user processes              (-u) 16108
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited

~~~

~~~
$ sudo reboot
~~~

~~~
$ grep  Core /etc/httpd/conf/httpd.conf
CoreDumpDirectory /tmp
~~~

~~~
$ sudo /etc/init.d/httpd restart
httpd を停止中:                                            [  OK  ]
httpd を起動中:                                            [  OK  ]
~~~


~~~
$ ls -l /tmp/core.*
-rw------- 1 apache apache 9347072  9月 30 09:00 /tmp/core.2885
~~~

~~~
$ gdb /usr/sbin/httpd -c /tmp/core.2885
~~~

~~~
(gdb) where
#0  0x04437136 in ?? () from /etc/httpd/modules/libphp5.so
#1  0x00c8412a in ?? () from /usr/lib/php/modules/pgsql.so
#2  0x0446f397 in zend_hash_clean () from /etc/httpd/modules/libphp5.so
#3  0x00c8b920 in ?? () from /usr/lib/php/modules/pgsql.so
#4  0x044663f8 in ?? () from /etc/httpd/modules/libphp5.so
#5  0x043f89a5 in php_request_shutdown () from /etc/httpd/modules/libphp5.so
#6  0x0450eb7f in ?? () from /etc/httpd/modules/libphp5.so
#7  0x0078408d in ap_run_handler ()
#8  0x00787a53 in ap_invoke_handler ()
#9  0x00793bee in ap_process_request ()
#10 0x0079096f in ?? ()
#11 0x0078bf8d in ap_run_process_connection ()
#12 0x0078c08c in ap_process_connection ()
#13 0x00798c84 in ?? ()
#14 0x00798f91 in ?? ()
#15 0x0079906a in ?? ()
#16 0x00799bcb in ap_mpm_run ()
#17 0x0076f2d7 in main ()

~~~


