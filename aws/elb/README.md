# ELB

- https://aws.amazon.com/jp/elasticloadbalancing/

## SSL の強制

- [How to force HTTPS behind AWS ELB](https://oanhnn.github.io/2016-02-29/how-to-force-https-behind-aws-elb.html)

```
server {
    listen 80 default_server;
    server_name "";
    location /health {
        access_log off;
        return  200;
    }
}
server {
    listen 80;
    server_name app.yourdomain.com;
    #....
    location / {
        if ($http_x_forwarded_proto != 'https') {
            return 301 https://$server_name$request_uri;
        }
        try_files $uri $uri/ /index.php?$args;
    }
    #....
}
```

## Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to

- [EC2 を停止して開始した時は ELB に再登録する](http://dev.classmethod.jp/cloud/aws/elb-re-register/)

## ACM Certificate: SSL の証明書

- [Request a Certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request.html)
- [Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate.html)
- [ACM SSL/TLS 証明書を Classic Load Balancer、Application Load Balancer、または Network Load Balancer と関連付ける方法を教えてください。 ](https://aws.amazon.com/jp/premiumsupport/knowledge-center/associate-acm-certificate-alb-nlb/)

ACM:

- ロードバランサーと同じリージョンで証明書を取得すること

送信メアド:

- administrator@your_domain
- hostmaster@your_domain
- postmaster@your_domain
- webmaster@your_domain
- admin@your_domain

## ヘルスチェック

nginx の`default_server` が正しく `200` を返すようにする:

- [ELB(https) + nginx でヘルスチェックがこける問題]https://qiita.com/ameyamashiro/items/63793a02d66b6c48ec09

## ホストヘッダー

アプリケーションロードバランサーは ELB の DNS 名をそのまま後ろに送ります。

- [How Elastic Load Balancing Works/Request Routing/HTTP Connection](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#request-routing)

  For Application Load Balancer,
  the host header contains the DNS name of the load balancer.

  For Classic Load Balancer,
  the host header contains the IP address of the load balancer node.

## その他

- [ELB を VPC 内に設置する際のサブネット設計の注意点](http://qiita.com/tetor/items/4c9e1aa58da2c5755452)
- [Amazon VPC でロードバランサーを使う](http://dev.classmethod.jp/cloud/amazon-vpc-elb/)
- [今更 VPC で 複数の AZ をまたいだ ELB を試す（1）](http://inokara.hateblo.jp/entry/2013/12/31/010647)
- [ELB + Postfix で Elastic な MTA(メール受信)システムの構築 – ELB Proxy Protocol Support の活用 ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/build-elastic-mta-by-proxy-protocol-enabled-elb-and-postfix/)

- [[ALB] CORS に対応したメンテナンスモード(503)を構築する](https://zenn.dev/taroshun32/articles/aws-alb-error-cors)
