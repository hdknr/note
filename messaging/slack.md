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

### コマンド送信

- debug(10) で送信

~~~bash
$ export SLACK_INCOMING_WEB_HOOK=https://hooks.slack.com/services/T03fdadJ9/BfdadKGFM/hfdadv4fdadljVfdad6fdadK
$ slackpy -c  '#general' -m "こんにちは" -l 10
True
~~~
