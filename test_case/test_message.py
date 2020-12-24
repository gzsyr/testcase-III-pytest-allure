import allure

from test_case.test_base import TestBase


class TestMessage(TestBase):
    """
    消息 页面测试用例
    """
    @allure.description("分别点击客户提醒、系统消息、楼盘动态")
    def test_message_click(self):
        msg = self.shouye.goto_message()
        msg.click_customer_remind().back(msg).\
            click_system_message().back(msg).\
            click_house_dynamic().back(msg)
