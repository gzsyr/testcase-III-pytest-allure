import allure

from page.addcustomer import AddCustomer
from page.base_page import BasePage
from page.customerdetail import CustomerDetail
from page.searchcustomer import SearchCustomer


class MyCustomer(BasePage):
    """
    我的客户 页面
    """
    def goto_customer_detail(self):
        """
        查看第一个客户详情
        :return: CustomerDetail(self._driver)
        """
        with allure.step("点击第一个客户，进入客户详情页面"):
            self.steps("../page/mycustomer.yaml")
        return CustomerDetail(self._driver)

    def click_phone(self):
        """
        点击第一个客户的拨打电话按钮
        :return: self
        """
        with allure.step("点击第一个客户的拨打电话按钮"):
            self.steps("../page/mycustomer.yaml")
        return self

    def goto_search_customer(self):
        """
        点击搜索按钮，进入搜索页面
        :return: SearchCustomer(self._driver)
        """
        with allure.step("点击搜索按钮"):
            self.steps("../page/mycustomer.yaml")
        return SearchCustomer(self._driver)

    def goto_add_customer(self):
        """
        点击“+”号，进入添加客户页面
        :return:
        """
        with allure.step("点击添加“+”按钮"):
            self.steps("../page/mycustomer.yaml")
        return AddCustomer(self._driver)

    def back_to_(self):
        """
        执行回退按钮
        :return:
        """
        with allure.step("点击返回键"):
            self.back()
        return self