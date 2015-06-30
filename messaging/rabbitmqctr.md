
- [man](http://www.rabbitmq.com/man/rabbitmqctl.1.man.html)

##  list_vhosts

~~~
# rabbitmqctl list_vhosts
Listing vhosts ...
/
...done.
~~~


~~~
# rabbitmqctl add_vhost /myhost 
Creating vhost "/myhost" ...
...done.
~~~


~~~
# rabbitmqctl add_user user1 password1
Creating user "user1" ...
...done.
~~~

~~~
# rabbitmqctl set_permissions -p /myhost user1 ".*" ".*" ".*"
Setting permissions for user "user1" in vhost "/myhost" ...
...done.
~~~
