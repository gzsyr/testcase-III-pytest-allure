import allure

from page.base_page import BasePage


class AddCommit(BasePage):
    """
    添加备注 页面
    """
    def submit_commit(self, commit):
        self._params["commit"] = commit
        with allure.step("输入备注，点击“提交”"):
            self.steps("../page/addcommit.yaml", replace=True)

        return
