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

    @allure.title("设置-关于手机")
    def test_1(self, driver):
        common.click(driver, "关于手机")
        common.set_color(driver, "手机名称/版本信息等名称字体颜色", 7)
        common.set_color(driver, "oppo R17pro/基带内核版本等字体颜色", 12)
        common.render(driver, 12)


if __name__ == '__main__':
    pytest.main("-v -s test_23设置-关于手机.py")
