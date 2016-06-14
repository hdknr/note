- [Selenium Client Driver](http://seleniumhq.github.io/selenium/docs/api/py/)
- [How to install Selenium WebDriver on Mac OS](http://stackoverflow.com/questions/18868743/how-to-install-selenium-webdriver-on-mac-os)


## Chrome Driver

~~~bash
$ brew install chromedriver
==> Downloading https://chromedriver.storage.googleapis.com/2.22/chromedriver_mac32.zip
######################################################################## 100.0%
==> Caveats
To have launchd start chromedriver now and restart at startup:
  sudo brew services start chromedriver
Or, if you dont want/need a background service you can just run:
  chromedriver
==> Summary
🍺  /usr/local/Cellar/chromedriver/2.22: 3 files, 11.6M, built in 4 seconds
~~~


## Safari

~~~
Exception: No executable path given, please add one to Environment Variable                 
'SELENIUM_SERVER_JAR'
~~~

- http://www.seleniumhq.org/download/


### jar

~~~bash
$ brew install selenium-server-standalone
==> Downloading https://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.0.jar
######################################################################## 100.0%
==> Caveats
To have launchd start selenium-server-standalone now and restart at login:
  brew services start selenium-server-standalone
Or, if you dont want/need a background service you can just run:
  selenium-server -p 4444
==> Summary
🍺  /usr/local/Cellar/selenium-server-standalone/2.53.0: 4 files, 20.2M, built in 13 seconds
~~~

~~~bash
$ export SELENIUM_SERVER_JAR=/usr/local/Cellar/selenium-server-standalone/2.53.0/libexec/selenium-server-standalone-2.53.0.jar
~~~
