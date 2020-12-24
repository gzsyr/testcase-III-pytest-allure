import allure

from page.base_page import BasePage


class DynamicDetail(BasePage):
    """
    合作动态 详情页面
    """
    def click_like(self):
        """
        点击“点赞”
        :return: self
        """
        with allure.step("点击“点赞”"):
            self.steps("../page/dynamicdetail.yaml")

        return self

    def click_commit(self, content="楼盘不错"):
        """
        点击“评论”
        :return: self
        """
        self._params['commit_content'] = content
        with allure.step("点击“评论”"):
            self.steps("../page/dynamicdetail.yaml")

        return self
