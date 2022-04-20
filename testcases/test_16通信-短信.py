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
    common.collapse(driver, "联系人&拨号")
    common.expand(driver, "短信")


@pytest.mark.usefixtures("init_feature")
@allure.feature("通信")
class TestClass(object):

    @allure.title("通信-短信-短信列表")
    def test_1(self, driver):
        common.click(driver, "短信列表")
        common.set_color(driver, "信息声明界面标题的字体颜色", 12)
        common.set_color(driver, "信息声明中副标题的字体颜色", 8)
        common.set_color(driver, "列表时间", 8)
        common.render(driver, 2)

    @allure.title("通信-短信-短信对话-气泡界面")
    def test_2(self, driver):
        common.click(driver, "短信对话-气泡界面")
        common.set_color(driver, "气泡-接收-文字", 30)
        common.set_color(driver, "气泡-发送-文字", 31)
        common.upload_pic(driver, "卡片接收背景（正常）", r"06 通信\短信\短信对话-气泡界面\1.9.png")
        common.upload_pic(driver, "卡片接收背景（下按）", r"06 通信\短信\短信对话-气泡界面\1.9.png")
        common.upload_pic(driver, "接收信息背景（正常）", r"06 通信\短信\短信对话-气泡界面\1.9.png")
        common.upload_pic(driver, "接收信息背景（下按）", r"06 通信\短信\短信对话-气泡界面\1.9.png")
        common.upload_pic(driver, "一对一发消息（正常）-rtl", r"06 通信\短信\短信对话-气泡界面\1.9.png")
        common.upload_pic(driver, "一对一发消息（下按）-rtl", r"06 通信\短信\短信对话-气泡界面\1.9.png")
        common.upload_pic(driver, "群发信息背景（正常）", r"06 通信\短信\短信对话-气泡界面\2.9.png")
        common.upload_pic(driver, "群发信息背景（下按）", r"06 通信\短信\短信对话-气泡界面\2.9.png")
        common.upload_pic(driver, "一对一发消息（正常）", r"06 通信\短信\短信对话-气泡界面\2.9.png")
        common.upload_pic(driver, "一对一发消息（下按）", r"06 通信\短信\短信对话-气泡界面\2.9.png")
        common.upload_pic(driver, "接收信息背景（下按）-rtl", r"06 通信\短信\短信对话-气泡界面\2.9.png")
        common.upload_pic(driver, "接收信息背景（正常）-rtl", r"06 通信\短信\短信对话-气泡界面\2.9.png")

    @allure.title("通信-短信-新建")
    def test_3(self, driver):
        common.click(driver, "新建")
        common.set_color(driver, "添加附件个数的文字颜色", 12)
        # TODO 颜色叠加，正常
        common.upload_pic(driver, "底部菜单背景", r"06 通信\短信\新建\mms_bg_bottom_menu.9.png")
        # TODO 颜色叠加，正常
        common.upload_pic(driver, "新建信息-号码编辑框-联系人名称以及号码背景", r"06 通信\短信\新建\mms_bg_chip.9.png")
        common.upload_pic(driver, "发送信息输入框背景", r"06 通信\短信\新建\mms_bg_compose_edit_text.9.png")

    @allure.title("通信-短信-工具栏icon")
    def test_4(self, driver):
        common.click(driver, "工具栏icon")
        common.render(driver, 2)

    @allure.title("通信-短信-网络消息")
    def test_5(self, driver):
        common.click(driver, "网络消息")
        common.upload_pic(driver, "顶部横幅-音频播放背景", r"06 通信\短信\网络消息\mms_bg_im_audio_play_mode.9.png")
        common.upload_pic(driver, "网络消息橱窗背景（正常）", r"06 通信\短信\网络消息\mms_bg_push_message_default_shop_window_normal.9.png")
        common.upload_pic(driver, "网络消息橱窗背景（下按）", r"06 通信\短信\网络消息\mms_bg_push_message_default_shop_window_pressed.9.png")
        common.upload_pic(driver, "网络消息橱窗滑动内部背景（正常）", r"06 通信\短信\网络消息\mms_bg_push_message_inner_shop_window_normal.9.png")
        common.upload_pic(driver, "网络消息橱窗滑动内部背景（下按）", r"06 通信\短信\网络消息\mms_bg_push_message_inner_shop_window_pressed.9.png")
        common.upload_pic(driver, "普通push消息背景（正常）", r"06 通信\短信\网络消息\mms_bg_push_message_normal.9.png")
        common.upload_pic(driver, "普通push消息背景（下按）", r"06 通信\短信\网络消息\mms_bg_push_message_pressed.9.png")
        common.upload_pic(driver, "网络消息-快速回复按钮背景", r"06 通信\短信\网络消息\mms_bg_quick_button_container.9.png")
        common.upload_pic(driver, "卡片-背景-正常", r"06 通信\短信\网络消息\mms_bg_common_card_normal.9.png")
        common.upload_pic(driver, "卡片-背景-按压", r"06 通信\短信\网络消息\mms_bg_common_card_pressed.9.png")


if __name__ == '__main__':
    pytest.main("-v -s test_16通信-短信.py")
