## ssh ログインしたIPアドレス記録

- Debian

~~~bash
$ zgrep sshd /var/log/auth.log* | grep "Accepted publickey for admin" | sed -re 's/.*from ([^: ]+).*/\1/' | sort -u | while read ip;do echo $ip `dig +short -x $ip`;done
154.167.141.179 p5491179-ipngn1402marunouchi.tokyo.ocn.ne.jp.
157.168.71.211 p7957211-ipngn1702marunouchi.tokyo.ocn.ne.jp.
222.229.233.5 p82335-ipbffx32marunouchi.tokyo.ocn.ne.jp.
~~~


## ネットワークを変えたら接続できなくなった

/etc/hosts.allow で日本ネットワークのみ許可制限がはいっているとか:

~~~
sshd: .jp
~~~
