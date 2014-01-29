Date: 2013-10-01  10:00
Title: Fabric: fexpect でsudoのパスワードを自動で入れるとか
Type: post  
Excerpt:   


fexpectを入れる：

    $ pip install fexpect
    
fabfile.pyの下に secrets.py を作って、SECRETSを定義する:

    SECRETS={
       'SUDO_PASSWORD': 'oh_my_god',
    }

secrets.py は .[svn|git|hg]ignore しておくこと。

    
fabfileで、まずsecrets.pyをインポートする:

    try:
        from secrets import SECRETS
        from ilogue.fexpect import expect
        from ilogue.fexpect import expecting, run as expect_run
    except:
        SECRETS={}
 

SUDO_PASSWORDが定義されていたら、fexpect.run() を使うようにした。

    def web_restart():
        print "execution ...", conf.STAGE['WEB_RESTART']
        if SECRETS.get('SUDO_PASSWORD',None):
            prompts =  []
            prompts += expect('password for system:',SECRETS['SUDO_PASSWORD'] )
            with expecting(prompts):
                expect_run(conf.STAGE['WEB_RESTART'] )
        else:
            cuisine.run( conf.STAGE['WEB_RESTART'] )

gunicornの起動スクリプトのを再起動するようにしてみた:

    (tact)Peeko: hide$ fab web_restart
    
    execution ... sudo supervisorctl restart djweb
    
    [dj.lafoglia-inc.net] Executing task 'web_restart'
    [dj.lafoglia-inc.net] put: /Users/hide/ve/tact/lib/python2.7/site-packages/pexpect.py -> /tmp/pexpect.py
    [dj.lafoglia-inc.net] put: <file obj> -> /tmp/fexpect_9UTPnSPXxYfDGLPWMEidEN
    [dj.lafoglia-inc.net] run: python /tmp/fexpect_9UTPnSPXxYfDGLPWMEidEN
    [dj.lafoglia-inc.net] out: [sudo] password for system: oh_my_god
    [dj.lafoglia-inc.net] out: 
    [dj.lafoglia-inc.net] out: 
    [dj.lafoglia-inc.net] out: djweb: stopped
    [dj.lafoglia-inc.net] out: 
    [dj.lafoglia-inc.net] out: djweb: started
    [dj.lafoglia-inc.net] out: 
    [dj.lafoglia-inc.net] out: Exiting fexpect for EOF.
    [dj.lafoglia-inc.net] out: 
    
 Pythonファイルを吐き出してそれを実行しているようです。
 ちなみに、Gunicornを起動するsupervisorの設定ファイルはこう:
 
 
    [program:djweb]
    command=/home/system/ve/lafoglia/bin/gunicorn -c /home/system/ve/lafoglia/src/djlafoglia/sites/dj/gunicorn.conf.py  app.wsgi:application
    user=system
    autostart=true
    autorestart=true
    redirect_stderr=true