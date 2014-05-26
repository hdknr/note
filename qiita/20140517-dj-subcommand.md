Django: managementコマンドのサブコマンド

コマンドが多くなるとごとにファイルを用意するのが面倒くさいから、似たような処理を１つのコマンドにまとめて、それぞれをサブコマンドとしてみる。

サブコマンドの定義。

```py

    import inspect
    import argparse
    
    class SubCommand(object):
        name = ''           # サブコマンド名
        description = ''    # サブコマンドの説明
        args = []   # add_argmentに追加する一覧
    
        def __init__(self, *args, **kwargs):
            self.parser = argparse.ArgumentParser(
                prog=self.name, add_help=False,
                description=self.description.__unicode__())
            map(lambda a: self.parser.add_argument(*a[0], **a[1]), self.args)
    
        def help(self):
            ''' ヘルプ '''
            self.parser.print_help()
    
        def execute(self, *args, **options):
            ''' 引数をparse_argsして、サブコマンドを実行する'''
            
            params = self.parser.parse_args(args)
            # サブコマンドでは位置引数だけを処理し、
            # オプション引数はDjangoのコマンドパーサーに処理させる、という変態仕様
            
            self.run(params, **options)
                
        def run(self, params , **options):
            ''' サブコマンドの本体 
            options には Djangoがパースしたオプション引数が渡る
            '''
            raise NotImplemented()
```

Django のコマンドをカスタマイズ。

```py

    from django.core.management.base import BaseCommand
    
    class GenericCommand(BaseCommand):
        args = ''
        help = ''
        model = None
       
        @classmethod
        def subcommands(cls):
            ''' サブコマンド一覧のdict化 '''
            return dict(
                (v.name, v) for k, v in cls.__dict__.items()
                if inspect.isclass(v) and issubclass(v, SubCommand))
    
        @classmethod
        def subcommand(cls, name):
            ''' サブコマンドクラスの取得 '''
            return cls.subcommands().get(name, None)
    
        def handle(self, *args, **options):
            '''  Djangoのコマンドのメイン '''
    
            if len(args) < 1:
                # 引数が無い時にはすべてのサブコマンドのヘルプを表示
                for k, v in self.subcommands().items():
                    print "\n\n*** Subcommand:", k
                    v().help()
    
            elif len(args) > 1 and args[0] == 'help':
                # サブコマンドにhelpがしていされたら、つづくサブコマンド名のヘルプ
                command = self.subcommand(args[1])
                command and command().help()        
            else:
                # サブコマンドに処理させる
                command = self.subcommand(args[0])
                command and command().execute(*args[1:], **options)
```


例えばrpコマンド(rp.py) で、サブコマンドを包含するCommandを定義:

```py

    class Command(GenericCommand):
    
        class PartyList(SubCommand):
            name = 'list_party'
            description = _(u'List Relying Party Command')
    
            def run(self, params, **options):
                # ... Relying Party 一覧を出力
        
        class PartyDescription(SubCommand):
            name = 'desc_party'
            description = _(u'Detail of Party Command')
            args = [
                (('id',), dict(nargs=1, type=int, help="RelyingParty id")),
            ]
    
            def run(self, params, **options):
    
                print "Relying Party", "ID=", params.id[0]            
                # ... 指定された Relying Partyの詳細を表示
```


実行

    $ python manage.py rp
    
    *** Subcommand: desc_party
    usage: desc_party id
    
    Detail of Party Command
    
    positional arguments:
      id  RelyingParty id
    
    *** Subcommand: list_party
    usage: list_party
    
    List Relying Party Command
    
    
    $ python manage.py rp help desc_party

    usage: desc_party id
    
    Detail of Party Command
    
    positional arguments:
      id  RelyingParty id        
     
    $ python manage.py rp list_party
    
    1 575166910909-tsq1shq9qtmio3ir72bmpqliudm2h8g3.apps.googleusercontent.com Google
    2 c571aa53-a5f7-4c30-95d9-4cdfcd0a4f93 Azure      
    

GenericCommand#run_from_argv() を定義して各サブコマンドにオプション引数を処理させる事も可能:  
    

    def run_from_argv(self, argv):
        ''' Django call this '''

        args = argv and argv[0] == 'manage.py' and argv[2:] or argv[1:0]

        if len(args) < 1:
            for k, v in self.subcommands().items():
                print "\n\n*** Subcommand:", k
                v().help()

        elif len(args) > 1 and args[0] == 'help':
            command = self.subcommand(args[1])
            command and command().help()
        else: 
            command = self.subcommand(args[0])
            command and command().execute(*args[1:])    
                
