import allure

from page.addcommit import AddCommit
from page.base_page import BasePage


class SignDetail(BasePage):
    """
    报备详情 页面
    """
    def click_add_commit(self):
        """
        点击“添加备注”，进入添加备注页面
        :return:
        """
        with allure.step("点击“添加备注”"):
            self.steps("../page/signdetail.yaml")

        return AddCommit(self._driver)
