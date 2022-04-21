# ドメイン登録


## 登録済みドメイン一覧

~~~
% aws route53domains list-domains --region us-east-1 | jq -r ".Domains[].DomainName"
~~~

- 登録済みドメインのゾーンは自動的に作成される