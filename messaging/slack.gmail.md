[gmail](gmail.md)

## 特定のアドレスからのメールを１件だけ報告

### 準備

 WebHook を追加する

- https://slack.com/apps/build
- "Make Custom Integration"
- "Incoming WebHooks"

情報をコピーしておく

- WebHook URL
- Channel

### Google App Script


- [GAS(google app script)で指定ラベルのGmailをslackに通知](https://gist.github.com/matsuyoro/c53d82017b2763633e5b)


- Goole Apps > スプレッドシート
- 追加
- "ツール" > "スクリプトエディタ"
- スクリプト編集

~~~javascript

var postUrl = "https://hooks.slack.com/services/T1111111/B22222222/333333333333";
var postChannel = "#channel";

function myFunction() {
  procThreads(GmailApp.search('is:unread from:info@domain.com'));
  procThreads(GmailApp.search('is:unread from:poromo@domain.net'));
}

function procThreads(threads){

  threads.forEach(function(thread, i, ar){
    var n = thread.getMessageCount();
    if( i < 1 && n > 0 ){
       var message = thread.getMessages()[n-1];

       var text = [
          message.getSubject(),
          message.getPlainBody() ,
          thread.getPermalink()].join("\n\n");

      sendHttpPost(text, "Gmail");
      thread.markRead();
    }
  });
}

function sendHttpPost(message, username)
{
  var jsonData = {
     "channel" : postChannel,
     "username" : username,
     "text" : message
  };
  var payload = JSON.stringify(jsonData);
  var options = {
    "method" : "post",
    "contentType" : "application/json",
    "payload" : payload
  };

  UrlFetchApp.fetch(postUrl, options);
}
~~~

### 定期実行

- スクリプトエディタより "現在のスクリプトのトリガー" (時計アイコン)
- 新しいトリガーを追加
- イベント: 時間主導型　で間隔をしていして定期実行トリガー


## 記事

- http://qiita.com/hokaccha/items/e41012cc3833ae9cbe13
