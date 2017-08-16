ssh

## ポートを固定する


~~~ruby
Vagrant.configure(2) do |config|
  # ...
  config.vm.network "forwarded_port", guest: 22, host: 2200, id: "ssh"
  # ...
end
~~~
