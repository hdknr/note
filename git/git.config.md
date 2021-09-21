# git config (git-config - Get and set repository or global options)

## SSHキーの設定

~~~bash
$ git config core.sshCommand "ssh -i ~/.ssh/id_rsa -F /dev/null"
~~~
## パスワードの保存

- [Git push: username, password, how to avoid?](http://stackoverflow.com/questions/8588768/git-push-username-password-how-to-avoid)

~~~
$ git config credential.helper store
$ git push https://github.com/repo.git

Username for 'https://github.com': <USERNAME>
Password for 'https://USERNAME@github.com': <PASSWORD>
~~~


## ユーザー指定

~~~bash
$ git config --global user.name hdknr
$ git config --global user.email gmail@hdknr.com
$ git remote set-url origin https://hdknr@github.com/hdknr/bin.git
~~~

## ツリー表示

~/.gitconfig:

~~~
[alias]
    tr = log --graph --pretty='format:%C(yellow)%h%Creset %s %Cgreen(%an)%Creset %Cred%d%Creset'
~~~    


## error: The requested URL returned error: 403 Forbidden while accessing

- エラー

~~~bash
$ git push
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/hdknr/bin.git/info/refs
fatal: HTTP request failed
~~~

~~~bash
$ export GIT_SSL_NO_VERIFY=true  
~~~

## ファイル名の大文字・小文字の変更を検知するようにする

~~~zsh
% git config -l --local | grep core.ignorecase
core.ignorecase=true

% git config core.ignorecase false

% git config -l --local | grep core.ignorecase
core.ignorecase=false
~~~
## その他

- [.gitignore をグローバル設定する](git.ignore.md)
- [gitconfig の基本を理解する](https://qiita.com/shionit/items/fb4a1a30538f8d335b35)
- [git-config - Get and set repository or global options](https://git-scm.com/docs/git-config)
