from appium import webdriver

from base_page.base_page import BasePage
from base_page.main import Main


class App(BasePage):

    _package = "com.house365.xinfangbao"
    _activity = "com.house365.xinfangbao.ui.activity.SplashActivity"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["automationName"] = "UiAutomator1"
            caps["platformVersion"] = "7.1.2"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)

        self._driver.implicitly_wait(10)
        print("app -> start")
        return self

    def main(self) -> Main:
        print("app -> main")
        return Main(self._driver)