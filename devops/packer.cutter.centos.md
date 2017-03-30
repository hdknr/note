~~~bash
$ git https://github.com/hdknr/Cutters.git

git: 'https://github.com/hdknr/Cutters.git' is not a git command. See 'git --help'.
(tact)Peeko:Projects hide$ git clone https://github.com/hdknr/Cutters.git
Cloning into 'Cutters'...
remote: Counting objects: 41, done.
remote: Total 41 (delta 0), reused 0 (delta 0), pack-reused 41
Unpacking objects: 100% (41/41), done.
Checking connectivity... done.
~~~

~~~bash
$ cd Cutters
~~~

~~~bash
$ git submodule update --init --recursive

Submodule 'centos' (https://github.com/boxcutter/centos.git) registered for path 'centos'
Submodule 'debian' (https://github.com/boxcutter/debian.git) registered for path 'debian'
Submodule 'ubuntu' (https://github.com/boxcutter/ubuntu.git) registered for path 'ubuntu'
Cloning into 'centos'...
remote: Counting objects: 1259, done.
remote: Total 1259 (delta 0), reused 0 (delta 0), pack-reused 1259
Receiving objects: 100% (1259/1259), 284.09 KiB | 295.00 KiB/s, done.
Resolving deltas: 100% (876/876), done.
Checking connectivity... done.
Submodule path 'centos': checked out '71f1f5eae168293106f1eef2b6525dd4a276f740'
Cloning into 'debian'...
remote: Counting objects: 776, done.
remote: Total 776 (delta 0), reused 0 (delta 0), pack-reused 776
Receiving objects: 100% (776/776), 164.26 KiB | 0 bytes/s, done.
Resolving deltas: 100% (514/514), done.
Checking connectivity... done.
Submodule path 'debian': checked out '11a2df7adb387b720a1a2e88c674cbad98fc6c5a'
Cloning into 'ubuntu'...
remote: Counting objects: 1607, done.
remote: Total 1607 (delta 0), reused 0 (delta 0), pack-reused 1607
Receiving objects: 100% (1607/1607), 282.96 KiB | 347.00 KiB/s, done.
Resolving deltas: 100% (1068/1068), done.
Checking connectivity... done.
Submodule path 'ubuntu': checked out 'a89681a5322c806fb6130c08e397eb9131c9ac92'
~~~

~~~bash
$ cd jp.centos/
~~~

~~~bash
$ mkdir -p ../centos/box
$ mkdir -p ../centos/packer_cache
$ ln -s ../centos/VERSION .
~~~

~~~bash
$ ~/packer/packer validate jp.centos66.json
Template validated successfully.
~~~

~~~bash
$ make virtualbox/jp.centos66
~~~

~~~bash
$ vagrant box add centos67 ~/Documents/Projects/Cutters/jp.centos/box/virtualbox/centos66-nocm-2.0.2.box

==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'centos67' (v0) for provider:
    box: Unpacking necessary files from: file:///Users/hide/Documents/Projects/Cutters/jp.centos/box/virtualbox/centos66-nocm-2.0.2.box
==> box: Successfully added box 'centos67' (v0) for 'virtualbox'!
~~~

~~~bash
$ vagrant box list

centos67          (virtualbox, 0)
coreos-alpha      (virtualbox, 472.0.0)
jessie            (virtualbox, 0)
kifli-devstack    (virtualbox, 0)
wagtail-base-v0.1 (virtualbox, 0)
~~~

~~~bash
$ vagrant init centos67

A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.

~~~


~~~bash
$ tree . -a
.
├── .vagrant
└── Vagrantfile

1 directory, 1 file
~~~

~~~bash
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'centos67'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: vm_default_1446422265095_39
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 => 2200 (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection timeout. Retrying...
    default: Warning: Connection timeout. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
GuestAdditions 4.3.30 running --- OK.
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /Users/hide/Documents/Eco/vm
~~~    

~~~bash
$ tree . -a
.
├── .vagrant
│   └── machines
│       └── default
│           └── virtualbox
│               ├── action_provision
│               ├── action_set_name
│               ├── creator_uid
│               ├── id
│               ├── index_uuid
│               ├── private_key
│               └── synced_folders
└── Vagrantfile

4 directories, 8 files
~~~

~~~bash
$ vagrant ssh

Last login: Sat Oct 31 06:24:09 2015
Welcome to your Packer-built virtual machine.

[vagrant@localhost ~]$ uname -a

Linux localhost.localdomain 2.6.32-573.el6.x86_64 #1 SMP Thu Jul 23 15:44:03 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
~~~
