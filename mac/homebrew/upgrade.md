# Update Log

~~~bash
$ brew upgrade
==> Upgrading 11 outdated packages:
glib 2.62.2 -> 2.62.3
erlang 22.1.7 -> 22.1.8
uncrustify 0.69.0 -> 0.70.0
numpy 1.17.2 -> 1.17.4
erlang@20 20.3.8.23 -> 20.3.8.24
zstd 1.4.3 -> 1.4.4
mercurial 5.1.2 -> 5.2_1
node 12.12.0 -> 13.1.0
unbound 1.9.4 -> 1.9.5
imagemagick 7.0.9-3 -> 7.0.9-5
git 2.24.0_1 -> 2.24.0_2
==> Upgrading erlang@20 
==> Downloading https://homebrew.bintray.com/bottles/erlang@20-20.3.8.24.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/cc/ccdc86633693f2dec689584d3104cd50d32b43ca6367ec464750740c886e8ff1?__gda__=exp=1574393143~hmac=4be31e2f765003d2148d43804004bdfa2bccacd429c5bf2e74585792e0758875&response-content-disposition=attachment%3Bfilename%3D%22erlang%4
######################################################################## 100.0%
==> Pouring erlang@20-20.3.8.24.catalina.bottle.tar.gz
==> Caveats
Man pages can be found in:
  /usr/local/opt/erlang@20/lib/erlang/man

Access them with `erl -man`, or add this directory to MANPATH.

erlang@20 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have erlang@20 first in your PATH run:
  echo 'export PATH="/usr/local/opt/erlang@20/bin:$PATH"' >> ~/.bash_profile

For compilers to find erlang@20 you may need to set:
  export LDFLAGS="-L/usr/local/opt/erlang@20/lib"

==> Summary
🍺  /usr/local/Cellar/erlang@20/20.3.8.24: 7,043 files, 277.5MB
Removing: /usr/local/Cellar/erlang@20/20.3.8.23... (7,043 files, 277.5MB)
Removing: /Users/hide/Library/Caches/Homebrew/erlang@20--20.3.8.23.catalina.bottle.tar.gz... (80.0MB)
==> Upgrading erlang 
==> Downloading https://homebrew.bintray.com/bottles/erlang-22.1.8.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/f7/f7c9b0d93f30d0f0ee2b311b7dacd3967c6065ebd2a3eea9b6ae31dc894ab9b6?__gda__=exp=1574393170~hmac=b0c6e1bbe481e491280d7ad82d92df97184ed32b22929dcacccda42437e0e2dc&response-content-disposition=attachment%3Bfilename%3D%22erlang-2
######################################################################## 100.0%
==> Pouring erlang-22.1.8.catalina.bottle.tar.gz
==> Caveats
Man pages can be found in:
  /usr/local/opt/erlang/lib/erlang/man

Access them with `erl -man`, or add this directory to MANPATH.
==> Summary
🍺  /usr/local/Cellar/erlang/22.1.8: 5,768 files, 280.2MB
Removing: /usr/local/Cellar/erlang/22.1.7... (5,768 files, 280.2MB)
Removing: /Users/hide/Library/Caches/Homebrew/erlang--22.1.7.catalina.bottle.tar.gz... (77.3MB)
==> Upgrading uncrustify 
==> Downloading https://homebrew.bintray.com/bottles/uncrustify-0.70.0.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/46/469d1f4300d8dbb2948c25e4e3f392bdde60e155826d4e600883cc2295b0416b?__gda__=exp=1574393195~hmac=6f9e4b66e15894a1cf4aeb7dff82d4f9b2f35c84fa92c3e95091ff9df36cb45e&response-content-disposition=attachment%3Bfilename%3D%22uncrusti
######################################################################## 100.0%
==> Pouring uncrustify-0.70.0.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/uncrustify/0.70.0: 67 files, 1.7MB
Removing: /usr/local/Cellar/uncrustify/0.69.0... (49 files, 1.3MB)
==> Upgrading numpy 
==> Downloading https://homebrew.bintray.com/bottles/numpy-1.17.4.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/7b/7b63631ab91df782aafe5662d11ad15265ff55ddd23647484ea51566e77e4ca1?__gda__=exp=1574393199~hmac=f2c592ce812a274e3d70c69ed897621982f4ab6e6a8dadad6670d066a8c25304&response-content-disposition=attachment%3Bfilename%3D%22numpy-1.
######################################################################## 100.0%
==> Pouring numpy-1.17.4.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/numpy/1.17.4: 483 files, 15.4MB
Removing: /usr/local/Cellar/numpy/1.17.2... (485 files, 15.6MB)
Removing: /Users/hide/Library/Caches/Homebrew/numpy--1.17.2.catalina.bottle.tar.gz... (4.2MB)
==> Upgrading zstd 
==> Downloading https://homebrew.bintray.com/bottles/zstd-1.4.4.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/31/31e79477416c7e8d44ca7e2339167a1892daea4885b95503b7bc316cae5159af?__gda__=exp=1574393204~hmac=453372a2e41b076f78b1ed4ff0bcd0515b3b869a6aa6487c005ae3a68c72779e&response-content-disposition=attachment%3Bfilename%3D%22zstd-1.4
######################################################################## 100.0%
==> Pouring zstd-1.4.4.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/zstd/1.4.4: 27 files, 3MB
Removing: /usr/local/Cellar/zstd/1.4.3... (27 files, 3MB)
Removing: /Users/hide/Library/Caches/Homebrew/zstd--1.4.3.mojave.bottle.tar.gz... (1.3MB)
==> Upgrading mercurial 
==> Downloading https://homebrew.bintray.com/bottles/mercurial-5.2_1.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/03/030be2cf0cbc0c7207c0cd630223407a989f49233cc75646b1a5df0c85451765?__gda__=exp=1574393208~hmac=0d16d62f92f5966815b83278e8e3880d3e466a611536796f8156908e0a6bb531&response-content-disposition=attachment%3Bfilename%3D%22mercuria
######################################################################## 100.0%
==> Pouring mercurial-5.2_1.catalina.bottle.tar.gz
*** failed to import extension info from ~/.hg/info.py: unicode 'info' found in cmdtable
*** (use b'' to make it byte string)
*** failed to import extension info from ~/.hg/info.py: unicode 'info' found in cmdtable
*** (use b'' to make it byte string)
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/mercurial/5.2_1: 652 files, 10.8MB
Removing: /usr/local/Cellar/mercurial/5.1.2... (656 files, 11.0MB)
Removing: /Users/hide/Library/Caches/Homebrew/mercurial--5.1.2.catalina.bottle.tar.gz... (2.5MB)
==> Upgrading node 
==> Downloading https://homebrew.bintray.com/bottles/node-13.1.0.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/58/5863d08b039c44d35a8343179cf93d495e1288efe2c669ccb77704a236e0e17b?__gda__=exp=1574393216~hmac=819f85c3c4367aacfa748d3bdb157032013877eb66d2547654d6c7ade37605d7&response-content-disposition=attachment%3Bfilename%3D%22node-13.
######################################################################## 100.0%
==> Pouring node-13.1.0.catalina.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> Summary
🍺  /usr/local/Cellar/node/13.1.0: 4,591 files, 54.2MB
Removing: /usr/local/Cellar/node/12.12.0... (4,595 files, 53.8MB)
Removing: /Users/hide/Library/Caches/Homebrew/node--12.12.0.catalina.bottle.tar.gz... (14.8MB)
==> Upgrading unbound 
==> Downloading https://homebrew.bintray.com/bottles/unbound-1.9.5.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/18/18d2518f1ba25c8667d96b2f0cc6c3c71e774cd2faf626e804eef4e58598e05e?__gda__=exp=1574393235~hmac=77db614fb12146e229754f099bf56690c411793a3a7c758521e120172c6d1be2&response-content-disposition=attachment%3Bfilename%3D%22unbound-
######################################################################## 100.0%
==> Pouring unbound-1.9.5.catalina.bottle.tar.gz
==> Caveats
To have launchd start unbound now and restart at startup:
  sudo brew services start unbound
==> Summary
🍺  /usr/local/Cellar/unbound/1.9.5: 57 files, 4.9MB
Removing: /usr/local/Cellar/unbound/1.9.4... (57 files, 4.9MB)
Removing: /Users/hide/Library/Caches/Homebrew/unbound--1.9.4.catalina.bottle.tar.gz... (2.5MB)
==> Upgrading imagemagick 
==> Installing dependencies for imagemagick: glib
==> Installing imagemagick dependency: glib
==> Downloading https://homebrew.bintray.com/bottles/glib-2.62.3.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/e4/e47b36ad0d3f8380b995573d5f545526bd6977a3196a282d91547d92d56c52f0?__gda__=exp=1574393241~hmac=9c70b37357e663b03b0bcfe8e4175c6097ceae5f3e2564174d4d087bd8bd3792&response-content-disposition=attachment%3Bfilename%3D%22glib-2.6
######################################################################## 100.0%
==> Pouring glib-2.62.3.catalina.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> Summary
🍺  /usr/local/Cellar/glib/2.62.3: 435 files, 15.4MB
==> Installing imagemagick
==> Downloading https://homebrew.bintray.com/bottles/imagemagick-7.0.9-5.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/54/54828695210a2c1cb268ad14087ffd36d2839366aeb98b288df2c58ead26081c?__gda__=exp=1574393245~hmac=8d5d35c83e77c16e42f5e975dfc4e7e43a0a8a89a4d9f321c012ce50eff6678a&response-content-disposition=attachment%3Bfilename%3D%22imagemag
######################################################################## 100.0%
==> Pouring imagemagick-7.0.9-5.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/imagemagick/7.0.9-5: 1,479 files, 24.4MB
Removing: /usr/local/Cellar/imagemagick/7.0.9-3... (1,479 files, 24.4MB)
Removing: /Users/hide/Library/Caches/Homebrew/imagemagick--7.0.9-3.catalina.bottle.tar.gz... (9.5MB)
Removing: /usr/local/Cellar/glib/2.62.2... (435 files, 15.4MB)
Removing: /Users/hide/Library/Caches/Homebrew/glib--2.62.2.catalina.bottle.tar.gz... (4.5MB)
==> Upgrading git 
==> Downloading https://homebrew.bintray.com/bottles/git-2.24.0_2.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/87/87100f6c01be17be5501be0ee5d674610e594ee0ae2d57ac3a2ebefec601e589?__gda__=exp=1574393254~hmac=526e5babdf380b2df730de543b61a5aa3c72d9c21370d8d62ae7f1f72001b112&response-content-disposition=attachment%3Bfilename%3D%22git-2.24
######################################################################## 100.0%
==> Pouring git-2.24.0_2.catalina.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions

Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/git
==> Summary
🍺  /usr/local/Cellar/git/2.24.0_2: 1,547 files, 45.5MB
Removing: /usr/local/Cellar/git/2.24.0_1... (1,547 files, 45.5MB)
==> Caveats
==> erlang@20
Man pages can be found in:
  /usr/local/opt/erlang@20/lib/erlang/man

Access them with `erl -man`, or add this directory to MANPATH.

erlang@20 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have erlang@20 first in your PATH run:
  echo 'export PATH="/usr/local/opt/erlang@20/bin:$PATH"' >> ~/.bash_profile

For compilers to find erlang@20 you may need to set:
  export LDFLAGS="-L/usr/local/opt/erlang@20/lib"

==> erlang
Man pages can be found in:
  /usr/local/opt/erlang/lib/erlang/man

Access them with `erl -man`, or add this directory to MANPATH.
==> mercurial
*** failed to import extension info from ~/.hg/info.py: unicode 'info' found in cmdtable
*** (use b'' to make it byte string)
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> node
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> unbound
To have launchd start unbound now and restart at startup:
  sudo brew services start unbound
==> glib
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> git
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions

Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/git
~~~
