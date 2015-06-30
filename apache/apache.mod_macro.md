## libapache2-mod-macro

~~~bash
hdknr@ubuntu:~$ sudo apt-get install libapache2-mod-macro

パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下のパッケージが新たにインストールされます:
  libapache2-mod-macro
アップグレード: 0 個、新規インストール: 1 個、削除: 0 個、保留: 3 個。
1,452 B のアーカイブを取得する必要があります。
この操作後に追加で 22.5 kB のディスク容量が消費されます。
取得:1 http://jp.archive.ubuntu.com/ubuntu/ trusty-updates/main libapache2-mod-macro amd64 1:2.4.7-1ubuntu4.1 [1,452 B]
1,452 B を 0秒 で取得しました (10.7 kB/s) 
以前に未選択のパッケージ libapache2-mod-macro を選択しています。
(データベースを読み込んでいます ... 現在 71485 個のファイルとディレクトリがインストールされています。)
Preparing to unpack .../libapache2-mod-macro_1%3a2.4.7-1ubuntu4.1_amd64.deb ...
Unpacking libapache2-mod-macro (1:2.4.7-1ubuntu4.1) ...
libapache2-mod-macro (1:2.4.7-1ubuntu4.1) を設定しています ...
~~~

~~~bash
hdknr@ubuntu:~$ sudo a2enmod macro
Enabling module macro.
To activate the new configuration, you need to run:
  service apache2 restart
~~~

~~~bash
hdknr@ubuntu:~$ sudo /etc/init.d/apache2 restart
 * Restarting web server apache2
   ...done.
~~~   

~~~ bash
hdknr@ubuntu:~$ ls -l /etc/apache2/mods-enabled/*macro*
lrwxrwxrwx 1 root root 28  8月 19 03:45 /etc/apache2/mods-enabled/macro.load -> ../mods-available/macro.load
~~~

~~~ bash
hdknr@ubuntu:~$ more /etc/apache2/mods-enabled/macro.load 

LoadModule macro_module /usr/lib/apache2/modules/mod_macro.so
~~~

## パターン

- gunicorn で django サイトをホスト

- サイトの基本機能を定義

~~~xml
<Macro Vhost $cname $base $proxyport>
    ServerAdmin webmaster@localhost
    ServerName  $cname

    ProxyPreserveHost On

    <Location / >
         
    	ProxyPass http://127.0.0.1:$proxyport/
    	ProxyPassReverse http://127.0.0.1:$proxyport/

    </Location>

    #  python manage.py collectstatic goes to $base/web/static
    Alias /static $base/web/static

    <Location /static >
       ProxyPass !
    </Location>


    LogLevel warn
    ErrorLog  $base/apache/logs/apache.error.log
    CustomLog $base/apache/logs/apache.access.log combined
    CustomLog $base/apache/logs/apache.env.log "%t %h X_HTTP_HOST=%{X_HTTP_HOST}e"
</Macro>
~~~

- 証明書関連を /etc/apache2/site-available/{{$cnam}}/certs/ の下に置く

~~~xml
<Macro Certs $cname>
 SSLEngine on

 SSLCACertificateFile sites-available/$cname/certs/cacert.pem
 SSLCertificateFile sites-available/$cname/certs/cert.pem
 SSLCertificateKeyFile sites-available/$cname/certs/key.pem

 SSLProtocol all -SSLv2 -SSLv3
 SSLHonorCipherOrder on
 SSLCipherSuite "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS"

</Macro>
~~~

- テストサイト、 通常サイト、 SSLサイトを定義

~~~xml
<VirtualHost *:80>
   Use Vhost test.service.net /home/system/projects/serviceapp 9000
</VirtualHost>

<VirtualHost *:80>
   Use Vhost www.service.net /home/system/projects/serviceapp 9000

   <Location /secure>
      RedirectMatch (.*)   https://www.service.net$1
   </Location>

</VirtualHost>

<VirtualHost *:443>
   Use Certs www.service.net
   Use Vhost www.service.net /home/system/projects/serviceapp 9000

</VirtualHost>
~~~