Django: モデルフィールドのプライバシー制御を設定する

## 方針

- あるモデルに OneToOneでプライバシー制御を設定するモデルを定義する
- プライバシー制御モデルは元のモデルと同じフィールド名とする
- プライバシー制御モデルは動的に定義する

## 元モデル:個人属性(Profile)

- 抽象モデル

~~~py

class AbstractProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.IntegerField(choices=((0, 'Femail', ), (1, 'Male', ), ))

    class Meta:
        abstract = True
~~~

- 具体モデル

~~~py
class Profile(AbstractProfile):                                                     
    pass   
~~~


## モデルに対してプライバシー制御モデルのフィールドを生成

- 抽象モデルのフィールドを返す

~~~py
def create_privacy_fields(model_class, field_class, **kwargs):    
	# メタクラスを abstract = Trueで作る                                               
    fields = {
        '__module__': model_class.__module__,
        'Meta': type('Meta', (object, ), {'abstract': True, }),
    }

    for i in model_class._meta.fields:
        if isinstance(i, models.AutoField):
            continue
        fields[i.name] = field_class(i.verbose_name, **kwargs)

    return fields
~~~    

## プライバシ制御モデル(ProfilePrivacy)

- 抽象モデルをAbstractProfileを元に動的に生成

~~~py
AbstractProfilePrivacy = type(
    'AbstractProfilePrivacy',
    (models.Model,),
    create_privacy_fields(
        AbstractProfile, models.BooleanField, default=False),
)   
~~~

- 具体モデル: `Profile <-(OneToOne)- ProfilePrivacy`

~~~py
class ProfilePrivacy(AbstractProfilePrivacy):
    profile = models.OneToOneField(Profile)
~~~

## マイグレーション


~~~bash
$ python manage.py makemigrations accounts

Migrations for 'accounts':
  0001_initial.py:
    - Create model Profile
    - Create model ProfilePrivacy
~~~

~~~bash
$ python manage.py migrate

Operations to perform:
  Apply all migrations: accounts
Running migrations:
  Rendering model states... DONE
  Applying accounts.0001_initial... OK
~~~

~~~bash
$ python manage.py shell
~~~
~~~py
In [1]: from django.contrib.auth.models import *
In [2]: from accounts.models import *
In [3]: u = User.objects.get(username='admin')
In [4]: p = Profile.objects.create(user=u, age=33, gender=0)
In [5]: pr = ProfilePrivacy.objects.create(profile=p)
In [6]: u.profile.profileprivacy.gender
Out[6]: False
In [7]: pr.gender = True
In [8]: pr.save()
In [9]: u.profile.profileprivacy.gender
Out[9]: True
~~~

## テンプレート

~~~html

<td>{% if request.user == profile.user or profile.profileprivacy.age %}
    {{ profile.age }} {% else %} 公開されていません {% endif %}</td>

~~~
