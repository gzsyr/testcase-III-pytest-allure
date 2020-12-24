import allure

from page.base_page import BasePage
from page.dynamicdetail import DynamicDetail


class NewsDynamic(BasePage):
    """
    项目动态 页面
    """
    def click_news(self):
        """
        点击“热门资讯”tab
        :return: self
        """
        with allure.step("点击“热门资讯”"):
            self.steps("../page/newsdynamic.yaml")

        return self

    def click_dynamic(self):
        """
        点击“合作动态”tab
        :return: self
        """
        with allure.step("点击“合作动态”"):
            self.steps("../page/newsdynamic.yaml")

        return self

    def click_first_news(self):
        """
        点击热门资讯下的第一条资讯，进入详情
        :return:
        """
        with allure.step("点击热门资讯下的第一条资讯"):
            self.steps("../page/newsdynamic.yaml")

        return

    def click_first_dynamic_title(self):
        """
        点击“合作动态”的第一条，进入详情
        :return:
        """
        with allure.step("点击“合作动态”的第一条，进入详情"):
            self.steps("../page/newsdynamic.yaml")

        return DynamicDetail(self._driver)

    def click_first_dynamic_like(self):
        """
        点击“合作动态”下第一条动态的，“点赞”
        :return: self
        """
        with allure.step("点击“合作动态”下第一条动态的，“点赞”"):
            self.steps("../page/newsdynamic.yaml")

        return self

    def click_first_dynamic_commit(self, content="楼盘不错"):
        """
        点击“合作动态”下第一条动态的，“评论”
        :return: self
        """
        self._params['commit_content'] = content
        with allure.step("点击“合作动态”下第一条动态的，“评论”"):
            self.steps("../page/newsdynamic.yaml", replace=True)

        return self
