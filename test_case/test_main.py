import pytest
import yaml

from base_page.app import App
from test_case.test_base import TestBase


class TestMain(TestBase):

    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    def test_demo(self, value1, value2):
        print(value1)
        print(value2)

    def test_goto_search(self):
        self.app.start().main().goto_search()

    def test_goto_my(self):
        self.app.start().main().goto_my()

    @pytest.mark.parametrize("name", yaml.safe_load(open("./test.yaml", encoding= "utf-8")))
    def test_goto_all_house(self):
        self.app.start().main().goto_all_house()

    def test_goto_house_detail(self):
        self.app.start().main().goto_all_house().goto_first_house_detail()