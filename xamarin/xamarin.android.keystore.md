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

$ export KEY_NANE=apps
$ export KEY_STORE=apps
$ keytool -genkey -v -keystore $KEY_STORE.keystore -alias $KEY_NAME -keyalg RSA -keysize 2048 -validity 10000
~~~

## 一覧(SHA1-1)

~~~bash
$ keytool -list -keystore $KEY_STORE.keystore
Picked up _JAVA_OPTIONS: -Dfile.encoding=UTF-8
キーストアのパスワードを入力してください:  

キーストアのタイプ: JKS
キーストアのプロバイダ: SUN

キーストアには 1 エントリが含まれます。

apps, 2016/01/06, PrivateKeyEntry,
証明書のフィンガープリント (MD5): 60:BD:8A:31:B7:74:44:7F:A0:DA:17:1D:BB:3C:55:B3
~~~

## パッケージ名

~~~bash
$ alias XJ='python -c "import xmltodict, json, sys; print json.dumps(xmltodict.parse(sys.stdin));"'
~~~

~~~bash
$ cat ../Properties/AndroidManifest.xml | XJ | jq '.manifest["@package"]' -r
jp.lafoglig.push.pushnotification
~~~
