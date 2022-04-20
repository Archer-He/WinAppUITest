# -*- coding: utf-8 -*-
# @Time    : 2021-09-24 17:09
# @Author  : 何忠意
# @FileName: 1.py
# @Software: PyCharm

import pytest
import os
import datetime
from config import *

# dir = os.path.dirname(__file__)
if not os.path.exists(REPORT):
    os.makedirs(REPORT)
timstamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
report_allure = (REPORT + "/allure/{}".format(timstamp)).replace("\\", "/")
report_allure_html = (REPORT + "/allure_html/{}".format(timstamp)).replace("\\", "/")
allure_path = RESOURCE + "/allure-2.13.9/bin/allure"

pytest.main(["-s", "--alluredir={}".format(report_allure), "testcases/test_01全局设置-主题色.py"])
os.system("{} generate {} -o {} --clean".format(allure_path, report_allure, report_allure_html))

