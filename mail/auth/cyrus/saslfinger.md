# saslfinger

## `-c`

エラー:

~~~
saslfinger -c
saslfinger - postfix Cyrus sasl configuration 2022年  1月 15日 土曜日 14:50:18 JST
version: 1.0.4
mode: client-side SMTP AUTH

-- basics --
Postfix: 3.4.13
System: Ubuntu 20.04.3 LTS \n \l

-- smtp is linked to --
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x00007f213ec28000)

-- active SMTP AUTH and TLS parameters for smtp --
relayhost =
smtp_tls_CApath = /etc/ssl/certs
smtp_tls_security_level = may
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache


-- listing of /usr/lib/sasl2 --
合計 16
drwxr-xr-x  2 root root 4096  1月 15 14:49 .
drwxr-xr-x 95 root root 4096  1月 13 14:18 ..
-rw-r--r--  1 root root    4  1月 13 14:36 berkeley_db.active
-rw-r--r--  1 root root    4 12月 26  2019 berkeley_db.txt

-- listing of /etc/postfix/sasl --
合計 12
drwxr-xr-x 2 root root 4096  1月 15 14:42 .
drwxr-xr-x 5 root root 4096  1月 14 22:51 ..
-rw-r--r-- 1 root root   24  1月 15 14:42 smtpd.conf


Cannot find the smtp_sasl_password_maps parameter in main.cf.
Client-side SMTP AUTH cannot work without this parameter!
~~~~