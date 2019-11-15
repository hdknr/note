# Update Log


~~~bash
$ brew upgrade
==> Upgrading 10 outdated packages:
libheif 1.5.1_2 -> 1.6.0
libxml2 2.9.9_2 -> 2.9.10
gdal 2.4.2_2 -> 2.4.2_3
erlang 22.1.6 -> 22.1.7
ruby-build 20191105 -> 20191111
giflib 5.1.4_1 -> 5.2.1
mysql 8.0.18 -> 8.0.18_1
leptonica 1.78.0 -> 1.78.0_1
imagemagick 7.0.9-2 -> 7.0.9-3
git 2.24.0 -> 2.24.0_1
==> Upgrading libxml2 
==> Downloading https://homebrew.bintray.com/bottles/libxml2-2.9.10.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/f2/f23173c9ac3fa357cb1cfe511e4e5c48f28b8a06430b5a5849bb800c3357a1af?__gda__=exp=1573813835~hmac=1b1234c52d9ab29f2cc6947cffd0f9a6a69eeee921b00b7f8ae
######################################################################## 100.0%
==> Pouring libxml2-2.9.10.catalina.bottle.tar.gz
==> Caveats
libxml2 is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have libxml2 first in your PATH run:
  echo 'export PATH="/usr/local/opt/libxml2/bin:$PATH"' >> ~/.bash_profile

For compilers to find libxml2 you may need to set:
  export LDFLAGS="-L/usr/local/opt/libxml2/lib"
  export CPPFLAGS="-I/usr/local/opt/libxml2/include"

For pkg-config to find libxml2 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/libxml2/lib/pkgconfig"

==> Summary
🍺  /usr/local/Cellar/libxml2/2.9.10: 280 files, 10.5MB
Removing: /usr/local/Cellar/libxml2/2.9.9_2... (281 files, 10.5MB)
==> Upgrading gdal 
==> Installing dependencies for gdal: giflib
==> Installing gdal dependency: giflib
==> Downloading https://homebrew.bintray.com/bottles/giflib-5.2.1.catalina.bottle.tar.gz
######################################################################## 100.0%
==> Pouring giflib-5.2.1.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/giflib/5.2.1: 19 files, 383.3KB
==> Installing gdal
==> Downloading https://homebrew.bintray.com/bottles/gdal-2.4.2_3.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/37/37370723c5db87a87aa05e6601b5ecd91829788770eb3b70b8728483fd42e950?__gda__=exp=1573813856~hmac=d784f40224e58eb1e500de47c396db91a593618179b395b782b
######################################################################## 100.0%
==> Pouring gdal-2.4.2_3.catalina.bottle.tar.gz
Warning: gdal dependency gcc was built with a different C++ standard
library (libstdc++ from clang). This may cause problems at runtime.
🍺  /usr/local/Cellar/gdal/2.4.2_3: 280 files, 54.7MB
Removing: /usr/local/Cellar/gdal/2.4.2_2... (280 files, 54.7MB)
==> Upgrading erlang 
==> Downloading https://homebrew.bintray.com/bottles/erlang-22.1.7.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/1f/1f80d00eb9d980c6185affa0abcc1ebbeac8017482429ccd563fdbe2710f8bff?__gda__=exp=1573813880~hmac=a5f79ba91b7ab2b1b9c63ccb6521558ff37fd9b58cd43779296
######################################################################## 100.0%
==> Pouring erlang-22.1.7.catalina.bottle.tar.gz
==> Caveats
Man pages can be found in:
  /usr/local/opt/erlang/lib/erlang/man

Access them with `erl -man`, or add this directory to MANPATH.
==> Summary
🍺  /usr/local/Cellar/erlang/22.1.7: 5,768 files, 280.2MB
Removing: /usr/local/Cellar/erlang/22.1.6... (5,768 files, 280.2MB)
Removing: /Users/hide/Library/Caches/Homebrew/erlang--22.1.6.catalina.bottle.tar.gz... (77.3MB)
==> Upgrading ruby-build 
==> Downloading https://github.com/rbenv/ruby-build/archive/v20191111.tar.gz
==> Downloading from https://codeload.github.com/rbenv/ruby-build/tar.gz/v20191111
######################################################################## 100.0%
==> ./install.sh
🍺  /usr/local/Cellar/ruby-build/20191111: 461 files, 231.0KB, built in 12 seconds
Removing: /usr/local/Cellar/ruby-build/20191105... (461 files, 231KB)
Removing: /Users/hide/Library/Caches/Homebrew/ruby-build--20191105.tar.gz... (62.6KB)
Removing: /usr/local/Cellar/giflib/5.1.4_1... (21 files, 312.6KB)
==> Upgrading mysql 
==> Installing dependencies for mysql: protobuf@3.7
==> Installing mysql dependency: protobuf@3.7
==> Downloading https://homebrew.bintray.com/bottles/protobuf@3.7-3.7.1_1.mojave.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/de/de40ff1011be89e49ac1baf9a973349d7ec26b3a3ae0f94defe7230d07099ca5?__gda__=exp=1573814020~hmac=c1c1b24bde657447a908a3e914f03bf4a9645d549b80274a6c1
######################################################################## 100.0%
==> Pouring protobuf@3.7-3.7.1_1.mojave.bottle.tar.gz
==> Caveats
protobuf@3.7 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have protobuf@3.7 first in your PATH run:
  echo 'export PATH="/usr/local/opt/protobuf@3.7/bin:$PATH"' >> ~/.bash_profile

For compilers to find protobuf@3.7 you may need to set:
  export LDFLAGS="-L/usr/local/opt/protobuf@3.7/lib"
  export CPPFLAGS="-I/usr/local/opt/protobuf@3.7/include"

For pkg-config to find protobuf@3.7 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/protobuf@3.7/lib/pkgconfig"

==> Summary
🍺  /usr/local/Cellar/protobuf@3.7/3.7.1_1: 264 files, 18.5MB
==> Installing mysql
==> Downloading https://homebrew.bintray.com/bottles/mysql-8.0.18_1.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/dd/dd0af1f15dd8906db5842329531548c4dc46b587e36647807b663162a8d83d7c?__gda__=exp=1573814046~hmac=b458eae1ec2ff3260089e357635022f192ea1f2b5d6ce25b5e0
######################################################################## 100.0%
==> Pouring mysql-8.0.18_1.catalina.bottle.tar.gz
==> Caveats
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To have launchd start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  mysql.server start
==> Summary
🍺  /usr/local/Cellar/mysql/8.0.18_1: 287 files, 278.6MB
Removing: /usr/local/Cellar/mysql/8.0.18... (293 files, 281.4MB)
==> Upgrading leptonica 
==> Downloading https://homebrew.bintray.com/bottles/leptonica-1.78.0_1.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/d9/d9e27aab9e580e3f25f3be0c59f18aaa54b644c5886a7a1557d7bd2fda5003ab?__gda__=exp=1573814210~hmac=7c664c584ae64da81733a271c067a5a36e64f035fcb2c9a6841
######################################################################## 100.0%
==> Pouring leptonica-1.78.0_1.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/leptonica/1.78.0_1: 49 files, 5.9MB
Removing: /usr/local/Cellar/leptonica/1.78.0... (49 files, 5.9MB)
==> Upgrading imagemagick 
==> Installing dependencies for imagemagick: libheif
==> Installing imagemagick dependency: libheif
==> Downloading https://homebrew.bintray.com/bottles/libheif-1.6.0.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/0f/0fc77c14dc4528aab60296ca21e215202d1d5bb8eede62e9230d25ea956561a2?__gda__=exp=1573814223~hmac=bb44b29a50be71786e1d6b041bc230484e9f58929241b071863
######################################################################## 100.0%
==> Pouring libheif-1.6.0.catalina.bottle.tar.gz
==> /usr/local/opt/shared-mime-info/bin/update-mime-database /usr/local/share/mime
🍺  /usr/local/Cellar/libheif/1.6.0: 36 files, 2.3MB
==> Installing imagemagick
==> Downloading https://homebrew.bintray.com/bottles/imagemagick-7.0.9-3.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/7e/7e262d735c94196b6d11c7d740f15add0f4a4498ec444b5dd8202623ccdf9d58?__gda__=exp=1573814228~hmac=b020a097e1fccbe2e0a2e73c6a1b4505656162b47c518c7e10b
######################################################################## 100.0%
==> Pouring imagemagick-7.0.9-3.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/imagemagick/7.0.9-3: 1,479 files, 24.4MB
Removing: /usr/local/Cellar/imagemagick/7.0.9-2... (1,479 files, 24.4MB)
Removing: /Users/hide/Library/Caches/Homebrew/imagemagick--7.0.9-2.catalina.bottle.tar.gz... (9.5MB)
Removing: /usr/local/Cellar/libheif/1.5.1_2... (32 files, 2.3MB)
Removing: /Users/hide/Library/Caches/Homebrew/libheif--1.5.1_2.catalina.bottle.tar.gz... (1.2MB)
Removing: /Users/hide/Library/Caches/Homebrew/libheif--1.5.1_1.catalina.bottle.tar.gz... (1.2MB)
Removing: /Users/hide/Library/Caches/Homebrew/libheif--1.5.1.mojave.bottle.tar.gz... (1.2MB)
==> Upgrading git 
==> Downloading https://homebrew.bintray.com/bottles/git-2.24.0_1.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/0c/0c78003ab0077aba1cb058380d2e2e5b7af2c4c2294eff125249b5d43b612562?__gda__=exp=1573814248~hmac=c454026defe647a9fc5d3c8367bc75d01b594d48b299d671e2b
######################################################################## 100.0%
==> Pouring git-2.24.0_1.catalina.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions

Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/git
==> Summary
🍺  /usr/local/Cellar/git/2.24.0_1: 1,547 files, 45.5MB
Removing: /usr/local/Cellar/git/2.24.0... (1,547 files, 45.5MB)
==> Caveats
==> libxml2
libxml2 is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have libxml2 first in your PATH run:
  echo 'export PATH="/usr/local/opt/libxml2/bin:$PATH"' >> ~/.bash_profile

For compilers to find libxml2 you may need to set:
  export LDFLAGS="-L/usr/local/opt/libxml2/lib"
  export CPPFLAGS="-I/usr/local/opt/libxml2/include"

For pkg-config to find libxml2 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/libxml2/lib/pkgconfig"

==> erlang
Man pages can be found in:
  /usr/local/opt/erlang/lib/erlang/man

Access them with `erl -man`, or add this directory to MANPATH.
==> protobuf@3.7
protobuf@3.7 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have protobuf@3.7 first in your PATH run:
  echo 'export PATH="/usr/local/opt/protobuf@3.7/bin:$PATH"' >> ~/.bash_profile

For compilers to find protobuf@3.7 you may need to set:
  export LDFLAGS="-L/usr/local/opt/protobuf@3.7/lib"
  export CPPFLAGS="-I/usr/local/opt/protobuf@3.7/include"

For pkg-config to find protobuf@3.7 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/protobuf@3.7/lib/pkgconfig"

==> mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To have launchd start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  mysql.server start
==> git
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions

Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/git

~~~
