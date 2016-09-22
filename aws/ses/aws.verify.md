## SES準備

- IAM でユーザーを作成
- 管理グループに入れるなどSESの権限を与える

## Service

- ses.Serviceにクレデンシャル設定

## Source

- ses.Service に対して、 ses.Source を作成
- 作成した ses.SourceをVerify
- メールボックスにAWSからメールが届くので、リンクをクリックしてベリファイ完了

## 受信先

- デフォルトでSESがサンドボックモードなので、送り先のメアドもベリファイが必要

~~~bash
$ python manage.py flierses verify_address 3 gmail@hdknr.com
~~~

## テスト送信




~~~
BotoServerError: 403 Forbidden
<ErrorResponse xmlns="http://ses.amazonaws.com/doc/2010-12-01/">
  <Error>
    <Type>Sender</Type>
    <Code>AccessDenied</Code>
    <Message>User: arn:aws:iam::764877781180:user/ses-hdknr is not authorized to perform: ses:VerifyEmailAddress</Message>
  </Error>
  <RequestId>bbdef64a-73cd-11e6-b413-7576da36bc5b</RequestId>
</ErrorResponse>
~~~
