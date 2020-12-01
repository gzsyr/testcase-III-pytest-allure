import allure
import pytest

from test_case.test_base import TestBase


class TestSearch(TestBase):
    @allure.description("测试搜索，显示搜索结果")
    @pytest.mark.parametrize('housename', ["滨江雅园", "苏宁"])
    def test_search(self, housename):
        self.shouye.goto_search().action_search(housename)

    @allure.description("点击搜索结果，进入楼盘详情页面")
    def test_goto_search_result(self):
        self.shouye.goto_search().action_search("滨江雅园").select_search_result()