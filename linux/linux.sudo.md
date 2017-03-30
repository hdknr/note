
## /etc/sudoers.d

~~~bash
$ echo "system ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/system
$ sudo chmod 0440 /etc/sudoers.d/system
~~~
