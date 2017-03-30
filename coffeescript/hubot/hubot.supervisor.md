hubot: slackbot を supervisord で動かす

- [Running Hubot in Production](http://www.forest-technologies.co.uk/blog/running-hubot-in-production)

- /etc/supervisord/conf.d/slackbot.conf

~~~ini
[program:slackbot]
directory=/home/system/projects/slackbot
user=system
command=/home/system/projects/slackbot/bin/hubot --adapter slack
autostart=true
autorestart=true
stdout_logfile=syslog
stderr_logfile=syslog
numprocs=1
startsecs=10
stopwaitsecs = 600
killasgroup=true    
environment=
   PATH="/home/system/.anyenv/envs/ndenv/shims:%(ENV_PATH)s",
   HUBOT_SLACK_TOKEN="xoxb-999999999-aaaaaaaaaaaaaa",
   HUBOT_CHATWORK_ROOMS="C1WS6EUA4",
~~~

~~~bash
$ sudo supervisorctl update
$ sudo supervisorctl status
slackbot                         RUNNING    pid 16715, uptime 0:04:25
~~~
