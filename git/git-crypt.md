# git-crypt

- [git-crypt を使って秘密情報を版管理する ｜ DevelopersIO](https://dev.classmethod.jp/tool/git/git-crypt/)
- [リモートリポジトリの特定のファイルを暗号化しておく - Qiita](https://qiita.com/yuhr/items/52cb02d46aa19b1b9e87)
- [[git-crypt] リモートリポジトリ内の特定ファイルの暗号化 - Qiita](https://qiita.com/task4233/items/fbb9625225294151c8ac)
- [macOS Sierraで、GitHubにGPG署名付きでコミットできるように設定する。 - Qiita](https://qiita.com/miya0001/items/0b50fd2c482d61479f54)

## GPG

- [githubで使うGPG鍵の作成 - Qiita](https://qiita.com/kanatatsu64/items/85104644d1599c244f35)
- [GPG で公開鍵を他者と交換して署名する手順 - yu8mada](https://yu8mada.com/2018/04/01/a-procedure-for-exchanging-public-keys-with-others-and-signing-them-in-gpg/)
- [gpg-agent not found for homebrew - Stack Overflow](https://stackoverflow.com/questions/52435650/gpg-agent-not-found-for-homebrew)

## gnupg

- [pinentryってなんだ - Qiita](https://qiita.com/satoruk/items/53b4a0f97bec0167bf62)
- [gpg (GNU Privacy Guard)の使い方 - Qiita](https://qiita.com/moutend/items/5c22d6e57a74845578f6)
- [GnuPGのコマンド](http://www.nina.jp/server/windows/gpg/commands.html#list)

~~~bash
$ brew install gnupg pinentry-mac
Warning: gnupg 2.2.13 is already installed and up-to-date
To reinstall 2.2.13, run `brew reinstall gnupg`
==> Downloading https://homebrew.bintray.com/bottles/pinentry-mac-0.9.4.mojave.bottle.tar.gz
######################################################################## 100.0%
==> Pouring pinentry-mac-0.9.4.mojave.bottle.tar.gz
==> Caveats
You can now set this as your pinentry program like

~/.gnupg/gpg-agent.conf
    pinentry-program /usr/local/bin/pinentry-mac
==> Summary
🍺  /usr/local/Cellar/pinentry-mac/0.9.4: 11 files, 401KB
~~~

## キーの生成

~~~bash
$ gpg --generate-key

gpg (GnuPG) 2.2.13; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

注意: 全機能の鍵生成には "gpg --full-generate-key" を使います。

GnuPGはあなたの鍵を識別するためにユーザIDを構成する必要があります。

本名: hdknr
電子メール・アドレス: hdknr@mydomain.co.jp
次のユーザIDを選択しました:                        
    "hdknr <hdknr@mydomain.co.jp>"

名前(N)、電子メール(E)の変更、またはOK(O)か終了(Q)? O
たくさんのランダム・バイトの生成が必要です。キーボードを打つ、マウスを動か
す、ディスクにアクセスするなどの他の操作を素数生成の間に行うことで、乱数生
成器に十分なエントロピーを供給する機会を与えることができます。
たくさんのランダム・バイトの生成が必要です。キーボードを打つ、マウスを動か
す、ディスクにアクセスするなどの他の操作を素数生成の間に行うことで、乱数生
成器に十分なエントロピーを供給する機会を与えることができます。
gpg: 鍵A8AE65BB2CC51F60を究極的に信用するよう記録しました
gpg: ディレクトリ'/Users/hide/.gnupg/openpgp-revocs.d'が作成されました
gpg: 失効証明書を '/Users/hide/.gnupg/openpgp-revocs.d/9055311658955590F57BEAE5A8AE65BB2CC51F60.rev' に保管しました。
公開鍵と秘密鍵を作成し、署名しました。

pub   rsa2048 2019-02-17 [SC] [有効期限: 2021-02-16]
      9055311658955590F57BEAE5A8AE65BB2CC51F60
uid                      hdknr <hdknr@mydomain.co.jp>
sub   rsa2048 2019-02-17 [E] [有効期限: 2021-02-16]
~~~

## 自分の公開鍵のエクスポート

~~~bash
$ gpg --output hdknr.gpg --export hdknr@mydomain.co.jp
.
~~~

- 相手に渡す

### Github.com に登録

~~~bash
$ gpg --armor --export hdknr@mydomain.co.jp | pbcopy
$ open https://github.com/settings/gpg/new
.
~~~

公開鍵の取得:

~~~bash
$ curl https://github.com/hdknr.gpg
.
~~~

- [Generating a new GPG key - User Documentation](https://help.github.com/articles/generating-a-new-gpg-key/)
- [Verifying your email address - User Documentation](https://help.github.com/articles/verifying-your-email-address/)

##　他のメンバーの公開鍵インポート

bobからもらう:

~~~bash
$ gpg --import bob.gpg
.
~~~

## 他のメンバーの公開鍵を信頼する

~~~bash
$ gpg --sign-key bob@example.com
.
~~~

## git-crypt 設定

~~~bash
$ brew install git-crypt
.
~~~

~~~bash
$ git crypt init
Generating key...
~~~

## ユーザーの追加

~~~bash
$ git crypt add-gpg-user hdknr@mydomain.co.jp
[alpha defd6fa] Add 1 git-crypt collaborator
 2 files changed, 4 insertions(+)
 create mode 100644 .git-crypt/.gitattributes
 create mode 100644 .git-crypt/keys/default/0/9055311658955590F57BEAE5A8AE65BB2CC51F60.gpg
~~~

## .gitattributes 設定

~~~bash
$ cat .gitattributes
ansible/keys/aws/app-server.pem filter=git-crypt diff=git-crypt
ansible/keys/bitbucket/app-server.pem filter=git-crypt diff=git-crypt
~~~

## commit & push

~~~bash
$ git add .gitattributes ansible
$ git commit -a -m "ansible and keys"
$ git push
.
~~~