# Postfix SASL

- http://www.postfix-jp.info/trans-2.1/jhtml/SASL_README.html

- [RFC 2554 - SMTP Service Extension for Authentication](http://www.faqs.org/rfcs/rfc2554.html)


## 1. Unixユーザ-(/etc/passwd) を使う


### 1-1. main.cf:

- SASLの有効化(smtpd_sasl_auth_enable)
- SASLのパス(Ubuntu:/etc/postfix/sasl/smtpd.conf)の設定(smtpd_sasl_path)(デフォルトで `smtpd`になっている) 
- smtpd_sasl_local_domain  を指定しない(しなくてよい)
- Outlookなど対応(broken_sasl_auth_clients)

~~~ini
smtpd_sasl_auth_enable = yes
smtpd_recipient_restrictions = permit_sasl_authenticated
broken_sasl_auth_clients = yes
smtpd_sasl_path = smtpd
~~~

### 1.2. SALS設定 (Ubuntu:/etc/postfix/sasl/smtpd.conf) 

- `saslauthd` に問い合わせる
- 平文認証を許す(平文がsaslauthdに渡る)

~~~conf
pwcheck_method: saslauthd
mech_list: PLAIN LOGIN
~~~

### 1.3 saslauthdの設定(Ubuntu: /etc/default/saslauthd)

- デーモンを起動する(START=Yes)
- それ以外はOSのデフォルト(`pam` を使う)

~~~ini
START=yes
DESC="SASL Authentication Daemon"
NAME="saslauthd"
MECHANISMS="pam"
MECH_OPTIONS=""
THREADS=5
OPTIONS="-c -m /var/run/saslauthd"
~~~

- システム起動時に `saslauthd` を起動させること



## 2  /etc/sasldb2 を使う 

(うまくいってない...)

### SASLの有効化

~~~ini
smtpd_sasl_auth_enable = yes
~~~

### 認証されたクライアントによるメールのリレーを許可

~~~ini
smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
~~~

### SMTP認証するlocal domainの指定

~~~ini
smtpd_sasl_local_domain = $mydomain
~~~
myoriginの設定とsaslpasswdの設定時のmydomainの設定の3個所が同一でないとエラー

#### saslライブラリ指定

~~~ini
smtpd_sasl_type = cyrus             # デフォルト
### SMTP認証するlocal domainの指定
smtpd_sasl_path = smtpd
~~~

パスは実装依存です。

- ubuntu : /etc/postfix/sasl/smtpd.conf


## [sasldb plugin](http://www.postfix.org/SASL_README.html#auxprop_sasldb)

/etc/sasl2/smtpd.conf:

~~~
pwcheck_method: auxprop
auxprop_plugin: sasldb
mech_list: PLAIN LOGIN CRAM-MD5 DIGEST-MD5 NTLM
~~~

(`mech_list`は環境依存で変更)

### `auxprop` プラグイン

- /etc/sasldb2 ( Cyrus SASLスキーマの Berkeley DB) を直接参照する
- パスワードは平文で入っている 
- ファイル権限:  `r+x` を postfix ユーザーに与えるか、 `postfix` のグループだけに与える


### saslpasswd2コマンド


~~~bash
% saslpasswd2 -c -u example.com username
Password:
Again (for verification):
This command creates an account username@example.com.
~~~
ログイン名は  username@example.com にすること!

Postfix `mydomain` value を使うには:

~~~bash
% saslpasswd2 -c -u `postconf -h mydomain` username
Password:
Again (for verification):
~~~


### sasldblistusers2 コマンド

~~~bash
% sasldblistusers2
username1@example.com: password1
username2@example.com: password2
~~~ 
