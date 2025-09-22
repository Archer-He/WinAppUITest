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
    common.expand(driver, "栏")


@pytest.mark.usefixtures("init_feature")
@allure.feature("全局设置")
class TestClass(object):

    @allure.title("全局设置-栏-状态栏")
    def test_1(self, driver):
        common.click(driver, "状态栏")
        common.click_by_xpath(driver, '//*[@Name="状态栏素材" and @LocalizedControlType="编辑"]')
        common.click(driver, FOREGGROUND_STYLE)
        common.click_by_xpath(driver, '//*[@Name="使用多彩电池" and @LocalizedControlType="编辑"]')
        common.click(driver, COLORFUL_BATTERY)  # 选择是、否？
        common.upload_pic(driver, "状态栏背景", r"01 全局设置\栏\状态栏\color_statusbar_bg.png")

    @allure.title("全局设置-栏-Tab栏")
    def test_2(self, driver):
        common.click(driver, "Tab栏")
        common.set_color(driver, "字体 未选中", 22)
        common.upload_pic(driver, "Tab - 背景", r"01 全局设置\栏\tab栏\color_tablayout_bg.png")

    @allure.title("全局设置-栏-导航栏")
    def test_3(self, driver):
        common.click(driver, "导航栏")
        common.set_color(driver, "图标/文字按钮-正常/按下", 5)
        common.set_color(driver, "标题 - 大标题", 12)
        common.set_color(driver, "标题 - 二级标题", 12)
        common.set_color(driver, "标题 - 副标题", 7)
        common.render(driver, 19)
        common.upload_pic(driver, "操作区 - 背景", png=r"01 全局设置\栏\导航栏\color_toolbar_bg.png")
        common.upload_pic(driver, "标题 - 背景", png=r"01 全局设置\栏\导航栏\color_toolbar_largest_title_bg.png")

    @allure.title("全局设置-栏-搜索栏")
    def test_4(self, driver):
        common.click(driver, "搜索栏")
        common.set_color(driver, "预置词-正常", 7)
        common.set_color(driver, "正在输入的关键字", 7)
        common.set_color(driver, "结果列表 - 高亮字", 36)
        common.set_color(driver, "结果列表 - 常规字", 8)
        common.upload_pic(driver, "搜索框", r"01 全局设置\栏\搜索栏\color_searchview_corner_rect_bg.9.png")
        common.upload_pic(driver, "搜索框-背景", r"01 全局设置\栏\搜索栏\color_search_view_animate_bg.9.png")

    @allure.title("全局设置-栏-工具栏")
    def test_5(self, driver):
        common.click(driver, "工具栏")
        common.set_color(driver, "icon标题-正常", 5)
        common.upload_pic(driver, "背景", r"01 全局设置\栏\工具栏\color_tool_navigation_view_bg.9.png")


if __name__ == '__main__':
    pytest.main("-v -s test_02全局设置-栏.py::TestClass_2::test_3")
