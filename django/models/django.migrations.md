## unique=True のフィールドを追加する

- code を追加

~~~py
class Region(BaseModel):
    code = models.CharField(
        max_length=20, unique=True, db_index=True)
~~~        

- マイグレーションスクリプト生成

~~~bash
$ python manage.py makemigrations maps
~~~

- スクリプト修正

~~~py

def unique_code(apps, schema_editor):
    # Regionをのすべてのコードをランダムにユニークにする
    for region in apps.get_model("maps", "Region").objects.all():
        region.code = key()
        region.save()

def key():
    # ランダム文字列
    res = ''.join([
        random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
        for i in xrange(20)])
    return res      

class Migration(migrations.Migration):
    # ...
    operations = [
        # AddFied を変更する
        migrations.AddField(
            model_name='region',
            name='code',
            field=models.CharField(
                default=key()                 # 仮のデフォルト
                max_length=20,
                unique=False,                 # unique=Falseで作るように
                verbose_name='Region Code'),
            preserve_default=False,
        ),

        # Region.code をユニークにするPyhonコード実行
        migrations.RunPython(unique_code),

        # unique=TrueでAlterFieldする
        migrations.AlterField(
            model_name='region',
            name='code',
            field=models.CharField(
                db_index=True,
                max_length=20, unique=True, verbose_name='Region Code'),
            preserve_default=False,
        ),
    ]
~~~

- マイグレート

~~~bash
$ python manage.py migrate maps
~~~
