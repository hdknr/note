#  リージョン一覧

~~~bash
$ aws ec2  describe-regions | jq -r ".Regions[] | [.Endpoint, .RegionName] | @csv" | grep "ap-"

"ec2.ap-south-1.amazonaws.com","ap-south-1"
"ec2.ap-southeast-1.amazonaws.com","ap-southeast-1"
"ec2.ap-southeast-2.amazonaws.com","ap-southeast-2"
"ec2.ap-northeast-2.amazonaws.com","ap-northeast-2"
"ec2.ap-northeast-1.amazonaws.com","ap-northeast-1"
~~~

- [AWS Regions and Endpoints : Amazon EC2](http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)
