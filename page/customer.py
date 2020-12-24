import allure

from page.addcustomer import AddCustomer
from page.base_page import BasePage
from page.customerdetail import CustomerDetail
from page.filtercustomer import FilterCustomer
from page.mycustomer import MyCustomer
from page.searchcustomer import SearchCustomer
from page.signcustomer import SignCustomer
from page.signdetail import SignDetail
from page.signhouse import SignHouse
from page.signlist import SignList


class Customer(BasePage):
    """
    客户页面
    """
    def goto_my_customer(self):
        """
        点击“我的客户”，进入我的客户页面
        :return: MyCustomer(self._driver)
        """
        with allure.step("点击“客户数”"):
            self.steps("../page/customer.yaml")
        return MyCustomer(self._driver)

    def goto_sign_list(self):
        """
        点击“我的报备”，进入报备列表
        :return: SignList(self._driver)
        """
        with allure.step("点击“我的报备”"):
            self.steps("../page/customer.yaml")
        return SignList(self._driver)

    def goto_add_customer(self):
        """
        点击“添加客户”，进入添加客户页面
        :return: AddCustomer(self._driver)
        """
        with allure.step("点击“添加客户”"):
            self.steps("../page/customer.yaml")
        return AddCustomer(self._driver)

    def goto_sign_customer(self):
        """
        点击“快速报备”，进入报备客户页面
        :return: SignCustomer(self._driver)
        """
        with allure.step("点击“快速报备”"):
            self.steps("../page/customer.yaml")
        return SignCustomer(self._driver)

    def goto_search_customer(self):
        """
        点击“搜索”，进入搜索页面
        :return: SearchCustomer(self._driver)
        """
        with allure.step("点击“搜索”"):
            self.steps("../page/customer.yaml")
        return SearchCustomer(self._driver)

    def goto_filter_customer(self):
        """
        点击“筛选”，进入筛选页面
        :return: FilterCustomer(self._driver)
        """
        with allure.step("点击“筛选”"):
            self.steps("../page/customer.yaml")
        return FilterCustomer(self._driver)

    def goto_customer_detail(self):
        """
        点击“最近报备”的第一条数据
        :return: CustomerDetail(self._driver)
        """
        with allure.step("点击“最近报备”的第一条数据"):
            self.steps("../page/customer.yaml")
        return CustomerDetail(self._driver)

    def goto_sign_house(self):
        """
        点击“最近报备”第一条的“+”号
        :return: SignHouse(self._driver)
        """
        with allure.step("点击“最近报备”第一条的“报备楼盘”"):
            self.steps("../page/customer.yaml")
        return SignHouse(self._driver)

    def click_call(self):
        """
        点击“最近报备”第一条的“+”号
        :return: self
        """
        with allure.step("点击“最近报备”第一条的“拨打电话”"):
            self.steps("../page/customer.yaml")
        return self

    def goto_sign_detail(self):
        """
        点击“最近报备”第一条的报备信息
        :return: SignDetail(self._driver)
        """
        with allure.step("点击“最近报备”第一条的报备信息"):
            self.steps("../page/customer.yaml")
        return SignDetail(self._driver)


