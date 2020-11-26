from test_case.test_base import TestBase


class TestHouseDetail(TestBase):
    def test_connect(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_connect()

    def test_bao(self):
        self.shouye.goto_all_house().goto_first_house_detail().goto_baobei()

