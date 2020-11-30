import allure
import pytest
import yaml

from test_case.test_base import TestBase


class TestMain(TestBase):

    @allure.description("进入横幅广告页面")
    def test_click_adv(self):
        self.shouye.goto_adv().screenshot()

    @allure.description("进入“全部”楼盘列表页面")
    def test_click_all(self):
        self.shouye.goto_all_house().screenshot()

    @allure.description("进入“住宅”楼盘列表页面")
    def test_click_zz(self):
        self.shouye.goto_zz_house().screenshot()

    @allure.description("进入“商业”楼盘列表页面")
    def test_click_sy(self):
        self.shouye.goto_sy_house().screenshot()

    @allure.description("进入“公寓”楼盘列表页面")
    def test_click_gy(self):
        self.shouye.goto_gy_house().screenshot()

    @allure.description("进入智能推荐右侧的“设置”")
    def test_click_setting(self):
        self.shouye.goto_setting().screenshot()

    @allure.description("进入智能推荐第一个楼盘")
    def test_click_recommend_first_house(self):
        self.shouye.goto_recommend_first_house().screenshot()

    @allure.description("进入精选推荐的“热门报备”")
    def test_click_hot(self):
        self.shouye.swipe_to_list().click_tab_hot().screenshot()

    @allure.description("进入精选推荐的“最新上架”")
    def test_click_new(self):
        self.shouye.swipe_to_list().click_tab_new().screenshot()

    @allure.description("进入精选推荐的“综合排序”")
    def test_click_all(self):
        self.shouye.swipe_to_list().click_tab_all().screenshot()

    # @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    # def test_demo(self, value1, value2):
    #     print(value1)
    #     print(value2)

    # def test_goto_search(self):
    #     self.app.start().main().goto_search()
    #
    # def test_goto_my(self):
    #     self.app.start().main().goto_my()

    # @pytest.mark.parametrize("name", yaml.safe_load(open("./test.yaml", encoding= "utf-8")))
    # def test_goto_all_house(self):
    #     self.app.start().main().goto_all_house()
    #
    # def test_goto_house_detail(self):
    #     self.app.start().main().goto_all_house().goto_first_house_detail()