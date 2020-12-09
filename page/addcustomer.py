import allure

from page.base_page import BasePage



class AddCustomer(BasePage):
    """
    添加客户 页面
    """
    def goto_address(self):
        """
        点击“通讯录”
        :return: self
        """
        with allure.step("点击“通讯录”"):
            self.steps("../page/addcustomer.yaml")
        return self

    def input_name(self, name="测试人"):
        """
        填写姓名
        :return: self
        """
        self._params["add_name"] = name
        with allure.step("勾选“女士”"):
            self.steps("../page/addcustomer.yaml", replace=True)
        return self

    def input_phone(self, phone="13000000001"):
        """
        填写手机号
        :return: self
        """
        self._params["add_phone"] = phone
        with allure.step("勾选“女士”"):
            self.steps("../page/addcustomer.yaml", replace=True)
        return self

    def select_female(self):
        """
        勾选“女士”
        :return: self
        """
        with allure.step("勾选“女士”"):
            self.steps("../page/addcustomer.yaml")
        return self

    def select_male(self):
        """
        勾选“女士”
        :return: self
        """
        with allure.step("勾选“先生”"):
            self.steps("../page/addcustomer.yaml")
        return self

    def select_area(self, area="不限"):
        """
        根据area选择区属
        :param area: 区属名称
        :return: self
        """
        self._params["area_name"] = area
        with allure.step("选择“区属”"):
            self.steps("../page/addcustomer.yaml", replace=True)
        return self

    def select_layout(self, layout="不限"):
        """
        根据“layout”选择户型
        :param layout: 户型名称
        :return: self
        """
        self._params["layout_name"] = layout
        with allure.step("选择“户型”"):
            self.steps("../page/addcustomer.yaml", replace=True)
        return self

    def select_label(self, label="地铁房"):
        """
        根据“label”选择标签
        :param label: 标签名称
        :return: self
        """
        self._params["label_name"] = label
        with allure.step("选择“标签”"):
            self.steps("../page/addcustomer.yaml", replace=True)
        return self

    def have_this_phone(self):
        """
        点击保存时，是否有“该号码已经存在”的提示
        :return:
        """
        # 使用toast方法判断，待确认，toast适用于uiautomator2
        # with allure.step("是否有“该号码已经存在”的提示"):
        #     return self.steps("../page/addcustomer.yaml")

        # 改为点击“保存”后，查看是否仍在添加客户页面
        if self.getCurrentActivity() == ".ui.activity.customer.CustomerAddActivity":
            return True
        else:
            return False


    def save_add_customer(self):
        """
        点击“保存”
        :return: self
        """
        with allure.step("点击“保存”"):
            self.steps("../page/addcustomer.yaml")

        if self.have_this_phone():
            with allure.step("号码已存在，返回"):
                self.back()

        from page.mycustomer import MyCustomer
        return MyCustomer(self._driver)
