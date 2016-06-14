selenium: AND/OR で要素を待つ

これでいいのかな？

## CSS ウェイター

~~~py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ByCss(object):
    def __init__(self, *args, **kwargs):
        self.meet_all = kwargs.get('meet_all', False)
        self.ecs = [
            EC.presence_of_element_located((By.CSS_SELECTOR, i)) for i in args]

    def __call__(self, driver):
        if self.meet_all:
            return all([fn(driver) for fn in self.ecs])
        else:
            for fn in self.ecs:
                try:
                    if fn(driver): return True
                except:
                    pass

    @classmethod
    def wait(cls, driver, *args, **kwargs):
        seconds = kwargs.get('seconds', 10)
        WebDriverWait(driver, seconds).until(cls(*args, **kwargs))
        return [driver.find_elements_by_css_selector(i) for i in args]
~~~


## サンプル

~~~py
from selenium import webdriver
br = webdriver.Safari()
login_portal(br)
~~~

~~~py
def login_portal(br):
    usr_name_css = 'form[name="auth"] input[name="usr_name"]'
    usr_password_css = 'form[name="auth"] input[name="usr_password"]'

    usr_name, usr_password = ByCss.wait(
        br, usr_name_css, usr_password_css, meet_all=True)

    usr_name[0].send_keys(USER)
    usr_password[0].send_keys(PASSWORD)

    submit_css = 'form[name=auth] input[type=submit]'
    br.find_elements_by_css_selector(submit_css)[0].click()
~~~
