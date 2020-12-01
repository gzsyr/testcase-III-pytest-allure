import inspect

import allure

from page.base_page import BasePage

class Login(BasePage):
    """
    登录页面
    """
    def islogin(self):
        """
        当前是否是登录状态，
        返回True：存在账号登录的文字，为“未登录”状态
        返回False：不存在“账号登录”的问题，为“已登录”状态
        :return:
        """
        with allure.step("登录2: 当前页面是否是登录页面"):
            return self.steps("../page/login.yaml")

    def login(self):
        """
        登录页面，登录完成后，回到“首页”tab
        直接从首页，点击“我的”进行登录，然后回到首页
        :return:
        """
        with allure.step("登录1: 先进入“我的”页面"):
            self.steps("../page/main.yaml", 'goto_my')

        if self.islogin():
            # “未登录”状态
            with allure.step("登录3: 当前在登录页面，执行登录"):
                self.steps("../page/login.yaml")
            with allure.step("登录4: 登录完成，回到首页"):
                self.steps("../page/main.yaml", 'goto_index')
        else:
            with allure.step("登录3: 当前已经是登录状态，回到首页"):
                self.steps("../page/main.yaml", 'goto_index')

        # return Main(self._driver)

    def closeloginpage(self):
        """
        关闭登录页面
        :return:
        """
        with allure.step("退出登录2: 关闭登录页面"):
            self.steps("../page/login.yaml")

    def logout(self):
        """
        退出登录
        直接从首页，点击“我的”进行查看
        :return:
        """
        # 先进入“我的”页面
        with allure.step("退出登录1: 先进入“我的”页面"):
            self.steps("../page/main.yaml", 'goto_my')

        if self.islogin():
            # “未登录”状态
            with allure.step("退出登录2: 当前为“未登录”状态，直接关闭登录页面"):
                self.steps("../page/login.yaml", 'closeloginpage')
        else:
            # “已登录”状态，需要退出登录
            with allure.step("退出登录2: 执行退出登录，设置->退出登录->确定"):
                self.steps("../page/login.yaml")

        with allure.step("退出登录3: 回到首页"):
            self.steps("../page/main.yaml", 'goto_index')
        # return Main(self._driver)
