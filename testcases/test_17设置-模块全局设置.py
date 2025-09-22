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


@pytest.mark.usefixtures("init_feature")
@allure.feature("设置")
class TestClass(object):

    @allure.title("设置-模块全局设置")
    def test_1(self, driver):
        common.click(driver, "模块全局设置")
        es = common.get_elements(driver, name="主题色&内文色选项")
        common.click_element(es[0])
        common.click(driver, SETTING_THEME)
        common.click_element(es[1])
        common.click(driver, FOREGGROUND_STYLE)


if __name__ == '__main__':
    pytest.main("-v -s test_17设置-模块全局设置.py")
