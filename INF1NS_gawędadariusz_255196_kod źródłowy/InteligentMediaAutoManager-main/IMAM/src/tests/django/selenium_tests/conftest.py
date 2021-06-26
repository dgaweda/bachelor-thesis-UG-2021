
from selenium import webdriver

def firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    firefox_webdriver = webdriver.Firefox(firefox_options=options)
    firefox_webdriver.implicitly_wait(11)
    yield firefox_webdriver
    firefox_webdriver.quit()

