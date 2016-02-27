# mobileprovision

## XMLにする

~~~bash
security cms -D -i your_bundle.mobileprovision
~~~

- [UUID](http://qiita.com/mattak@github/items/dcb25ad7e12501d1525d)

~~~bash
$ xmllint <(security cms -D -i your.mobileprovision) --xpath '/plist/dict/key[text()="UUID"]/following-sibling::string[position()=1]/text()'
~~~

- Name

~~~bash
$ xmllint <(security cms -D -i your.mobileprovision) --xpath '/plist/dict/key[text()="Name"]/following-sibling::string[position()=1]/text()'
~~~

## XML

- PEM 形式で入っています

~~~XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>DeveloperCertificates</key>
    <array>
        <data>MIIFnTCCBIWgAwIBAg ....</data>
    </array>
</dict>
~~~          

~~~py
from bs4 import BeautifulSoup as Soup
from binascii import a2b_base64

soup = Soup(open('profile.xml'), "html.parser")
der = a2b_base64(soup.select('data')[0].text))
open("cert.der", "w").write(der)
~~~

~~~
$ openssl x509 -in cert.der -inform der -text -noout
~~

## ~/Library/MobileDevice/Provisioning Profiles

- XCodeでよみこむとここに格納される


# IPA

## チェックリスト

- パッケージ名 (unzip your.ipa)
- Info.plist
- アイコン画像(AppIcon*.png)

## Info.plist 抜き出し

- http://stackoverflow.com/questions/27053361/how-to-parse-the-info-plist-file-from-an-ipa

~~~bash
$ which plutil
/usr/bin/plutil
$ plutil -convert xml1 Info.plist  -o ~/Download/Info.plist.xml      # To XML
$ plutil -convert binary1 filename.plist    # to Binary
~~~~

# 証明書

- [aps_developer_identity.cer to p12 without having to export from Key Chain?](http://stackoverflow.com/questions/1453286/aps-developer-identity-cer-to-p12-without-having-to-export-from-key-chain)

~~~
$ openssl x509 -in aps_dev.cer -inform DER -noout -text
~~~

- PEM 化
~~~
$ openssl x509 -in aps_dev.cer -inform DER -out aps_dev.pem -outform PEM
~~~
