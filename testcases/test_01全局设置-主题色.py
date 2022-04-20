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
    common.click(driver, "全局设置")


@pytest.mark.usefixtures("init_feature")
@allure.feature("全局设置")
class TestClass(object):

    @allure.title("全局设置-主题色")
    def test_1(self, driver):
        common.click(driver, "主题色")
        common.set_color(driver, "主色调-正常", 2)
        common.set_color(driver, "主色调-按下", 2)
        common.set_color(driver, "次色调-正常", 2, transparent=True)  # transparent=True表示透明，即在颜色后面加26
        common.set_color(driver, "次色调-按下", 2, transparent=True)  # transparent=True表示透明，即在颜色后面加26


if __name__ == '__main__':
    pytest.main("-s", "test_01全局设置-主题色.py")
