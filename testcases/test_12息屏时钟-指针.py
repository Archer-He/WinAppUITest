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
    common.click(driver, "息屏时钟")


@pytest.mark.usefixtures("init_feature")
@allure.feature("息屏时钟")
class TestClass(object):

    @allure.title("息屏时钟-指针")
    def test_1(self, driver):
        common.click(driver, "指针")
        common.set_color(driver, "该区域文字（包括图标）", "#FFFFFF")
        common.multiple_upload(driver, r"05 息屏时钟\05 息屏时钟.zip")


if __name__ == '__main__':
    pytest.main("-v -s test_12息屏时钟-指针.py")
