# Django モデル関連

## ForeignObject

- キーフィールドを指定できる
- 複合キーも可能
- [Django Meetup: Django Multicolumn Joins](http://www.slideshare.net/HearsaySocial/django-meetup-django-multicolumn-joins)

  * ForeignKey is a ForeignObject

  ~~~py
  user = ForeignKey(User)
  ~~~
  ~~~py
  user = ForeignObject(
    User,
    from_fields=(('self',)),
    to_fields=((User._meta.pk.nae),))
  ~~~

## save() で UPDATE か INSERTかの判定

~~~python

if not self.pk:
  do_something()
~~~  
