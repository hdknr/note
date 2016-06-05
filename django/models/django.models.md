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


## `__getattr__`


- リレーションモデルのキャッシュなど特殊なことをしているので、 `__getattr__` をオーバーライドしないこと
- `__getattribute__` の例外処理で実装

~~~~python
class AlumnusDeclare(models.Model):
    '''  instance.field が instance.alumnus.field と差分があるかどうかを
         instance.field_diff で返す
    '''
    def __getattribute__(self, name):
        try:
            return super(AlumnusDeclare, self).__getattribute__(name)
        except Exception, ex:
            m = re.search(r'^(?P<field>.+)_diff$', name)
            field = m and m.groupdict()['field']
            if field and field in self._meta.get_all_field_names():
                if self.alumnus:
                    if getattr(self.alumnus, field) == getattr(self, field):
                        return 0
                    return 1
                else:
                    return -1
            raise ex
~~~
