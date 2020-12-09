import allure

from page.base_page import BasePage
from page.customerdetail import CustomerDetail
from page.filtercustomer import FilterCustomer
from page.searchcustomer import SearchCustomer
from page.signdetail import SignDetail
from page.signhouse import SignHouse


class SignList(BasePage):
    """
    报备列表 页面
    """
    def goto_customer_detail(self):
        """
        点击第一条客户，进入客户详情
        :return: CustomerDetail(self._driver)
        """
        with allure.step("点击第一条客户，进入客户详情"):
            self.steps("../page/signlist.yaml")

        return CustomerDetail(self._driver)

    def click_phone(self):
        """
        点击第一条客户的拨打电话按钮
        :return: self
        """
        with allure.step("点击第一条客户，拨打电话"):
            self.steps("../page/signlist.yaml")

        return self

    def add_sign_house(self):
        """
        点击第一条客户的，“+”添加报备楼盘按钮
        :return: SignHouse(self._driver)
        """
        with allure.step("点击第一条客户，“+”添加报备楼盘按钮"):
            self.steps("../page/signlist.yaml")

        return SignHouse(self._driver)

    def goto_sign_detail(self):
        """
        第一条客户的，第一条报备数据
        :return: SignDetail(self._driver)
        """
        with allure.step("点击第一条客户的第一条报备数据"):
            self.steps("../page/signlist.yaml")

        return SignDetail(self._driver)

    def goto_search_customer(self):
        """
        点击右上角搜索
        :return: SearchCustomer(self._driver)
        """
        with allure.step("点击右上角搜索按钮"):
            self.steps("../page/signlist.yaml")

        return SearchCustomer(self._driver)

    def goto_filter_customer(self):
        """
        点击右上角筛选按钮
        :return: FilterCustomer(self._driver)
        """
        with allure.step("点击右上角筛选按钮"):
            self.steps("../page/signlist.yaml")

        return FilterCustomer(self._driver)
