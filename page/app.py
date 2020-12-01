from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    _package = "com.house365.xinfangbao"
    _activity = "com.house365.xinfangbao.ui.activity.SplashActivity"

    def start(self):
        """
        执行appium连接设备
        :return:self
        """
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["automationName"] = "UiAutomator1"
            caps["platformVersion"] = "7.1.2"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            print("driver is none, 重新建立driver")
        else:
            # self._driver.start_activity(self._package, self._activity)
            self._driver.launch_app()
            print("driver is OK, 不需要重新建立driver")

        self.set_implicity(10)
        print("app -> start")
        return self

    def stop(self):
        """
        关闭连接
        :return:self
        """
        if self._driver is not None:
            self._driver.quit()

    def openapp(self):
        """
        打开执行的app
        :return:self
        """
        if self._driver is not None:
            self._driver.launch_app()
            print("openapp: 执行launch_app")
        else:
            self.start()

        return self

    def closeapp(self):
        """
        关闭执行的app
        :return:self
        """
        if self._driver is not None:
            self._driver.close_app()

    def main(self) -> Main:
        print("app -> main")
        return Main(self._driver)