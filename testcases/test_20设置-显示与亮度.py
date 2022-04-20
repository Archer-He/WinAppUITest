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
    common.collapse(driver, "搜索")
    common.expand(driver, "显示与亮度")


@pytest.mark.usefixtures("init_feature")
@allure.feature("设置")
class TestClass(object):

    @allure.title("设置-显示与亮度-显示与亮度")
    def test_1(self, driver):
        common.click_by_xpath(driver, '//*[@Name="显示与亮度" and @LocalizedControlType="链接"]')
        common.set_color(driver, '底部推荐"你可能想找"字体颜色', 12)
        common.set_color(driver, '底部推荐字体颜色', 12)


if __name__ == '__main__':
    pytest.main("-v -s test_20设置-显示与亮度.py")
