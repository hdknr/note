# vsftpd

- https://security.appspot.com/vsftpd.html
- [sftp](../command/sftp.md)

## /etc/vsftpd.conf

~~~ini
listen=NO
listen_ipv6=YES
anonymous_enable=NO
local_enable=YES
local_umask=022
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
~~~

### umask

- [vsftpd umask | technote](https://tech.withsin.net/2018/02/26/vsftpd-umask/)

~~~ini
local_umask=002
~~~

## トラブル

- [Windowsから繋がらない](https://github.com/hdknr/scriptogr.am/issues/39)
- [アップロード時のパーミッション書き換え設定 - Knowlege Database](http://extstrg.asabiya.net/pukiwiki/index.php?%A5%A2%A5%C3%A5%D7%A5%ED%A1%BC%A5%C9%BB%FE%A4%CE%A5%D1%A1%BC%A5%DF%A5%C3%A5%B7%A5%E7%A5%F3%BD%F1%A4%AD%B4%B9%A4%A8%C0%DF%C4%EA)

## PUre FTP

- [Pure-FTPd の存在を知ってしまったので試さざるを得ない - Qiita](https://qiita.com/koshigoe/items/92aaf30966dfe65be85f)