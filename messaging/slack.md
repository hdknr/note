## slackpy

- [iktakahiro/slackpy](https://github.com/iktakahiro/slackpy)

~~~ bash
$ pip install slackpy
Collecting slackpy
  Downloading slackpy-1.3.1.tar.gz
Requirement already satisfied (use --upgrade to upgrade): requests<3,>=2.8.0 in /home/vagrant/.anyenv/envs/pyenv/versions/2.7.10/lib/python2.7/site-packages (from slackpy)
Installing collected packages: slackpy
  Running setup.py install for slackpy ... done
Successfully installed slackpy-1.3.1
~~~

- [AWS Lambda Function (Python) から Slack へ 簡単通知](http://qiita.com/iktakahiro/items/b3de0474b81edb115655)

### コマンド送信

- debug(10) で送信

~~~bash
$ export SLACK_INCOMING_WEB_HOOK=https://hooks.slack.com/services/T03fdadJ9/BfdadKGFM/hfdadv4fdadljVfdad6fdadK
$ slackpy -c  '#general' -m "こんにちは" -l 10
True
~~~




## その他

- [loisaidasam/pyslack](https://github.com/loisaidasam/pyslack)
- [SlackのWebhook URL取得手順](http://qiita.com/vmmhypervisor/items/18c99624a84df8b31008)

~~~
https://slack.com/services/new/incoming-webhook
~~~
