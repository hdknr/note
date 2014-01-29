Date: 2013-11-26  10:00
Title: Trac:Subversionのpost-commitフックをPythonでchangeset 反映
Type: post  
Excerpt:   



以下のPythonスクリプト(svnhook.py)で trac.admin.console.runを呼ぶ。
このスクリプトを $SVN/conf にコピーするかシンボリックリンクしておく。

    #!/home/hdknr/ve/sandbox/bin/python
    # -- TracをインストールしたvirtualenvのPythonのパスに設定しておく
    #
    import sys
    import os
    #    
    BASE='/home/hdknr/tracs/prj'
    get_repo = lambda name: os.path.join(BASE,name)
    VENV = os.path.dirname(sys.executable)
    #
    from trac.admin.console import run

    # 呼び出したsvnのレポジトリに対して、changesetを更新する
    # ('tracの名前','tracに定義したレポジトリの名称',)
    SVN2TRACS= {
        'system': [('system','system',)],
    }
    
    def post_commit():
        repo = sys.argv[2].split('/')[-1:][0]
        rev  = sys.argv[3]
        for trac, repo_name in SVN2TRACS[repo]: 
            run( [get_repo(trac),
                 "changeset","added",
                 repo_name,
                 rev])
    
    def help():
        pass
    
    if __name__ == '__main__':
        getattr( sys.modules[__name__],  
                len( sys.argv ) >  1 and sys.argv[1].split('/')[-1:][0].replace('-','_') or 'help',
                help)()



$SVN/hooks/post-commitは一行 :

    #!/bin/sh
    $REPOS/conf/svnhook.py $0 $1 $2

これで、 svnhook.py $SVN/hooks/post-commit system 35 のようにコールされるので、
最終的にsvnhook.py の post_commit() が呼ばれます。あ、post-commit にちょくsimlinkでいいのか？

