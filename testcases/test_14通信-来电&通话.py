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
    common.expand(driver, "来电&通话")


@pytest.mark.usefixtures("init_feature")
@allure.feature("通信")
class TestClass(object):

    @allure.title("通信-来电&通话-陌生号码来电挂机")
    def test_1(self, driver):
        common.click(driver, "陌生号码来电挂机")
        # TODO 颜色叠加，线性加深
        common.upload_pic(driver, "挂机弹窗背景-亮色", r"06 通信\来电&通话\陌生号码来电挂机\incall_bg_numbermark.9.png")


if __name__ == '__main__':
    pytest.main("-v -s test_14通信-来电&通话.py")
