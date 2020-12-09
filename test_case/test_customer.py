import allure

from test_case.test_base import TestBase


class TestCustomer(TestBase):
    """
    客户页面的测试用例
    """
    @allure.description("点击“我的客户”")
    def test_goto_my_customer(self):
        self.shouye.goto_custom().goto_my_customer().screenshot()

    @allure.description("点击“我的报备”")
    def test_goto_sign_list(self):
        self.shouye.goto_custom().goto_sign_list().screenshot()

    @allure.description("点击“添加客户”")
    def test_goto_add_customer(self):
        self.shouye.goto_custom().goto_add_customer().screenshot()

    @allure.description("点击“快速报备”")
    def test_goto_sign_customer(self):
        self.shouye.goto_custom().goto_sign_customer().screenshot()

    @allure.description("点击“搜索”按钮")
    def test_click_search(self):
        self.shouye.goto_custom().goto_search_customer().screenshot()

    @allure.description("点击“筛选”按钮")
    def test_click_filter(self):
        self.shouye.goto_custom().goto_filter_customer().screenshot()

    @allure.description("点击“最近报备”第一条数据，查看客户详情")
    def test_show_customer_detail(self):
        self.shouye.goto_custom().goto_customer_detail().screenshot()

    @allure.description("点击“最近报备”第一条数据的拨打电话按钮")
    def test_click_call(self):
        self.shouye.goto_custom().click_call().screenshot()

    @allure.description("点击“最近报备”第一条数据的“+”报备楼盘按钮")
    def test_goto_sign_house(self):
        self.shouye.goto_custom().goto_sign_house().screenshot()