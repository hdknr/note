## ssh-config

~~~
Peeko:js2 hide$ vagrant ssh-config
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /Users/hide/.vagrant.d/insecure_private_key
  IdentitiesOnly yes
  LogLevel FATAL
~~~
  
## ssh 接続

~~~
Peeko:js2 hide$ vagrant ssh

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have new mail.
Last login: Tue Jan 13 23:46:58 2015 from 10.0.2.2
~~~


## ポートを固定する


~~~ruby
Vagrant.configure(2) do |config|
  # ...
  config.vm.network "forwarded_port", guest: 22, host: 2200, id: "ssh"
  # ...
end
~~~


## 参考

- [Vagrant FILE PROVISIONER](http://docs.vagrantup.com/v2/provisioning/file.html)
- 