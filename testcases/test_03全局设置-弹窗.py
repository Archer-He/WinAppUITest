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
    common.collapse(driver, "栏")
    common.expand(driver, "弹窗")


@pytest.mark.usefixtures("init_feature")
@allure.feature("全局设置")
class TestClass(object):

    @allure.title("全局设置-弹窗-底部弹窗")
    def test_1(self, driver):
        common.click(driver, "底部弹窗")
        common.set_color(driver, "补述文字", 8)
        common.set_color(driver, "选项 - 主标题", 12)
        common.set_color(driver, "选项 - 副标题", 8)
        common.upload_pic(driver, "背景 - 竖屏", r"01 全局设置\弹窗\底部弹窗\color_bottom_alert_dialog_bg_portrait.9.png")
        common.upload_pic(driver, "背景 - 横屏", r"01 全局设置\弹窗\底部弹窗\color_bottom_alert_dialog_bg_landscape.9.png")
        common.upload_pic(driver, "底部弹窗背景图片", r"01 全局设置\弹窗\底部弹窗\coui_bottom_alert_dialog_bg.9.png")

    @allure.title("全局设置-弹窗-居中弹窗")
    def test_2(self, driver):
        common.click(driver, "居中弹窗")
        common.set_color(driver, "标题", 12)
        common.set_color(driver, "正文字体", 8)
        common.set_color(driver, "按钮文字 - 正常", 12)
        common.set_color(driver, "按钮文字 - 按下", 8)
        common.set_color(driver, "居中弹窗背景颜色", 12)
        common.upload_pic(driver, "背景", r"01 全局设置\弹窗\居中弹窗\color_center_alert_dialog_bg_no_orientation.9.png")

    @allure.title("全局设置-弹窗-[更多]浮层")
    def test_3(self, driver):
        common.click(driver, "[更多]浮层")
        common.set_color(driver, "选项文字_常规", 12)
        common.set_color(driver, "选项文字-正常", 12)
        common.upload_pic(driver, "背景", r"01 全局设置\弹窗\更多浮层\color_popup_list_window_bg.9.png")


if __name__ == '__main__':
    pytest.main("-v test_03全局设置-弹窗.py")
