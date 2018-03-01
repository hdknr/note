## SSLの強制

- [How to force HTTPS behind AWS ELB](https://oanhnn.github.io/2016-02-29/how-to-force-https-behind-aws-elb.html)

~~~
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
~~~


## Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to

- [EC2を停止して開始した時はELBに再登録する](http://dev.classmethod.jp/cloud/aws/elb-re-register/)



## ACM Certificate: SSLの証明書

- [Request a Certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request.html)
- [Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate.html)

送信メアド:

- administrator@your_domain
- hostmaster@your_domain
- postmaster@your_domain
- webmaster@your_domain
- admin@your_domain


## ヘルスチェック

nginxの`default_server` が正しく `200` を返すようにする:

- [ELB(https) + nginx でヘルスチェックがこける問題]https://qiita.com/ameyamashiro/items/63793a02d66b6c48ec09


## その他

- [ELBをVPC内に設置する際のサブネット設計の注意点](http://qiita.com/tetor/items/4c9e1aa58da2c5755452)
- [Amazon VPCでロードバランサーを使う](http://dev.classmethod.jp/cloud/amazon-vpc-elb/)
- [今更 VPC で 複数の AZ をまたいだ ELB を試す（1）](http://inokara.hateblo.jp/entry/2013/12/31/010647)
