# Q オブジェクト

- [Complex lookups with Q objects](https://docs.djangoproject.com/en/1.8/topics/db/queries/#complex-lookups-with-q-objects)

~~~py
from django.db.models import Q
Q(question__startswith='What')
~~~
