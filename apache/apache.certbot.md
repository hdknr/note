# Let's Encrypt / CertBot

## CentOS7

~~~bash
% sudo yum install epel-release -y
% sudo yum install certbot python-certbot-apache -y
~~~

~~~bash
% sudo  certbot certonly --webroot -w /var/www/html/ -d server.shaper.co.jp
~~~

/etc/httpd/conf.d/ssl.conf.server:

~~~bash
Listen 443 https
SSLPassPhraseDialog exec:/usr/libexec/httpd-ssl-pass-dialog
SSLSessionCache         shmcb:/run/httpd/sslcache(512000)
SSLSessionCacheTimeout  300
SSLRandomSeed startup file:/dev/urandom  256
SSLRandomSeed connect builtin
SSLCryptoDevice builtin
<VirtualHost _default_:443>
ErrorLog logs/ssl_error_log
TransferLog logs/ssl_access_log
LogLevel warn
SSLEngine on
SSLProtocol all -SSLv2 -SSLv3
SSLCipherSuite HIGH:3DES:!aNULL:!MD5:!SEED:!IDEA
# --- CertBot Begin
SSLCertificateFile /etc/letsencrypt/live/server.shaper.co.jp/cert.pem
SSLCertificateKeyFile /etc/letsencrypt/live/server.shaper.co.jp/privkey.pem
SSLCertificateChainFile /etc/letsencrypt/live/server.shaper.co.jp/chain.pem
# --- CertBot End
<Files ~ "\.(cgi|shtml|phtml|php3?)$">
    SSLOptions +StdEnvVars
</Files>
<Directory "/var/www/cgi-bin">
    SSLOptions +StdEnvVars
</Directory>
BrowserMatch "MSIE [2-5]" \
         nokeepalive ssl-unclean-shutdown \
         downgrade-1.0 force-response-1.0
CustomLog logs/ssl_request_log \
          "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"
</VirtualHost>                                  
~~~

~~~bash
% sudo systemctl restart httpd
~~~
