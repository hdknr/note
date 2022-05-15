# ルール

- ルール名
- [ルールアクション](aws.waf.action.md)
- Web リクエストのラベル
- ルールステートメント

サンプル:

~~~tf
resource "aws_wafv2_web_acl" "this" {
  name = "site-proc-webacl-main"
  scope = "CLOUDFRONT"
  provider = aws.east

  default_action {
    allow {}
  }

  rule {
    name     = "site-prod-rule-1"
    priority = 5

    action {
      block {}
    }

    statement {
        # ....
    }

    visibility_config {
        # ....
    }
  }


  rule {
    name     = "site-prod-rule-2"
    priority = 6
    # ....
  }

  visibility_config {
      # ...
  }
}
~~~

## 資料

- [AWS WAF ルール](https://docs.aws.amazon.com/ja_jp/waf/latest/developerguide/waf-rules.html)
