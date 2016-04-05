## Python logging

- [15.7. logging — Python 用ロギング機能](http://docs.python.jp/2/library/logging.html)
- [16.8. logging.handlers — ロギングハンドラ](http://docs.python.jp/3/library/logging.handlers.html)
- [Python の logging 力を高める](http://momijiame.tumblr.com/post/41503983502/python-%E3%81%AE-logging-%E5%8A%9B%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B)

### logging.exception()

- [logging.exception()](http://www.alexconrad.org/2013/02/loggingexception.html)

## handlers

- [How to write custom python logging handler?](http://stackoverflow.com/questions/3118059/how-to-write-custom-python-logging-handler)

## syslog

- [How to setup SysLogHandler with Django 1.3 logging dictionary configuration](http://stackoverflow.com/questions/6205254/how-to-setup-sysloghandler-with-django-1-3-logging-dictionary-configuration)

~~~py
'handlers': {
  'syslog':{
        'level':'DEBUG',
        'class': 'logging.handlers.SysLogHandler',
        'formatter': 'verbose',
        'facility': 'local1',
        'address': '/dev/log',
    },
}
~~~

## Tracking Application
- [bashu/django-tracking](https://github.com/bashu/django-tracking)
- [Google Analytics](http://www.google.com/analytics/)
- [piwik/piwik](https://github.com/piwik/piwik) (Google Analytics Alternative)
- [djangoのloggerの(最低限の)使い方](http://qiita.com/sakamossan/items/a98b949738028ad39a6b)

## raven

- [reave to Django Sentry](https://docs.getsentry.com/hosted/clients/python/integrations/django/)
- [raven/handlers/logging.py](https://github.com/getsentry/raven-python/blob/master/raven/handlers/logging.py)

## Slack

- [django-slack](http://django-slack.readthedocs.org/)
- [AWS Lambda Function (Python) から Slack へ 簡単通知](http://qiita.com/iktakahiro/items/b3de0474b81edb115655)
- [非エンジニアでもできるSlackbotの追加方法
](http://qiita.com/yukihirai0505/items/b74425cb70dd7c045219)

## SNS

- [dreipol/django-scarface:  Send push notifications to mobile devices using Amazon SNS](https://github.com/dreipol/django-scarface)
