from appium.webdriver.common.mobileby import MobileBy

from base_page.base_page import BasePage


class HouseDetail(BasePage):
    def goto_connect(self):
        self.click(MobileBy.ID, "tv_detail_tel")

    def goto_baobei(self):
        self.click(MobileBy.ID, "tv_detail_baobei")