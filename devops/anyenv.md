# anyenv

- https://github.com/anyenv/anyenv

## インストール

macOS:

~~~bash
$ brew install anyenv
.
$ echo 'eval "$(anyenv init -)"' >> ~/.zshenv
.
$ exec $SHELL
.
~~~~

~~~bash
$ anyenv install --init
Manifest directory doesnt exist: /Users/hdknr/.config/anyenv/anyenv-install
Do you want to checkout ? [y/N]: y
Cloning https://github.com/anyenv/anyenv-install.git master to /Users/hdknr/.config/anyenv/anyenv-install...
Cloning into '/Users/hdknr/.config/anyenv/anyenv-install'...
remote: Enumerating objects: 48, done.
remote: Total 48 (delta 0), reused 0 (delta 0), pack-reused 48
Unpacking objects: 100% (48/48), done.

Completed!

$ anyenv install pyenv
/var/folders/m0/27vm0kbd5ys1_rs1l54zmwq00000gp/T/pyenv.20191017174713.4195 ~
Cloning https://github.com/pyenv/pyenv.git master to pyenv...
Cloning into 'pyenv'...
remote: Enumerating objects: 78, done.
remote: Counting objects: 100% (78/78), done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 17489 (delta 32), reused 26 (delta 11), pack-reused 17411
Receiving objects: 100% (17489/17489), 3.44 MiB | 1.94 MiB/s, done.
Resolving deltas: 100% (11879/11879), done.

Install pyenv succeeded!
Please reload your profile (exec $SHELL -l) or open a new session.

$ mkdir -p ~/.anyenv/plugins
.
$ git clone https://github.com/znz/anyenv-update.git ~/.anyenv/plugins/anyenv-update
.

$ git clone https://github.com/znz/anyenv-git.git ~/.anyenv/plugins/anyenv-git
.

$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
.
~~~

## bash

~~~zsh
$ vim .anyenvrc
..
~~~

~~~bash
if ! [ -x "$(command -v anyenv)" ]; then
   export PATH=$HOME/.anyenv/bin:$PATH
fi
eval "$(anyenv init -)"
eval "$(pyenv virtualenv-init -)"
for D in `\ls $HOME/.anyenv/envs`; do
    export PATH="$HOME/.anyenv/envs/$D/shims:$PATH"
done
~~~

~~~bash
$ vim .profile

...
if  -f "$HOME/.anyenvrc" ]; then
   . "$HOME/.anyenvrc"
fi
~~~
