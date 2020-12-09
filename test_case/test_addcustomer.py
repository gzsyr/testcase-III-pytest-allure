import allure
import pytest
import yaml

from test_case.test_base import TestBase


class TestAddCustomer(TestBase):
    """
    添加客户 页面的测试用例
    """
    @allure.description("添加客户页面，点击“通讯录”")
    def test_click_address(self):
        self.shouye.goto_custom().goto_my_customer().goto_add_customer().goto_address()

    # @allure.description("添加客户页面，勾选女士")
    # def test_click_female(self):
    #     self.shouye.goto_custom().goto_my_customer().goto_add_customer().select_female()
    #
    # @allure.description("添加客户页面，选择区属")
    # @pytest.mark.parametrize('name', ["鼓楼区"])
    # def test_select_area(self, name):
    #     self.shouye.goto_custom().goto_my_customer().goto_add_customer().select_area(name)
    #
    # @allure.description("添加客户页面，选择户型")
    # @pytest.mark.parametrize('name', ["单身公寓"])
    # def test_select_layout(self, name):
    #     self.shouye.goto_custom().goto_my_customer().goto_add_customer().select_layout(name)
    #
    # @allure.description("添加客户页面，选择标签")
    # @pytest.mark.parametrize('name', ["刚需房"])
    # def test_select_label(self, name):
    #     self.shouye.goto_custom().goto_my_customer().goto_add_customer().swipe_to_buttom().select_label(name)

    @allure.description("添加客户页面，点击保存")
    @pytest.mark.parametrize("add_name, add_phone, area_name, layout_name, label_name",
                             yaml.safe_load(open("test_addcustomer.yaml", encoding='utf-8')))
    def test_save_customer(self, add_name, add_phone, area_name, layout_name, label_name):
        self.shouye.\
            goto_custom().\
            goto_my_customer().\
            goto_add_customer().\
            input_name(add_name).\
            input_phone(add_phone).\
            select_female().\
            select_area(area_name).\
            select_layout(layout_name).\
            swipe_to_buttom().\
            select_label(label_name).\
            save_add_customer()

    @allure.description("添加客户页面，点击保存后，回到我的客户页面，点击第一条客户数据")
    @pytest.mark.parametrize("add_name, add_phone, area_name, layout_name, label_name",
                             yaml.safe_load(open("test_addcustomer.yaml", encoding='utf-8')))
    def test_ok_customer(self, add_name, add_phone, area_name, layout_name, label_name):
        self.shouye. \
            goto_custom(). \
            goto_my_customer(). \
            goto_add_customer(). \
            input_name(add_name). \
            input_phone(add_phone). \
            select_female(). \
            select_area(area_name). \
            select_layout(layout_name). \
            swipe_to_buttom(). \
            select_label(label_name). \
            save_add_customer().\
            goto_customer_detail()

    # @pytest.mark.parametrize("add_name, add_phone, area_name, layout_name, label_name",\
    #                          yaml.safe_load(open("test_addcustomer.yaml", encoding='utf-8')))
    # def test_read_customer(self, add_name, add_phone, area_name, layout_name, label_name):
    #
    #     print(add_name)