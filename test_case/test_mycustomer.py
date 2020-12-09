import allure

from test_case.test_base import TestBase


class TestMyCustomer(TestBase):
    """
    我的客户 页面测试用例
    """

    @allure.description("点击第一个客户，进入客户详情页面")
    def test_show_customer(self):
        self.shouye.goto_custom().goto_my_customer().goto_customer_detail().screenshot()

    @allure.description("点击第一个客户的拨打电话按钮")
    def test_call_phone(self):
        self.shouye.goto_custom().goto_my_customer().click_phone().screenshot()

    @allure.description("点击搜索按钮")
    def test_search_customer(self):
        self.shouye.goto_custom().goto_my_customer().goto_search_customer().screenshot()

    @allure.description("点击添加客户按钮")
    def test_add_customer(self):
        self.shouye.goto_custom().goto_my_customer().goto_add_customer().screenshot()

