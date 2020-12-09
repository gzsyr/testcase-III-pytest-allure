import allure

from page.base_page import BasePage
from page.mycustomer import MyCustomer
from page.myshop import MyShop
from page.setting import Setting
from page.moreservice import MoreService
from page.signlist import SignList


class My(BasePage):
    """
    我的 页面
    """
    def click_photo(self):
        """
        点击自己的头像
        :return:self---后面增加上传图片的功能
        """
        with allure.step("点击“头像”"):
            self.steps("../page/my.yaml")
        return self

    def goto_setting(self):
        """
        点击“设置”，进入设置页面
        :return:Setting(self._driver)
        """
        with allure.step("点击“设置”"):
            self.steps("../page/my.yaml")
        return Setting(self._driver)

    def goto_my_customer(self):
        """
        点击“客户数”，进入我的客户页面
        :return: MyCustomer(self._driver)
        """
        with allure.step("点击“客户数”"):
            self.steps("../page/my.yaml")
        return MyCustomer(self._driver)

    def goto_sign_num(self):
        """
        点击“签约量”，进入报备列表页面
        :return: ReportList(self._driver)
        """
        with allure.step("点击“签约量”"):
            self.steps("../page/my.yaml")
        return SignList(self._driver)

    def goto_deal_num(self):
        """
        点击“成交额”，进入报备列表页面
        :return: ReportList(self._driver)
        """
        with allure.step("点击“成交额”"):
            self.steps("../page/my.yaml")
        return SignList(self._driver)

    def goto_my_shop(self):
        """
        点击“我的店铺”，进入我的店铺页面
        :return: MyShop(self._driver)
        """
        with allure.step("点击“我的店铺”"):
            self.steps("../page/my.yaml")
        return MyShop(self._driver)

    def goto_my_favourite(self):
        """
        点击“我的关注”，进入收藏页面
        :return:
        """
        with allure.step("点击“关注”"):
            self.steps("../page/my.yaml")
        return self

    def goto_authentication(self):
        """
        点击“认证”，进入认证页面
        :return:
        """
        with allure.step("点击“认证”"):
            self.steps("../page/my.yaml")
        return self

    def goto_coupon(self):
        """
        点击“带看券”，进入优惠券页面
        :return:
        """
        with allure.step("点击“带看券”"):
            self.steps("../page/my.yaml")
        return self

    def goto_loan_cal(self):
        """
        点击“贷款计算器”，进入触屏贷款计算页面
        :return: self
        """
        with allure.step("点击“贷款计算器”"):
            self.steps("../page/my.yaml")
        return self

    def goto_taxes_cal(self):
        """
        点击“税费计算”，进入触屏税费计算页面
        :return: self
        """
        with allure.step("点击“税费计算器”"):
            self.steps("../page/my.yaml")
        return self

    def goto_buyhouse(self):
        """
        点击“购房资格”， 进入购房资格触屏页面
        :return: self
        """
        with allure.step("点击“购房资格”"):
            self.steps("../page/my.yaml")
        return self

    def goto_address_book(self):
        """
        点击“通讯录“，进入通讯录页面
        :return:
        """
        with allure.step("点击“通讯录”"):
            self.steps("../page/my.yaml")
        return self

    def goto_shop_entry(self):
        """
        点击“门店入驻”，进入门店入驻页面
        :return: ShopEntry(self._driver)
        """
        with allure.step("点击“门店入驻”"):
            self.steps("../page/my.yaml")
        return MoreService(self._driver)

    def goto_cooperation(self):
        """
        点击“项目合作”，进入项目合作页面
        :return:
        """
        with allure.step("点击“项目合作“"):
            self.steps("../page/my.yaml")
        return MoreService(self._driver)