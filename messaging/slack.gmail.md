## 特定のアドレスからのメールを１件だけ報告

- [GAS(google app script)で指定ラベルのGmailをslackに通知](https://gist.github.com/matsuyoro/c53d82017b2763633e5b)

~~~javascript

var postUrl = "https://hooks.slack.com/services/T1111111/B22222222/333333333333";
var postChannel = "#channel";

function myFunction() {
  procThreads(GmailApp.search('is:unread from:info@domain.com'));
  procThreads(GmailApp.search('is:unread from:poromo@domain.net'));
}

function procThreads(threads){
  if( threads.length < 1)
      return ;

  var count = Math.max(threads.length, 10);
  for(var i = 0; i < count; i++) {
    var lastDate = threads[i].getLastMessageDate();
    if( i == 0 ){
      var msg  = threads[i].getFirstMessageSubject() ;
      msg = msg + " " +  threads[i].getMessages()[0].getPlainBody();
      msg = msg + " " + threads[i].getPermalink();
      sendHttpPost(msg, "Gmail");
    }
    threads[i].markRead();        // 既読
    threads[i].moveToTrash();     // ゴミ箱行き
  }
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
