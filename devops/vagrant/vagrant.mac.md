## RubyGem でインストールされない

~~~
Peeko:Downloads hide$ which ruby
/usr/bin/ruby

Peeko:Downloads hide$ ruby -v
ruby 2.0.0p481 (2014-05-08 revision 45883) [universal.x86_64-darwin13]
~~~

~~~
Peeko:Downloads hide$ brew install rbenv
==> Downloading https://github.com/sstephenson/rbenv/archive/v0.4.0.tar.gz
######################################################################## 100.0%
==> Caveats
To use Homebrew's directories rather than ~/.rbenv add to your profile:
  export RBENV_ROOT=/usr/local/var/rbenv

To enable shims and autocompletion add to your profile:
  if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
==> Summary
🍺  /usr/local/Cellar/rbenv/0.4.0: 31 files, 152K, built in 3 seconds
Peeko:
~~~

~~~

Peeko:Downloads hide$ brew install ruby-build
==> Installing ruby-build dependency: openssl
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/openssl-1.0.1j.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring openssl-1.0.1j.mavericks.bottle.tar.gz
==> Caveats
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

This formula is keg-only, which means it was not symlinked into /usr/local.

Mac OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include

==> Summary
🍺  /usr/local/Cellar/openssl/1.0.1j: 431 files, 15M
==> Installing ruby-build
==> Downloading https://github.com/sstephenson/ruby-build/archive/v20141016.tar.gz
######################################################################## 100.0%
==> ./install.sh
🍺  /usr/local/Cellar/ruby-build/20141016: 129 files, 552K, built in 4 seconds

~~~

~~~
Peeko:Downloads hide$ rbenv install 2.1.3
Downloading ruby-2.1.3.tar.gz...
-> http://dqw8nmjcqpjn7.cloudfront.net/0818beb7b10ce9a058cd21d85cfe1dcd233e98b7342d32e9a5d4bebe98347f01
Installing ruby-2.1.3...
Installed ruby-2.1.3 to /Users/hide/.rbenv/versions/2.1.3
~~~

~~~
Peeko:Downloads hide$ rbenv global 2.1.3
Peeko:Downloads hide$ rbenv rehash

Peeko:Downloads hide$ ruby -v
ruby 2.0.0p481 (2014-05-08 revision 45883) [universal.x86_64-darwin13]
~~~

~~~
Peeko:Downloads hide$ echo 'eval "$(rbenv init -)"' > ~/.bash_extra/rbenv.bash
Peeko:Downloads hide$ source ~/.bash_profile 
Peeko:Downloads hide$ ruby -v
ruby 2.1.3p242 (2014-09-19 revision 47630) [x86_64-darwin13.0]
~~~

~~~
Peeko:Downloads hide$ gem -v
2.2.2
~~~

~~~
Peeko:Downloads hide$ gem install vagrant
Fetching: vagrant-1.5.0.gem (100%)
Thanks for wanting to use Vagrant! Unfortunately, this is not the way
to install Vagrant anymore. We now make installers for the various operating
systems Vagrant supports.

Vagrant is no longer distributed as a RubyGem. Please download the latest
version for your operating system from the URL below. If you still wish
to use the RubyGem version, you can manually install version 1.0.7. Note that
the RubyGem version hasn't been updated in over a year and will no longer
receive any updates.

Prior to installing Vagrant using the installer, make sure you uninstall
all your Vagrant gems, since they sometimes conflict.

http://www.vagrantup.com

If you want to learn more about why we don't distribute using RubyGems
anymore, please read this: http://mitchellh.com/abandoning-rubygems
Successfully installed vagrant-1.5.0
Parsing documentation for vagrant-1.5.0
Installing ri documentation for vagrant-1.5.0
Done installing documentation for vagrant after 0 seconds
1 gem installed
~~~

## パッケージインストーラでインストールする

- http://www.vagrantup.com/downloads.html

~~~
Peeko:Downloads hide$ which vagrant
/usr/bin/vagrant
~~~

~~~
Peeko:Downloads hide$ man vagrant
No manual entry for vagrant
Peeko:Downloads hide$ vagrant -v
Vagrant 1.6.5
~~~
