php-fpm: nginx で動かす

- 基本的に&quot;[nginx + php-fpm のPHPをバーチャルホストごとにユーザー権限で動かす](http://qiita.com/kijtra/items/022d3cde07046e396486) &quot;の写経


## php-fpmがインストールされていること

- phpenv + php-buildだと普通に入っているっぽい

~~~bash
$ find $PHPENV_ROOT -name "php-fpm*" -print
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.9/etc/php-fpm.conf.default
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.9/sbin/php-fpm
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.9/php/man/man8/php-fpm.8
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/etc/php-fpm.conf.default
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/sbin/php-fpm
/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/php/man/man8/php-fpm.8
~~~

```
vagrant@10:~/projects$ /home/vagrant/.phpenv/versions/5.5.19/sbin/php-fpm  --help

Usage: php-fpm [-n] [-e] [-h] [-i] [-m] [-v] [-t] [-p <prefix>] [-g <pid>] [-c <file>] [-d foo[=bar]] [-y <file>] [-D] [-F]
  -c <path>|<file> Look for php.ini file in this directory
  -n               No php.ini file will be used
  -d foo[=bar]     Define INI entry foo with value 'bar'
  -e               Generate extended information for debugger/profiler
  -h               This help
  -i               PHP information
  -m               Show compiled in modules
  -v               Version number
  -p, --prefix <dir>
                   Specify alternative prefix path to FastCGI process manager (default: /home/vagrant/.phpenv/versions/5.5.19).
  -g, --pid <file>
                   Specify the PID file location.
  -y, --fpm-config <file>
                   Specify alternative path to FastCGI process manager config file.
  -t, --test       Test FPM configuration and exit
  -D, --daemonize  force to run in background, and ignore daemonize option from config file
  -F, --nodaemonize
                   force to stay in foreground, and ignore daemonize option from config file
  -R, --allow-to-run-as-root
                   Allow pool to run as root (disabled by default)

```

## php-fpm.conf

- 設定コピー

```
vagrant@10:~/projects/wordpress$ cp /home/vagrant/.phpenv/versions/5.5.19/etc/php-fpm.conf.default  /home/vagrant/.phpenv/versions/5.5.19/etc/php-fpm.conf

```

- "wordpress" プールを追加


```
[wordpress]
listen = /home/vagrant/projects/wordpress/run/php-fpm.sock
listen.mode = 0666
user = vagrant
group = vagrant
pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
```

- 起動。sudo で起動すると、 user, group で起動してくれる

```
vagrant@10:~/projects/wordpress$ sudo $PHP_PATH/sbin/php-fpm 
```

```
vagrant@10:~/projects/wordpress$ sudo lsof -c php-fpm | grep php-fpm.sock
php-fpm 29637     root   10u  unix 0xffff880079df8480      0t0  57962 /home/vagrant/projects/wordpress/run/php-fpm.sock
php-fpm 29640  vagrant    0u  unix 0xffff880079df8480      0t0  57962 /home/vagrant/projects/wordpress/run/php-fpm.sock
php-fpm 29641  vagrant    0u  unix 0xffff880079df8480      0t0  57962 /home/vagrant/projects/wordpress/run/php-fpm.sock

```

- supervisor とかで起動設定するといいんでしょう

## nginx

- 仮想ホスト(wp.deb)設定

```
vagrant@10:~/projects/wordpress$ cat nginx.conf 

upstream php-fpm-wordpress{
  ip_hash;
  server unix:/home/vagrant/projects/wordpress/run/php-fpm.sock;
}

server {
    listen 80;
    listen [::]:80;

    server_name wp.deb;

    root /home/vagrant/projects/wordpress/www;
    index index.php index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    access_log /home/vagrant/projects/wordpress/logs/access.log;
    error_log  /home/vagrant/projects/wordpress/logs/error.log debug;

    location ~ \.php$ {
        fastcgi_pass  php-fpm-wordpress;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_buffer_size  128k;
        fastcgi_buffers  256 16k;
        fastcgi_busy_buffers_size  256k;
        fastcgi_temp_file_write_size  256k;
        include  fastcgi_params;
    }
}
```

- Debian way

```
vagrant@10:~/projects/wordpress$ sudo ln -s `pwd`/nginx.conf /etc/nginx/sites-enabled/wp.deb
```

- nginxリスタート

```
vagrant@10:~/projects/wordpress$ sudo /etc/init.d/nginx restart
Restarting nginx (via systemctl): nginx.service.
```


# ホストからアクセス

```
Peeko:hide$ curl -s http://wp.deb/info.php | grep php-fpm

<tr><td class="e">php-fpm </td><td class="v">active </td></tr>
```
