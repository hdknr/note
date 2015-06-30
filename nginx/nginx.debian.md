## Debian Install

```
vagrant@10:~/projects$ sudo apt-get install nginx
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libgd3 libvpx1 nginx-common nginx-full
Suggested packages:
  libgd-tools fcgiwrap nginx-doc ssl-cert
The following NEW packages will be installed:
  libgd3 libvpx1 nginx nginx-common nginx-full
0 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
Need to get 1,334 kB of archives.
After this operation, 3,803 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
```

```
vagrant@10:~/projects$ dpkg -L nginx
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/nginx
/usr/share/doc/nginx/changelog.Debian.gz
/usr/share/doc/nginx/copyright
/usr/share/doc/nginx/changelog.gz
```

```
vagrant@10:~/projects$ dpkg -L nginx-full
/.
/usr
/usr/share
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/nginx-full
/usr/share/doc
/usr/share/doc/nginx-full
/usr/share/doc/nginx-full/changelog.Debian.gz
/usr/share/doc/nginx-full/copyright
/usr/share/doc/nginx-full/changelog.gz
/usr/sbin
/usr/sbin/nginx
```

```
/.
/usr
/usr/share
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/nginx-common
/usr/share/doc
/usr/share/doc/nginx-common
/usr/share/doc/nginx-common/changelog.Debian.gz
/usr/share/doc/nginx-common/README.Debian
/usr/share/doc/nginx-common/NEWS.Debian.gz
/usr/share/doc/nginx-common/copyright
/usr/share/doc/nginx-common/changelog.gz
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/nginx.1.gz
/usr/share/nginx
/usr/share/nginx/html
/usr/share/nginx/html/index.html
/var
/var/www
/var/www/html
/var/log
/var/log/nginx
/var/lib
/var/lib/nginx
/etc
/etc/init.d
/etc/init.d/nginx
/etc/default
/etc/default/nginx
/etc/ufw
/etc/ufw/applications.d
/etc/ufw/applications.d/nginx
/etc/logrotate.d
/etc/logrotate.d/nginx
/etc/nginx
/etc/nginx/proxy_params
/etc/nginx/koi-utf
/etc/nginx/scgi_params
/etc/nginx/sites-enabled
/etc/nginx/snippets
/etc/nginx/snippets/snakeoil.conf
/etc/nginx/snippets/fastcgi-php.conf
/etc/nginx/sites-available
/etc/nginx/sites-available/default
/etc/nginx/win-utf
/etc/nginx/mime.types
/etc/nginx/uwsgi_params
/etc/nginx/conf.d
/etc/nginx/koi-win
/etc/nginx/nginx.conf
/etc/nginx/fastcgi_params
/etc/nginx/fastcgi.conf
/lib
/lib/systemd
/lib/systemd/system
/lib/systemd/system/nginx.service
```


## 仮想ホスト

```
vagrant@10:~/projects/wordpress$ pwd
/home/vagrant/projects/wordpress
vagrant@10:~/projects/wordpress$ tree .
.
├── nginx.conf
└── www
    └── index.html

1 directory, 2 files
```

```
vagrant@10:~/projects/wordpress$ more nginx.conf 

server {
    listen 80;
    listen [::]:80;

    server_name wp.deb;

    root /home/vagrant/projects/wordpress/www;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
    
    access_log /home/vagrant/projects/wordpress/logs/access.log;
    error_log  /home/vagrant/projects/wordpress/logs/error.log debug;
    
}
```

```
vagrant@10:~/projects/wordpress$ sudo ln -s `pwd`/nginx.conf /etc/nginx/sites-enabled/wp.deb
```

```
vagrant@10:~/projects/wordpress$ sudo /etc/init.d/nginx restart
Restarting nginx (via systemctl): nginx.service.
```

```
$ curl http://wp.deb
hello wordpress
```

