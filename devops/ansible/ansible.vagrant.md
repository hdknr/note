Ansible: Vagrantの Debian Jessieにパッケージインストール

- メモ

## Ansible + Vagrant 

- [Using Vagrant and Ansible](http://docs.ansible.com/guide_vagrant.html)


### Init Vagrant (Debian Guest)

~~~
(sandbox)Peeko:Boxes hide$ mkdir js2
(sandbox)Peeko:Boxes hide$ cd js2
~~~

~~~
(sandbox)Peeko:js2 hide$ vagrant init jessie
~~~
~~~
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
~~~

~~~
(sandbox)Peeko:js2 hide$ tree -a .
.
└── Vagrantfile

0 directories, 1 file
~~~

- IPアドレス、メモリ設定

~~~
(sandbox)Peeko:js2 hide$ GREP_OPTIONS= grep -v '^\s*#' Vagrantfile  | GREP_OPTIONS= grep -v "^$"
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "jessie"
  config.vm.network "private_network", ip: "192.168.56.51"
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end
end
~~~

### inventory

~~~
(sandbox)Peeko:js2 hide$ vi hosts 
~~~

~~~
[servers]
192.168.56.51
~~~


### playbook

~~~
(sandbox)Peeko:js2 hide$ vi debinit.yml 
~~~

~~~
- hosts: servers
  sudo: true
  user: vagrant
  tasks:
    - name: Update apt repository
      apt: update_cache=yes state=latest
    - name: "Upgrade Packages"
      apt: upgrade=yes state=latest
    - name: add package $item
      apt: pkg={{item}} state=installed
      with_items:
        - git
        - build-essential
        - wget 
        - curl 
        - lsb-release 
        - rsync 
        - make 
        - gcc 
        - g++ 
        - bison 
        - lsof 
        - locate 
        - ntpdate 
        - tmux 
        - vim 
        - dnsutils 
        - unzip 
        - subversion 
        - git 
        - mercurial 
        - libyaml-dev 
        - pkg-config
        - apparix 
        - tree
        - libpq-dev  
        - libmemcached-dev 

~~~


~~~
(sandbox)Peeko:js2 hide$ GREP_OPTIONS= grep -v '^\s*#' Vagrantfile  | GREP_OPTIONS= grep -v "^$"
~~~
~~~
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "jessie"
  config.vm.network "private_network", ip: "192.168.56.51"
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end
  
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "debinit.yml"
    ansible.inventory_path = "hosts"  
    ansible.limit = 'all'
  end 
end
~~~


### vagrant up


~~~
(sandbox)Peeko:js2 hide$ vagrant up
~~~

~~~
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'jessie'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: js2_default_1414462751668_32867
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 => 2222 (adapter 1)
==> default: Running 'pre-boot' VM customizations...
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
    default: /vagrant => /Users/hide/Documents/Boxes/js2
==> default: Running provisioner: ansible...

PLAY [servers] **************************************************************** 

GATHERING FACTS *************************************************************** 
ok: [192.168.56.51]

TASK: [Update apt repository] ************************************************* 
ok: [192.168.56.51]

TASK: [add package $item] ***************************************************** 
changed: [192.168.56.51] => (item=git,build-essential,wget,curl,lsb-release,rsync,make,gcc,g++,bison,lsof,locate,ntpdate,tmux,vim,dnsutils,unzip,subversion,git,mercurial,libyaml-dev,pkg-config,apparix,tree,libpq-dev,libmemcached-dev)

PLAY RECAP ******************************************************************** 
192.168.56.51              : ok=4    changed=2    unreachable=0    failed=0   
~~~

~~~
(sandbox)Peeko:js2 hide$ ansible -i hosts  -a "dpkg -l"  servers  | GREP_OPTIONS= grep tmux
~~~

~~~
ii  tmux                           1.9-6                       amd64        terminal multiplexer
~~~
    
