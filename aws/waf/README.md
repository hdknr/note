# AWS: WAF(Web Application Firewall)

- [AWS WAF（Web アプリケーションファイアーウォール） AWS](https://aws.amazon.com/jp/waf/)
- [WAF（Web アプリケーションファイアウォール）とは？- AWS](https://aws.amazon.com/jp/waf/what-is-waf/)
- [AWS WAFを使って接続できるIPアドレスを制限してみた  DevelopersIO](https://dev.classmethod.jp/cloud/aws/aws-waf-ip-block/)
- [[素朴な手順]Cloudfrontに対してAWS WAFで地域制限をかけつつ特定IPからアクセス許可を入れてみました  DevelopersIO](https://dev.classmethod.jp/cloud/waf-cloudfront-geographic-match-and-ip-match/)

[機能](https://aws.amazon.com/jp/waf/what-is-waf/):

- アプリケーション脆弱性の保護: SQL インジェクション、クロスサイトスクリプティングのルール, OWASP Top10 などの脅威から Web サイトを守るためのテンプレート
- L7 層の DDoS 対策: レートベースルール(一定期間のリクエスト数の閾値/マッチ条件), AWS Shield Advanced(有料)
- ボットアクセスやコンテンツの不正利用対策: CloudFront のログ解析, API を使ったハニーポットなどの設置
- IP レピュテーションリストのインポート(IPブラックリスト): Tor出口ノードIP, Spamhaus, Proofpoint Emerging Threat IP list

CloudFront:

- [AWS WAF での Amazon CloudFront 機能の使用方法 - AWS WAF、AWS Firewall Manager、および AWS Shield アドバンスド](https://docs.aws.amazon.com/ja_jp/waf/latest/developerguide/cloudfront-features.html)
- [AWS WAFを使うためシステムにCloudFrontを導入した時の注意点まとめ ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/setup-amazon-waf-and-cloudfront/)

ALB:

- [AWS WAFがALB(Application Load Balancer)で利用出来るようになりました ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/aws-waf-alb-support/)

OWASP Top10:

- [ウェブセキュリティで注目が高まる「OWASP Top10」 - ZDNet Japan](https://japan.zdnet.com/article/35116378/)

    A1：2017：インジェクション
    A2：2017：認証の不備
    A3：2017：機微な情報の露出
    A4：2017：XML外部エンティティ参照（XXE）
    A5：2017：アクセス制御の不備
    A6：2017：不適切なセキュリティ設定
    A7：2017：クロスサイトスクリプティング（XSS）
    A8：2017：安全でないデシリアライゼーション
    A9：2017：既知の脆弱性のあるコンポーネントの使用
    A10：2017：不十分なロギングとモニタリング

AWS Shield Advanced:

- Standard は AWS 標準で付いている
- [AWS Shield (マネージド型の DDoS 保護) - AWS](https://aws.amazon.com/jp/shield/)
- [料金は高額です](https://aws.amazon.com/jp/shield/pricing/)

Tor exit node list:

- 出口ノードは実際にアクセスするサーバとの通信を行うため、このipを規制することで、Torを利用した直接のアクセスを制限することができます。
- https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1
- https://check.torproject.org/exit-addresses
- [Torについて調べてみた - Qiita](https://qiita.com/totatoti/items/d230dd0c754826f1b68e)

Spamhouse:

- https://www.spamhaus.org/
- [[AWS][EIP]汚れたIPじゃないかspamhausでチェックする - Qiita](https://qiita.com/imura81gt/items/4464c388d235bff1bb41)
- https://github.com/perusio/nginx-spamhaus-drop

Proofpoint Emerging Threats(ET):

- https://www.proofpoint.com/jp/products/et-intelligence
- https://ipcheck.proofpoint.com/

