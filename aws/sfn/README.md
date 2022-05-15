# Step Functions


## Terraform

ステートマシンを定義:

~~~tf
resource "aws_sfn_state_machine" "sfn" {
  name     = "${var.enviroment}-sfn"

  # ロール
  role_arn = "${aws_iam_role.sfn.arn}"

  # ソースコード
  definition = <<EOT
    .....
  EOT

  # ログ
  logging_configuration {
    log_destination = "${var.sfn_arn}"
    include_execution_data = true
    level                  = "ALL"
  }
}
~~~


ロール:


~~~tf
resource "aws_iam_role" "sfn" {
  name               = "${var.env}-sfn-role"
  assume_role_policy = "${data.aws_iam_policy_document.sfn.json}"
}

data "aws_iam_policy_document" "sfn" {
  statement {
    sid     = "SFNAssumeRolePolicy"
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals = {
      type        = "Service"
      identifiers = ["states.${var.region}.amazonaws.com"]      # Step Functionでステートマシンを利用
    }
  }
}
~~~


ポリシー追加(ステートマシンの中でlambdaを実行したい):

~~~tf
resource "aws_iam_policy_attachment" "sfn" {
  name       = "AWSLambdaRole"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaRole"
  roles      = ["${aws_iam_role.sfn.name}"]
}
# その他のポリシーを付与する
~~~


## 統合サービスの IAM ポリシー

[統合サービスの IAM ポリシー](https://docs.aws.amazon.com/ja_jp/step-functions/latest/dg/service-integration-iam-templates.html) にあるように必要なポリシーを付与する必要がある
