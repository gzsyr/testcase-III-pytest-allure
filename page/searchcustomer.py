import allure

from page.base_page import BasePage
from page.customerdetail import CustomerDetail


class SearchCustomer(BasePage):
    """
    搜索客户 页面
    """
    def search_customer(self, search_name="111"):
        """
        输入关键词，点击搜索
        :return:
        """
        self._params["customer"] = search_name
        with allure.step("输入搜索客户的关键词: " + self._params["customer"]):
            self.steps("../page/searchcustomer.yaml", replace=True)

        # 切换输入法，使用键盘的“搜索”键
        self.adbshell('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        self.tsleep(3)
        self._driver.press_keycode('66')  # os.system("adb shell input keyevent 66")
        self.adbshell('adb shell ime set io.appium.settings/.UnicodeIME')
        self.tsleep(3)

        return self

    def have_search_result(self):
        """
        search_customer执行后是否有搜索结果
        :return:
        """
        with allure.step("是否查询到结果？"):
            return self.steps("../page/searchcustomer.yaml")

    def select_customer_name_result(self):
        """
        选择输入的测试结果
        :return:
        """
        if self.have_search_result():
            return self
        else:
            with allure.step("选择第一个搜索结果查看"):
                self.steps("../page/searchcustomer.yaml")

        return CustomerDetail(self._driver)

    def select_customer_sign_result(self):
        """
        选择输入的测试结果
        :return:
        """
        if self.have_search_result():
            return self
        else:
            with allure.step("选择第一个搜索结果查看"):
                self.steps("../page/searchcustomer.yaml")

        return CustomerDetail(self._driver)