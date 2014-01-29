Date: 2013-11-19  12:00
Title: DjangoでApacheの基本認証IDを管理する
Type: post  
Excerpt:   


[django-auth-external](https://github.com/hdknr/django-auth-external) というしょぼいDjangoアプリでApacheの基本認証を管理するようにしてみました。

ユーザーの追加、パスワードの設定、グループ管理とか面倒くさいのでDjanog Admin UIでやるようにしました。 ユーザーをグループにいれれば、Apache の Require group {{グループ名}} でグループベースで認証できるようにした。

# mod_auth_external #

レポジトリ名にあるように最初は [mod_auth_external](https://code.google.com/p/mod-auth-external/)でやってみたけど、遅いので困った。スクリプト起動するからしょうがないですね。

DebianやCentOSのパッケージになっていないのもなんかあれですし。

# mod_wsgi 認証 #

[mod_wsgi](https://code.google.com/p/modwsgi/)にも認証の仕組みがあるのでそれも実装してみました。

WSGIAuthUserScript/WSGIAuthGroupScriptに引数をあたえられないので、VirtualenvでPython入れているとactivateするパスとDjangoのアプリのパスの２つをなんとかくふうして与えないといけないですね。

とりあえず、 $VIRTUAL_ENV/bin に スクリプトを置いて、そこにアプリケーションのパスを書いて対応。

Amazon Linux(CentOS)のyumで入れるmod_wsgiは Python 2.6なのでバージョン落とさないとですね。 Debian Wheezyは2.7です。

mod_auth_exernalよりは早いとはおもいますが、やはりもっさりですね。

# mod_auth_mysql #


[mod_auth_mysql](http://modauthmysql.sourceforge.net/) だとMySQL直なので、はやいとおもうのでこれもためしてみました。結果としてこれでいいかな。

## パスワードの制限 ##

この方式だとdjango.conrib.auth.models.User をちょく使えないです。
ので、別途テーブルを用意してそこにユーザー名とパスワードを入れる必要があります。

## パスワードの２重管理しない ##

[２重管理したくないので Admin UI でパスワードリセットしたらテーブルを更新するようにしました](https://github.com/hdknr/django-auth-external/blob/master/src/authx/models.py#L25)。

set_passwordメソッドを強制的にオーバーライドして、入力された生パスワードをインターセプトしてSHA1でパスワード管理テーブルにいれることにしました。データが存在しない時は作るようにした。SHA1以外の対応もいつかするでしょう。

## DebianとCentOSでApacheの設定名が異なる #

これは面倒くさい。/usr/share/doc の下のドキュメントをにらめっこする必要がある。

[設定サンプル](https://github.com/hdknr/django-auth-external/blob/master/apache/conf/httpd.conf)はDebianで動いているもの。

[CentOS](https://github.com/hdknr/django-auth-external/blob/master/apache/conf/centos.conf) の mod_auth_mysql の設定だけ別。
