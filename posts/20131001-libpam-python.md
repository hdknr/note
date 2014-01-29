Date: 2013-10-01  18:00
Title: libpam-python
Type: post  
Excerpt:   


Debian/Ubuntuでパッケージインストール:


    $ sudo aptitude install libpam-python 
    
    $ sudo ls -al /lib/security/
    
    合計 608 
    drwxr-xr-x 2 root root 4096 10月 1 16:06 .
    drwxr-xr-x 14 root root 4096 3月 10 2013 ..
    -rw-r--r-- 1 root root 50488 4月 12 2012 pam_python.so
    
試しに chsh を必ず無効にするpamモジュールだけで認証させる：

    $ grep -v "^#" /etc/pam.d/chsh 

    auth required pam_python.so /home/hdknr/ve/sandbox/src/any_auth/never_auth.py
    

never_auth.pyの内容:

    import syslog
    syslog.openlog(ident="NEVER_AUTH",logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0)
    syslog.syslog("NEVER_AUTH:START")
    
    def pam_sm_authenticate(pamh, flags, argv):
      syslog.syslog("NEVER_AUTH:pam_sm_authenticate")
      return pamh.PAM_AUTH_ERR        #:always fails
      
実行:


    $ chsh
    chsh: PAM authentication failed
     

ログ:

    $ sudo tailf /var/log/syslog

    Oct  1 18:13:46 ubt3 NEVER_AUTH[10924]: NEVER_AUTH:START
    Oct  1 18:13:46 ubt3 NEVER_AUTH[10924]: NEVER_AUTH:pam_sm_authenticate

ちなみにpython-pamでやるとセグメンテーションフォルト。これははまった:

    >>> import pam
    >>> pam.authenticate('hoge','hoge','chsh')
    Segmentation fault (コアダンプ)    

    
RESTでリモートリクエストさせるためにrequestをインストール:

    $ sudo pip install requests
    
    $ which pip
    /usr/local/bin/pip
    
    
    $ python
    Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import requests
    >>> requests.__file__
    '/usr/local/lib/python2.7/dist-packages/requests/__init__.pyc'

REST呼び出しがOKな場合にchshを許すとか:

    $ more rest_auth.py
    
    import syslog
    NAME="REST_AUTH"
    syslog.openlog(ident=NAME,logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0)
    syslog.syslog("%s:START NOW" % NAME)
    
    # MUST paths be append!!!!    
    import sys 
    sys.path.append("/usr/local/lib/python2.7")
    sys.path.append("/usr/local/lib/python2.7/dist-packages")
    
    def pam_sm_authenticate(pamh, flags, argv):
      import requests
      syslog.syslog("%s:pam_sm_authenticate" %NAME ) 
      ep="https://github.com/hdknr"
      res = requests.get(ep)
      syslog.syslog("%s:%s" % (NAME,str(res)) )
      return pamh.PAM_SUCCESS if res.status_code == 200 else pamh.PAM_AUTH_ERR

やってみるとOK:

    $ chsh
    Changing the login shell for hdknr
    Enter the new value, or press ENTER for the default
        Login Shell [/bin/bash]: /bin/bash
        
        