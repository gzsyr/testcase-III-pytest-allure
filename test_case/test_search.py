import allure

from test_case.test_base import TestBase


class TestSearch(TestBase):
    @allure.description("测试搜索")
    def test_search(self):
        self.shouye.goto_search().action_search("滨江雅园")

    @allure.description("进入搜索结果页面")
    def test_goto_search_result(self):
        self.shouye.goto_search().action_search("滨江雅园").select_search_result()