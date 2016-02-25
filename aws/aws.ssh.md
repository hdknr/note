## ssh で接続できない

~~~bash
$ ssh ubuntu@52.68.90.125 -i ~/.ssh/vagrant.pem

ssh: connect to host 52.68.90.125  port 22: connection refused
~~~

### sshdが起動したいない

- アクション > インスタンスの設定 > システムログの取得
- sshdが起動していればログに残っている

~~~
 * Starting OpenSSH server  OK 
~~~

### /etc/fstab にアタッチされていないボリュームが指定されている

- fstabからエントリを削除する

### サブネットがおかしい

- IGW(Intenet Gate Way)が割り当てられているサブネットで起動する
