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
    common.collapse(driver, "弹窗")
    common.expand(driver, "控件组件")


@pytest.mark.usefixtures("init_feature")
@allure.feature("全局设置")
class TestClass(object):

    @allure.title("全局设置-控件组件-窗口背景")
    def test_1(self, driver):
        common.click(driver, "窗口背景")
        elements = common.get_elements_by_xpath(driver, '//*[@Name="窗口背景" and @LocalizedControlType="文本"]')
        if len(elements) != 2:
            raise ValueError("未获取到两个元素！")
        common.set_color_by_element(driver, elements[0], 15)
        common.upload_pic_by_element(driver, elements[1], r"01 全局设置\控件组件\窗口\color_window_background.png")

    @allure.title("全局设置-控件组件-按钮")
    def test_2(self, driver):
        common.click(driver, "按钮")
        common.click_by_xpath(driver, '//*[@Name="是否使用切图" and @LocalizedControlType="编辑"]')
        common.click(driver, USE_CUT_VIEW)
        common.set_color(driver, "主按钮-文字-正常", 5)
        common.set_color(driver, "主按钮-文字-按下", 5)
        common.set_color(driver, "主按钮-背景-正常", 15)
        common.set_color(driver, "次按钮-文字-正常", 32)

    @allure.title("全局设置-控件组件-列表")
    def test_3(self, driver):
        common.click(driver, "列表")
        common.set_color(driver, "主标题 - 常规", 12)
        common.set_color(driver, "主标题 - 按下", 12)
        common.set_color(driver, "赋值 - 常规", 2)
        common.set_color(driver, "赋值 - 按下", 2)
        common.set_color(driver, "焦点色标题 - 常规", 2)
        common.set_color(driver, "副标题/辅助文案-正常", 7)
        common.set_color(driver, "底部推荐背景", 21)
        common.set_color(driver, "主标题-选中", 12)
        common.set_color(driver, "底部推荐菜单项文字颜色", 12)
        common.set_color(driver, '底部推荐"你可能想找"字体颜色', 12)
        common.upload_pic(driver, "整个列表背景", r"01 全局设置\控件组件\列表\color_list_preference_bg.9.png")

    @allure.title("全局设置-控件组件-虚拟按键")
    def test_4(self, driver):
        common.click(driver, "虚拟按键")
        common.set_color(driver, "虚拟按键背景", 15)

    @allure.title("全局设置-控件组件-开关")
    def test_5(self, driver):
        common.click(driver, "开关")
        common.click_by_xpath(driver, '//*[@Name="是否切图" and @LocalizedControlType="编辑"]')
        common.click(driver, CUT_VIEW)
        common.set_color(driver, "开 - 焦点背景_常规", 20)
        common.set_color(driver, "关 - 灰色背景_常规", 22)
        common.set_color(driver, "白色圆点", 24)

    @allure.title("全局设置-控件组件-单选、复选")
    def test_6(self, driver):
        common.click(driver, "单选、复选")
        common.set_color(driver, "单选 - 已选", 20)
        common.set_color(driver, "复选 - 已选", 20)
        common.set_color(driver, "复选 - 半选", 20)

    @allure.title("全局设置-控件组件-悬浮按钮")
    def test_7(self, driver):
        common.click(driver, "悬浮按钮")
        common.set_color(driver, "背景颜色", 21)

    @allure.title("全局设置-控件组件-滑动条")
    def test_8(self, driver):
        common.click(driver, "滑动条")
        common.set_color(driver, "滑块 - 内圆_常规", 24)
        common.set_color(driver, "进度/滑块外圈-常规", 20)

    @allure.title("全局设置-控件组件-选择器")
    def test_9(self, driver):
        common.click(driver, "选择器")
        common.set_color(driver, "选中字体", 20)
        common.set_color(driver, "待选字体", 22)

    @allure.title("全局设置-控件组件-输入框")
    def test_10(self, driver):
        common.click(driver, "输入框")
        common.set_color(driver, "正在输入字体 - 有焦点", 12)
        common.set_color(driver, "正在输入字体 - 无焦点", 12)

    @allure.title("全局设置-控件组件-字母索引条")
    def test_11(self, driver):
        common.click(driver, "字母索引条")
        common.set_color(driver, "弹起popup背景", 21)
        common.set_color(driver, "弹起popup 白色字体", 21)
        common.set_color(driver, "字母 - 选中焦点", 19)

    @allure.title("全局设置-控件组件-loading、进度条")
    def test_12(self, driver):
        common.click(driver, "loading、进度条")
        common.set_color(driver, "loading - 圆弧颜色", 2)
        common.set_color(driver, "水平进度 - 进度背景_常规", 2)

    @allure.title("全局设置-控件组件-Tips")
    def test_13(self, driver):
        common.click(driver, "Tips")
        common.set_color(driver, "Tips - 文字", 12)
        common.upload_pic(driver, "Tips - 背景", r"01 全局设置\控件组件\Tips\color_tool_tips_background.9.png")

    @allure.title("全局设置-控件组件-列表详情")
    def test_14(self, driver):
        common.click(driver, "列表详情")
        common.set_color(driver, "浮层 - 文字", 12)
        common.upload_pic(driver, "详情浮层 - 背景", r"01 全局设置\控件组件\列表详情\color_detail_floating_background.9.png")

    @allure.title("全局设置-控件组件-面板")
    def test_15(self, driver):
        common.click(driver, "面板")
        common.set_color(driver, "面板背景", 21)
        elements = common.get_elements_by_xpath(driver, '//*[@Name="面板背景" and @LocalizedControlType="文本"]')
        if len(elements) != 2:
            raise ValueError("未获取到两个元素！")
        common.upload_pic_by_element(driver, elements[1], r"01 全局设置\控件组件\面板\color_panel_bg_without_shadow.9.png")
        common.upload_pic(driver, "面板背景(有投影)", r"01 全局设置\控件组件\面板\color_panel_bg_without_shadow.9.png")


if __name__ == '__main__':
    pytest.main("-v -s test_04全局设置-控件组件.py")
