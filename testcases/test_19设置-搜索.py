# -*- coding: utf-8 -*-
# @Time    : 2021-09-24 17:09
# @Author  : 何忠意
# @FileName: 1.py
# @Software: PyCharm

import pytest
import allure
import common
from config import *


@pytest.fixture(scope="class")
def init_feature(driver):
    common.click(driver, "设置")
    common.expand(driver, "搜索")


@pytest.mark.usefixtures("init_feature")
@allure.feature("设置")
class TestClass(object):

    @allure.title("设置-搜索-搜索历史")
    def test_1(self, driver):
        common.click(driver, "搜索历史")
        common.upload_pic(driver,"搜索区域背景",r"07 设置\搜索历史\oplus_toolbar_bg.9.png")



if __name__ == '__main__':
    pytest.main("-v -s test_19设置-搜索.py")
