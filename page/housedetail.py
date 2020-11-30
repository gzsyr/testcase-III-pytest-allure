import allure
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class HouseDetail(BasePage):
    def goto_connect(self):
        """
        点击沟通
        :return:self
        """
        with allure.step("点击“沟通”"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_report(self):
        """
        点击报备
        :return:self
        """
        with allure.step("点击报备"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_collect(self):
        """
        点击收藏
        :return:self
        """
        with allure.step("点击收藏"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_post(self):
        """
        点击海报
        :return:self
        """
        with allure.step("点击海报"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_photo(self):
        """
        点击相册
        :return:self
        """
        with allure.step("点击相册"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_address(self):
        """
        点击地址
        :return:self
        """
        with allure.step("点击地址"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_project_detail(self):
        """
        点击项目详情
        :return:self
        """
        with allure.step("点击项目详情"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_share(self):
        """
        点击分享
        :return:self
        """
        with allure.step("点击分享"):
            self.steps("../page/housedetail.yaml")
        return self

    # def scroll_to_buttom(self):
    #     """
    #     滑动到页面至底部
    #     :return:self
    #     """
    #     with allure.step("滑动楼盘详情页面至底部"):
    #         self.steps("../page/housedetail.yaml")
    #     return self

    def project_detail_more(self):
        """
        滑动到项目详情TAB下面的“更多”
        :return:self
        """
        with allure.step("滑动到项目详情TAB下面的“更多”"):
            self.steps("../page/housedetail.yaml")
        return self

    def goto_more_project_detail(self):
        """
        点击项目详情页面TAB下面的“更多”
        :return:self
        """
        with allure.step("点击项目详情页面TAB下面的“更多”"):
            self.steps("../page/housedetail.yaml")
        return self
