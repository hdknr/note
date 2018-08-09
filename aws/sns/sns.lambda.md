## コード

- `SLACK_WEBHOOK` 変数に webhook url を設定すること

~~~py 
def send_message_to_slack(text, *args, **kwargs):
    import os
    from urllib import request
    import json
    URL = os.environ['SLACK_WEBHOOK']

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request(
            URL, data=json_data.encode('ascii'),
            headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

if __name__ == '__main__':
    send_message_to_slack('hello')
~~~

## zip

- アップロード用のZipファイル

~~~bash
$ cd lambda_alert
$ zip -r lambda_alert.zip .
  adding: __init__.py (stored 0%)
  adding: README.md (stored 0%)
  adding: slack.py (deflated 40%)
~~~
