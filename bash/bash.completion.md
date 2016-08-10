- [bash-completionで独自の補完関数を作成する方法（gistyのサブコマンドを補完するやつ書いてみた）](http://d.hatena.ne.jp/snaka72/20090930/1254316751)
- [bash なんて書いたことない人が補完関数をとりあえず自作する](http://qiita.com/sosuke/items/06b64068155ae4f8a853)
- [bash-completionで ssh コマンドなどの補完を強化してみる](http://qiita.com/murachi1208/items/c6aadc7a6e455a78bb3f)
- [初めてのオレオレbash補完](https://blog.riywo.com/2012/08/27/235239/)

## bash-completion

~~~bash
$ dpkg -L bash-completion | grep -v "/usr/share/bash-completion"
/.
/etc
/etc/profile.d
/etc/profile.d/bash_completion.sh
/etc/bash_completion
/etc/bash_completion.d
/usr
/usr/share
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/dh_bash-completion.1.gz
/usr/share/doc
/usr/share/doc/bash
/usr/share/doc/bash-completion
/usr/share/doc/bash-completion/changelog.Debian.gz
/usr/share/doc/bash-completion/copyright
/usr/share/doc/bash-completion/README.Debian
/usr/share/doc/bash-completion/AUTHORS
/usr/share/doc/bash-completion/changelog.gz
/usr/share/doc/bash-completion/README.gz
/usr/share/perl5
/usr/share/perl5/Debian
/usr/share/perl5/Debian/Debhelper
/usr/share/perl5/Debian/Debhelper/Sequence
/usr/share/perl5/Debian/Debhelper/Sequence/bash_completion.pm
/usr/share/bug
/usr/share/bug/bash-completion
/usr/share/bug/bash-completion/presubj
/usr/share/pkgconfig
/usr/share/pkgconfig/bash-completion.pc
/usr/bin
/usr/bin/dh_bash-completion
/usr/share/doc/bash/README.bash_completion.gz
~~~

## help

~~~bash
$ help complete
$ man complete
~~~    


##  大文字小文字の無視

~/.inputrc:

~~~bash
set completion-ignore-case on
~~~

##  プロジェクトディレクトリに移動: cdpj

cdpj.conf:

~~~bash
#!/bin/bash
declare -A PJ

PJ['dogs']=/vagrant/projects/dogs
PJ['cats']=/home/projects/cats

_cdpj()
{
    local pj; pj=${!PJ[@]};
    COMPREPLY=( $( compgen -W "$pj"  ${COMP_WORDS[COMP_CWORD]} ) )
}
complete -F _cdpj cdpj

function inArray # ( keyOrValue, arrayKeysOrValues )
{
  local e
  for e in "${@:2}"; do
    [[ "$e" == "$1" ]] && return 0;
  done
  return 1
}

function cdpj(){
  if inArray $1 ${!PJ[@]}; then
    cd ${PJ[$1]}
  else
    echo "Projects not found: ${!PJ[@]}"
  fi  
}
~~~

~~~bash
$ source cdpj.conf
~~~
