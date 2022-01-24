# awscli

- [awscli > cloudfront](https://docs.aws.amazon.com/cli/latest/reference/cloudfront/index.html#cli-aws-cloudfront)


## IDを確認

~~~bash
aws --profile $PROFILE cloudfront list-distributions | jq '.DistributionList.Items[]|select(.Enabled)|[.Id, .Aliases.Items[]]'
~~~

## キャッシュをクリア

~~~bash
aws --profile $PROFILE cloudfront create-invalidation --distribution-id=$ID --paths "$PREFIX*"
~~~
