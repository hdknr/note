## トピック

- [インストール](ansible.install.md)
- [設定関連](ansible.config.md)
- [file](ansible.file.md)
- [ssh](ansible.ssh.md)
- [playbook](ansible.playbook.md)
- [YAML](ansible.yaml.md)
- [command](ansible.command.md) : ドキュメントビルド
- [タグ](ansible.tags.md)

## AWS

- [ec2](ansible.ec2.md)
- [vpc](ansible.ec2_vpc.md)


## プラグイン

- [filter_plugins](ansible.filter_plugins.md)


## プラクティス

- 対象作業ごとにフォルダーを作る(Vagrantと同様)
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

- http://docs.ansible.com/ansible/playbooks_best_practices.html
- https://github.com/enginyoyen/ansible-best-practises
- https://openedx.atlassian.net/wiki/display/OpenOPS/Ansible+Code+Conventions
- [Ansibleを使い出す前に押さえておきたかったディレクトリ構成のベストプラクティス](http://bit.ly/2cxwIUC)
- [Ansible - ディレクトリ構成について](http://qiita.com/makaaso/items/0375081c1600b312e8b0)
- [Ansible : Best Practices](http://docs.ansible.com/ansible/playbooks_best_practices.html)
- [Ansibleを複数ホストへのコマンド投げツールとしてad-hocに使う](http://d.sunnyone.org/2016/01/ansiblead-hoc.html)

## メモ

- [Ansible Tutorial](https://yteraoka.github.io/ansible-tutorial/#simple-playbook)
- [入門Ansible(未発表箇所)](http://www.slideshare.net/takushimizu/ansible-28951674)
- [DevOps Technologies: Fabric or Ansible](https://insights.sei.cmu.edu/devops/2015/03/devops-technologies-fabric-or-ansible.html)
- [http://qiita.com/unarist/items/39f5510f95c752c10df1](http://qiita.com/hnakamur/items/c7c4f7277c07a14a4a59)
- [jcalazan/ansible-django-stack](https://github.com/jcalazan/ansible-django-stack)
- [ansibleで特定のtaskを特定のhostに実行する](http://qiita.com/346@github/items/00122556cb2bd6f57998)
- [How can you run only one task out of a playbook, for debug purposes](https://coderwall.com/p/ur8qnw/how-can-you-run-only-one-task-out-of-a-playbook-for-debug-purposes)
