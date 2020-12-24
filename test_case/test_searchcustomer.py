import allure
import pytest

from test_case.test_base import TestBase


class TestSearchCustome(TestBase):
    """
    搜索客户 页面的测试用例
    """
    @allure.description("我的->客户数->搜索->输入关键词搜索")
    @pytest.mark.parametrize("name", ["测试", "淘房"])
    def test_search_customer(self, name):
        self.shouye.\
            goto_my().\
            goto_my_customer().\
            goto_search_customer().\
            search_customer(name).\
            select_customer_name_result().\
            screenshot()

    @allure.description("客户->搜索->输入关键词搜索")
    @pytest.mark.parametrize("name", ["测试", "淘房"])
    def test_search_customer_1(self, name):
        self.shouye.\
            goto_custom().\
            goto_search_customer().\
            search_customer(name).\
            select_customer_sign_result().\
            screenshot()