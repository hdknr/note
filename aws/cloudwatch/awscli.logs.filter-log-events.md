# filter-log-events


~~~bash
env $(cat .env|xargs) aws logs filter-log-events --log-group-name /ecs/tage-ecs-app --filter-pattern "testing" --start-time 1653886581  
~~~