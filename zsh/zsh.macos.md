## zsh

- [linux - Adding a new entry to the PATH variable in ZSH - Stack Overflow](https://stackoverflow.com/questions/11530090/adding-a-new-entry-to-the-path-variable-in-zsh)
- [zsh - What should/shouldn't go in .zshenv, .zshrc, .zlogin, .zprofile, .zlogout? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/71253/what-should-shouldnt-go-in-zshenv-zshrc-zlogin-zprofile-zlogout)
- [Mac OSX El Capitan での ~/.zshenv の扱いについて](https://qiita.com/t-takaai/items/8574ff312f2caa5177c2)
- [初心者向け：Zshの導入](https://qiita.com/iwaseasahi/items/a2b00b65ebd06785b443)

### ファイル

.zshenv:

- .zshenv はzshを起動したときに必ず読み込まれるファイル。
- ログインシェルとして起動したときだけでなく、zshのシェルスクリプトを実行したときや、コマンドラインから直接zshを起動したときも含まれる。
- `PATH`

.zshrc:

- シェルスクリプトを実行したときは読み込まれない
- キーバインドなど

#### 設定ファイル1

- /etc/zshenv
- ~/.zshenv
- /etc/zprofile
- ~/.zprofile
- /etc/zshrc  (以下インタラクティブの場合のみ)
- ~/.zshrc
- /etc/zlogin
- ~/.zlogin

### zsh Files

- [5.1 Startup/Shutdown Files](http://zsh.sourceforge.net/Doc/Release/Files.html#Startup_002fShutdown-Files)

システム:

- Commands are first read from `/etc/zshenv`;  this cannot be overridden.
- Subsequent behaviour is modified by the `RCS` and `GLOBAL_RCS` options;
- the former(`RCS`) affects all startup files,
- while the second(`GLOBAL_RCS`) only affects global startup files (those shown here with an path starting with a /).
- If one of the options is unset at any point, any subsequent startup file(s) of the corresponding type will not be read.
- It is also possible for a file in $ZDOTDIR to re-enable GLOBAL_RCS. Both RCS and GLOBAL_RCS are set by default.

ユーザー：

- Commands are then read from `$ZDOTDIR/.zshenv`.
- If the shell is a login shell, commands are read from `/etc/zprofile` and then `$ZDOTDIR/.zprofile`.
- Then, if the shell is interactive, commands are read from `/etc/zshrc` and then `$ZDOTDIR/.zshrc`.
- Finally, if the shell is a login shell, `/etc/zlogin` and `$ZDOTDIR/.zlogin` are read.

ログインシェルから抜ける時:

- When a login shell exits, the files `$ZDOTDIR/.zlogout` and then `/etc/zlogout` are read. 
- This happens with either an explicit exit via the exit or logout commands, or an implicit exit by reading end-of-file from the terminal. 
- However, if the shell terminates due to exec’ing another process, the logout files are not read. 
- These are also affected by the `RCS` and `GLOBAL_RCS` options. 
- Note also that the `RCS` option affects the saving of history files, i.e. if `RCS` is unset when the shell exits, no history file will be saved.

ZDOTDIR:

- If `ZDOTDIR` is unset, `HOME` is used instead. 
- Files listed above as being in /etc may be in another directory, depending on the installation.

- As `/etc/zshenv` is run for all instances of zsh, it is important that it be kept as small as possible. 
- In particular, it is a good idea to put code that does not need to be run for every single shell behind a test of the form `‘if [[ -o rcs ]]; then ...’` so that it will not be executed when zsh is invoked with the `‘-f’` option.

### macOS Catalina

- https://opensource.apple.com/source/zsh/zsh-72/
- [zsh を Mac のデフォルトシェルとして使う - Apple サポート](https://support.apple.com/ja-jp/HT208050)

#### /etc/zshenv

- Catalina にはない

#### `~/.zshenv`

- この時点では、 `/etc/paths` がよまれていないので、 `/usr/local/bin` のコマンド設定は使えない

#### `/etc/zprofile`

~~~zsh
# zsh(1) ログインシェル 用のシステムプロファイル
# 個人用は ~/.zprofile
# zshbuiltins(1) : https://linux.die.net/man/1/zshbuiltins

if [ -x /usr/libexec/path_helper ]; then
    eval `/usr/libexec/path_helper -s`  # /etc/paths を読む
fi
~~~

`/etc/paths`:

~~~bash
/usr/local/bin
/usr/bin
/bin
/usr/sbin
/sbin
/Library/Apple/usr/bin
/Library/Apple/bin
~~~

#### `~/.zprofile`

- `/etc/zprofile` で `/etc/paths` がよまれているので、 `/usr/local/bin` コマンドなどのパスが通っている
- anyenv の設定などはここでやる

#### `/etc/zshrc`

~~~zsh
# zsh(1) 用のシステムプロファイル
# ユーザー用は ~/.zhsrc
# zshbuiltins(1): https://linux.die.net/man/1/zshbuiltins
# zshoptions(1): https://linux.die.net/man/1/zshoptions

if [[ "$(locale LC_CTYPE)" == "UTF-8" ]]; then
    setopt COMBINING_CHARS
fi

# `/usr/bin/log` と競合させないために無効にする
disable log

# コマンド履歴
HISTFILE=${ZDOTDIR:-$HOME}/.zsh_history
HISTSIZE=2000
SAVEHIST=1000

# ビープ音
setopt BEEP

# zkbd によるキーコードがあれば採用する
if [[ -r ${ZDOTDIR:-$HOME}/.zkbd/${TERM}-${VENDOR} ]] ; then
    source ${ZDOTDIR:-$HOME}/.zkbd/${TERM}-${VENDOR}
else
    #  なかったらバインドする
    typeset -g -A key

    [[ -n "$terminfo[kf1]" ]] && key[F1]=$terminfo[kf1]
    [[ -n "$terminfo[kf2]" ]] && key[F2]=$terminfo[kf2]
    [[ -n "$terminfo[kf3]" ]] && key[F3]=$terminfo[kf3]
    [[ -n "$terminfo[kf4]" ]] && key[F4]=$terminfo[kf4]
    [[ -n "$terminfo[kf5]" ]] && key[F5]=$terminfo[kf5]
    [[ -n "$terminfo[kf6]" ]] && key[F6]=$terminfo[kf6]
    [[ -n "$terminfo[kf7]" ]] && key[F7]=$terminfo[kf7]
    [[ -n "$terminfo[kf8]" ]] && key[F8]=$terminfo[kf8]
    [[ -n "$terminfo[kf9]" ]] && key[F9]=$terminfo[kf9]
    [[ -n "$terminfo[kf10]" ]] && key[F10]=$terminfo[kf10]
    [[ -n "$terminfo[kf11]" ]] && key[F11]=$terminfo[kf11]
    [[ -n "$terminfo[kf12]" ]] && key[F12]=$terminfo[kf12]
    [[ -n "$terminfo[kf13]" ]] && key[F13]=$terminfo[kf13]
    [[ -n "$terminfo[kf14]" ]] && key[F14]=$terminfo[kf14]
    [[ -n "$terminfo[kf15]" ]] && key[F15]=$terminfo[kf15]
    [[ -n "$terminfo[kf16]" ]] && key[F16]=$terminfo[kf16]
    [[ -n "$terminfo[kf17]" ]] && key[F17]=$terminfo[kf17]
    [[ -n "$terminfo[kf18]" ]] && key[F18]=$terminfo[kf18]
    [[ -n "$terminfo[kf19]" ]] && key[F19]=$terminfo[kf19]
    [[ -n "$terminfo[kf20]" ]] && key[F20]=$terminfo[kf20]
    [[ -n "$terminfo[kbs]" ]] && key[Backspace]=$terminfo[kbs]
    [[ -n "$terminfo[kich1]" ]] && key[Insert]=$terminfo[kich1]
    [[ -n "$terminfo[kdch1]" ]] && key[Delete]=$terminfo[kdch1]
    [[ -n "$terminfo[khome]" ]] && key[Home]=$terminfo[khome]
    [[ -n "$terminfo[kend]" ]] && key[End]=$terminfo[kend]
    [[ -n "$terminfo[kpp]" ]] && key[PageUp]=$terminfo[kpp]
    [[ -n "$terminfo[knp]" ]] && key[PageDown]=$terminfo[knp]
    [[ -n "$terminfo[kcuu1]" ]] && key[Up]=$terminfo[kcuu1]
    [[ -n "$terminfo[kcub1]" ]] && key[Left]=$terminfo[kcub1]
    [[ -n "$terminfo[kcud1]" ]] && key[Down]=$terminfo[kcud1]
    [[ -n "$terminfo[kcuf1]" ]] && key[Right]=$terminfo[kcuf1]
fi

# デフォルトのキーバインド
[[ -n ${key[Delete]} ]] && bindkey "${key[Delete]}" delete-char
[[ -n ${key[Home]} ]] && bindkey "${key[Home]}" beginning-of-line
[[ -n ${key[End]} ]] && bindkey "${key[End]}" end-of-line
[[ -n ${key[Up]} ]] && bindkey "${key[Up]}" up-line-or-search
[[ -n ${key[Down]} ]] && bindkey "${key[Down]}" down-line-or-search

# プロンプト
PS1="%n@%m %1~ %# "

# macOSの Terminal.app の場合のセッテイング
[ -r "/etc/zshrc_$TERM_PROGRAM" ] && . "/etc/zshrc_$TERM_PROGRAM"
~~~

#### `/etc/zshrc_Apple_Terminal` 

~~~zsh
# zsh support for Terminal.

# Working Directory
#
# Tell the terminal about the current working directory at each prompt.

if [ -z "$INSIDE_EMACS" ]; then

    update_terminal_cwd() {
        # Identify the directory using a "file:" scheme URL, including
        # the host name to disambiguate local vs. remote paths.

        # Percent-encode the pathname.
        local url_path=''
        {
            # Use LC_CTYPE=C to process text byte-by-byte. Ensure that
            # LC_ALL isn't set, so it doesn't interfere.
            local i ch hexch LC_CTYPE=C LC_ALL=
            for ((i = 1; i <= ${#PWD}; ++i)); do
                ch="$PWD[i]"
                if [[ "$ch" =~ [/._~A-Za-z0-9-] ]]; then
                    url_path+="$ch"
                else
                    printf -v hexch "%02X" "'$ch"
                    url_path+="%$hexch"
                fi
            done
        }

        printf '\e]7;%s\a' "file://$HOST$url_path"
    }

    # Register the function so it is called at each prompt.
    autoload add-zsh-hook
    add-zsh-hook precmd update_terminal_cwd
fi
~~~
