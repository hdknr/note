# AWS: iam

- [AWS IAMアカウントの作成、設定、IAMアカウントでのログイン](http://qiita.com/akkisu/items/5e3439ba9c47b9a7f094)

## アカウント

- [AWS アカウント ID](https://docs.aws.amazon.com/ja_jp/general/latest/gr/acct-identifiers.html)

| **項目**          | **内容**                         |
| ----------------- | -------------------------------- |
| AWS アカウント ID | 12 桁の数値                      |
| 正規ユーザー ID   | アカウント ID の難読化された形式 |

~~~bash
aws sts get-caller-identity --query Account --output text --profile spindd
~~~
~~~
695*****8753
~~~


## IAM ログイン

- URL

~~~text
https://{{ your_alias }}.signin.aws.amazon.com/console
~~~

## キーペア

- [Amazon EC2 のキーペア](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair)


## 請求情報

- [ポリシー設定](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html?icmpid=docs_iam_console#tutorial-billing-step1)
- [アクセス権限付与](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html?icmpid=docs_iam_console#tutorial-billing-step2)