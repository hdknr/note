# Let's Encrypt

## Ubuntu

~~~bash
$ sudo apt-get install letsencrypt
..
~~~

~~~bash
$ dpkg -L letsencrypt

/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/letsencrypt
/usr/share/doc/letsencrypt/README.rst.gz
/usr/share/doc/letsencrypt/copyright
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/letsencrypt.1.gz
/usr/bin
/usr/bin/letsencrypt
/usr/share/doc/letsencrypt/changelog.Debian.gz
~~~

~~~bash
$ sudo letsencrypt certonly --standalone -d {{ ドメイン名前 }}
~~~

## 起動中のサーバーで設定

~~~bash
$ sudo letsencrypt certonly --webroot -w /home/ubuntu/lafoglia/html -m supervisor@lafoglia.com -d www.lafoglia.com -d lafoglia.com


IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/www.lafoglia.com/fullchain.pem. Your cert
   will expire on 2019-03-07. To obtain a new version of the
   certificate in the future, simply run Let's Encrypt again.
 - If you like Let's Encrypt, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
~~~

nginx設定(default):

~~~
include sites-available/lafoglia/upstream.conf;
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # SSL
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;
        include sites-available/lafoglia/keys.conf;

        root /home/ubuntu/lafoglia/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        
        location / {
            try_files $uri $uri/ =404;
            include sites-available/kitayama/root.conf;
        }
}
~~~

keys.conf:

~~~
ssl_certificate /etc/letsencrypt/live/www.lafoglia.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/www.lafoglia.com//privkey.pem;
~~~

## 記事

- [Let’s encryptを利用して、https通信を構築する - Qiita](https://qiita.com/kouji555/items/4dbccc6aad32278e2cc6)
- [Let’s Encryptの使い方。standaloneとwebroot - Qiita](https://qiita.com/f_uto/items/4178a9fdd657b78672ea)
- [Let's Encrypt でワイルドカード証明書を発行してみる - Qiita](https://qiita.com/noumia/items/64d8bb59e35151fc4fd6)
- [let's encrypt で複数ホスト名対応な証明書を作る - 日記](https://tnamao.hatenablog.com/entry/2016/08/21/173521)
