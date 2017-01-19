## 準備

- AWS アカウントを用意
- 送信ドメインでメールを受け取れるサービスを準備
- [SES で利用するアクセスキー](http://rriifftt.hatenablog.com/entry/2015/03/26/104806)

東京は使えません:

~~~
 SES is not available in アジアパシフィック (東京). Please select another region.
~~~

## リソース

- [Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)
- [API Reference](http://docs.aws.amazon.com/ses/latest/APIReference/Welcome.html)
- [awscli:ses](http://docs.aws.amazon.com/cli/latest/reference/ses/index.html)
- [bot: ses](http://boto.cloudhackers.com/en/latest/ref/ses.html)

### サンドボックス解除

- [Amazon SES サンドボックスの外への移動](https://docs.aws.amazon.com/ja_jp/ses/latest/DeveloperGuide/request-production-access.html)

## DNS : SPF/TXT

~~~
groups.rioja.jp. spf "v=spf1 include:amazonses.com +mx ~all"
groups.rioja.jp. TXT "v=spf1 include:amazonses.com +mx ~all"
~~~

## クイックスタート

[Amazon SES Quick Start](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/quick-start.html)

- Step 1. [Signing up for AWS](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sign-up-for-aws.html)
- Step 2: [Verify your email address](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html)
- Step 3: [Step 3: Send your first email](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/getting-started-send-from-console.html)

  - Toの送り先アドレスもVerifyする必要がある(Sandboxモード)

- Step 4: [Consider how you will handle bounces and complaints](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/best-practices-bounces-complaints.html)

- Step 5: [Move out of the Amazon SES sandbox](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html)


## SNS

- [Amazon SES Notifications Through Amazon SNS](
http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications-via-sns.html)
- [Amazon SESとSNSを利用してバウンスメールを自動的にハンドリングする](http://blog.shibayu36.org/entry/2015/08/27/101815)


## django-ses

- [django-ses](https://github.com/django-ses/django-ses)




## Send

~~~py
>>> from django.core.mail import EmailMultiAlternatives
>>> msg = EmailMultiAlternatives(subject='test2', body='test2', from_email=addr_from, to=[addr_to])
>>> from emailses.models import *
>>> s = Service.objects.first()
>>> s.key and s.secret and True
True
>>> s.send_raw_message(addr_from, addr_to, msg.message().as_string())
~~~

~~~
Delivered-To: hdknr@destination.com

Received: by 10.28.65.132 with SMTP id o126csp327440wma;
        Wed, 7 Oct 2015 21:57:14 -0700 (PDT)

X-Received: by 10.140.147.77 with SMTP id 74mr6119215qht.52.1444280234169;
        Wed, 07 Oct 2015 21:57:14 -0700 (PDT)

Return-Path: <0000000000000000-000000000000000000000000000000-000000@amazonses.com>

Received: from a8-28.smtp-out.amazonses.com (a8-28.smtp-out.amazonses.com. [54.240.8.28])
        by mx.google.com with ESMTPS id h37si37619225qge.58.2015.10.07.21.57.13
        for <hdknr@destination.com>
        (version=TLSv1 cipher=ECDHE-RSA-RC4-SHA bits=128/128);
        Wed, 07 Oct 2015 21:57:14 -0700 (PDT)

Received-SPF: pass (google.com: domain of 0000000000000000-000000000000000000000000000000-000000@amazonses.com designates 54.240.8.28 as permitted sender) client-ip=54.240.8.28;

Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of 0000000000000000-000000000000000000000000000000-000000@amazonses.com designates 54.240.8.28 as permitted sender) smtp.mailfrom=0000000000000000-000000000000000000000000000000-000000@amazonses.com;
       dkim=pass header.i=@amazonses.com

DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=xxxxxxxxxxxxxxx; d=amazonses.com; t=1444280233;
	h=MIME-Version:Content-Type:Content-Transfer-Encoding:Subject:From:To:Date:Message-ID:Feedback-ID;
	bh=xxxxxxxxxxx/xxxxxxxxxxxx+xxx/xxxxxx=;
	b=xxxx/xxxxxxxxxxxxxx+xxxxxx+xxxxxxxxxxx=

MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
Subject: test2
From: aws@magazine.com
To: hdknr@destination.com
Date: Thu, 8 Oct 2015 04:57:13 +0000
Message-ID: <0000015045cf6d18-ff4475d1-373b-4562-abe6-a050d2157e1d-000000@email.amazonses.com>
X-SES-Outgoing: 2015.10.08-54.240.8.28
Feedback-ID: 1.us-east-1.7ZSHU4tdE5+0pCbM8Zdfop3GEihj1a78zWZuofveMwA=:AmazonSES

test2
~~~


## From : 検証されていないアドレスに送ることはできません

~~~xml
SESAddressNotVerifiedError: SESAddressNotVerifiedError: 400 Email address is not verified.
<ErrorResponse xmlns="http://ses.amazonaws.com/doc/2010-12-01/">
  <Error>
    <Type>Sender</Type>
    <Code>MessageRejected</Code>
    <Message>Email address is not verified.</Message>
  </Error>
  <RequestId>d9667c37-6d7d-11e5-bd9a-8d6157fae000</RequestId>
</ErrorResponse>
~~~

## To: 本文のとsend_raw_emailのdestinationを合わせる必要があります

- 本文Toが正しいアドレスで、 destinationが不正な場合、正しいアドレスに送信されます


## テストアドレス

[5つのテストアドレス](http://bit.ly/1Np25An)

- Success : success@simulator.amazonses.com
無事に送信が成功するアドレス

- Bounce : bounce@simulator.amazonses.com
宛先不明で戻ってくるアドレス

- Out of the Office : ooto@simulator.amazonses.com
宛先のメールボックスには届くが、out-of-the-office(OOTO)で戻ってくるアドレス

- Complaint : complaint@simulator.amazonses.com
宛先のメールボックスには届くが、スパムとして報告される挙動を示すアドレス

- Address Blacklisted : blacklist@simulator.amazonses.com
SESでブラックリストに登録されているアドレス。(※SESで送信しようとすると怒られます。)


## Message ID

- [SES SMTP インターフェイスで Message-ID が上書きされる問題と対応](http://bit.ly/1hy90sy)
