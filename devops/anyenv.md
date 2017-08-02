## anyenv - install

~~~
$ ~/bin/setup/anyenv.bash
Cloning into '/home/vagrant/.anyenv'...
remote: Counting objects: 139, done.
remote: Total 139 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (139/139), 22.07 KiB | 0 bytes/s, done.
Resolving deltas: 100% (47/47), done.
Checking connectivity... done.
~~~

~~~
$ source ~/bin/env/anyenv.bash
~~~

## list env

~~~
$ anyenv install -l
Available **envs:
  denv
  goenv
  jenv
  luaenv
  ndenv
  phpenv
  plenv
  pyenv
  rbenv
  scalaenv

~~~

## ndenv

~~~
$ anyenv install ndenv
/tmp/ndenv.20150211141812.8780 ~
Cloning https://github.com/riywo/ndenv.git...
Cloning into 'ndenv'...
remote: Counting objects: 54, done.
remote: Total 54 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (54/54), done.
Checking connectivity... done.
~
~/.anyenv/envs/ndenv/plugins ~
Cloning https://github.com/riywo/node-build.git...
Cloning into 'node-build'...
remote: Counting objects: 37, done.
remote: Total 37 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (37/37), done.
Checking connectivity... done.
~

Install ndenv succeeded!
Please reload your profile (exec $SHELL -l) or open a new session.
~~~

~~~
$ ndenv
ndenv 0.4.0
Usage: ndenv <command> [<args>]

Some useful ndenv commands are:
   commands    List all available ndenv commands
   local       Set or show the local application-specific Node version
   global      Set or show the global Node version
   shell       Set or show the shell-specific Node version
   install     Install a Node version using the node-build plugin
   uninstall   Uninstall a specific Node version
   rehash      Rehash ndenv shims (run this after installing executables)
   version     Show the current Node version and its origin
   versions    List all Node versions available to ndenv
   which       Display the full path to an executable
   whence      List all Node versions that contain the given executable

See `ndenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/riywo/ndenv#readme
~~~

~~~
$ ndenv install 0.12.0
Downloading node-v0.12.0-linux-x64.tar.gz...
-> http://nodejs.org/dist/v0.12.0/node-v0.12.0-linux-x64.tar.gz
Installing node-v0.12.0-linux-x64...
Installed node-v0.12.0-linux-x64 to /home/vagrant/.anyenv/envs/ndenv/versions/0.12.0
~~~

~~~
$ ndenv global 0.12.0
~~~

~~~
$ anyenv versions
ndenv:
* 0.12.0 (set by /home/vagrant/.anyenv/envs/ndenv/version)
~~~

~~~
$ which npm
/home/vagrant/.anyenv/envs/ndenv/shims/npm
~~~

## pyenv: error: failed to download Python-2.7.10.tgz

- OSが古いとエラーになる

~~~
$ pyenv install 2.7.10
Downloading Python-2.7.10.tgz...
-> https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
error: failed to download Python-2.7.10.tgz

BUILD FAILED (Ubuntu 8.04 using python-build 20150601-6-g22ecefd)
~~~

~~~
$ export PYTHON_BUILD_MIRROR_URL="http://yyuu.github.io/pythons"
~~~

## pyenv global とかで切り替わらない

- `~/.python-version` が存在する

~~~bash
$ rm -rf .python-version
~~~

## anyenv update

~~~bash
$ anyenv update
Updating 'anyenv'...
Updating 'anyenv/anyenv-update'...
Updating 'ndenv'...
Updating 'ndenv/node-build'...
Updating 'phpenv'...
Updating 'phpenv/php-build'...
 |  Pull is not possible because you have unmerged files.
 |  Please, fix them up in the work tree, and then use 'git add/rm <file>'
 |  as appropriate to mark resolution, or use 'git commit -a'.
 |  Failed to update. Use 'verbose' option for detailed, or 'force' option.
Updating 'pyenv'...
 |  From https://github.com/yyuu/pyenv
 |  4a707c2..7dae197  master     -> origin/master
 |  * [new branch]      copy-libpypy3 -> origin/copy-libpypy3
 |  * [new tag]         v1.1.2     -> v1.1.2
 |  * [new tag]         v1.1.3     -> v1.1.3
Updating 'pyenv/pyenv-doctor'...
Updating 'pyenv/pyenv-installer'...
Updating 'pyenv/pyenv-update'...
 |  From https://github.com/yyuu/pyenv-update
 |  c468d9f..efd96e2  master     -> origin/master
Updating 'pyenv/pyenv-virtualenv'...
 |  From https://github.com/yyuu/pyenv-virtualenv
 |  c677627..2727087  master     -> origin/master
 |  * [new tag]         v1.1.0     -> v1.1.0
Updating 'pyenv/pyenv-which-ext'...
 |  From https://github.com/yyuu/pyenv-which-ext
 |  2aaf7d9..9d37659  master     -> origin/master
Skipping 'pyenv/python-build'; not git repo
Updating 'rbenv'...
 |  From https://github.com/sstephenson/rbenv
 |  6cd487d..615f844  master     -> origin/master
Updating 'rbenv/ruby-build'...
 |  From https://github.com/sstephenson/ruby-build
 |  476d09b..59607cb  master     -> origin/master
 |  * [new tag]         v20170726  -> v20170726
 ~~~
