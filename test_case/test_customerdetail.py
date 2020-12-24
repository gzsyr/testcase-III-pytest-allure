import allure
import pytest

from test_case.test_base import TestBase


class TestCustomerDetail(TestBase):
    """
    客户详情 页面的测试用例
    备注：使用夜神模拟器，不能执行以下用例
        使用华为Mate30真机，可以执行
        原因待确认
    """
    @pytest.mark.skip
    @allure.description("点击客户详情的“编辑”按钮")
    def test_click_edit(self):
        self.shouye\
            .goto_custom()\
            .goto_my_customer()\
            .goto_customer_detail()\
            .goto_edit_customer()\
            .screenshot()

    @allure.description("点击客户详情的“拨打电话”按钮")
    def test_call(self):
        self.shouye\
            .goto_custom()\
            .goto_my_customer()\
            .goto_customer_detail()\
            .goto_call_phone()\
            .screenshot()

    @allure.description("点击客户详情的“报备动态”按钮")
    def test_sign_detail(self):
        self.shouye\
            .goto_custom()\
            .goto_my_customer()\
            .goto_customer_detail()\
            .goto_sign_detail()\
            .screenshot()
