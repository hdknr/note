# キーストア

## Xamarin

- [Finding your Keystore's MD5 or SHA1 Signature](http://developer.xamarin.com/guides/android/deployment,_testing,_and_metrics/MD5_SHA1)
- [Windows](http://developer.xamarin.com/guides/android/deployment,_testing,_and_metrics/MD5_SHA1/#Windows) (Debug)
- [OSX](http://developer.xamarin.com/guides/android/deployment,_testing,_and_metrics/MD5_SHA1/#OSX) (Debug)
- [Xamarin.Android のアプリケーションを APK にしてリリース
](http://www.xlsoft.com/jp/products/xamarin/publish_android.html)
- [Google Map API を使用するためのAPIキーを作成する](http://mattsudev.hatenablog.com/entry/2015/07/06/214407)
- [Xamarin.Android での Google Map(というか Play Service) 利用が、本家より簡単になった件](http://qiita.com/amay077/items/14191c808e9cac4eae2c)

## キーストア生成

キーツールの文字化け対処

~~~bash
$ export _JAVA_OPTIONS='-Dfile.encoding=UTF-8'
~~~

~~~bash

$ export KEY_NAME=apps
$ export KEY_STORE=apps
$ keytool -genkey -v -keystore $KEY_STORE.keystore -alias $KEY_NAME -keyalg RSA -keysize 2048 -validity 10000
~~~

## 一覧(SHA1-1)

~~~bash
$ keytool -v -list -keystore $KEY_STORE.keystore
Picked up _JAVA_OPTIONS: -Dfile.encoding=UTF-8
キーストアのパスワードを入力してください:  

キーストアのタイプ: JKS
キーストアのプロバイダ: SUN

キーストアには 1 エントリが含まれます。

別名: apps
作成日: 2016/01/08
エントリタイプ: PrivateKeyEntry
証明連鎖の長さ: 1
証明書[1]:
所有者: CN=nara, OU=lafoglia, O=lafoglia, L=tokyo, ST=tokyo, C=jp
発行者: CN=nara, OU=lafoglia, O=lafoglia, L=tokyo, ST=tokyo, C=jp
シリアル番号: 568fa2e7
有効期間の開始日: Fri Jan 08 20:52:07 JST 2016 終了日: Tue May 26 20:52:07 JST 2043
証明書のフィンガープリント:
         MD5:  E4:18:11:EE:3F:07:0E:C0:74:13:22:AC:8F:DD:75:E7
         SHA1: 9A:02:AE:21:3C:9B:38:33:96:07:FD:3B:E0:E1:8F:42:B5:61:6C:1B
         署名アルゴリズム名: SHA1withRSA
         バージョン: 3

*******************************************
*******************************************

~~~

## パッケージ名

~~~bash
$ alias XJ='python -c "import xmltodict, json, sys; print json.dumps(xmltodict.parse(sys.stdin));"'
~~~

~~~bash
$ cat ../Properties/AndroidManifest.xml | XJ | jq '.manifest["@package"]' -r
jp.lafoglig.push.pushnotification
~~~
