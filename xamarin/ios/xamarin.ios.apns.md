# 事前準備

- APNS プロバイダ証明書
- Entrustルート証明書
- iOS Application プロビジョニングプロファイル
- APNSと通信するためのプロバイダ(サーバー)
- アプリで取得したデバイストークン


## キー + 証明書

- エクスポート

- PEMに変換

~~~bash
$ openssl pkcs12 -in apns.p12 -out apns.pem -nodes -clcerts
Enter Import Password:
MAC verified OK
~~~

# 参考

- [Push Notifications in iOS](https://developer.xamarin.com/guides/cross-platform/application_fundamentals/notifications/ios/remote_notifications_in_ios/)
- [iOSでプッシュ通知を実装する方法の超詳細まとめ(前編)](http://www.lancork.net/2013/08/how-to-ios-push-first/)
- [iOSでプッシュ通知を実装する方法の超詳細まとめ(後半)](http://www.lancork.net/2013/08/how-to-ios-push-second/)
- [How to create a Push Notification certificate in iPhone Developer Program Portal ](https://code.google.com/p/apns-php/wiki/CertificateCreation)
- [iOS デバイスへのプッシュ通知と node.js (プロバイダ編)](http://intink.blogspot.jp/2012/11/ios-nodejs.html)
