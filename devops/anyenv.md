# anyenv

- https://github.com/anyenv/anyenv

~~~bash
$ git clone https://github.com/anyenv/anyenv ~/.anyenv
$ export PATH="$HOME/.anyenv/bin:$PATH"
$ ~/.anyenv/bin/anyenv init
.
~~~

shell:

~~~bash
BASE="$HOME"
export PATH="$BASE/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

for D in `\ls $BASE/.anyenv/envs`; do
    export PATH="$BASE/.anyenv/envs/$D/shims:$PATH"
done
~~~

## anyenv-update

- https://github.com/znz/anyenv-update

~~~bash
$ mkdir -p $(anyenv root)/plugins
$ git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update
.
~~~

## pyenv

- https://github.com/pyenv/pyenv
- https://github.com/pyenv/pyenv-virtualenv
