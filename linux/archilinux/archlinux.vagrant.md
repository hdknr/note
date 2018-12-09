# Arch Linux Vagrnt

- https://app.vagrantup.com/archlinux/boxes/archlinux
- https://wiki.archlinux.jp/index.php/Vagrant

macOSで `vagrant` で作成:

~~~bash 
$ vagrant box add archlinux/archlinux

==> box: Loading metadata for box 'archlinux/archlinux'
    box: URL: https://vagrantcloud.com/archlinux/archlinux
This box can work with multiple providers! The providers that it
can work with are listed below. Please review the list and choose
the provider you will be working with.

1) libvirt
2) virtualbox

Enter your choice: 2

==> box: Adding box 'archlinux/archlinux' (v2018.09.05) for provider: virtualbox
    box: Downloading: https://vagrantcloud.com/archlinux/boxes/archlinux/versions/2018.09.05/providers/virtualbox.box
==> box: Box download is resuming from prior download progress
==> box: Successfully added box 'archlinux/archlinux' (v2018.09.05) for 'virtualbox'!
~~~

~~~bash 
$ vagrant box list | grep arch
archlinux/archlinux              (virtualbox, 2018.09.05)
~~~

~~~bash 
$ vagrant init archlinux/archlinux
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
~~~

Vagrantfile:

~~~ruby
Vagrant.configure("2") do |config|
    config.vm.box = "archlinux/archlinux"

    # 追加
    config.vm.network "forwarded_port", guest: 22, host: 2221, id: "ssh"
    config.vm.network "private_network", ip: "192.168.56.54"
    config.vm.provider "virtualbox" do |vb|
        vb.memory = "2048"
    end
end
~~~

~~~bash
$ vagrant up

Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'archlinux/archlinux' is up to date...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 (guest) => 2221 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2221
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.0
VBoxService inside the vm claims: 5.2.18
Going on, assuming VBoxService is correct...
[default] GuestAdditions 5.2.18 running --- OK.
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.0
VBoxService inside the vm claims: 5.2.18
Going on, assuming VBoxService is correct...
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /Users/hide/Documents/Boxes/arch
~~~

~~~bsh 
$ vagrant ssh
$ pwd
/home/vagrant
~~~