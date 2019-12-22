# CloudFront + Wordpress

- [CloudFront対応のWordPress、Host設定でELB直接続も可能な環境を構築してみた](https://dev.classmethod.jp/cloud/aws/cloudfront-wordpress-cfn/)
- [WordPressサイトをCloudFrontで配信する](https://qiita.com/Ichiro_Tsuji/items/38592e737257cb45ca13)

## TODO

### 1. サーバーのキャッシュ制御を停止する

- CloudFront に任せるため
- [Nginx Cache Controller：Nginxのキャッシュをコントロールできる](https://www.hiskip.com/wp/plugin/site-manage/site-acceleration/cache/nginx/11432.html) とか

### 2. ディストリビューション作成

| **項目**  |   **値**          |
| :------- | :---------------- |
| `Origin Domain Name`      |  `test-cdn.debug.spin-dd.com` など(EC2, ELBを刺すネーム) |
| `Origin ID`               |  `cdn.test-cdn.debug.spin-dd.com` など         |
| `Allowed HTTP Methods`    |  `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE` を選択 |
| `Object Caching`          |  `Customize` を選択                                    |
| `Minimum TTL`             |  `300` とか                                           |
| `Maximum TTL`             |  `300` とか                                           |
| `Default TTL`             |  `300` とか                                           |
| `Forward Cookie`          |  `ALL` を選択                                         |
| `Query String Forwarding and Caching` |  `Forward all, cache based on all` を選択 |
| `Alternate Domain Names (CNAMEs)`     |  実際のドメイン名: `test.debug.spin-dd.com` など (設定すると `SSL Certificate` のドメイン名に一致する必要がある) |
| `SSL Certificate`                     | 選択する (`us-east-1` のACMから選ぶ)              |

### 3. ドメイン名設定

### 4. Wordpress用設定変更

- ログイン時のCookieエラー が起きたら対応
- wp-adminをキャッシュさせない
