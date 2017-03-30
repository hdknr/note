## slackの準備

- `+ Add an app or custom integration` -> https://{{ your team}}.slack.com/apps
- HubotをInstall: https://{{ your team }}.slack.com/apps/A0F7XDU93-hubot
- 名前を指定してbotを作成する(`ictactserver`)
- このbotさんをチャネルに invite して参加させる

## HUBOT_SLACK_TOKEN

- slackのhubot設定からコピーしてきて設定する

~~~bash
$ echo $HUBOT_SLACK_TOKEN
ioib-7515010g8995-iw0sd8hPhXv9bTgWzL1PZeBj
~~~

##  HUBOT_CHATWORK_ROOMS

- https://api.slack.com/methods/channels.list/test
- 送信するとJSONが帰るので、 目的のチャネルの `id` を取得する
- トークンは作っておくこと( https://api.slack.com/docs/oauth-test-tokens )

~~~bash
$ echo $HUBOT_CHATWORK_ROOMS                                                                                                   
DEGEJDKGQS
~~~

## サンプル:時刻報告報告スクリプト

~~~bash
$ npm install -g cron                                                                                                          
~~~

~~~bash
$ cat scripts/notice.coffee
~~~

- 定期的に時刻を報告する

~~~coffee
cronJob = require('cron').CronJob
module.exports = (robot) ->
  new cronJob('0 * * * * *', () =>
    date     = new Date()
    hour     = date.getHours()
    minutes  = date.getMinutes()
    envelope = room: process.env.HUBOT_CHATWORK_ROOMS
    robot.send envelope, "時刻は #{hour}:#{minutes}です。"
  ).start()
~~~


## 実行

~~~bash
$ ./bin/hubot --adapter slack
[Thu Sep 01 2016 16:54:34 GMT+0900 (JST)] INFO Logged in as ictactserver of fanimalcore
[Thu Sep 01 2016 16:54:34 GMT+0900 (JST)] INFO Slack client now connected
[Thu Sep 01 2016 16:54:34 GMT+0900 (JST)] WARNING Loading scripts from hubot-scripts.json is deprecated and will be removed in 3.0 (https://github.com/github/hubot-scripts/issues/1113) in favor of packages for each script.

Your hubot-scripts.json is empty, so you just need to remove it.
[Thu Sep 01 2016 16:54:35 GMT+0900 (JST)] ERROR hubot-heroku-alive included, but missing HUBOT_HEROKU_KEEPALIVE_URL. `heroku config:set HUBOT_HEROKU_KEEPALIVE_URL=$(heroku apps:info -s  | grep web-url | cut -d= -f2)`
[Thu Sep 01 2016 16:54:35 GMT+0900 (JST)] INFO hubot-redis-brain: Using default redis on localhost:6379
[Thu Sep 01 2016 16:54:35 GMT+0900 (JST)] INFO hubot-redis-brain: Data for hubot brain retrieved from Redis
~~~

- TCP8080

~~~bash
$ lsof -c node | grep TCP
node    25219 admin   12u  IPv4 2458018      0t0     TCP *:http-alt (LISTEN)
~~~

## サンプル:`test` メッセージリレー

~~~bash
$ more scripts/backlog.coffee
~~~

~~~coffee
module.exports = (robot) ->
  robot.router.post "/change_later/:room", (req, res) ->
    { room } = req.params
    { body } = req

    message = 'test'
    try
      if message?
        robot.messageRoom room, message
        res.end "OK"
      else
        robot.messageRoom room, "Error."
        res.end "Error"
    catch error
      robot.send
      res.end "Error"
~~~      

- 起動後

~~~bash
$ curl http://localhost:8080/change_later/DEGEJDKGQS -X POST -F "key=value"
OK
~~~

- 送信された
