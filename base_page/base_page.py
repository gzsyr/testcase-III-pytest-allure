import inspect
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from base_page.execise_wapper import handle_black


class BasePage:
    _driver:WebDriver
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver:WebDriver=None):
        self._driver = driver

    def set_implicity(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    @handle_black
    def find(self, locator, value):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

        '''
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator, value)
        '''

    def finds(self, locator, value:str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def click(self, locator, value):
        self.find(locator, value).click()
        return self

    def find_elements(self, locator, value, position):
        elements = self._driver.find_elements(locator, value)
        return elements[position]

    def click_element(self, locator, value, position):
        element = self.find_elements(locator, value, position)
        element.click()
        return self

    def steps(self, path, name = None):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function#可以不通过name来传参，而使用调用的函数名称
            steps = yaml.safe_load(f)[name]
            print(steps)
        for step in steps:
            #element = None
            #if "by" in step.keys():
                #element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    value = step["value"]
                    self.find(step["by"], step["locator"]).send_keys(value)
                    print(f"send({value})")

    def back(self):
        self._driver.back()