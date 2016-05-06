##  AutoScaling ヘルスチェック

- [Health Checks for Auto Scaling Instances](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/healthcheck.html)

Auto Scaling periodically performs health checks on the instances
in your Auto Scaling group
and identifies any instances that are unhealthy.

After Auto Scaling marks an instance as unhealthy,
it is scheduled for replacement.

For more information,
see [Replacing Unhealthy Instances](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-maintain-instance-levels.html#replace-unhealthy-instance).

Auto Scaling determines the health status of an instance using one or more of the following:

- EC2
- ELB
- Custom

### EC2 status checks

For more information, see
[Status Checks for Your Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)
 in the Amazon EC2 User Guide for Linux Instances.

### ELB health checks

For more information, see
[Configure Health Checks](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-healthchecks.html)
in the Elastic Load Balancing Developer Guide.

### Custom health checks

For more information, see
[Set Instance Health Status Based on Custom Health Checks](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/healthcheck.html#as-configure-healthcheck).


### Default = EC2

By default,
Auto Scaling health checks use the results of the EC2 status checks
to determine the health status of an instance.

Auto Scaling marks an instance as unhealthy
if its instance status is any value other than `running` or its system status is `impaired`.

### Loadbalancing

If you have attached a `load balancer` to your Auto Scaling group,
you can optionally have Auto Scaling include the results of
Elastic Load Balancing health checks
when determining the health status of an instance.

After you add ELB health checks,
Auto Scaling also marks an instance as unhealthy if Elastic Load Balancing reports the instance state as `OutOfService`.

For more information, see
[Adding an ELB Health Check to Your Auto Scaling Group](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-add-elb-healthcheck.html).

### ウォームアップ

Frequently,
an Auto Scaling instance that has just come into service needs
to warm up before it can pass the Auto Scaling health check.

Auto Scaling waits until the health check grace period ends
before checking the health status of the instance.

While the EC2 status checks and ELB health checks can complete
before the health check grace period expires,
Auto Scaling does not act on them until the health check grace period expires.

By default,
the health check grace period is `5 minutes`.

To provide ample warm-up time for your instances, ensure that the health check grace period covers the expected startup time for your application.

Note that
if you add a lifecycle hook to perform actions as your instances launch, the health check grace period does not start until the lifecycle hook is completed and the instance enters the `InService` state.


## 記事

- [オートスケールグループのヘルスチェックについて調べてみた](http://qiita.com/toshihirock/items/eeb0c24671f0239c3288)
