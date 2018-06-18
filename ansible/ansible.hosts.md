## hosts


プレイブックにある `hosts` で ターゲットグループが指定される.

~~~yaml
---
- hosts: targets
  roles:
    - apps
~~~

`target` が [インベントリファイル](https://docs.ansible.com/ansible/2.4/intro_inventory.html) から参照される

hosts.aws.conf:

~~~ini
[targets]

server1
server2
~~~

プレイブックの実行にインベントリファイルを指定する:


~~~bash
$ ansible-playbook -i hosts.aws.conf book.update.yml 
~~~

実際のサーバーへの接続方法は ssh.conf で指定すると良いかも:

~~~
hoost server1
  HostName 13.230.53.172
  User ubuntu
  Port 22
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile keys/aws/ec2.pem
  IdentitiesOnly yes
  LogLevel FATAL
~~~

ssh.conf は ansible.cfgで設定するとよいかも:

~~~
[ssh_connection]
ssh_args = -F ssh.conf
~~~