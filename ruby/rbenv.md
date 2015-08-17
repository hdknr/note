## anyenv + rbenv

~~~bash
$ anyenv install rbenv
/tmp/rbenv.20150724175208.8606 ~
Cloning https://github.com/sstephenson/rbenv.git...
Cloning into 'rbenv'...
remote: Counting objects: 2075, done.
remote: Total 2075 (delta 0), reused 0 (delta 0), pack-reused 2075
Receiving objects: 100% (2075/2075), 352.32 KiB | 455.00 KiB/s, done.
Resolving deltas: 100% (1290/1290), done.
Checking connectivity... done.
~
~/.anyenv/envs/rbenv/plugins ~
Cloning https://github.com/sstephenson/ruby-build.git...
Cloning into 'ruby-build'...
remote: Counting objects: 4956, done.
remote: Compressing objects: 100% (32/32), done.
remote: Total 4956 (delta 22), reused 0 (delta 0), pack-reused 4923
Receiving objects: 100% (4956/4956), 918.87 KiB | 503.00 KiB/s, done.
Resolving deltas: 100% (2660/2660), done.
Checking connectivity... done.
~

Install rbenv succeeded!
Please reload your profile (exec $SHELL -l) or open a new session.
~~~

~~~bash
$ exec $SHELL -l

$ rbenv version
system (set by /home/vagrant/.anyenv/envs/rbenv/version)
~~~

~~~bash
$ anyenv versions
ndenv:
* 0.12.0 (set by /home/vagrant/.anyenv/envs/ndenv/version)
phpenv:
  system
* 5.6.10 (set by /home/vagrant/.anyenv/envs/phpenv/version)
  5.6.9
pyenv:
  system
* 2.7.9 (set by /home/vagrant/.anyenv/envs/pyenv/version)
  sentry
  wordpress
rbenv:
* system (set by /home/vagrant/.anyenv/envs/rbenv/version)
~~~

## ruby インストール

~~~bash
$ rbenv install -l | grep "^ \+2" | tail
  2.1.5
  2.1.6
  2.2.0-dev
  2.2.0-preview1
  2.2.0-preview2
  2.2.0-rc1
  2.2.0
  2.2.1
  2.2.2
  2.3.0-dev
~~~

~~~bash
$ rbenv install 2.2.2
Downloading ruby-2.2.2.tar.gz...
-> https://dqw8nmjcqpjn7.cloudfront.net/5ffc0f317e429e6b29d4a98ac521c3ce65481bfd22a8cf845fa02a7b113d9b44
Installing ruby-2.2.2...
Installed ruby-2.2.2 to /home/vagrant/.anyenv/envs/rbenv/versions/2.2.2

~~~

~~~bash
$ rbenv global 2.2.2
$ which gem
/home/vagrant/.anyenv/envs/rbenv/shims/gem
~~~


### bundler

~~~bash
$ gem install bundler
Fetching: bundler-1.10.6.gem (100%)
Successfully installed bundler-1.10.6
Parsing documentation for bundler-1.10.6
Installing ri documentation for bundler-1.10.6
Done installing documentation for bundler after 3 seconds
1 gem installed
~~~

- [Bundler概要](http://qiita.com/hisonl/items/162f70e612e8e96dba50)

python だと

~~~bash
$ vim requiremtns.txt
$ pip install -r requirements.txt
$ pip freeze > requirements.txt
~~~

#### bundle init

~~~bash
$ bundle init
Writing new Gemfile to /home/vagrant/projects/helloruby/Gemfile
~~~

~~~bash
$ more Gemfile 
# A sample Gemfile
source "https://rubygems.org"

# gem "rails"
~~~

- [gemライブラリの依存はGemfileではなくgemspecに記述する理由](http://qiita.com/metheglin/items/32fe6042fb0416e04359)

	結論を言うと他の様々なサイトでも指摘されている通り、gemライブラリの依存関係はgemspecに記述し、Gemfileはgemspec1行書くにとどめておく.


	