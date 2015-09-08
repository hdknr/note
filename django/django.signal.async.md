Django: モデルシグナルをCelery経由で非同期に処理する

## デリゲートタスク

- `pydoc.locate` でモジュールをみつけて、 関数名で呼び出すタスクを定義
- モデルインスタンスをシリアライズできないので id で渡してもらうからそれで復元する
- 関数を呼ぶ際に `delayed=True` の引数を付与する

~~~py
from celery.task import task
import pydoc

@task
def async_delegate(modname, funcname, instance_id=None, sender=None,
               *args, **kwargs):
    if sender and instance_id:
        instance = sender.objects.get(id=instance_id)
        mod = pydoc.locate(modname)
        getattr(mod, funcname)(instance=instance, delayed=True,
                               *args, **kwargs)
~~~


## デコレータ

- シグナルからの呼び出しをインターセプトする
- `signal` 引数は無視して、 呼び出しを`async_call` にデリゲートする
- `instance` の代わりに `instnace_id` を渡す
- `async_delegate` から代理呼び出しされると`delayed=True` になっているので、実際のシグナルレシーバーを呼ぶ

~~~py
from functools import wraps

def async_signal(*args, **kwargs):
    def _wrapper(decorated, *wargs, **wkwargs):
        def _decorator(instance,
                       delayed=False, signal=None, *dargs, **dkwargs):
            if delayed:
                return decorated(instance, *dargs, **dkwargs)
            else:
                async_delegate.delay(
                    decorated.__module__, decorated.func_name,
                    instance_id=instance.id,
                    *dargs, **dkwargs)

        return wraps(decorated)(_decorator)

    return _wrapper
~~~    

## シグナルレシーバ

-  `@async_signal` デコレートした関数を `@recevier` で登録する

~~~py
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
@async_signal()
def on_user_saved(instance, **kwargs):
    print instance, "is saved."
~~~
