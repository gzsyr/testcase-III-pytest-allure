import allure

from test_case.test_base import TestBase


class TestNewsDynamic(TestBase):
    """
    项目动态 页面测试用例
    """
    @allure.description("进入合作动态详情页面点赞，评论")
    def test_click_dynamic(self):
        nd = self.shouye.goto_news_dynamic()
        nd.click_dynamic().click_first_dynamic_like().\
            click_first_dynamic_title().\
            click_like().back(nd).click_news().click_first_news()
