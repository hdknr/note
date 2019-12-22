# update-rc.d

- [update-rc.d | 我が社を有名にするブログ](https://at-j.co.jp/blog/?tag=update-rc-d)

登録:

~~~bash
$ sudo update-rc.d php7.3-fpm defaults
.
~~~

確認:

~~~bash
$ find /etc/rc*.d -name "*php7.3*fpm" -print
/etc/rc0.d/K01php7.3-fpm
/etc/rc1.d/K01php7.3-fpm
/etc/rc2.d/S01php7.3-fpm
/etc/rc3.d/S01php7.3-fpm
/etc/rc4.d/S01php7.3-fpm
/etc/rc5.d/S01php7.3-fpm
/etc/rc6.d/K01php7.3-fpm
~~~

解除:

~~~bash
$ sudo update-rc.d -f php7.3-fpm remove
.
~~~
