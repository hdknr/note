- Debian Jessie を Packerで作ってみる
- 途中

## Packer インストール

- http://www.packer.io/downloads.html

~~~
Peeko:~ hide$ unzip  ~/Downloads/packer_0.7.1_darwin_amd64  -d packer
~~~

~~~
Peeko:~ hide$ echo 'export PATH=~/packer:$PATH'  > ~/.bash_extra/packer.bash
Peeko:~ hide$ source ~/.bash_extra/packer.bash 

~~~

~~~
Peeko:~ hide$ cd ~/Downloads/
Peeko:Downloads hide$ packer
usage: packer [--version] [--help] <command> [<args>]

Available commands are:
    build       build image(s) from template
    fix         fixes templates from old versions of packer
    inspect     see components of a template
    validate    check that a template is valid

Globally recognized options:
    -machine-readable    Machine-readable output format.
~~~
