Date: 2013-08-30  10:00
Title: openssl:共有キーで暗号化
Type: post  
Excerpt:   



AES256で暗号化します :

    hdknr@wzy:/tmp$ date > date.txt 
    hdknr@wzy:/tmp$ openssl enc -e -aes256 -in date.txt -out date.enc -k mypassword
    hdknr@wzy:/tmp$ openssl enc -d -aes256 -in date.enc -k mypassword
    2013年  8月 30日 金曜日 10:13:26 JST