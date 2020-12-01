import allure
from page.base_page import BasePage
from page.housedetail import HouseDetail


class Search(BasePage):
    house_name = "滨江雅园"

    def action_search(self, housename):
        self._params["house_name"] = housename
        with allure.step("输入搜索关键词: " + self._params["house_name"]):
            self.steps("../page/search.yaml", replace=True)

        # 切换输入法，使用键盘的“搜索”键
        self.adbshell('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        self.tsleep(3)
        self._driver.press_keycode('66')        # os.system("adb shell input keyevent 66")
        self.adbshell('adb shell ime set io.appium.settings/.UnicodeIME')
        self.tsleep(3)

        return self

    def select_search_result(self, housename = None):
        # self._params["house_name"] = housename
        with allure.step("点击搜索结果楼盘页面"):
            self.steps("../page/search.yaml", replace=True)

        return HouseDetail(self._driver)
