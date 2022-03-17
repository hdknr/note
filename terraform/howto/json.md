# JSONの利用

- IAMポリシーや、 ECRのタスク定義で JSONが必要な場合

JSONの指定方法:

- `file`(ファイル外だし)
- `templatefile`(ファイル外だし(動的な値が必要な場合))
- ヒアドキュメント(`<<EOT ..json.. EOT`)を使う
- `jsonencode`関数を使う
- `iam_policy_document`(専用のData Source)を使う


ファイル外だし:

~~~tf
resource "aws_iam_policy" "file" {
  name = "file"
  policy = file("./ddb-allow-policy.json")
}
~~~

`templdatefile`:

~~~tf
resource "aws_iam_policy" "templatefile" {
  policy = templatefile(
    "./ddb-allow-policy-with-templatefile.json",
    {
      region     = data.aws_region.current.id,
      account_id = data.aws_caller_identity.current.account_id,
      table_name = aws_dynamodb_table.book.name
    }
  )
}
~~~ 

ヒアドキュメント:

~~~tf
resource "aws_iam_policy" "heredoc" {
  policy = <<EOT
{
  "Version": "2012-10-17",
  "Statement": {
    .... // 
  },
  "//": "コメントは書けます"
}
EOT
}
~~~


`jsonencode`:

~~~tf
resource "aws_iam_policy" "jsonencode" {
  policy = jsonencode({
    "Statement" = {
      "Effect"   = "Allow"
      "Action"   = "dynamodb:*"
      "Resource" = "${aws_dynamodb_table.book.arn}"
    }
  })
}
~~~

`aws_iam_policy_document`:

~~~tf
data "aws_iam_policy_document" "allow_ddb" {
  statement {
    actions = [
      "dynamodb:*"
    ]
    resources = [
      aws_dynamodb_table.book.arn
    ]
  }
}

resource "aws_iam_policy" "datasource" {
  ...
  policy = data.aws_iam_policy_document.allow_ddb.json
}
~~~

## 資料

[TerraformでIAM Policyを書く方法5つ](https://dev.classmethod.jp/articles/writing-iam-policy-with-terraform/):