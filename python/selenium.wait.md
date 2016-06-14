WebDriverWait

~~~py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
~~~

## Safari

- Javaインストールすみ前提

~~~
$ brew install selenium-server-standalone
$ export SELENIUM_SERVER_JAR=/usr/local/Cellar/selenium-server-standalone/2.53.0/libexec/selenium-server-standalone-2.53.0.jar
~~~


## Webドライバー

~~~py

br = webdriver.Safari()
login_portal(br, 'admin', 'adminpass')
...
~~~

## login_portal: WebDriverWait で待つ

- EC.presence_of_element_located( (待ちタイプ, 待ちデータ))

~~~py
def login_portal(br, username, password):
    user_name_css = 'form[name="login"] input[name="user_name"]'
    user_password_css = 'form[name="login"] input[name="user_password"]'
    submit_css = 'form[name=login] input[type=submit]'

    #  <input name="user_name" > タグがHTMLに帰るまで待つ
    WebDriverWait(br, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, user_name_css)))

    # フォーム入力
    br.find_elements_by_css_selector(usr_name_css)[0].send_keys(username)
    br.find_elements_by_css_selector(usr_password_css)[0].send_keys(password)

    # フォーム送信
    br.find_elements_by_css_selector(submit_css)[0].click()
~~~

## 記事

- [Selenium WebDriverのwaitを活用しよう](http://softwaretest.jp/labo/tech/labo-294/)

### or 待ち

- [Selenium Expected Conditions - possible to use 'or'?](http://stackoverflow.com/questions/16462177/selenium-expected-conditions-possible-to-use-or)

~~~py
WebDriverWait(driver, 10).until(
  lambda a:
    a.presence_of_element_located(By.CSS_SELECTOR, "div.some_result") OR
    a.presence_of_element_located(By.CSS_SELECTOR, "div.no_result"))
~~~  
