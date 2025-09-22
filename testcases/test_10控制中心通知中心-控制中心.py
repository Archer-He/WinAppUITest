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
    common.click(driver, "控制中心通知中心")
    common.expand(driver, "控制中心")


@pytest.mark.usefixtures("init_feature")
@allure.feature("控制中心通知中心")
class TestClass(object):

    @allure.title("控制中心通知中心-控制中心-开关")
    def test_1(self, driver):
        common.click(driver, "开关")
        common.click_by_xpath(driver, '//*[@Name="图标是否使用颜色" and @LocalizedControlType="编辑"]')  # 图标是否使用颜色
        common.click(driver, ICON_USE_COLOR)
        common.click_by_xpath(driver, '//*[@Name="组件说明" and @LocalizedControlType="编辑"]')  # 开关背景是否使用颜色
        common.click(driver, SWITCH_BACKGROUND_USE_COLOR)
        common.set_color(driver, "图标开启状态/开启状态不可用", "#FFFFFF")
        common.set_color(driver, "图标关闭状态", "#000000")
        common.set_color(driver, "图标关闭不可用状态", "#0000008C")
        common.set_color(driver, "关闭状态背景", 21)
        common.upload_pic(driver, "开关背景-开启状态背景", r"04 控制中心_通知中心\控制中心\开关\status_bar_qs_tile_bg_active.png")
        common.upload_pic(driver, "开关背景-关闭状态背景", r"04 控制中心_通知中心\控制中心\开关\status_bar_qs_tile_bg_inactive.png")

    @allure.title("控制中心通知中心-控制中心-下拉展开")
    def test_2(self, driver):
        common.click(driver, "下拉展开")
        common.set_color(driver, "背景", 15)


if __name__ == '__main__':
    pytest.main("-v -s test_10控制中心通知中心-控制中心.py")
