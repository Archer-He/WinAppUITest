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


@pytest.mark.usefixtures("init_feature")
@allure.feature("桌面")
class TestClass(object):

    @allure.title("桌面-桌面文件夹")
    def test_1(self, driver):
        common.click(driver, "桌面文件夹")
        common.set_color(driver, "应用名称文字颜色", FOREGROUND_COLOR)
        common.upload_pic(driver, "翻页页码", r"02 桌面\桌面文件夹\ic_launcher_page_point_focused.png")
        common.upload_pic(driver, "翻页页码-其他", r"02 桌面\桌面文件夹\ic_launcher_folder.png")
        common.upload_pic(driver, "文件夹缩略图背景", r"02 桌面\桌面文件夹\ic_launcher_page_point_normal.png")


if __name__ == '__main__':
    pytest.main("-v -s test_05桌面-桌面文件夹.py")
