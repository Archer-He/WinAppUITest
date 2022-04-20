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

    @allure.title("设置-导航方式")
    def test_1(self, driver):
        common.click(driver, "导航方式")
        common.set_color(driver, "两侧滑动手势布局引导词条颜色", 12)
        common.set_color(driver, "上滑手势布局引导词条颜色", 12)
        common.set_color(driver, "分页器-未选中", 12)
        common.set_color(driver, "分页器-选中", 12)
        if BACKGROUND_STYLE == "深色背景":
            path = r"07 设置\导航方式深色\导航方式深色.zip"
        elif BACKGROUND_STYLE == "浅色背景":
            path = r"07 设置\导航方式浅色\导航方式浅色.zip"
        common.multiple_upload(driver, path)


if __name__ == '__main__':
    pytest.main("-v -s test_22设置-导航方式.py")
