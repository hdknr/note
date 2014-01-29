Date: 2013-10-02  10:42
Title: libpam-python : cyrus-imapdのPAM認証をDjangoでやる
Type: post  
Excerpt:   


改良してcyrus-imapdの認証できるようにした:

    import traceback
    #   
    sys.path.insert(0,"/usr/local/lib/python2.7")
    sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages")
    #   
    syslog.syslog("%s:START REAdy" % NAME)
    PRJ_PATH= os.path.dirname( os.path.abspath(__file__))
    sys.path.insert(0, PRJ_PATH )
    sys.path.insert(0, os.path.join(PRJ_PATH ,'app'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
    #   
    def pam_sm_authenticate(pamh, flags, argv):
      
      if pamh.authtok == None:
        passmsg = pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "Have a good access token?")
        res = pamh.conversation(passmsg)
        pamh.authtok = res.resp
      
      username = pamh.user 
      password = pamh.authtok
          
      try:
          from django.contrib.auth import authenticate
          user = authenticate(username=username,password=password )
          
          if user:
              syslog.syslog("%s: %s is authenticated." % ( NAME,username) )
          else:
              syslog.syslog("%s: %s is not authenticated." % ( NAME,username) )
          return pamh.PAM_SUCCESS if user else pamh.PAM_AUTH_ERR 
      except:
          for err in traceback.format_exc().split('\n'):
              syslog.syslog("%s: %s" % (NAME, err ))
          return pamh.PAM_AUTH_ERR 

Djangoのデータベースがsqlite3だとアクセス権なのかパスの問題なのか例外が発生する   :


    Oct  2 10:39:34 ubt3 DJ_AUTH[1092]: DJ_AUTH: DatabaseError: no such table: auth_user

ので、データベースをMySQLに変えた。変えた直後もなぜかsqlite3見に行くのでとりあえずUbuntuリブートして動いた。

       