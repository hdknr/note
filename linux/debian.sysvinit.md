## update-rc.d

~~~
# update-rc.d supervisord defaults 99 1
~~~

- supervisord　を99番目（実際はスクリプトの総数による）に開始し
- 1番目に終わらせる

~~~
# update-rc.d supervisord defaults
~~~
~~~
 Adding system startup for /etc/init.d/supervisord ...
   /etc/rc0.d/K20supervisord -> ../init.d/supervisord
   /etc/rc1.d/K20supervisord -> ../init.d/supervisord
   /etc/rc6.d/K20supervisord -> ../init.d/supervisord
   /etc/rc2.d/S20supervisord -> ../init.d/supervisord
   /etc/rc3.d/S20supervisord -> ../init.d/supervisord
   /etc/rc4.d/S20supervisord -> ../init.d/supervisord
   /etc/rc5.d/S20supervisord -> ../init.d/supervisord
~~~

- デフォルトで登録

### オプション

- `-n`  : 実際にはリンクを作ることなく動作のみが表示
- `-f`  : 強制的にシンボリックリンクを削除する