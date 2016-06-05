Q オブジェクト

- [Complex lookups with Q objects](https://docs.djangoproject.com/en/1.8/topics/db/queries/#complex-lookups-with-q-objects)

~~~py
from django.db.models import Q
Q(question__startswith='What')
~~~

## AND / OR

- AND

~~~py
In [4]: Q(id=1, is_superuser=True)
Out[4]: <Q: (AND: ('is_superuser', True), ('id', 1))>

In [6]: User.objects.filter(Q(id=1, is_superuser=True))
Out[6]: [<User: admin>]

In [7]: User.objects.filter(Q(id=1, is_superuser=False))                                                                                       
Out[7]: []
~~~

- OR

~~~py
In [8]: Q(id=1)|Q(is_superuser=True)
Out[8]: <Q: (OR: ('id', 1), ('is_superuser', True))>

In [9]: User.objects.filter(Q(id=1)|Q(is_superuser=True))
Out[9]: [<User: admin>, <User: webmaster>, <User: vagrantuser>]
~~~
