Django 1.7:リリースノート: その他

# manage.py check #

- https://docs.djangoproject.com/en/dev/releases/1.7/#new-system-check-framework
- [モデル、シグナル, admin, 互換性のチェックできる](https://docs.djangoproject.com/en/dev/ref/checks/)

エラーを起こしてみる:

    class Todo(models.Model):
        # ....
        class Meta:
            unique_together = (('hoge',))       # hoge フィールドはないです

   (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py check
   CommandError: System check identified some issues:
   
   ERRORS:
   todos.Todo: (models.E012) 'unique_together' refers to the non-existent field 'hoge'.


# adminでのタイムゾーン #

- https://docs.djangoproject.com/en/dev/releases/1.7/#admin-shortcuts-support-time-zones

- "today", "now" のタイムゾーンはアプリの現在のタイムゾーンを使うようになった。
- 以前はブラウザのタイムゾーンを使ってた。

