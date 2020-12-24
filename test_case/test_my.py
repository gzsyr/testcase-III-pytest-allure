import allure

from test_case.test_base import TestBase


class TestMy(TestBase):
    """
    我的 页面上面的用例
    """
    @allure.description("点击我的头像")
    def test_click_photo(self):
        self.shouye.goto_my().click_photo().screenshot()

    @allure.description("点击“客户数”")
    def test_my_customer(self):
        self.shouye.goto_my().goto_my_customer().screenshot()

    @allure.description("点击“成交额”")
    def test_my_deal(self):
        self.shouye.goto_my().goto_deal_num().screenshot()

    @allure.description("点击“签约量”")
    def test_my_sign(self):
        self.shouye.goto_my().goto_sign_num().screenshot()

    @allure.description("点击“我的店铺”")
    def test_my_shop(self):
        self.shouye.goto_my().goto_my_shop().screenshot()

    @allure.description("点击“我的关注”")
    def test_my_fav(self):
        self.shouye.goto_my().goto_my_favourite().screenshot()

    @allure.description("点击“认证”")
    def test_my_auth(self):
        self.shouye.goto_my().goto_authentication().screenshot()

    @allure.description("点击“带看券”")
    def test_my_coupon(self):
        self.shouye.goto_my().goto_coupon().screenshot()

    @allure.description("点击“贷款计算”")
    def test_my_loan(self):
        self.shouye.goto_my().goto_loan_cal().screenshot()

    @allure.description("点击“税费计算”")
    def test_my_taxes(self):
        self.shouye.goto_my().goto_taxes_cal().screenshot()

    @allure.description("点击“购房资格”")
    def test_buy_house(self):
        self.shouye.goto_my().goto_buyhouse().screenshot()

    @allure.description("点击“通讯录”")
    def test_address_list(self):
        self.shouye.goto_my().goto_address_book().screenshot()

    @allure.description("点击“门店入驻”")
    def test_shop_entry(self):
        self.shouye.goto_my().goto_shop_entry().screenshot()  #

    @allure.description("点击“项目合作”")
    def test_coop(self):
        self.shouye.goto_my().goto_cooperation().screenshot()

    @allure.description("点击“设置”按钮")
    def test_goto_setting(self):
        self.shouye.goto_my().goto_setting().screenshot()
