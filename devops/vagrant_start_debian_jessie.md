# Vagrant:  Debian Jessie をインストール

- VirualBoxをインストールしていること
- http://www.vagrantbox.es/


# vagrant box add {{name}} :Debian Jessieのboxを追加

~~~
Peeko:Downloads hide$ vagrant box add jessie https://downloads.sourceforge.net/project/vagrantboxjessie/debian80.box
==> box: Adding box 'jessie' (v0) for provider: 
    box: Downloading: https://downloads.sourceforge.net/project/vagrantboxjessie/debian80.box
    box: Progress: 91% (Rate: 685k/s, Estimated time remaining: 0:00:41)
    
==> box: Successfully added box 'jessie' (v0) for 'virtualbox'!    
~~~

## vagrant list: 確認

~~~
Peeko:Downloads hide$ vagrant box list
jessie (virtualbox, 0)
~~~

- ディレクトリツリー

~~~
/Users/hide/.vagrant.d/
├── boxes
│   └── jessie
│       └── 0
│           └── virtualbox
│               ├── Vagrantfile
│               ├── box-disk1.vmdk
│               ├── box.ovf
│               └── metadata.json
├── data
│   ├── checkpoint_cache
│   ├── checkpoint_signature
│   └── machine-index
│       └── index.lock
├── gems
│   └── ruby
│       └── 2.0.0
├── insecure_private_key
├── rgloader
│   └── loader.rb
├── setup_version
└── tmp

11 directories, 10 files
~~~    


# vagrant init {{name}} : 作成

- ディレクトリ作成

~~~
Peeko:~ hide$ mkdir -p ~/Documents/Boxes/jssie1
Peeko:~ hide$ cd !$
cd ~/Documents/Boxes/jssie1
~~~

- vagrant init jessie

~~~
Peeko:jssie1 hide$ vagrant init jessie
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.

Peeko:jssie1 hide$ tree .
.
└── Vagrantfile

0 directories, 1 file
~~~

## ホストオンリーアダプタを追加

~~~
Peeko:jssie1 hide$ vi Vagrantfile 

    config.vm.network "private_network", ip: "192.168.56.50"

~~~

# vagrant up: 起動

~~~
Peeko:jssie1 hide$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'jessie'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: jssie1_default_1413678798477_55336
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 => 2222 (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection timeout. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /Users/hide/Documents/Boxes/jssie1
~~~

# vagrant ssh: 接続

~~~
Peeko:jssie1 hide$ vagrant ssh
Linux 10 3.14-2-amd64 #1 SMP Debian 3.14.13-2 (2014-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Aug 18 07:11:18 2014 from 10.0.2.2
~~~

# vagrant halt: シャットダウン

~~~
Peeko:jssie1 hide$ vagrant halt
==> default: Attempting graceful shutdown of VM...
~~~

# vagrant destroy: 削除

~~~
Peeko:jssie1 hide$ vagrant destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==> default: Destroying VM and associated drives...
~~~

