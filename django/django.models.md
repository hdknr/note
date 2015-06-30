# Django モデル関連


## save() で UPDATE か INSERTかの判定

~~~python

if not self.pk:
  do_something()
~~~  

