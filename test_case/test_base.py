from page.app import App


class TestBase:
    app = None
    def setup(self):
        self.app = App()
        self.shouye = self.app.start().main()
        # self.housedetail = self.shouye.goto_all_house().goto_first_house_detail()
