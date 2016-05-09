
- [click](http://click.pocoo.org/6/) by Armin Ronacher ([github](https://github.com/pallets/click))
- [django-click](https://github.com/GaretJax/django-click)

# Install

~~~py
$ pip install click
$ pip install django-click
~~~

# パラメータ

~~~
パラメータ := オプション | 引数
~~~

- 基本的にはオプションを使いましょう

## 引数

引数のユースケース:

- サブコマンド
- ファイル名
- URL

~~~py
@click.argument('name')
def cmd(name):
  pass
~~~

## オプション

- 入力不足の時にプロンプトする
- フラグ(論理/その他)
- 環境変数から取得可能
- ヘルプで完全ドキュメント

# django コマンドサンプル

- management/commands/oil.py

~~~py
import djclick as click


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    click.secho(
        'executing.... {}'.format(ctx.invoked_subcommand),
        fg="green")


@main.command()
@click.argument('name')
@click.pass_context
def subcmd1(ctx, name):
    click.echo(name)


@main.command(name='subcmd3')
@click.option('--n', default=1)
def subcmd2(n):
    click.echo('SUB2')
~~~

~~~bash
$ python manage.py help oil

Usage: manage.py oil [OPTIONS] COMMAND [ARGS]...

Options:
  --version                      Show the version and exit.
  -h, --help                     Show this message and exit.
  -v, --verbosity INTEGER RANGE  Verbosity level; 0=minimal output, 1=normal
                                 output, 2=verbose output, 3=very verbose
                                 output.
  --settings SETTINGS            The Python path to a settings module, e.g.
                                 "myproject.settings.main". If this is not
                                 provided, the DJANGO_SETTINGS_MODULE
                                 environment variable will be used.
  --pythonpath PYTHONPATH        A directory to add to the Python path, e.g.
                                 "/home/djangoprojects/myproject".
  --traceback / --no-traceback   Raise on CommandError exceptions.
  --color / --no-color           Enable or disable output colorization.
                                 Default is to autodetect the best behavior.

Commands:
  subcmd1
  subcmd3
~~~

~~~bash
$ python manage.py oil subcmd3 --help
executing.... subcmd3
Usage: manage.py subcmd3 [OPTIONS]

Options:
  --n INTEGER
  -h, --help   Show this message and exit.

~~~

# Articles

- [Python: コマンドラインパーサの Click が便利すぎた](http://blog.amedama.jp/entry/2015/10/14/232045)
