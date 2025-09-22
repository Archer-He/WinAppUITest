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
    common.collapse(driver, "桌面壁纸")
    common.expand(driver, "图标")


@pytest.mark.usefixtures("init_feature")
@allure.feature("桌面")
class TestClass(object):

    @allure.title("桌面-图标-系统图标-静态")
    def test_1(self, driver):
        common.click(driver, "系统图标-静态")
        # common.multiple_upload(driver, r"02 桌面\图标\系统图标-静态\系统图标-静态.zip")  #人工处理

    @allure.title("桌面-图标-系统图标-动态")
    def test_2(self, driver):
        common.click(driver, "系统图标-动态")
        # common.multiple_upload(driver, r"02 桌面\图标\系统图标-动态\系统图标-动态.zip")  #人工处理
        common.set_color(driver, "日历图标内文字颜色", FOREGROUND_COLOR)

    @allure.title("桌面-图标-第三方图标")
    def test_3(self, driver):
        if common.get_attribute(driver, "第三方图标", "ExpandCollapse.ExpandCollapseState") == "LeafNode":
            common.click(driver, "第三方图标")
        common.click_by_xpath(driver, '//*[@Name="样板" and @LocalizedControlType="链接"]')
        # common.multiple_upload(driver, r"02 桌面\图标\第三方图标\样板\样板.zip")  #人工处理
        common.click_by_xpath(driver, '//*[@Name="图标" and @LocalizedControlType="链接"]')
        # common.multiple_upload(driver, r"02 桌面\图标\第三方图标\图标\图标.zip")  #人工处理

    @allure.title("桌面-图标-时钟插件")
    def test_4(self, driver):
        if common.get_attribute(driver, "时钟插件", "ExpandCollapse.ExpandCollapseState") == "LeafNode":
            common.click(driver, "时钟插件")
        common.click_by_xpath(driver, '//*[@Name="时钟插件" and @LocalizedControlType="链接"]')
        common.set_color(driver, "日期天气城市文字色", FOREGROUND_COLOR)
        common.render(driver, FOREGROUND_COLOR)


if __name__ == '__main__':
    pytest.main("-v -s test_07桌面-图标.py")
