# キャッシュ

## クリア

一覧:

~~~bash
aws cloudfront list-distributions | jq ".DistributionList.Items[]|[.Id, .Aliases.Items[0]]" | jq --slurp
~~~

~~~
aws cloudfront create-invalidation --distribution-id=YOUR_DISTRIBUTION_ID --paths "/*"
~~~
