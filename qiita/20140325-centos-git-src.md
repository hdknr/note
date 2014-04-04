git: ソースからビルド

CentOS 5.10 にgitをソースから入れてみた:

依存:

    # yum install gcc gcc-c++  autoconf automake kernel-devel ncurses-devel
    # yum install gettext
    # yum install zlib-devel curl-devel
    
ソースをgithubより:
    
    # wget https://github.com/git/git/archive/master.zip
    # unzip master
    # cd git-master/
    # autoconf
    # ./configure --prefix=$HOME/local --with-curl=/usr/local --with-expat
    # make all
    # make install
    # ~/local/bin/git --version
    
    git version 1.9.0.GIT
