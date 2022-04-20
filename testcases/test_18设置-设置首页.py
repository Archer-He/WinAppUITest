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

    @allure.title("设置-设置首页")
    def test_1(self, driver):
        common.click(driver, "设置首页")
        common.set_color(driver, "虚拟按键颜色", 12)
        common.set_color(driver, "广告与隐私声明文本颜色", 12)
        common.set_color(driver, "引导图下面文字颜色", 12)


if __name__ == '__main__':
    pytest.main("-v -s test_18设置-设置首页.py")
