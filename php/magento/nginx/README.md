## 配置


/etc/nginx/sites-available/magent に一式をコピーし、ファイルを修正:

~~~bash 
$ sudo cp -r magent /etc/nginx/sites-available
~~~

PHPの var/run のシンボリックリンク

~~~bash
$ sudo ln -s $(phpenv prefix)/var/run /etc/nginx/sites-available/magento/
~~~


~~~bash 
sudo /home/vagrant/.anyenv/envs/phpenv/versions/7.2.8/sbin/php-fpm --nodaemonize  -y /etc/nginx/sites-available/magento/phpfpm.conf  
~~~


## phpfpm

- https://gist.github.com/miped/5116146