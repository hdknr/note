# console

- https://www.terraform.io/cli/commands/console


~~~bas
% env $(cat ../.env|xargs) terraform -chdir=stage console
~~~

`locals`*

~~~tf
> local.environment
"stage"
~~~


モジュールの`output` は評価可能:

~~~tf
> module.ami.images
tomap({
  "masters" = "ami-0d4976a80375c348e"
  "services" = "ami-0b933320c14971d28"
  "users" = "ami-04a14ea9b194d4655"
})
~~~