import allure

from test_case.test_base import TestBase


class TestSignList(TestBase):
    """
    报备列表 页面的测试用例
    """
    @allure.description("报备列表中，点击第一条数据查看客户详情")
    def test_goto_customer_detail(self):
        self.shouye.\
            goto_custom().\
            goto_sign_list().\
            goto_customer_detail()

    @allure.description("报备列表中，点击第一条数据的拨打电话按钮")
    def test_click_phone(self):
        self.shouye.\
            goto_custom().\
            goto_sign_list().\
            click_phone().\
            screenshot()

    @allure.description("报备列表中，点击第一条数据的添加报备楼盘按钮")
    def test_goto_add_sign_house(self):
        self.shouye.\
            goto_custom().\
            goto_sign_list().\
            add_sign_house().\
            screenshot()

    @allure.description("报备列表中，点击第一条数据下方的第一条报备楼盘")
    def test_goto_sign_detail(self):
        self.shouye.\
            goto_custom().\
            goto_sign_list().\
            goto_sign_detail().\
            screenshot()

    @allure.description("报备列表中，点击右上角搜索按钮")
    def test_click_search(self):
        self.shouye.\
            goto_custom().\
            goto_sign_list().\
            goto_search_customer().\
            screenshot()

    @allure.description("报备列表中，点击右上角筛选按钮")
    def test_click_filter(self):
        self.shouye. \
            goto_custom(). \
            goto_sign_list(). \
            goto_filter_customer().\
            screenshot()
