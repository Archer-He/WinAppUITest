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
    common.click(driver, "桌面")
    common.expand(driver, "桌面壁纸")


@pytest.mark.usefixtures("init_feature")
@allure.feature("桌面")
class TestClass(object):

    @allure.title("桌面-桌面壁纸-静态桌面壁纸")
    def test_1(self, driver):
        common.click(driver, "静态桌面壁纸")
        common.upload_pic_by_size(driver, "尺寸：1440x3168", r"02 桌面\静态桌面壁纸\oppo_default_wallpaper.jpg")


if __name__ == '__main__':
    pytest.main("-v -s test_06桌面-桌面壁纸.py")
