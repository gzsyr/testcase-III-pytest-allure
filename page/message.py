import allure

from page.base_page import BasePage


class Message(BasePage):
    """
    消息页面
    """
    def click_customer_remind(self):
        """
        点击“客户提醒”
        :return: self
        """
        with allure.step("点击“客户提醒”"):
            self.steps("../page/message.yaml")

        return self

    def click_system_message(self):
        """
        点击“系统消息”
        :return: self
        """
        with allure.step("点击“系统消息”"):
            self.steps("../page/message.yaml")

        return self

    def click_house_dynamic(self):
        """
        点击“楼盘动态”
        :return:
        """
        with allure.step("点击“系统消息”"):
            self.steps("../page/message.yaml")

        return self

