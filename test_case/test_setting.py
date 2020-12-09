import allure

from test_case.test_base import TestBase


class TestSetting(TestBase):
    """
    我的->设置 页面
    """

    @allure.description("进入“个人资料”")
    def test_goto_personal(self):
        self.shouye.goto_my().goto_setting().goto_personal().screenshot()

    @allure.description("进入“修改手机”")
    def test_change_phone(self):
        self.shouye.goto_my().goto_setting().goto_change_phone().screenshot()

    @allure.description("进入“修改密码”")
    def test_change_pwd(self):
        self.shouye.goto_my().goto_setting().goto_change_pw().screenshot()

    @allure.description("进入“偏好设置”")
    def test_fav_setting(self):
        self.shouye.goto_my().goto_setting().goto_fav_setting().screenshot()

    @allure.description("进入“清理缓存”")
    def test_clean_cache(self):
        self.shouye.goto_my().goto_setting().goto_clean_cache().screenshot()

    @allure.description("进入“意见反馈”")
    def test_feedback(self):
        self.shouye.goto_my().goto_setting().goto_feedback().screenshot()

    @allure.description("进入“关于”")
    def test_about(self):
        self.shouye.goto_my().goto_setting().goto_about().screenshot()

    @allure.description("进入“关于”")
    def test_back_to_my(self):
        self.shouye.goto_my().goto_setting().back_to_my()
