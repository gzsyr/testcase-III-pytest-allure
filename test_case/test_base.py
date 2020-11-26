from base_page.app import App


class TestBase:
    app = None
    def setup(self):
        self.app = App()
        self.shouye = self.app.start().main()