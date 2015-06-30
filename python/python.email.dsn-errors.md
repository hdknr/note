## DSNメール

- email.message.Message

~~~python
>>> from email import message_from_string 
>>> m = message_from_string(raw_message_text)                                           
~~~

- マルチパートである

~~~ python
>>> m.is_multipart()
True
~~~

- ペイロードが複数存在する

~~~ python
>>> len(m.get_payload())
3
>>> type(m.get_payload())
<type 'list'>
~~~

- messasge/delivery-status を含んでいる
- [人間が読めるテキストエラーメッセージ, DSN, オリジナルメッセージ]

~~~ python
>>> [p.get_content_type() for p in m.get_payload()]
['text/plain', 'message/delivery-status', 'message/rfc822']
~~~

### エラーメッセージ(0)

~~~python
>>> print m.get_payload()[0]
From nobody Mon Jun 22 10:11:49 2015
Content-Description: Notification
Content-Type: text/plain; charset=us-ascii

This is the mail system at host ip-10-150-226-188.ap-northeast-1.compute.internal.

I'm sorry to have to inform you that your message could not
be delivered to one or more recipients. It's attached below.

For further assistance, please send mail to postmaster.

If you do so, please include this problem report. You can
delete your own text from the attached returned message.

                   The mail system

<user-not-found@hdknr.com>: host aspmx.l.google.com[74.125.204.26] said:
    550-5.1.1 The email account that you tried to reach does not exist. Please
    try 550-5.1.1 double-checking the recipient's email address for typos or
    550-5.1.1 unnecessary spaces. Learn more at 550 5.1.1
    https://support.google.com/mail/answer/6596 s1si361011pdr.203 - gsmtp (in
    reply to RCPT TO command)
~~~
	
### DSN(1)

~~~
>>> for k, v in m.get_payload()[1].items():
...     print k, " : ", v
... 
Content-Description  :  Delivery report
Content-Type  :  message/delivery-status
~~~

~~~
>>> m.get_payload(1).get_payload()
[<email.message.Message instance at 0x7f89eb214ea8>, <email.message.Message instance at 0x7f89eb214f38>]
>>> m.get_payload()[1].get_payload()
[<email.message.Message instance at 0x7f89eb214ea8>, <email.message.Message instance at 0x7f89eb214f38>]
~~~	

~~~
>>> for k, v in m.get_payload(1).get_payload()[0].items():
...     print k , "===>" , v
... 
Reporting-MTA ===> dns; ip-10-150-226-188.ap-northeast-1.compute.internal
X-Postfix-Queue-ID ===> B7CD71A393
X-Postfix-Sender ===> rfc822; test-1-3@test.myservice.net
Arrival-Date ===> Sun, 21 Jun 2015 18:44:54 +0900 (JST)
~~~

~~~
>>> for k, v in m.get_payload(1).get_payload()[1].items():
...     print k , "===>" , v
... 
Final-Recipient ===> rfc822; user-not-found@hdknr.com
Original-Recipient ===> rfc822;user-not-found@hdknr.com
Action ===> failed
Status ===> 5.1.1
Remote-MTA ===> dns; aspmx.l.google.com
Diagnostic-Code ===> smtp; 550-5.1.1 The email account that you tried to reach does
    not exist. Please try 550-5.1.1 double-checking the recipient's email
    address for typos or 550-5.1.1 unnecessary spaces. Learn more at 550 5.1.1
    https://support.google.com/mail/answer/6596 s1si361011pdr.203 - gsmtp
~~~

#### DSN

- [RFC3464](https://tools.ietf.org/html/rfc3464#page-7)

~~~
A DSN is a MIME message with a top-level content-type of
multipart/report (defined in [REPORT]).  When a multipart/report
content is used to transmit a DSN:

(a) The report-type parameter of the multipart/report content is
    "delivery-status".

(b) The first component of the multipart/report contains a human-
    readable explanation of the DSN, as described in [REPORT].

(c) The second component of the multipart/report is of content-type
    message/delivery-status, described in section 2.1 of this
    document.

(d) If the original message or a portion of the message is to be
    returned to the sender, it appears as the third component of the
    multipart/report.
~~~    

### オリジナルメッセージ(2)

~~~
>>> m.get_payload(2).get_payload()[0].get_payload()
'44OG44K544OI44Oh44O844Or\n'
~~~    


    