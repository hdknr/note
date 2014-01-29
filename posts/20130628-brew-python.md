Date: 2013-06-28 12:00
Title: Homebrew でMacにPythonをインストール
Type: post  
Excerpt:   

Homebrew の更新:

    pokemon:~ hide$ brew upgrade
    Warning: It appears you have MacPorts or Fink installed.
    Software installed with other package managers causes known problems for
    Homebrew. If a formula fails to build, uninstall MacPorts/Fink and try again.

MacPortsのアンインストール:

    pokemon:~ hide$ sudo port -fp uninstall --follow-dependents installed

    Warning: port definitions are more than two weeks old, consider using selfupdate
    --->  Uninstalling nmap @5.50_0
    .....
    

Pythonのインストール:
    
    pokemon:~ hide$ brew install python
    ==> Installing python dependency: pkg-config
    ==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/pkg-config-0.28.mountain_lion.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring pkg-config-0.28.mountain_lion.bottle.tar.gz
    /usr/local/Cellar/pkg-config/0.28: 10 files, 636K
    ==> Installing python dependency: readline
    ==> Downloading http://ftpmirror.gnu.org/readline/readline-6.2.tar.gz
    ######################################################################## 100.0%
    ==> Patching
    patching file callback.c
    patching file input.c
    patching file patchlevel
    patching file support/shobj-conf
    patching file vi_mode.c
    ==> ./configure --prefix=/usr/local/Cellar/readline/6.2.4 --mandir=/usr/local/Cellar/readline/6.2.4/share/man --infodir=/usr/local/Cellar/
    ==> make install
    ==> Caveats
    This formula is keg-only: so it was not symlinked into /usr/local.
    
    OS X provides the BSD libedit library, which shadows libreadline.
    In order to prevent conflicts when programs look for libreadline we are
    defaulting this GNU Readline installation to keg-only.
    
    Generally there are no consequences of this for you. If you build your
    own software and it requires this formula, you'll need to add to your
    build variables:
    
        LDFLAGS:  -L/usr/local/opt/readline/lib
        CPPFLAGS: -I/usr/local/opt/readline/include
    
    ==> Summary
    /usr/local/Cellar/readline/6.2.4: 31 files, 1.6M, built in 51 seconds
    ==> Installing python dependency: sqlite
    ==> Downloading http://sqlite.org/2013/sqlite-autoconf-3071700.tar.gz
    ######################################################################## 100.0%
    ==> ./configure --prefix=/usr/local/Cellar/sqlite/3.7.17 --enable-dynamic-extensions
    ==> make install
    ==> Caveats
    This formula is keg-only: so it was not symlinked into /usr/local.
    
    Mac OS X already provides this software and installing another version in
    parallel can cause all kinds of trouble.
    
    OS X provides an older sqlite3.
    
    Generally there are no consequences of this for you. If you build your
    own software and it requires this formula, you'll need to add to your
    build variables:
    
        LDFLAGS:  -L/usr/local/opt/sqlite/lib
        CPPFLAGS: -I/usr/local/opt/sqlite/include
    
    ==> Summary
    /usr/local/Cellar/sqlite/3.7.17: 9 files, 2.0M, built in 49 seconds
    ==> Installing python dependency: gdbm
    ==> Downloading http://ftpmirror.gnu.org/gdbm/gdbm-1.10.tar.gz
    ######################################################################## 100.0%
    ==> ./configure --prefix=/usr/local/Cellar/gdbm/1.10 --mandir=/usr/local/Cellar/gdbm/1.10/share/man --infodir=/usr/local/Cellar/gdbm/1.10/
    ==> make install
    /usr/local/Cellar/gdbm/1.10: 11 files, 240K, built in 29 seconds
    ==> Installing python
    ==> Downloading http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2
    ######################################################################## 100.0%
    ==> ./configure --prefix=/usr/local/Cellar/python/2.7.5 --enable-ipv6 --datarootdir=/usr/local/Cellar/python/2.7.5/share --datadir=/usr/lo
    ==> make
    ==> make install PYTHONAPPSDIR=/usr/local/Cellar/python/2.7.5
    ==> make frameworkinstallextras PYTHONAPPSDIR=/usr/local/Cellar/python/2.7.5/share/python
    ==> Downloading https://pypi.python.org/packages/source/d/distribute/distribute-0.6.45.tar.gz
    ######################################################################## 100.0%
    ==> /usr/local/Cellar/python/2.7.5/bin/python2 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/Cellar/pyt
    ==> Downloading https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz
    ######################################################################## 100.0%
    ==> /usr/local/Cellar/python/2.7.5/bin/python2 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/Cellar/pyt
    ==> Caveats
    Python demo
      /usr/local/share/python/Extras
    
    Distribute and Pip have been installed. To update them
      pip install --upgrade distribute
      pip install --upgrade pip
    
    To symlink "Idle" and the "Python Launcher" to ~/Applications
      `brew linkapps`
    
    You can install Python packages with (the outdated easy_install or)
      `pip install <your_favorite_package>`
    
    They will install into the site-package directory
      /usr/local/lib/python2.7/site-packages
    
    See: https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python
    Warning: Could not link python. Unlinking...
    Error: The `brew link` step did not complete successfully
    The formula built, but is not symlinked into /usr/local
    You can try again using `brew link python'

シンボリックリンクの強制追加:

    pokemon:~ hide$ brew link --overwrite python
    Linking /usr/local/Cellar/python/3.7.5... 34 symlinks created
    
    pokemon:~ hide$ which python
    /usr/bin/python


OSXのデフォルトのパスの順番

    pokemon:~ hide$ more /etc/paths

    /usr/bin
    /bin
    /usr/sbin
    /sbin
    /usr/local/bin

この順番を変更したらログインし直し。

    pokemon:Blog hide$ which python
    /usr/local/bin/python


