import allure

from test_case.test_base import TestBase


class TestHouseDetail(TestBase):

    @allure.description("搜索进入楼盘详情页面")
    def test_goto_house_detail(self):
        self.shouye.goto_search().action_search("滨江雅园").select_search_result().screenshot()

    @allure.description("点击沟通")
    def test_connect(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_connect().screenshot()

    @allure.description("点击报备")
    def test_bao(self, login):
        self.shouye.goto_all_house().goto_first_house_detail().goto_report().screenshot()

    @allure.description("点击收藏")
    def test_collect(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_collect().screenshot()

    @allure.description("点击海报")
    def test_post(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_post().screenshot()

    @allure.description("点击相册")
    def test_photo(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_photo().screenshot()

    @allure.description("点击地址")
    def test_address(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_address().screenshot()

    @allure.description("点击项目详情tab")
    def test_project_detail(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_project_detail().screenshot()

    @allure.description("点击分享")
    def test_share(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_share().screenshot()

    @allure.description("滚动到项目详情tab的底部")
    def test_project_detail_scroll_buttom(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_project_detail().swipe_to_buttom().screenshot()

    @allure.description("展示楼盘详情页面底部")
    def test_scroll_buttom(self):
        self.shouye.goto_all_house().goto_first_house_detail().swipe_to_buttom().screenshot()

    @allure.description("展示项目详情tab下的更多")
    def test_more_project_detail(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_project_detail().project_detail_more().goto_more_project_detail().screenshot()
