# ルールグループ 

- Web ACL に追加できる再利用可能なルールのセット(Web ACLから利用可能なACL) (つまり、Web ACLもルールグループ)


以下のタイプのルールステートメントは参照できない:

- ルールグループの参照ステートメント
- レートベースのルールステートメント


ルールグループにはデフォルトのアクションがない:

- それぞれの ルール/ルールグループで アクションを定義する

## 例

`complex` ルールグループを定義:

~~~tf
resource "aws_wafv2_rule_group" "complex" {
  capacity = 10
  name     = "site-prod-waf-rule-group-complex"
  scope    = "CLOUDFRONT"

  rule {
    name     = "site-prod-waf-rule-group-complex-rule-1"
    priority = 1

    action {
      count {}
    }

    statement {
      ip_set_reference_statement {
        arn = aws_wafv2_ip_set.whitelist.arn
      }
    }

    visibility_config {
      # ...
    }
  }

  visibility_config {
    # ...
  }
}
~~~


Web ACLのルールとして採用:

~~~tf
resource "aws_wafv2_web_acl" "edge" {
  name  = "site-prod-waf-acl-edge"
  scope = "CLOUDFRONT"

  default_action {
    allow {}
  }

  rule {
    name     = "site-prod-waf-acl-edge-rule-1"
    priority = 1

    override_action {
      count {}
    }

    statement {
      rule_group_reference_statement {
        arn = aws_wafv2_rule_group.complex.arn
      }
    }

    visibility_config {
      # ....
    }
  }

  visibility_config {
    # ...
  }
}
~~~



## 資料

- [AWS::WAFv2::RuleGroup](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html)
- [ルールグループ](https://docs.aws.amazon.com/ja_jp/waf/latest/developerguide/waf-rule-groups.html)
