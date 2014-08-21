SPNEGO:curlで確認

/etc/krb5.conf

	[libdefaults]
        default_realm = OPENID.LOCAL

	[realms]
        OPENID.LOCAL = {
                kdc = windomain.openid.local
                admin_server = windomain.openid.local
        }


シェルでKerberos TGT(ticket-granting ticket)を取得:

    $ kinit Administrator
    
    Password for Administrator@OPENID.LOCAL: パスワード

TGTキャッシュ:

    $ klist

    Ticket cache: FILE:/tmp/krb5cc_1000
    Default principal: Administrator@OPENID.LOCAL

    Valid starting       Expires              Service principal
    2014-07-22T04:41:12  2014-07-22T14:41:12  krbtgt/OPENID.LOCAL@OPENID.LOCAL
        renew until 2014-07-23T04:41:08

        

オプション指定でcurlでアクセスできる:

	$ curl -I --negotiate -u: http://ubuntu.openid.local/i/info.php -v
    

トレース

    * Hostname was NOT found in DNS cach
    * Connected to ubuntu.openid.local (192.168.1.70) port 80 (#0
    > HEAD /i/info.php HTTP/1.1
    > User-Agent: curl/7.35.0
    > Host: ubuntu.openid.local
    > Accept: */*
    > 
    < HTTP/1.1 401 Unauthorized
    < Date: Mon, 21 Jul 2014 19:47:28 GMT
    * Server Apache/2.4.7 (Ubuntu) is not blackliste
    < Server: Apache/2.4.7 (Ubuntu)
    < WWW-Authenticate: Negotiate
    < Content-Type: text/html; charset=iso-8859-1
        
        
        
    * Connection #0 to host ubuntu.openid.local left intac
    * Issue another request to this URL: 'http://ubuntu.openid.local/i/info.php
    * Found bundle for host ubuntu.openid.local: 0x250a86
    * Re-using existing connection! (#0) with host ubuntu.openid.loca
    * Connected to ubuntu.openid.local (192.168.1.70) port 80 (#0
    * Server auth using GSS-Negotiate with user '
    > HEAD /i/info.php HTTP/1.1
    > Authorization: Negotiate YIIFngYJKoZIhvcSAQICAQBuggWNMIIFiaADAgEFoQ.....(省略)...HmXgPLE=
    > User-Agent: curl/7.35.0
    > Host: ubuntu.openid.local
    > Accept: */*
    > 
    < HTTP/1.1 200 OK
    < Date: Mon, 21 Jul 2014 19:47:28 GMT
    * Server Apache/2.4.7 (Ubuntu) is not blackliste
    < Server: Apache/2.4.7 (Ubuntu)
    < WWW-Authenticate: Negotiate YIGVBgkqhkiG9xIBAgICAG+BhTCBgqADAgEFoQMCAQ+idjB0oAMCAReibQRr2ETxT7sk/FHPLBqpARkq9LjtneuS4FUeCg9jEHv5zGylQjgzmv/xqaWlqUJ3U/hHavXX9OCQeARAF8GiihrmYxnVwZ3jXGbztQkTVLBdHGBxA3J1lh6DbsLLGtiqmg2IV/Brk15Wyynpjdc=
    < X-Powered-By: PHP/5.5.9-1ubuntu4.3
    < Content-Type: text/html
    * Connection #0 to host ubuntu.openid.local left intac
    

ユーザー名:

    $ curl --negotiate -u: http://ubuntu.openid.local/i/info.php | grep REMOTE_USER
    
    <tr><td class="e">REMOTE_USER </td><td class="v">Administrator@OPENID.LOCAL </td></tr>
    <tr><td class="e">_SERVER["REMOTE_USER"]</td><td class="v">Administrator@OPENID.LOCAL</td></tr>

        
