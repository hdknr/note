- http://mushikago.com/i/?p=6164
- http://www.jianfeice.com/ios-9-not-opening-instagram-app-with-url-scheme/
- https://chomado.com/note/tech/working-with-new-features-in-ios-9/

- https://riccardo-moschetti.org/2014/10/03/opening-a-mobile-app-from-a-link-the-xamarin-way-url-schemas/

- onetwopunch://」というURLスキームを呼び出せるように設定するには、
- Info.plistで「LSApplicationQueriesSchemes」をArray型で作成し、
- URLスキーム部分（「://」のない「onetwopunch」でいいみたい）をその配列に加えていく、ということです。カスタムスキームをここに設定することで特定のアプリだけを起動する、ということが可能になります。ここに指定がない場合やその対象となるアプリがインストールされていない場合は、.canOpenURL(url)がtrueを返しません。


- http://stackoverflow.com/questions/27068473/call-viewcontroller-method-from-appdelegate-after-url-scheme-openurl
