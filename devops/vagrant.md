# ssh


## ssh-config

~~~
(sandbox)Peeko:js1 hide$ vagrant ssh-config 
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


### up 後

~~~
Peeko:js1 hide$ sudo lsof -i:2222
~~~
~~~
COMMAND    PID USER   FD   TYPE            DEVICE SIZE/OFF NODE NAME
VBoxHeadl 1033 hide   19u  IPv4 0xcb1914cf1c0226f      0t0  TCP localhost:rockwell-csp2 (LISTEN)
VBoxHeadl 1033 hide   20u  IPv4 0xcb1914d03a1526f      0t0  TCP localhost:rockwell-csp2->localhost:49192 (CLOSED)
VBoxHeadl 1033 hide   22u  IPv4 0xcb1914cf1aec26f      0t0  TCP localhost:rockwell-csp2->localhost:49197 (CLOSED)
~~~~

~~~
Peeko:js1 hide$ sudo lsof -i:22
~~~

~~~
COMMAND PID USER   FD   TYPE            DEVICE SIZE/OFF NODE NAME
launchd   1 root   34u  IPv6 0xcb1914ce8d675a7      0t0  TCP *:ssh (LISTEN)
launchd   1 root   35u  IPv4 0xcb1914ce8d78a87      0t0  TCP *:ssh (LISTEN)
~~~

## ssh

~~~
Peeko:js1 hide$ vagrant ssh
~~~

- host

~~~
(nri)Peeko:devops hide$ ps ax | GREP_OPTIONS="" grep ssh
 1118   ??  S      0:00.57 /usr/bin/ssh-agent -l
55393 s001  S+     0:00.01 bash /usr/bin/vagrant ssh
55402 s001  S+     0:01.04 ssh vagrant@127.0.0.1
                           -p 2222
                           -o Compression=yes
                           -o DSAAuthentication=yes
                           -o LogLevel=FATAL
                           -o StrictHostKeyChecking=no
                           -o UserKnownHostsFile=/dev/null
                           -o IdentitiesOnly=yes
                           -i /Users/hide/.vagrant.d/insecure_private_key
55422 s003  S+     0:00.00 grep ssh
~~~

- guest (root)

~~~
root@js1:~# lsof -i:22
COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    1114    root    3u  IPv4  10648      0t0  TCP *:ssh (LISTEN)
sshd    1114    root    4u  IPv6  10659      0t0  TCP *:ssh (LISTEN)
sshd    1198    root    3u  IPv4  11223      0t0  TCP 10.0.2.15:ssh->10.0.2.2:49202 (ESTABLISHED)
sshd    1200 vagrant    3u  IPv4  11223      0t0  TCP 10.0.2.15:ssh->10.0.2.2:49202 (ESTABLISHED)
~~~


# sudo 


## Debian: /etc/sudoers.d/vagrant 

~~~
root@js1:~# more /etc/sudoers.d/vagrant 
vagrant ALL=NOPASSWD:ALL
~~~

## GuestAdditions

~~~
$ vagrant vbguest --status
GuestAdditions versions on your host (4.3.22) and guest (4.3.18) do not match.
~~~

~~~
$ sudo apt-get install linux-headers-$(uname -r) build-essential

Reading package lists... Done
Building dependency tree       
Reading state information... Done
build-essential is already the newest version.
linux-headers-3.16.0-4-amd64 is already the newest version.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
~~~

- [これでうまく行く](http://qiita.com/catatsuy/items/7969c0b8c6ea4c30ea97)

~~~
#!/bin/bash -xe
virtualbox_ver=4.3.22

wget http://download.virtualbox.org/virtualbox/${virtualbox_ver}/VBoxGuestAdditions_${virtualbox_ver}.iso
mkdir /media/VBoxGuestAdditions
mount -o loop,ro VBoxGuestAdditions_${virtualbox_ver}.iso /media/VBoxGuestAdditions
sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
rm VBoxGuestAdditions_${virtualbox_ver}.iso
umount /media/VBoxGuestAdditions
rmdir /media/VBoxGuestAdditions
~~~

## 共有フォルダ

### デフォルトで/vagrant -> プロジェクトフォルダ

~~~
$ vagrant reload

==> default: Mounting shared folders...
    default: /vagrant => /Users/hide/Documents/Boxes/wagtail-torchbox
~~~

[Wagtailのtorchbox実装](https://github.com/torchbox/wagtail-torchbox) でVagrant 4.3.26 だとうまくマウントできていないのは /vagrantがないからゲストでシンボリックリックを作ってやる。

~~~
$ sudo mkdir -p /vagrant
$ sudo chmod 777 /vagrant
$ sudo rmdir /home/vagrant/wagtail-torchbox
$ sudo ln -s /vagrant /home/vagrant/wagtail-torchbox
~~~

これで`vagrant reload`したらマウントされているようです。

### 明示的にマウント

- ゲストでディレクトリ

~~~
$ mkdir ~/Downloads
~~~

- Vagrantfile

~~~
config.vm.synced_folder 
	"/Users/hide/Downloads", 
	"/home/vagrant/Downloads", 
	owner: "vagrant", 
	group: "vagrant", 
	mount_options: ["dmode=777", "fmode=777"]

~~~

`vagrant reload` で Macのダウンロードフォルダが共有