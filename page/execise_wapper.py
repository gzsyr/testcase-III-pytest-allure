import logging

from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    """
    解释器
    查找元素时，处理异常弹框
    :param func:
    :return:
    """
    logging.basicConfig(level=logging.INFO)

    def wapper(*args, **kwargs):
        from page.base_page import BasePage

        _black_list = [
            (MobileBy.XPATH, "//*[@text='下次再说']"),
            (MobileBy.XPATH, "//*[@text='确定']"),
            (MobileBy.XPATH, "//*[@text='不查看']")
        ]

        _max_num = 3
        _error_num = 0

        instance: BasePage = args[0]

        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)

            _error_num = 0

            instance.set_implicity(10)
            return element
        except Exception as e:
            logging.error("element not find, handle black list")

            # with open("tmp.png", "rb") as f:
            #     content = f.read()
            # allure.attach(content, attachment_type=allure.attachment_type.PNG)

            instance.set_implicity(1)

            if _error_num > _max_num:
                instance.screenshot("tmp.png")
                raise e
            _error_num += 1

            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wapper(*args, **kwargs)

            instance.screenshot("tmp.png")
            raise e
    return wapper
