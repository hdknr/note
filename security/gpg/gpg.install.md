## macOS

~~~bash
$ brew install gpg
~~~


## 操作

~~~bash
$ gpg
gpg: ディレクトリ'/Users/hide/.gnupg'が作成されました
gpg: keybox'/Users/hide/.gnupg/pubring.kbx'が作成されました
~~~

.gnupg( [3. GnuPGの扱う内部データについて](http://no-passwd.net/fst-01-gnuk-handbook/gnupg-data.html)):

~~~
$ tree /Users/hide/.gnupg
/Users/hide/.gnupg
├── S.gpg-agent
├── S.gpg-agent.browser
├── S.gpg-agent.extra
├── S.gpg-agent.ssh
├── private-keys-v1.d
├── pubring.kbx                   # keybox
├── random_seed
└── trustdb.gpg

1 directory, 7 files
~~~

### 一覧

公開鍵一覧:
~~~bash
$ gpg --list-key

gpg: /Users/hide/.gnupg/trustdb.gpg: 信用データベースができました
~~~

秘密鍵:

~~~bash
$ gpg --list-secret-key
~~~

署名:

~~~bash
$ gpg --list-secret-key
~~~

フィンガープリント:

~~~bash
$ gpg --fingerprint
~~~
