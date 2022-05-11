# tailコマンド

[tail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/tail.html):

~~~bash
env $(cat .secrets/.env.user|xargs) aws logs tail  /ecs/app-prod-ecs-app
~~~

## ポリシー

~~~
An error occurred (AccessDeniedException) 
when calling the FilterLogEvents operation: 

User: arn:aws:iam::230254826330:user/user 
    is not authorized to perform: 

logs:FilterLogEvents on resource: 
    arn:aws:logs:ap-northeast-1:230254826330:log-group:/ecs/app-prod-ecs-app:log-stream: 
        because no identity-based policy allows the logs:FilterLogEvents action
~~~