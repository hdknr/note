# tar

## リモートサーバーのディレクトリを管理者権限でダウンロード

~~~bash
$ ssh -F ssh.conf yourserver "sudo tar cvfz - /etc/letsencrypt" | tar xvfz - -C ../yourserver
.
~~~
