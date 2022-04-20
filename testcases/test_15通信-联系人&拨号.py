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
    common.click(driver, "通信")
    common.collapse(driver, "来电&通话")
    common.expand(driver, "联系人&拨号")


@pytest.mark.usefixtures("init_feature")
@allure.feature("通信")
class TestClass(object):

    @allure.title("通信-联系人&拨号-拨号-无联系人")
    def test_1(self, driver):
        common.click(driver, "拨号-无联系人")
        common.set_color(driver, "无内容文字颜色", 12)
        common.render(driver, 2)
        common.upload_pic(driver, "底图-正常", r"06 通信\联系人&拨号\拨号-无联系人\pb_bg_unavaliable_contact.9.png")

    @allure.title("通信-联系人&拨号-新建联系人")
    def test_2(self, driver):
        common.click(driver, "新建联系人")
        common.set_color(driver, "标题", 12)
        common.set_color(driver, "拖拽提示条", 12)
        common.set_color(driver, "模态视图小标题", 12)
        common.render(driver, 2)
        common.upload_pic(driver, "模态视图背景", r"06 通信\联系人&拨号\新建联系人\pb_bg_window.9.png")

    @allure.title("通信-联系人&拨号-拨号")
    def test_3(self, driver):
        common.click(driver, "拨号")
        common.multiple_upload(driver, "06 通信\联系人&拨号\拨号\键盘\键盘.zip")
        common.render(driver, 25)
        common.upload_pic(driver, "拨号-按钮-正常", r"06 通信\联系人&拨号\拨号\pb_bg_dial_btn_normal.9.png")
        common.upload_pic(driver, "拨号-按钮-下按", r"06 通信\联系人&拨号\拨号\pb_bg_dial_btn_pressed.9.png")
        common.upload_pic(driver, "拨号盘背景", r"06 通信\联系人&拨号\拨号\pb_bg_dialer.9.png")

    @allure.title("通信-联系人&拨号-拨号-通话记录")
    def test_4(self, driver):
        common.click(driver, "拨号-通话记录")
        common.set_color(driver, "拨号盘-号码归宿地", 8)
        # TODO 颜色叠加，浅色
        common.upload_pic(driver, "收起键盘-正常", r"06 通信\联系人&拨号\拨号-通话记录\pb_dr_floating_dial_btn_normal.png")
        # TODO 颜色叠加，浅色
        common.upload_pic(driver, "收起键盘-下按", r"06 通信\联系人&拨号\拨号-通话记录\pb_dr_floating_dial_btn_pressed.png")
        common.upload_pic(driver, "列表顶部提示背景图", r"06 通信\联系人&拨号\拨号-通话记录\pb_bg_dial_header_tips.9.png")
        common.upload_pic(driver, "云服务搜索背景", r"06 通信\联系人&拨号\拨号-通话记录\pb_bg_cloud_header.9.png")

    @allure.title("通信-联系人&拨号-联系人详情")
    def test_5(self, driver):
        common.click(driver, "联系人详情")
        if BACKGROUND_STYLE == "深色背景":
            path = r"06 通信\联系人&拨号\联系人详情深色\联系人详情深色.zip"
        elif BACKGROUND_STYLE == "浅色背景":
            path = r"06 通信\联系人&拨号\联系人详情浅色\联系人详情浅色.zip"
        common.multiple_upload(driver, path)

    @allure.title("通信-联系人&拨号-联系人列表")
    def test_6(self, driver):
        common.click(driver, "联系人列表")
        common.upload_pic(driver, "主列表搜索框背景", r"06 通信\联系人&拨号\联系人列表\pb_bg_search_view.9.png")
        common.upload_pic(driver, "A字母的背景", r"06 通信\联系人&拨号\联系人列表\pb_bg_not_transparent.9.png")
        common.upload_pic(driver, "其他列表搜索背景", r"06 通信\联系人&拨号\联系人列表\pb_bg_another_search_view.9.png")


if __name__ == '__main__':
    pytest.main("-v -s test_15通信-联系人&拨号.py")
