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
    common.click(driver, "音量调节")


@pytest.mark.usefixtures("init_feature")
@allure.feature("音量调节")
class TestClass(object):

    @allure.title("音量调节")
    def test_1(self, driver):
        common.set_color(driver, "字体颜色", 20)
        common.set_color(driver, "音量条当前进度颜色", 20)
        common.set_color(driver, "音量弹框中每个音量条的背景颜色（圆角矩形）", 22)
        common.upload_pic(driver, "音量背景", r"08 音量\systemui_icon_volume_bg.9.png")


if __name__ == '__main__':
    pytest.main("-v -s test_24音量调节.py")
