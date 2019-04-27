# synced_folder

- [Basic Usage - Synced Folders - Vagrant by HashiCorp](https://www.vagrantup.com/docs/synced-folders/basic_usage.html)

## 例

~~~ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 22, host: 2224, id: "ssh"
  config.vm.network "private_network", ip: "192.168.56.54"
  config.vm.synced_folder "./projects", "/home/vagrant/projects"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
~~~

## 記事

- [[Vagrant]ホスト/ゲスト間のファイルの共有/同期機能（SYNCED FOLDERS）について | Coffee Breakにプログラミング備忘録](http://to-developer.com/blog/?p=1834)
- [Vagrant | synced_folder でホストOSとゲストOSの任意のフォルダを同期する - Qiita](https://qiita.com/tbpgr/items/67125ea883409ae5fd51)
