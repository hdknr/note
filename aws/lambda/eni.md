# Elastic Network Interface

- [仮想ネットワークカードを表す VPC 内の論理ネットワーキングコンポーネント](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/using-eni.html)
- Lambda が作成するネットワークインターフェース = Hyperplane Elastic Network Interfaces、または Hyperplane ENI

## [Amazon VPC 内のリソースに Lambda 関数をアクセスさせる](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)

- Amazon Virtual Private Cloud（Amazon VPC）を使用すると、Amazon Elastic Compute Cloud（Amazon EC2）インスタンス、Amazon Relational Database Service（Amazon RDS）インスタンス、Amazon ElastiCache インスタンスなどのリソースをホストするプライベートネットワークを AWS アカウントに作成できます。
- リソースを含むプライベートサブネットを介して VPC に関数をアタッチすることで、Amazon VPC でホストされているリソースに Lambda 関数をアクセスさせることができます。
- 以下のセクションの指示に従って、Lambda コンソール、AWS コマンドラインインターフェイス（AWS CLI）、または AWS SAM を使用して、Amazon VPC に Lambda 関数をアタッチします。

Note:

- すべての Lambda 関数は、Lambda サービスが所有・管理する VPC 内で実行される。
- これらの VPC は Lambda によって自動的に管理され、顧客からは見えません。
- Amazon VPC 内の他の AWS リソースにアクセスするように関数を設定しても、関数が内部で実行される Lambda が管理する VPC には影響しません。

### 必要な IAM 権限

- AWS アカウントの Amazon VPC に Lambda ファンクションをアタッチするには、Lambda がファンクションに VPC 内のリソースへのアクセスを与えるために使用するネットワークインタフェースを作成および管理する権限が必要です。
- Lambda が作成するネットワークインターフェースは、Hyperplane Elastic Network Interfaces、または Hyperplane ENI として知られています。
- これらのネットワークインターフェースの詳細については、[ハイパープレーン ENI](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#configuration-vpc-enis) についてをご覧ください。

- AWS マネージドポリシー AWSLambdaVPCAccessExecutionRole を関数の実行ロールにアタッチすることで、関数に必要な権限を与えることができます。
- Lambda コンソールで新しい関数を作成して VPC にアタッチすると、Lambda が自動的にこの権限ポリシーを追加してくれます。
- 独自の IAM パーミッションポリシーを作成したい場合は、以下のパーミッションをすべて追加してください：

      - ec2:CreateNetworkInterface
      - ec2:DescribeNetworkInterfaces - このアクションは、すべてのリソースで許可されている場合にのみ動作します (「Resource」: 「*」)。
      - ec2:DescribeSubnets
      - ec2:DeleteNetworkInterface - 実行ロールの DeleteNetworkInterface にリソース ID を指定しないと、関数が VPC にアクセスできないことがあります。一意のリソース ID を指定するか、すべてのリソース ID を含めてください： 「arn:aws:ec2:us-west-2:123456789012:_/_」.
      - ec2:AssignPrivateIpAddresses
      - ec2:UnassignPrivateIpAddresses(プライベート IP アドレスの割り当て解除)

- 関数のロールがこれらの権限を必要とするのは、関数を呼び出すためではなく、ネットワークインターフェースを作成するためだけであることに注意してください。
- 関数の実行ロールからこれらのパーミッションを削除しても、Amazon VPC にアタッチされた関数を正常に呼び出すことができます。

- 機能を VPC にアタッチするために、Lambda は IAM ユーザー・ロールを使用してネットワーク・リソースを確認する必要もあります。
- ユーザーロールが以下の IAM 権限を持っていることを確認してください：

      - ec2:DescribeSecurityGroups
      - ec2:DescribeSubnets
      - ec2:DescribeVpcs

Note:

- 関数の実行ロールに付与する Amazon EC2 のパーミッションは、Lambda サービスが関数を VPC にアタッチするために使用します。
- しかし、関数のコードにも暗黙的にこれらの権限を付与していることになる。
- これは、関数のコードが Amazon EC2 API を呼び出せることを意味する。セキュリティのベストプラクティスに従うためのアドバイスについては、セキュリティのベストプラクティスを参照してください。

### AWS アカウントの Amazon VPC に Lambda 関数をアタッチする

- Lambda コンソール、AWS CLI、または AWS SAM を使用して、AWS アカウントの Amazon VPC に関数をアタッチします。
- AWS CLI または AWS SAM を使用する場合、または Lambda コンソールを使用して既存の関数を VPC にアタッチする場合は、関数の実行ロールが前のセクションに記載されている必要な権限を持っていることを確認してください。
- Lambda 関数は、専用インスタンステナンシーを持つ VPC に直接接続することはできません。
- 専用 VPC のリソースに接続するには、デフォルトテナンシーを持つ 2 つ目の VPC にピアを設定してください。

Amazon VPC の作成時に関数をアタッチするには:

- Lambda 関数を作成して VPC にアタッチするには、CLI で以下の create-function コマンドを実行する。

```bash
aws lambda create-function --function-name my-function \
--runtime nodejs20.x --handler index.js --zip-file fileb://function.zip \
--role arn:aws:iam::123456789012:role/lambda-role \
--vpc-config Ipv6AllowedForDualStack=true,SubnetIds=subnet-071f712345678e7c8,subnet-07fd123456788a036,SecurityGroupIds=sg-085912345678492fb
```

- 独自のサブネットとセキュリティグループを指定し、使用するケースに応じて Ipv6AllowedForDualStack を true または false に設定する

既存の関数を Amazon VPC にアタッチするには:

- 既存の機能を VPC にアタッチするには、次の CLI update-function-configuration コマンドを実行します。

```bash
aws lambda update-function-configuration --function-name my-function \
--vpc-config Ipv6AllowedForDualStack=true, SubnetIds=subnet-071f712345678e7c8,subnet-07fd123456788a036,SecurityGroupIds=sg-085912345678492fb
```

VPC から関数を削除するには:

- VPC から機能をアタッチ解除するには、VPC サブネットとセキュリティグループのリストを空にして、次の update-function-configurationCLI コマンドを実行します。

```bash
aws lambda update-function-configuration --function-name my-function \
--vpc-config SubnetIds=[],SecurityGroupIds=[]
```

### VPC に接続した場合のインターネット・アクセス

- デフォルトでは、Lambda 関数はパブリックインターネットにアクセスできます。
- 関数を VPC にアタッチすると、その VPC 内で利用可能なリソースにのみアクセスできます。
- ファンクションがインターネットにアクセスできるようにするには、VPC もインターネットにアクセスできるように設定する必要があります。
- 詳しくは、「VPC に接続した Lambda ファンクションのインターネットアクセスを有効にする」を参照してください。

### Amazon VPC で Lambda を使用するためのベストプラクティス

Lambda VPC の設定がベストプラクティスのガイドラインに適合していることを確認するには、以下のセクションのアドバイスに従ってください。
