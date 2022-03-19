import selenium.webdriver.chrome.webdriver
from selenium import webdriver

webdriver.Chrome()

class Browser:
    def __init__(self):
        self.browser = webdriver.Chrome()

