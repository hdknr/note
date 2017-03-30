## hubot インストール

~~~bash
$ npm install -g yo generator-hubot
$ ndenv rehash
$ which yo
/home/admin/.anyenv/envs/ndenv/shims/yo
~~~


~~~
$ pwd
/home/admin/projects/slackbot

$ git init
Initialized empty Git repository in /home/admin/projects/slackbot/.git/

~~~

- ｀Bot name` は `hubot` にはできませんので注意！

~~~bash
$ yo hubot
                     _____________________________  
                    /                             \
   //\              |      Extracting input for    |
  ////\    _____    |   self-replication process   |
 //////\  /_____\   \                             /
 ======= |[^_/\_]|   /----------------------------  
  |   | _|___@@__|__                                
  +===+/  ///     \_\                               
   | |_\ /// HUBOT/\\                             
   |___/\//      /  \\                            
         \      /   +---+                            
          \____/    |   |                            
           | //|    +===+                            
            \//      |xx|                            

? Owner Hideki Nara <hdknr@ic-tact.co.jp>
? Bot name slackbot
? Description tact
? Bot adapter slack
   create bin/hubot
   create bin/hubot.cmd
   create Procfile
   create README.md
   create external-scripts.json
   create hubot-scripts.json
   create .gitignore
   create package.json
   create scripts/example.coffee
   create .editorconfig
                     _____________________________  
 _____              /                             \
 \    \             |   Self-replication process   |
 |    |    _____    |          complete...         |
 |__\\|   /_____\   \     Good luck with that.    /
   |//+  |[^_/\_]|   /----------------------------  
  |   | _|___@@__|__                                
  +===+/  ///     \_\                               
   | |_\ /// HUBOT/\\                             
   |___/\//      /  \\                            
         \      /   +---+                            
          \____/    |   |                            
           | //|    +===+                            
            \//      |xx|                            

~~~

## 実行

~~~bash

$ bin/hubot
slackbot> [Thu Sep 01 2016 16:38:15 GMT+0900 (JST)] WARNING Loading scripts from hubot-scripts.json is deprecated and will be removed in 3.0 (https://github.com/github/hubot-scripts/issues/1113) in favor of packages for each script.

Your hubot-scripts.json is empty, so you just need to remove it.
[Thu Sep 01 2016 16:38:15 GMT+0900 (JST)] ERROR hubot-heroku-alive included, but missing HUBOT_HEROKU_KEEPALIVE_URL. `heroku config:set HUBOT_HEROKU_KEEPALIVE_URL=$(heroku apps:info -s  | grep web-url | cut -d= -f2)`
[Thu Sep 01 2016 16:38:16 GMT+0900 (JST)] INFO hubot-redis-brain: Using default redis on localhost:6379
[Thu Sep 01 2016 16:38:16 GMT+0900 (JST)] INFO hubot-redis-brain: Initializing new data for hubot brain

slackbot>
~~~
