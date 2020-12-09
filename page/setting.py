import allure

from page.base_page import BasePage
from page.favsetting import FavSetting
from page.moreservice import MoreService
from page.personal import Personal


class Setting(BasePage):
    """
    设置页面
    """
    def goto_personal(self):
        """
        点击“个人资料”，进入个人资料页面
        :return: Personal(self._driver)
        """
        with allure.step("点击“个人资料”"):
            self.steps("../page/setting.yaml")
        return Personal(self._driver)

    def goto_change_phone(self):
        """
        点击“修改手机”
        :return: Personal(self._driver)
        """
        with allure.step("点击“修改手机”"):
            self.steps("../page/setting.yaml")
        return Personal(self._driver)

    def goto_change_pw(self):
        """
        点击“修改密码”，进入修改密码页面（修改密码、修改手机页面放在personal个人资料页面）
        :return: Personal(self._driver)
        """
        with allure.step("点击“修改密码”"):
            self.steps("../page/setting.yaml")
        return Personal(self._driver)

    def goto_fav_setting(self):
        """
        点击“偏好设置”，进入偏好设置页面
        :return: FavSetting(self._driver)
        """
        with allure.step("点击“偏好设置”"):
            self.steps("../page/setting.yaml")
        return FavSetting(self._driver)

    def goto_clean_cache(self):
        """
        点击“清理缓存”，进入偏好设置页面
        :return: self
        """
        with allure.step("点击“清理缓存”"):
            self.steps("../page/setting.yaml")
        return self

    def goto_feedback(self):
        """
        点击“意见反馈”，进入意见反馈页面（意见反馈、门店入驻、合作，都放在一个页面moreservice）
        :return: self
        """
        with allure.step("点击“意见反馈”"):
            self.steps("../page/setting.yaml")
        return MoreService(self._driver)

    def goto_about(self):
        """
        点击“关于”
        :return: self
        """
        with allure.step("点击“关于”"):
            self.steps("../page/setting.yaml")
        return self

    def back_to_my(self):
        """
        设置页面，点击物理键返回，回到我的页面
        :return:
        """
        with allure.step("返回回到我的页面"):
            self.back()
        from page.my import My
        return My(self._driver)