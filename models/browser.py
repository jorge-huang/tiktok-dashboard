from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Browser:
    def __init__(self):
        options = Options()
        options.headless = True
        self.__browser = webdriver.Firefox(options=options)

    def __navigate_to(self, url):
        self.__browser.get(url)

    def get_inner_text_by_class_name(self, url, class_name):
        self.__navigate_to(url)
        el = self.__browser.find_element_by_class_name(class_name)
        return el.get_attribute('innerText')