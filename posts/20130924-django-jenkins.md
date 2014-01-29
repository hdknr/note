Date: 2013-09-24  10:00
Title: Subversion管理のDjangoのプロジェクトをJenkinsでテスト
Type: post  
Excerpt:   



# SunJavaのインストール #

Debian Squeezeに add-apt-repository が無いっぽい:

    root@deb1:~/bin# wget http://blog.anantshri.info/content/uploads/2010/09/add-apt-repository.sh.txt -O add-apt-repository.sh
    root@deb1:~/bin# chmod +x add-apt-repository.sh 

Debian Way:

    root@deb1:~# update-alternatives --install /usr/sbin/add-apt-repository add-apt-repository /root/bin/add-apt-repository.sh 1
    
    update-alternatives: /usr/sbin/add-apt-repository (add-apt-repository) を提供するために 自動モード で /root/bin/add-apt-repository.sh を使います。

/etc/apt/source.listとかに追加:

    root@deb1:~# sudo add-apt-repository ppa:webupd8team/java

    admin@deb1:~$ grep java /etc/apt/sources.list
    /etc/apt/sources.list:20:deb http://ppa.launchpad.net/webupd8team/java/ubuntu lucid main

    root@deb1:~# apt-get update

Javaインストーラーパッケージからインストール:

    root@deb1:~# sudo apt-get install oracle-java7-installer
    パッケージリストを読み込んでいます... 完了
    依存関係ツリーを作成しています                
    状態情報を読み取っています... 完了
    以下の特別パッケージがインストールされます:
      gsfonts gsfonts-x11 java-common
    提案パッケージ:
      default-jre equivs binfmt-support visualvm ttf-baekmuk ttf-unfonts ttf-unfonts-core ttf-kochi-gothic ttf-sazanami-gothic ttf-kochi-mincho ttf-sazanami-mincho ttf-arphic-uming firefox
      firefox-2 iceweasel mozilla-firefox iceape-browser mozilla-browser epiphany-gecko epiphany-webkit epiphany-browser galeon midbrowser moblin-web-browser xulrunner xulrunner-1.9
      konqueror chromium-browser midori google-chrome
    以下のパッケージが新たにインストールされます:
      gsfonts gsfonts-x11 java-common oracle-java7-installer
    アップグレード: 0 個、新規インストール: 4 個、削除: 0 個、保留: 0 個。
    3,456 kB のアーカイブを取得する必要があります。
    この操作後に追加で 5,317 kB のディスク容量が消費されます。
    続行しますか [Y/n]? y

バージョン確認:

    root@deb1:~# java -version
    java version "1.7.0_40"
    Java(TM) SE Runtime Environment (build 1.7.0_40-b43)
    Java HotSpot(TM) Server VM (build 24.0-b56, mixed mode)

# Jenkins インストール #

- [Ubuntuの手順](https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Ubuntu) で。

レポジトリ:

    root@deb1:~# wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -

    root@deb1:~# sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'

    root@deb1:~# sudo apt-get update
     :
     :
    無視 http://pkg.jenkins-ci.org/debian/ binary/ Translation-ja                                                                                                                            
    取得:2 http://pkg.jenkins-ci.org binary/ Release [2,046 B]                                                                                                                               
    取得:3 http://pkg.jenkins-ci.org binary/ Packages [582 B]       
     :
     
インストール :

     root@deb1:~# sudo apt-get install jenkins
    パッケージリストを読み込んでいます... 完了
    依存関係ツリーを作成しています                
    状態情報を読み取っています... 完了
    以下の特別パッケージがインストールされます:
      daemon
    以下のパッケージが新たにインストールされます:
      daemon jenkins
    アップグレード: 0 個、新規インストール: 2 個、削除: 0 個、保留: 0 個。
    57.5 MB のアーカイブを取得する必要があります。
    この操作後に追加で 63.3 MB のディスク容量が消費されます。
    続行しますか [Y/n]? Y

起動しています:

    root@deb1:~# lsof -i:8080
    COMMAND   PID    USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
    java    26205 jenkins  149u  IPv6 124561575      0t0  TCP *:http-alt (LISTEN)

# Jenkins 設定 #

Tracの仮想サーバーにapacheのAlias指定したいので:

    root@deb1:~# dpkg -L jenkins | grep etc |  while read e ; do if [ -f $e ] ; then grep -H JENKINS_ARGS $e ; fi; done

    /etc/default/jenkins:JENKINS_ARGS="--webroot=/var/cache/jenkins/war --httpPort=$HTTP_PORT --ajp13Port=$AJP_PORT"
    /etc/init.d/jenkins:    $SU -l $JENKINS_USER --shell=/bin/bash -c "$DAEMON $DAEMON_ARGS -- $JAVA $JAVA_ARGS -jar $JENKINS_WAR $JENKINS_ARGS" || return 2


prefixを追加します :

    root@deb1:~# grep JENKINS_ARG /etc/default/jenkins 
    JENKINS_ARGS="--webroot=/var/cache/jenkins/war --httpPort=$HTTP_PORT --ajp13Port=$AJP_PORT --prefix=/ci"


    root@deb1:~# /etc/init.d/jenkins restart
    Restarting Jenkins Continuous Integration Server: jenkins.

確認:

    root@deb1:~# curl -I http://localhost:8080/ci
    HTTP/1.1 302 Found
    Server: Winstone Servlet Engine v0.9.10
    Location: http://localhost:8080/ci/?
    Content-Length: 0
    Connection: Keep-Alive
    Date: Mon, 23 Sep 2013 16:29:54 GMT
    X-Powered-By: Servlet/2.5 (Winstone/0.9.10)

# apacheでproxy #

mod_proxy mod_http_proxyの追加:

    root@deb1:~# a2enmod proxy
    Enabling module proxy.
    Run '/etc/init.d/apache2 restart' to activate new configuration!
    
    root@deb1:~# a2enmod proxy_http
    Considering dependency proxy for proxy_http:
    Module proxy already enabled
    Enabling module proxy_http.
    Run '/etc/init.d/apache2 restart' to activate new configuration!

Aliasの設定:

    root@deb1:~# vi /usr/share/jenkins/apache.conf
    <Location /ci >
    Order deny,allow
    Allow from all
    #
    ProxyPass http://localhost:8080/ci
    ProxyPassReverse http://localhost:8080/ci
    #
    # 実際はここにTracと同じ基本認証の設定
    #
    </Location>
    
    
        # vi /etc/apache2/sites-available/host-trac.lafoglia.co.jp.conf 
    
httpd.confにInclude:

    root@deb1:~# grep Include /etc/apache2/sites-available/trac.conf

	Include  /usr/share/jenkins/apache.conf

再起動:

    root@deb1:~# sudo /etc/init.d/apache2 restart
    Restarting web server: apache2 ... waiting .
    

確認:

    Peeko:~ hide$ curl -I https://trac.lafoglia.co.jp/ci -k
    
    HTTP/1.1 401 Authorization Required
    Date: Mon, 23 Sep 2013 16:54:57 GMT
    WWW-Authenticate: Basic realm="You are requested to input id and password"
    Vary: Accept-Encoding
    Content-Type: text/html; charset=iso-8859-1

# Pythonのインストール #

Squeezeは2.6。2.7 使いたいので。

unix ユーザー "ci" を作る:

    admin@deb1:/home$ sudo groupadd -g 2000 ci
    admin@deb1:/home$ sudo useradd -g ci -d /home/ci -u 2000 -m ci
    admin@deb1:/home$ sudo vi /etc/group
    admin@deb1:/home$ grep ci /etc/group
    /etc/group:53:ci:x:2000:ci,jenkins

Pythonのビルドに必要なライブラリを入れる。libbz2-devは後ではまった事がある:


    admin@deb1:/home$ sudo aptitude install libbz2-dev


ciユーザーでPythonzインストール:

    $ curl -kL https://raw.github.com/saghul/pythonz/master/pythonz-install | bash

2.7.3インストール

    ci@deb1:~$ pythonz install 2.7.3
    Downloading Python-2.7.3.tgz as /home/ci/.pythonz/dists/Python-2.7.3.tgz
    ########################################################################## 100%
    Extracting Python-2.7.3.tgz into /home/ci/.pythonz/build/CPython-2.7.3
    
    This could take a while. You can run the following command on another shell to track the status:
      tail -f /home/ci/.pythonz/log/build.log
    
    Installing CPython-2.7.3 into /home/ci/.pythonz/pythons/CPython-2.7.3
    
    Installed CPython-2.7.3 successfully.


2.7.3 にパス通したりとかする:

    ci@deb1:~$ which python
    /home/ci/.pythonz/pythons/CPython-2.7.3/bin/python
    ci@deb1:~$ which easy_install
    /home/ci/.pythonz/pythons/CPython-2.7.3/bin/easy_install

pipなどのインストール:

    ci@deb1:~$ easy_install pip
    ci@deb1:~$ pip install virtualenv virtualenvwrapper

# Subversion のレポジトリにあるDjangoプロジェクトをテスト #

## 方針 ##

- チェックアウトした時にvirtualenvを作る("ve")
- プロジェクトに必要なPYPIパッケージやGithub,Bitbucketなどのプロジェクトインストール
- テスト対象プロジェクト内のパッケージをPYTHONPATHする
- django-jenkinsのテストランナーを動かす


## Jenkinsのビルドの設定 ##

bashスクリプトを登録します。$WORKSPACEはJenkinsが設定する変数:


    #!/bin/bash
    #
    PATH=$WORKSPACE/ve/bin:/home/ci/.pythonz/pythons/CPython-2.7.3/bin:/usr/local/bin:$PATH
    if [ ! -d $WORKSPACE/ve ]; then
      virtualenv --distribute ve;
    fi
    source $WORKSPACE/ve/bin/activate
    bash $WORKSPACE/ci_init.bash
    bash $WORKSPACE/ci_run.bash

ここで、

- /home/ci/.pythonz/pythons/CPython-2.7.3/binのPythonはvirtualenvを作る為に必要なPythonのパスです
- $WORKSPACE/ve/bin は 作成されたVirtualenvで動くPythonのパスです。Djangoアプリケーションが動きます。 
- source $WORKSPACE/ve/bin/activate していますが、 ci_run.bash でPythonをフルパス起動しているので無くてもいいです。

### ci_init.bash ###

- アプリケーションプロジェクトが必要なPYPIとかGithub,Bitbucketのレポジトリをpipでインストールします。
- django-jenkinsを入れておく事がミソです。

こんな感じ:

    #!/bin/bash
    
    pip install -r $WORKSPACE/requirements.txt
    pip install -r $WORKSPACE/requirements.repos.txt

### ci_run.bash ###

python manage.py jenkins でテスト実行します。PYTHONPATHを設定 :

    #!/bin/bash
    
    export PYTHONPATH=$WORKSPACE/src/your:$WORKSPACE/src 
    $WORKSPACE/ve/bin/python  $WORKSPACE/sites/myproj/manage.py jenkins --settings=app.settings_ci
    
app/settings_ci.py は:

    from app.testing import *
    INSTALLED_APPS += ( 'django_jenkins',)
    JENKINS_TASKS = ('django_jenkins.tasks.django_tests',)
    PROJECT_APPS = ('your.apps',)           #:テストランナー対象のモジュール

app/testing.pyはsqlite3指定します。south を外したりしています。:

    from app.settings import *
    import traceback
    
    _TEST_ENGINE='django.db.backends.sqlite3'
    if DATABASES['default']['ENGINE'] != _TEST_ENGINE: 
        DATABASES['default']['ENGINE']=_TEST_ENGINE
        DATABASES['default']['NAME']=DATABASES['default']['NAME'] + ".sqlite5"
    
    INSTALLED_APPS=tuple([ i for i in INSTALLED_APPS if i not in ['south']])
 
# Jenkins実行 #

settings.pyなどをVirtualBoxで更新&ローカルテストが通ってからSubversionにコミットしてからJenkins実行:

    ユーザーanonymousが実行
    ビルドします。 ワークスペース: /var/lib/jenkins/jobs/Customer/workspace
    Updating https://svn.lafoglia.co.jp/customer/django-unions/trunk/djunions at revision '2013-09-24T10:12:20.043 +0900'
    U         sites/myproj/app/settings.py
    U         sites/myproj/app/testing.py
    At revision 379
    [workspace] $ /bin/bash /tmp/hudson4624023736130707975.sh
    ..............
    ----------------------------------------------------------------------
    Ran 14 tests in 17.401s
    
    OK
    Creating test database for alias 'default'...
    Destroying test database for alias 'default'...
    Finished: SUCCESS