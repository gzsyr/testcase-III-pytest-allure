import inspect

from page.app import App


class TestBase:
    app = None
    shouye = None

    def setup_class(self):
        if self.app is None:
            self.app = App()

            self.shouye = self.app.openapp().main()  # self.app.start().main()
            print('&&&&&&&' + inspect.stack()[1].filename)
            print(self.shouye)
        else:
            print("app: " + self.app)
        # self.housedetail = self.shouye.goto_all_house().goto_first_house_detail()

    def teardown_class(self):
        self.app.stop()
        print("teardown_class")

    def setup_method(self):
        self.app.openapp()
        print("setup_method")

    def teardown_method(self):
        self.app.closeapp()
        print("teardown_method")