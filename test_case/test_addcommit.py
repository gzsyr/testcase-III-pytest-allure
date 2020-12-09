import allure
import pytest

from test_case.test_base import TestBase


class TestAddCommit(TestBase):
    """
    添加备注 页面的测试用例
    """
    @allure.description("在“客户”tab页面，直接进入报备详情，输入备注信息，点击“提交”")
    @pytest.mark.parametrize("commit", ["commit content"])
    def test_add_commit(self, commit):
        """
        输入备注信息，点击“提交”
        :return:
        """
        self.shouye.goto_custom().goto_sign_detail().click_add_commit().submit_commit(commit)

    @allure.description("在报备列表页面，进入第一个客户的第一个报备详情，输入备注信息，点击“提交”")
    @pytest.mark.parametrize("commit", ["commit content"])
    def test_add_commit_from_sign_list(self, commit):
        """
        输入备注信息，点击“提交”
        :return:
        """
        self.shouye.goto_custom().goto_sign_list().goto_sign_detail().click_add_commit().submit_commit(commit)