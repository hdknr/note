## 存在した時だけなにかする

~~~bash
if grep -q xvdf1 /etc/fstab; then
    echo found
else
    echo not found
fi
~~~
