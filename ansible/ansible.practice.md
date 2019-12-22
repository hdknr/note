# Ansible Pactice

## プラクティス

- 対象作業ごとにフォルダーを作る
- ansible.cfg を用意する
- ssh_connectionで、 ssh.configファイルを参照するようにする
- インベントリファイル(hostfile)には、ssh.configのHost名を指定する

### 例

#### ansible.cfg

- ssh.confファイルに接続情報を書く

~~~
[ssh_connection]
ssh_args = -F ssh.conf

[defaults]
hostfile = hosts
~~~

#### hosts

- サーバー名は ssh.conf のHostエントリ

~~~
[server]
default
~~~


#### ssh.conf

~~~
Host default
  HostName wzy
  User hdknr
  Port 22
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes
  LogLevel FATAL
~~~

#### 実行

~~~
$ ansible default -a "uptime"
default | success | rc=0 >>
 00:31:13 up 10 days, 22:50,  4 users,  load average: 0.03, 0.03, 0.05
~~~

~~~
$ ssh -F ssh.conf default uptime
 00:32:06 up 10 days, 22:51,  3 users,  load average: 0.01, 0.02, 0.05
~~~

- リモートログイン

~~~
$ ssh -F ssh.conf default

Linux wzy 3.2.0-4-amd64 #1 SMP Debian 3.2.63-2+deb7u2 x86_64
....
Last login: Sun Feb  1 00:31:51 2015 from mac
hdknr@wzy:~$
~~~

### Practice in the world

- [Best Practices — Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [enginyoyen/ansible-best-practises: A project structure that outlines some best practises of how to use ansible](https://github.com/enginyoyen/ansible-best-practises)
- [Ansible Code Conventions - Open edX Operations - Confluence](https://openedx.atlassian.net/wiki/spaces/OpenOPS/pages/26837527/Ansible+Code+Conventions)
- [Ansibleを使い出す前に押さえておきたかったディレクトリ構成のベストプラクティス](http://bit.ly/2cxwIUC)
- [Ansible - ディレクトリ構成について](http://qiita.com/makaaso/items/0375081c1600b312e8b0)
- [Ansible : Best Practices](http://docs.ansible.com/ansible/playbooks_best_practices.html)
- [Ansibleを複数ホストへのコマンド投げツールとしてad-hocに使う](http://d.sunnyone.org/2016/01/ansiblead-hoc.html)
- [Ansibleのベストプラクティスなディレクトリ構成の雛形を一撃で作りたい - Qiita](https://qiita.com/n-funaki/items/0156fd038df1787cae77)
