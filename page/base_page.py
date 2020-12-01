import inspect
import json
import os
import time

import allure
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.execise_wapper import handle_black


class BasePage:
    _driver: WebDriver

    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicity(self, sec):
        """
        设置隐式等待
        :param sec:
        :return:
        """
        self._driver.implicitly_wait(sec)

    def screenshot(self, name="tmp.png"):
        self.tsleep(2)  # 等待两秒，让页面加载完成后截图
        self._driver.save_screenshot(name)
        with open(name, "rb") as f:
            content = f.read()
        allure.attach(content, attachment_type=allure.attachment_type.PNG)

    @handle_black
    def find(self, locator, value):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    @handle_black
    def finds(self, locator, value: str = None):
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

    def swipe_to_buttom(self, text=None):
        """
        text=None:	直接滑动到页面底部
        text!=None:	滑动到text的地方
        """
        device_size = self._driver.get_window_size()
        p_e = self._driver.page_source

        while (1):
            p_s = p_e
            if text != None and (text in p_s):
                break
            s_x = device_size['width'] * 0.5
            s_y = device_size['height'] * 0.75
            e_y = device_size['height'] * 0.5
            self._driver.swipe(s_x, s_y, s_x, e_y, 500)
            p_e = self._driver.page_source
            self.tsleep(1)
            if p_s == p_e:
                print("找到所需要的地方！退出")
                break

    def steps(self, path, name=None, replace=False):
        with open(path, encoding="utf-8") as f:
            if name is None:
                name = inspect.stack()[1].function  # 可以不通过name来传参，而使用调用的函数名称
            steps = yaml.safe_load(f)[name]
            print(steps)

        if replace:
            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace('${' + key + '}', value)
            steps = json.loads(raw)
            print(steps)

        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    # 点击事件
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    # 发送文本
                    value = step["value"]
                    self.find(step["by"], step["locator"]).send_keys(value)
                    print(f"send({value})")
                if "press" == action:
                    # 按键操作
                    value = step["value"]
                    self._driver.press_keycode(value)
                if "swipe" == action:
                    # 向下滑动操作
                    value = step["value"]
                    if "buttom" != value:
                        self.swipe_to_buttom(value)
                    else:
                        self.swipe_to_buttom()
                if "len>0" == action:
                    # 查找元素是否存在
                    ele = self.finds(step["by"], step["locator"])
                    return len(ele) > 0

    def back(self):
        self._driver.back()

    def tsleep(self, sec):
        time.sleep(sec)

    def adbshell(self, command):
        os.system(command)