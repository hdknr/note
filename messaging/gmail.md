- [Google Gmail APIでメールを取得する](http://qiita.com/ryurock/items/4b063372ede81780c3c8)
- [Google Apps ScriptでGmailをもっと自動化してみる](http://news.mynavi.jp/articles/2015/03/20/gmailauto/)
- [GASで監視メールをSlackに流す](http://tech.sanwasystem.com/entry/2015/04/28/143541)

## Google

- [Gmail API Overview](https://developers.google.com/gmail/api/guides/overview)


## Google App Script

### GmailApp

- [Class GmailApp](https://developers.google.com/apps-script/reference/gmail/gmail-app)
- [search(query)](https://developers.google.com/apps-script/reference/gmail/gmail-app#searchquery)


### GmailThread

- [Class GmailThread](https://developers.google.com/apps-script/reference/gmail/gmail-thread)

[最後のメッセージ](http://stackoverflow.com/questions/33754496/last-newest-mail-of-a-thread-gmail-script):

~~~js
var thread = threads[i];
var messages = thread.getMessages();
var message= messages[thread.getMessageCount()-1];
~~~
