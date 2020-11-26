from appium.webdriver.common.mobileby import MobileBy

from base_page.base_page import BasePage
from base_page.housedetail import HouseDetail


class HouseList(BasePage):
    def goto_first_house_detail(self):
        self.click_element(MobileBy.ID, "iv_image", 0)
        return HouseDetail(self._driver)