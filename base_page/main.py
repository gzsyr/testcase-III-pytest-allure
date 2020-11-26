import yaml
from appium.webdriver.common.mobileby import MobileBy

from base_page.base_page import BasePage
from base_page.houselist import HouseList
from base_page.my import My
from base_page.search import Search


class Main(BasePage):

    def goto_search(self):
        self.steps("../base_page/main.yaml")
        return Search(self._driver)

    def goto_my(self):
        self.steps("../base_page/main.yaml")
        return My(self._driver)

    def goto_house_detail(self):
        pass

    def goto_all_house(self):
        #self.click(MobileBy.XPATH, "//*[@text='全部']")
        self.steps("../base_page/main.yaml")

        return HouseList(self._driver)