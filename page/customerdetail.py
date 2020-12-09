import allure
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage

from page.signdetail import SignDetail


class CustomerDetail(BasePage):
    """
    客户详情 页面
    """
    def goto_edit_customer(self):
        """
        点击“编辑”按钮，进入编辑页面
        :return:
        """
        with allure.step("点击“编辑”按钮，进入编辑页面"):
            self.steps("../page/customerdetail.yaml")
        return self

    def goto_call_phone(self):
        """
        点击“拨打电话”按钮
        :return:
        """
        with allure.step("点击“拨打电话”按钮"):
            self.steps("../page/customerdetail.yaml")
        return self

    def goto_sign_detail(self):
        """
        查看客户的第一个报备状态，进入报备详情
        :return:
        """
        with allure.step("点击客户的第一个报备状态"):
            self.steps("../page/customerdetail.yaml")
        return SignDetail(self._driver)

    # def back_to_my_customer(self):
    #     """
    #     点击返回，回到“我的客户”页面
    #     :return:
    #     """
    #     with allure.step("点击返回，回到“我的客户”页面"):
    #         self.back()
    #     from page.mycustomer import MyCustomer
    #     return MyCustomer(self._driver)
