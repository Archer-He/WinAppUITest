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
    common.collapse(driver, "显示与亮度")
    common.expand(driver, "声音、震动、铃声")


@pytest.mark.usefixtures("init_feature")
@allure.feature("设置")
class TestClass(object):

    @allure.title("设置-声音、震动、铃声-声音与振动")
    def test_1(self, driver):
        common.click(driver, "声音与振动")
        common.set_color(driver, "媒体音量/铃声音量/闹钟音量字体颜色", 12)
        common.render(driver, 12)


if __name__ == '__main__':
    pytest.main("-v -s test_21设置-声音、震动、铃声.py")
