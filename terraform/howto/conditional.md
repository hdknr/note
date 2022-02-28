# 条件でリソースを作る  

## Terraform: if 文はない

- [Terraform tips & tricks: loops, if-statements, and gotchas](https://blog.gruntwork.io/terraform-tips-tricks-loops-if-statements-and-gotchas-f739bbae55f9#0223)


もしも `if` があったら:

~~~tf
# This is just pseudo code. It won't actually work in Terraform.
if var.enable_autoscaling {
  resource "aws_autoscaling_schedule" "scale_out_business_hours" {
    scheduled_action_name  = "scale-out-during-business-hours"
    ...
  }
  resource "aws_autoscaling_schedule" "scale_in_at_night" {
    scheduled_action_name  = "scale-in-at-night"
    ...
  }
}
~~~

ないので:

- `count`: 0 だとリソースが作成されない。1だと１つ作成される。
- `<CONDITION> ? <TRUE_VAL> : <FALSE_VAL>` をつかって `count` を設定する。


~~~tf
resource "aws_autoscaling_schedule" "scale_out_business_hours" {
  count = var.enable_autoscaling ? 1 : 0
  scheduled_action_name  = "scale-out-during-business-hours"
  ...
}
resource "aws_autoscaling_schedule" "scale_in_at_night" {
  count = var.enable_autoscaling ? 1 : 0
  scheduled_action_name  = "scale-in-at-night"
  ...
}
~~~