import os

import pytest

if __name__ == "__main__":
    # delfolder(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\screenshots')
    # delfolder(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\result')

    pytest.main(["-v",
                 "-s",
                 "--show-capture=all",
                 "--alluredir", "./result",  ##"--html=testreport.html", "--self-contained-html",
                 # "./test_house_detail.py",
                 # "./test_main.py::TestMain::test_goto_my",
                 # "./test_my.py",
                 "./test_customer.py",
                 # "-m hello"
                 ])

    # os.system(r"allure generate --clean result -o ./report")
    # os.system(r"allure open report")  # 打开测试报告
