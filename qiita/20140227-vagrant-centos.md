(tact)PeekoOne:~ hide$ brew update


(tact)PeekoOne:~ hide$ brew install rbenv

Warning: No developer tools installed.
You should install the Command Line Tools.
Run `xcode-select --install` to install them.
Warning: It appears you have MacPorts or Fink installed.
Software installed with other package managers causes known problems for
Homebrew. If a formula fails to build, uninstall MacPorts/Fink and try again.
==> Downloading https://github.com/sstephenson/rbenv/archive/v0.4.0.tar.gz
######################################################################## 100.0%
==> Caveats
To use Homebrew's directories rather than ~/.rbenv add to your profile:
  export RBENV_ROOT=/usr/local/var/rbenv

To enable shims and autocompletion add to your profile:
  if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
==> Summary
🍺  /usr/local/Cellar/rbenv/0.4.0: 31 files, 152K, built in 3 seconds



(tact)PeekoOne:~ hide$ xcode-select --install
xcode-select: note: install requested for command line developer tools

MacPortsの削除は[ここ](https://abeerforyou.com/?p=334)とか。MacPortは削除済。

太古のFinkの残骸が残っていた。:

(tact)PeekoOne:~ hide$ sudo rm -rf /sw

これで"Warning: It appears you have MacPorts or Fink installed."のメッセージ消えた。

(tact)PeekoOne:~ hide$ vi ~/.bash_extra/rbenv.bash

(tact)PeekoOne:~ hide$ source !$
source ~/.bash_extra/rbenv.bash

(tact)PeekoOne:~ hide$ tree .rbenv/
.rbenv/
├── shims
└── versions

2 directories, 0 files

git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build


(tact)PeekoOne:~ hide$ git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
Cloning into '/Users/hide/.rbenv/plugins/ruby-build'...
remote: Reusing existing pack: 3004, done.
remote: Counting objects: 39, done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 3043 (delta 19), reused 0 (delta 0)
Receiving objects: 100% (3043/3043), 516.27 KiB | 200 KiB/s, done.
Resolving deltas: 100% (1380/1380), done.


(tact)PeekoOne:~ hide$ ruby -v
ruby 2.0.0p247 (2013-06-27 revision 41674) [universal.x86_64-darwin13]

(tact)PeekoOne:~ hide$ rbenv install -l | grep "^ \+2"
  2.0.0-dev
  2.0.0-p0
  2.0.0-p195
  2.0.0-p247
  2.0.0-p353
  2.0.0-p451
  2.0.0-preview1
  2.0.0-preview2
  2.0.0-rc1
  2.0.0-rc2
  2.1.0
  2.1.0-dev
  2.1.0-preview1
  2.1.0-preview2
  2.1.0-rc1
  2.1.1
  2.2.0-dev


(tact)PeekoOne:~ hide$ rbenv install 2.1.1

ruby-build: definition not found: install

You can list all available versions with `rbenv install --list'.

If the version you're looking for is not present, first try upgrading
ruby-build. If it's still missing, open a request on the ruby-build
issue tracker: https://github.com/sstephenson/ruby-build/issues
(tact)PeekoOne:~ hide$ rbenv install 2.1.1
Downloading openssl-1.0.1e.tar.gz...
-> http://dqw8nmjcqpjn7.cloudfront.net/66bf6f10f060d561929de96f9dfe5b8c
Installing openssl-1.0.1e...
Installed openssl-1.0.1e to /Users/hide/.rbenv/versions/2.1.1

Downloading ruby-2.1.1.tar.gz...
-> http://dqw8nmjcqpjn7.cloudfront.net/e57fdbb8ed56e70c43f39c79da1654b2
Installing ruby-2.1.1...
Installed ruby-2.1.1 to /Users/hide/.rbenv/versions/2.1.1


(tact)PeekoOne:~ hide$ rbenv global 2.1.1

(tact)PeekoOne:~ hide$ ruby -v
ruby 2.1.1p76 (2014-02-24 revision 45161) [x86_64-darwin13.0]

(tact)PeekoOne:~ hide$ which gem
/Users/hide/.rbenv/shims/gem

(tact)PeekoOne:~ hide$ cd ~/Desktop/
(tact)PeekoOne:Desktop hide$ git clone https://github.com/mitchellh/vagrant.git

(tact)PeekoOne:Desktop hide$ cd vagrant/

(tact)PeekoOne:vagrant hide$ gem install bundler
Fetching: bundler-1.5.3.gem (100%)
Successfully installed bundler-1.5.3
Parsing documentation for bundler-1.5.3
Installing ri documentation for bundler-1.5.3
Done installing documentation for bundler after 2 seconds
1 gem installed

(tact)PeekoOne:~ hide$ which bundle
/Users/hide/.rbenv/shims/bundle


(tact)PeekoOne:vagrant hide$ bundle install
Fetching https://github.com/mitchellh/vagrant-spec.git
remote: Reusing existing pack: 820, done.
remote: Total 820 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (820/820), 107.22 KiB | 98 KiB/s, done.
Resolving deltas: 100% (413/413), done.
Fetching gem metadata from http://rubygems.org/.......
Fetching additional metadata from http://rubygems.org/..
Resolving dependencies...
Installing rake (10.1.1)
Using bundler (1.5.3)
Installing timers (1.1.0)
Installing celluloid (0.15.2)
Installing ffi (1.9.3)
Installing childprocess (0.5.1)
Installing contest (0.1.3)
Installing diff-lcs (1.2.5)
Installing erubis (2.7.0)
Installing i18n (0.6.9)
Installing rb-fsevent (0.9.4)
Installing rb-inotify (0.9.3)
Installing listen (2.4.1)
Installing log4r (1.1.10)
Installing metaclass (0.0.4)
Installing minitest (2.5.1)
Installing mocha (1.0.0)
Installing net-ssh (2.7.0)
Installing net-scp (1.1.2)
Installing rb-kqueue (0.2.2)
Installing rspec-core (2.14.7)
Installing rspec-expectations (2.14.5)
Installing rspec-mocks (2.14.6)
Installing rspec (2.14.1)
Installing thor (0.18.1)
Installing wdm (0.1.0)
Using vagrant (1.5.0.dev) from source at .
Using vagrant-spec (0.0.1) from https://github.com/mitchellh/vagrant-spec.git (at master)
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is installed.

(tact)PeekoOne:vagrant hide$ gem build vagrant.gemspec
WARNING:  licenses is empty, but is recommended.  Use a license abbreviation from:
http://opensource.org/licenses/alphabetical
WARNING:  pessimistic dependency on bundler (~> 1.5.2) may be overly strict
  if bundler is semantically versioned, use:
    add_runtime_dependency 'bundler', '~> 1.5', '>= 1.5.2'
WARNING:  pessimistic dependency on childprocess (~> 0.5.0) may be overly strict
  if childprocess is semantically versioned, use:
    add_runtime_dependency 'childprocess', '~> 0.5', '>= 0.5.0'
WARNING:  pessimistic dependency on erubis (~> 2.7.0) may be overly strict
  if erubis is semantically versioned, use:
    add_runtime_dependency 'erubis', '~> 2.7', '>= 2.7.0'
WARNING:  pessimistic dependency on i18n (~> 0.6.0) may be overly strict
  if i18n is semantically versioned, use:
    add_runtime_dependency 'i18n', '~> 0.6', '>= 0.6.0'
WARNING:  pessimistic dependency on listen (~> 2.4.0) may be overly strict
  if listen is semantically versioned, use:
    add_runtime_dependency 'listen', '~> 2.4', '>= 2.4.0'
WARNING:  pessimistic dependency on net-scp (~> 1.1.0) may be overly strict
  if net-scp is semantically versioned, use:
    add_runtime_dependency 'net-scp', '~> 1.1', '>= 1.1.0'
WARNING:  pessimistic dependency on rb-kqueue (~> 0.2.0) may be overly strict
  if rb-kqueue is semantically versioned, use:
    add_runtime_dependency 'rb-kqueue', '~> 0.2', '>= 0.2.0'
WARNING:  pessimistic dependency on wdm (~> 0.1.0) may be overly strict
  if wdm is semantically versioned, use:
    add_runtime_dependency 'wdm', '~> 0.1', '>= 0.1.0'
WARNING:  open-ended dependency on rake (>= 0, development) is not recommended
  if rake is semantically versioned, use:
    add_development_dependency 'rake', '~> 0'
WARNING:  open-ended dependency on contest (>= 0.1.2, development) is not recommended
  if contest is semantically versioned, use:
    add_development_dependency 'contest', '~> 0.1', '>= 0.1.2'
WARNING:  pessimistic dependency on minitest (~> 2.5.1, development) may be overly strict
  if minitest is semantically versioned, use:
    add_development_dependency 'minitest', '~> 2.5', '>= 2.5.1'
WARNING:  open-ended dependency on mocha (>= 0, development) is not recommended
  if mocha is semantically versioned, use:
    add_development_dependency 'mocha', '~> 0'
WARNING:  pessimistic dependency on rspec (~> 2.14.0, development) may be overly strict
  if rspec is semantically versioned, use:
    add_development_dependency 'rspec', '~> 2.14', '>= 2.14.0'
WARNING:  See http://guides.rubygems.org/specification-reference/ for help
  Successfully built RubyGem
  Name: vagrant
  Version: 1.5.0.dev
  File: vagrant-1.5.0.dev.gem

(tact)PeekoOne:vagrant hide$ gem install vagrant-1.5.0.dev.gem 
Successfully installed vagrant-1.5.0.dev
Parsing documentation for vagrant-1.5.0.dev
Installing ri documentation for vagrant-1.5.0.dev
Done installing documentation for vagrant after 3 seconds
1 gem installed


(tact)PeekoOne:~ hide$ which vagrant
/Users/hide/.rbenv/shims/vagrant

(tact)PeekoOne:~ hide$ vagrant -v
Vagrant 1.5.0.dev


(tact)PeekoOne:~ hide$ vagrant box add "CentOS 5.10" https://dl.dropboxusercontent.com/s/r5okkx8330h3tzh/vagrant-centos-5.10-x86_64.box
You appear to be running Vagrant outside of the official installers.
Note that the installers are what ensure that Vagrant has all required
dependencies, and Vagrant assumes that these dependencies exist. By
running outside of the installer environment, Vagrant may not function
properly. To remove this warning, install Vagrant using one of the
official packages from vagrantup.com.

==> box: Adding box 'CentOS 5.10' (v0) for provider: 
    box: Downloading: https://dl.dropboxusercontent.com/s/r5okkx8330h3tzh/vagrant-centos-5.10-x86_64.box
==> box: Successfully added box 'CentOS 5.10' (v0) for 'vmware_fusion'!


(tact)PeekoOne:~ hide$ vagrant init "CentOS 5.10"
You appear to be running Vagrant outside of the official installers.
Note that the installers are what ensure that Vagrant has all required
dependencies, and Vagrant assumes that these dependencies exist. By
running outside of the installer environment, Vagrant may not function
properly. 
To remove this warning, install Vagrant using one of the
official packages from vagrantup.com.

A `Vagrantfile` has been placed in this directory. 
You are now ready to `vagrant up` your first virtual environment! 
Please read the comments in the Vagrantfile as well as documentation 
on `vagrantup.com` for more information on using Vagrant.


(tact)PeekoOne:~ hide$ tree ~/.vagrant.d/
/Users/hide/.vagrant.d/
├── boxes
│   └── CentOS\ 5.10
│       └── 0
│           └── vmware_fusion
│               ├── Virtual\ Disk-s001.vmdk
│               ├── Virtual\ Disk-s002.vmdk
│               ├── Virtual\ Disk-s003.vmdk
│               ├── Virtual\ Disk-s004.vmdk
│               ├── Virtual\ Disk-s005.vmdk
│               ├── Virtual\ Disk-s006.vmdk
│               ├── Virtual\ Disk-s007.vmdk
│               ├── Virtual\ Disk-s008.vmdk
│               ├── Virtual\ Disk-s009.vmdk
│               ├── Virtual\ Disk-s010.vmdk
│               ├── Virtual\ Disk-s011.vmdk
│               ├── Virtual\ Disk.vmdk
│               ├── metadata.json
│               ├── vagrant-centos-5.10-x86_64.nvram
│               ├── vagrant-centos-5.10-x86_64.plist
│               ├── vagrant-centos-5.10-x86_64.vmsd
│               ├── vagrant-centos-5.10-x86_64.vmx
│               └── vagrant-centos-5.10-x86_64.vmxf
├── data
├── gems
│   └── ruby
│       └── 2.1.0
├── insecure_private_key
├── rgloader
│   └── loader.rb
├── setup_version
└── tmp

10 directories, 21 files


(tact)PeekoOne:.vagrant hide$ vagrant box remove "CentOS 5.10"
You appear to be running Vagrant outside of the official installers.
Note that the installers are what ensure that Vagrant has all required
dependencies, and Vagrant assumes that these dependencies exist. By
running outside of the installer environment, Vagrant may not function
properly. To remove this warning, install Vagrant using one of the
official packages from vagrantup.com.

Removing box 'CentOS 5.10' with provider 'vmware_fusion'...

(tact)PeekoOne:.vagrant hide$ tree ~/.vagrant.d/boxes/
/Users/hide/.vagrant.d/boxes/
└── CentOS\ 5.10
    └── 0

2 directories, 0 files



(tact)PeekoOne:.vagrant hide$ vagrant init "CentOS_5_10" https://dl.dropboxusercontent.com/s/r5okkx8330h3tzh/vagrant-centos-5.10-x86_64.box
You appear to be running Vagrant outside of the official installers.
Note that the installers are what ensure that Vagrant has all required
dependencies, and Vagrant assumes that these dependencies exist. By
running outside of the installer environment, Vagrant may not function
properly. To remove this warning, install Vagrant using one of the
official packages from vagrantup.com.

A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
(tact)PeekoOne:.vagrant hide$ vagrant box add CentOS_5_10 https://dl.dropboxusercontent.com/s/r5okkx8330h3tzh/vagrant-centos-5.10-x86_64.box
You appear to be running Vagrant outside of the official installers.
Note that the installers are what ensure that Vagrant has all required
dependencies, and Vagrant assumes that these dependencies exist. By
running outside of the installer environment, Vagrant may not function
properly. To remove this warning, install Vagrant using one of the
official packages from vagrantup.com.

==> box: Adding box 'CentOS_5_10' (v0) for provider: 
    box: Downloading: https://dl.dropboxusercontent.com/s/r5okkx8330h3tzh/vagrant-centos-5.10-x86_64.box
==> box: Successfully added box 'CentOS_5_10' (v0) for 'vmware_fusion'!

(tact)PeekoOne:Desktop hide$ vagrant init CentOS_5_10
You appear to be running Vagrant outside of the official installers.
Note that the installers are what ensure that Vagrant has all required
dependencies, and Vagrant assumes that these dependencies exist. By
running outside of the installer environment, Vagrant may not function
properly. To remove this warning, install Vagrant using one of the
official packages from vagrantup.com.

A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.





