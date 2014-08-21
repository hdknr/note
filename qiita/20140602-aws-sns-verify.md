Amazon SNS: pycryptoでNotificationの署名を検証する


SNSのJSONのパラメータから[Signature Version 1](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.verify.signature.html)で定義された手順でパラメータをカノニカライズして文字列(signin input)を作ります。

```py

      NOTIFICATION_SIGNING_INPUT_KEY = [
          "Message",
          "MessageId",
          "Subject",
          "SubscribeURL",
          "Timestamp",
          "Token",
          "TopicArn",
          "Type",
      ]       
          
      NOTIFICATION_SIGNING_INPUT = lambda jobj:\
        "".join([
          "%s\n%s\n" % (k, jobj.get(k))
          for k in NOTIFICATION_SIGNING_INPUT_KEY
          if k in jobj
      ])

```

SNS サービスハンドラに検証メソッドを実装します:

```py

      import json
      import requests
              

      def verify_notification(self, notification):
          # Notification モデル message にSNSのJSONはいっています
          
          jobj = json.loads(notification.message)
          sinput = NOTIFICATION_SIGNING_INPUT(jobj)
  
          if not self.service.public_key:
              # Service オブジェクトがPEMを持っていなかったら取得します
              # 厳密にはSSL Certificate をチェックします
              res = requests.get(jobj['SigningCertURL'])
              self.service.public_key = res.text
              self.service.save()
  
          # 証明書、singing input , シグネチャーを pycryptoで署名検証します 
          return verify_pycrypto(
              self.service.public_key, sinput, jobj['Signature'])
```

検証ルーチン:

```py

      from Crypto.Signature import PKCS1_v1_5
      from Crypto.Hash import SHA
      from base64 import standard_b64decode

      def verify_pycrypto(pem, signing_input, b64signature):
            pub = import_pubkey_from_x509(pem)    # パブリックキーを抜く(下)
            verifier = PKCS1_v1_5.new(pub)        # PKCS 1.5 パディングサイナー
        
            sig = standard_b64decode(b64signature)
            if isinstance(signing_input, unicode):
                signing_input = signing_input.encode('utf8')

            dig = SHA.new(signing_input)
        
            return verifier.verify(dig, sig)
```            



指定されたPEMの証明書からパブリックキーを抜きます。なぜかRSA.importKey(pem) で書式エラーするので:



```py

      from Crypto.PublicKey import RSA
      from Crypto.Util.asn1 import DerSequence

      def import_pubkey_from_x509(pem):
            b64der = ''.join(pem.split('\n')[1:][:-2])
            cert = DerSequence() 
            cert.decode(b64decode(b64der))
                        
            tbs_certificate = DerSequence()
            tbs_certificate.decode(cert[0])
        
            subject_public_key_info = tbs_certificate[6]
        
            return RSA.importKey(subject_public_key_info)
  
```

ちなみに、 pyOpenSSLバージョン:

```py

      from OpenSSL.crypto import verify
      from OpenSSL import crypto

      def verify_openssl(pem, signing_input, b64signature):
          if isinstance(signing_input, unicode):
              signing_input = signing_input.encode('utf8')
          cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem)
          sig = b64decode(b64signature)
          return verify(cert, sig, signing_input, 'sha1') is None
```
