## zipmap: リストからマップを作成する

~~~tf
locals {
    apps =  ["users", "masters", "services"]
    db_urls = zipmap([for key in local.apps: upper("${key}_database_url")], [for key in local.apps: null])
}
~~~

~~~json 
{
    "USER_DATABASE_URL": null,
    "MASTERS_DATABASE_URL": null,
    "SERVICES_DATABASE_URL": null
}
~~~ 
