# ステートメント


| 種類         | ステートメント                        | 内容                                                                   |
| ------------ | ------------------------------------- | ---------------------------------------------------------------------- |
| 定義ルール   | managed_rule_group_statement          | マネージドルールの評価。ネスト不可                                     |
| 定義ルール   | rule_group_reference_statement        | `WAFv2 Rule Group` / `aws_wafv2_rule_group` のルールを評価。ネスト不可 |
| パターン     | byte_match_statement                  | バイト列チェック                                                       |
| パターン     | label_match_statement                 | 文字列チェック                                                         |
| パターン     | regex_pattern_set_reference_statement | `aws_wafv2_regex_pattern_set` で定義された正規表現で評価               |
| パターン     | size_constraint_statement             | バイト長チェック(8192バイトまで)                                       |
| ネットワーク | geo_match_statement                   | カントリーコードの評価                                                 |
| ネットワーク | ip_set_reference_statement            | リクエスターネットワークアドレス 評価                                  |
| ネットワーク | rate_based_statement                  | リクエスターIPアドレスごとに５分間のリクエスト数で評価                 |
| 特殊         | sqli_match_statement                  | SQLインジェクション条件                                                |
| 特殊         | xss_match_statement                   | XSSを検出                                                              |
| 連結         | and_statement                         | 他の `statement` と `AND` で連結。 ネスト可能                          |
| 連結         | not_statement                         | 条件を否定する `statement` ネスト可能                                  |
| 連結         | or_statement                          | 他の `statement` と `OR` で連結。ネスト可能                            |


# 連結

( `正規表現ルール1` || `正規表現ルール2`) && ( ! `IPアドレスルール`)

~~~tf
resource "aws_wafv2_web_acl" "this" {
  default_action {
    allow {}
  }

  rule {

    statement {
      and_statement {
        statement { # AND対象
          or_statement {

            statement { # OR対象
              regex_pattern_set_reference_statement {
                # 正規表現パターン1
                # ....
              }
            }

            statement { # OR対象
              regex_pattern_set_reference_statement {
                # 正規表現パターン2
                # ...
              }
            }
        }

        statement { # AND対象
          not_statement {
            statement {
              ip_set_reference_statement {
                # IPアドレス条件
              }
            }
          }
        }

      }
    }

  }
}
~~~

## 資料

- [Resource: aws_wafv2_web_acl](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/wafv2_web_acl#byte-match-statement)
