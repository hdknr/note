# `init`


~~~zsh
% vagrant init ubuntu/focal64
~~~ 


~~~ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network "forwarded_port", guest: 22, host: 2224, id: "ssh"
  config.vm.network "private_network", ip: "192.168.56.54"
  config.vm.synced_folder "#{ENV['HOME']}/Documents/DropBox/Projects", "/home/vagrant/projects"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
~~~
