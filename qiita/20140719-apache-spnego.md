SPNEGO: apacheでActive Directoryログイン

# ADにユーザーを作成する
ドメイン名 =  openid.local

    C:\Windows\System32>dsquery user -samid %username%
    
    "CN=Administrator,CN=Users,DC=openid,DC=local"


apache@openid.local を作成


    @echo off

    SET USER=apache
    SET DOMAIN=DC=openid,DC=local
    SET PN="CN=%USER%,CN=Users,%DOMAIN%"
    SET PWD=twitter!@2014
    SET GROUP="CN=Domain Admins,CN=Users,%DOMAIN%"


    dsadd user %PN% -pwd %PWD% -mustchpwd no -pwdneverexpires yes -memberof %GROUP%

確認

    C:\Windows\System32>dsquery user -samid apache
    
    "CN=apache,CN=Users,DC=openid,DC=local"



# SPN(サービス プリンシパル名)とキータブを作る

キータブ = SPN + Key

作成スクリプト

    @echo off

    REM --- AD Domain 
    SET REALM=OPENID.LOCAL                      
    SET NTDOM=OPENID

    REM --- Server
    SET CNAME=ubuntu.openid.local
    SET SPN=HTTP/%CNAME%@%REALM%
    
    REM --- User
    SET SERVICE_USER=apache
    SET USER=%SERVICE_USER%@%NTDOM%

    REM --- Crypto
    SET CRYPTO=RC4-HMAC-NT
    REM --- Principal Type
    SET PTYPE=KRB5_NT_PRINCIPAL
    REM --- Keytab File
    SET OUT=%SERVICE_USER%.krb5.http.keytab

    ktpass -princ %SPN% -mapuser %USER%  -crypto %CRYPTO% -ptype %PTYPE% -out %OUT%  +rndPass

確認:

    C:> setspn -Q HTTP/*
    
    ドメイン DC=openid,DC=local を確認しています
    CN=apache,CN=Users,DC=openid,DC=local
            HTTP/ubuntu.openid.local               
    既存の SPN が見つかりました


パラメータ変えて作り直す時は削除する

    C:>setspn -d HTTP/ubuntu.openid.local apache
    
    CN=apache,CN=Users,DC=openid,DC=local の ServicePrincipalNames  
    の登録を解除しています
        HTTP/ubuntu.openid.local
    更新されたオブジェクト                

    
# mod_auth_kerb

Ubuntu:

    $ sudo apt-get install libapache2-mod-auth-kerb krb5-user -y

# /etc/krb5.conf


    [libdefaults]
        default_realm = OPENID.LOCAL
        
    [realms]
        OPENID.LOCAL = {
                kdc = windomain.openid.local
                admin_server = windomain.openid.local
        }
    [domain_realm]
        .openid.local = OPENID.LOCAL
        openid.local = OPENID.LOCAL
    
    
# keytabをUbuntuに設定

コピーして 400

    $ sudo cp apache.krb5.http.keytab  /etc
    $ sudo chown www-data:www-data /etc/apache.krb5.http.keytab 
    $ sudo chmod 400 /etc/apache.krb5.http.keytab     
 
内容:
    


    $ sudo ktutil list
    ktutil:

    ktutil:  rkt /etc/apache.krb5.http.keytab

    ktutil:  l
    slot KVNO Principal
    ---- ---- ---------------------------------------------------------------------
       1    4    HTTP/ubuntu.openid.local@OPENID.LOCAL


- あるいは

```bash

$ sudo -u www-data klist -k /etc/apache2/krb/abop.deb.keytab

Keytab name: FILE:/etc/apache2/krb/abop.deb.keytab
KVNO Principal
---- --------------------------------------------------------------------------
   3 HTTP/ubuntu.tact.local@TACT.LOCAL

```


# 初期化

~~~

    $ sudo -u www-data kinit -k -t /etc/apache.krb5.http.keytab HTTP/ubuntu.openid.local@OPENID.LOCAL

    $ sudo -u www-data klist -e

    Ticket cache: FILE:/tmp/krb5cc_33
    Default principal: HTTP/ubuntu.openid.local@OPENID.LOCAL

    Valid starting       Expires              Service principal
    2014-07-18T16:13:44  2014-07-19T02:13:44  krbtgt/OPENID.LOCAL@OPENID.LOCAL
        renew until 2014-07-19T16:13:44, Etype (skey, tkt): arcfour-hmac, aes256-cts-hmac-sha1-96

~~~

```bash

$ ls -al /tmp/k*


-rw------- 1 www-data www-data 1518 11月 13 19:14 /tmp/krb5cc_33

```

##  kinit: Permission denied while getting initial credentials

このエラーがでたらキータブファイルの権限がおかしいです。 chown(www-data), chmod (400) を正しく
   
## kdestroy: チケットキャッシュクリア

- 特定のチケットを指定してクリアできません

```bash

$ sudo -u www-data kdestroy

$ sudo -u www-data klist -e

klist: No credentials cache found (ticket cache FILE:/tmp/krb5cc_33)
```
    
# apache仮想サイト

ルートにSPNEGO(Negotiate)認証設定する

    <VirtualHost ubuntu.openid.local:80>

        ServerAdmin admin@i-c-i.jp
        ServerName  ubuntu.openid.local
        DocumentRoot /home/hdknr/apache/www

        LogLevel debug
        ErrorLog /home/hdknr/apache/logs/error.log
        CustomLog /home/hdknr/apache/logs/access.log combined

        <Location / >
        #Require all granted

        AuthType Kerberos
        AuthName "AD Auth for OPENID.LOCAL"

        KrbAuthRealms OPENID.LOCAL
        Krb5KeyTab /etc/apache.krb5.http.keytab
        KrbMethodNegotiate on
        KrbMethodK5Passwd off
        KrbServiceName Any

        require valid-user
        </Location>

    </VirtualHost>    
 
# 確認 
 
## User Agent 
 
### IEの設定

* ![ローカルイントラネットに仮想ホストを追加すること](https://lh4.googleusercontent.com/-cqikesub0Ng/U8m5Bek1QVI/AAAAAAAAAiU/eapCt7F52dk/w746-h512-no/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588+2014-07-19+9.16.20.png)    
* Windows 統合認証を有効にする


### Firefox

* about:config
* network.negotiate-auth.delegation-uris
* network.negotiate-auth.trusted-uris

![negotiate でURLを設定する](https://lh3.googleusercontent.com/-cATBYJ5g9Lo/U8m5cpO7MgI/AAAAAAAAAi4/r3DJl1JjlUY/w786-h321-no/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588+2014-07-19+9.18.32.png)

## phpinfo() のページにアクセスしてみる

* Active DirectoryにログインしたWindowsのデスクトップでアクセス
* パスワード入力なしでアクセスできる


errors.logのデバッグメッセージ

     AH01626: authorization result of <RequireAny>: denied (no authenticated user yet)
     kerb_authenticate_user entered with user (NULL) and auth_type Kerberos
     AH01626: authorization result of Require valid-user : denied (no authenticated user yet)
     AH01626: authorization result of <RequireAny>: denied (no authenticated user yet)
     kerb_authenticate_user entered with user (NULL) and auth_type Kerberos
     Verifying client data using KRB5 GSS-API with our SPNEGO lib
     Client didn't delegate us their credential
     GSS-API token of length 180 bytes will be sent back
     AH01626: authorization result of Require valid-user : granted
     AH01626: authorization result of <RequireAny>: granted


* `REMOTE_USER` に hide@OPENID.LOCAL で認証していることが表示されてる
* `AUTH_TYPE` に `Negotiate` で認証されていることが表示されている

     

# その他

## Unspecified GSS failure

```
[Thu Dec 04 10:05:24.479956 2014] [auth_kerb:error] [pid 34832] [client 192.168.10.220:58592] 
gss_accept_sec_context() failed: Unspecified GSS failure.  
Minor code may provide more information 
(, Ticket not yet valid), referer: http://ubuntu.tact.local/abrp/

```

これはLinuxの時刻が著しくWindowsと違っていたため。 ntpdate などで合わせる。
