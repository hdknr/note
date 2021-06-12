## git がブロックされる

- git のURLにユーザー名が指定されていて、パスワードが要求されている

~~~bash
$ git config --list | grep hdknr
remote.origin.url=https://hdknr@github.com/hdknr/bin.git
~~~

- URLを修正

~~~bash
$ git remote set-url origin https://github.com/hdknr/bin.git
~~~

## 変数(vars)

- 変数の参照

~~~
$var
${var}
{{ var }}
~~~

## Task

tags を指定して個別のタスクを実行
- [How to run only one task in ansible playbook?](http://stackoverflow.com/questions/23945201/how-to-run-only-one-task-in-ansible-playbook)


## git モジュール

- [git - Deploy software (or files) from git checkouts](http://docs.ansible.com/git_module.html)


## いろいろ

- ホストを絞る [Safely limiting Ansible playbooks to a single machine?](https://stackoverflow.com/questions/18195142/safely-limiting-ansible-playbooks-to-a-single-machine)

	- `--limit servers[0]` を使う
	- `--extra-vars "target=server1"` を使う
	- ` -i "imac1-local,"` をつかう(カンマ注意)


## Vagrant

- [geerlingguy/ansible-vagrant-examples](https://github.com/geerlingguy/ansible-vagrant-examples)

- Vagrantfile

~~~ruby
config.vm.provision "ansible" do |ansible|
	ansible.playbook = "your_playbook.yml"
	ansible.inventory_path = "hosts"  
	ansible.limit = 'all'
end
~~~

- hosts

~~~
[servers]
default
~~~

- ansible.cfg

~~~
[ssh_connection]
ssh_args = -F ssh.conf

[defaults]
hostfile = hosts
~~~

- ssh.conf

~~~
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /Users/hide/Documents/Boxes/js2/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL
~~~


## MySQL

- [DebianのAnsibleにMySQLを入れる](http://utisam.hateblo.jp/entry/2014/11/12/135145)

~~~yaml
vars:
    mysql_root_pass: yourRootPassword

tasks:

  - name: Set MySQL root password before installing
    debconf: name='mysql-server' question='mysql-server/root_password' value='{{mysql_root_pass | quote}}' vtype='password'

  - name: Confirm MySQL root password before installing
    debconf: name='mysql-server' question='mysql-server/root_password_again' value='{{mysql_root_pass | quote}}' vtype='password'
~~~

- [Ansibleでのパスワードの取り扱い](http://qiita.com/jimaoka/items/535d5feb9b99fe5b3318)
- [ansibleで実行対象を切り替える方法](http://tdoc.info/blog/2014/05/30/ansible_target_switching.html)
