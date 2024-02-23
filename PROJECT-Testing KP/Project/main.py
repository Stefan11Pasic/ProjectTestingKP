import time

from selenium import webdriver
from selenium_setup import SetupSelenium
from selenium.webdriver.remote import webelement

def test():
    driver = webdriver.Chrome()
    driver.get('https:/www.google.com')
    time.sleep(5)
    driver.find
test()