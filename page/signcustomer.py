import allure

from page.base_page import BasePage
from page.signhouse import SignHouse


class SignCustomer(BasePage):
    """
    报备客户 页面
    """
    def input_customer_info(self,
                            sign_name="test",
                            sign_phone="13000000000",
                            sign_sex="先生",
                            sign_commit="测试备注"):
        """
        输入姓名、手机号、性别、备注
        :return: self
        """
        self._params["sign_name"] = sign_name
        self._params["sign_phone"] = sign_phone
        self._params["sign_sex"] = sign_sex
        self._params["sign_commit"] = sign_commit
        with allure.step("输入姓名、性别、手机号"):
            self.steps("../page/signcustomer.yaml", replace=True)

        return self

    def click_send(self):
        """
        点击“提交”按钮
        :return:
        """
        with allure.step("点击“提交”按钮"):
            self.steps("../page/signcustomer.yaml")

        return

    def goto_sign_house(self):
        """
        点击请选择楼盘
        :return:
        """
        with allure.step("点击选择楼盘报备"):
            self.steps("../page/signcustomer.yaml")

        return SignHouse(self._driver)