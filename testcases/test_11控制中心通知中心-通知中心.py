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
    common.collapse(driver, "控制中心")
    common.expand(driver, "通知中心")


@pytest.mark.usefixtures("init_feature")
@allure.feature("控制中心通知中心")
class TestClass(object):

    @allure.title("控制中心通知中心-通知中心-通知中心")
    def test_1(self, driver):
        common.click_by_xpath(driver, '//*[@Name="通知中心" and @LocalizedControlType="链接"]')
        common.set_color(driver, "通知图标收纳视图背景", 21)
        common.set_color(driver, "标准通知背景", 21)
        common.set_color(driver, "横幅通知背景颜色", 21)
        common.set_color(driver, "通知侧滑菜单背景", 21)
        common.set_color(driver, "锁屏通知背景", 21)

    @allure.title("控制中心通知中心-通知中心-音乐")
    def test_2(self, driver):
        common.click(driver, "音乐")
        common.set_color(driver, "通知栏歌曲名称文案颜色以及主标题颜色-R", 12)
        common.set_color(driver, "通知栏歌手名称文案颜色-R", 12)


if __name__ == '__main__':
    pytest.main("-v -s test_11控制中心通知中心-通知中心.py")
