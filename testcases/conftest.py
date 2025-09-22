# -*- coding: utf-8 -*-
# @Time    : 2021-09-24 17:09
# @Author  : 何忠意
# @FileName: 1.py
# @Software: PyCharm

from appium import webdriver
from selenium.common.exceptions import TimeoutException
import pytest
import subprocess
import time
import os
import sys
import shutil
import common
from config import *
import allure

_driver = None

@pytest.fixture(scope="session")
def driver():
    print("初始化...")
    # render_dian9()
    # render_not_dian9()
    try:
        p = subprocess.Popen(r' @taskkill /f /im Photoshop.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for line in p.stdout.readlines():
            print(line.decode(encoding="GB2312"))
        p = subprocess.Popen(r' @taskkill /f /im WinAppDriver.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for line in p.stdout.readlines():
            print(line.decode(encoding="GB2312"))
        p = subprocess.Popen(r' @taskkill /f /im HeyTapThemeEditor.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for line in p.stdout.readlines():
            print(line.decode(encoding="GB2312"))
        # 运行WinAppDriver进行监听127.0.0.1:4723
        p = subprocess.Popen(r'start "" /d "{}/Windows Application Driver/" "WinAppDriver.exe"'.format(RESOURCE), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line.decode(encoding="GB2312"))
    finally:
        sys.stdout.flush()
        sys.stderr.flush()

    print("启动oppo主题编辑器...")
    global _driver
    desired_caps = {}
    desired_caps["app"] = OPPO_THEME_EDITOR
    desired_caps["waitForAppLaunch"] = 25
    _driver = webdriver.Remote(command_executor=SERVER_URL, desired_capabilities=desired_caps)
    _driver.implicitly_wait(15)
    time.sleep(5)
    # common.click(_driver, "theme1")
    common.click(_driver, "新建主题")
    common.send_text(_driver, "请输入主题名称，不多于12字", THEME_NAME)
    common.click(_driver, "全局主题")
    common.click(_driver, "确定")
    yield _driver

    print("收尾清理环境...")
    time.sleep(1)
    _driver.quit()
    try:
        p = subprocess.Popen(r' @taskkill /f /im WinAppDriver.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for line in p.stdout.readlines():
            print(line.decode(encoding="GB2312"))
        p = subprocess.Popen(r' @taskkill /f /im HeyTapThemeEditor.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for line in p.stdout.readlines():
            print(line.decode(encoding="GB2312"))
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
    # remove_temp_dian9()
    # remove_temp_not_dian9()


def jsx_handler(dian9, png, color):
    # cur_dir = os.path.split(os.path.realpath(__file__))[0]
    temp = ROOT + "temp"
    if not os.path.exists(temp):
        os.makedirs(temp)
    temp_jsx = r"{}/{}.jsx".format(temp, round(time.time())).replace("\\", "/")
    try:
        for root, dirs, files in os.walk(temp):
            for file in files:
                print(file)
                os.remove(os.path.join(temp, file))
    except:
        print('删除失败')
    if dian9 == True:
        shutil.copy(PS_DIAN9_JSX, temp_jsx)
    elif dian9 == False:
        shutil.copy(PS_NOT_DIAN9_JSX, temp_jsx)
    else:
        raise TypeError("dian9参数不为布尔值！")
    lines = []
    with open(temp_jsx, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        f.close()
    with open(temp_jsx, 'w', encoding='UTF-8') as f:
        lines[0] = 'var png = "{}";\n'.format(png)
        lines[1] = 'var color = "{}";\n'.format(color)
        f.writelines(lines)
        f.close()
    return temp_jsx


# 使用photoshop脚本处理点九图，dian9=True处理点9图，dian9=False处理非点9图
def ps_handler(dian9, png, color):
    png = png.replace("\\", "/")
    color = color.replace("#", "")
    temp_jsx = jsx_handler(dian9, png, color).replace("/", "\\")
    temp_png = png + "副本.png"
    if os.path.exists(temp_png):
        os.remove(temp_png)
    try:
        print('执行"{}" "{}"'.format(PHOTOSHOP_EXE, temp_jsx))
        os.popen('"{}" "{}"'.format(PHOTOSHOP_EXE, temp_jsx))
        count = 0
        while True:
            count += 1
            if count > 10:
                raise TimeoutException
            if os.path.exists(temp_png):
                print("【JSX执行成功】生成副本：{}".format(temp_png))
                os.remove(temp_jsx)
                break
            else:
                time.sleep(2)
    except Exception as e:
        print(e)


# 渲染所有点九图
def render_dian9():
    print("对点九图进行颜色渲染...")
    for _ in DIAN9:
        png = (PNG_ROOT + _[0]).replace("\\", "/")
        if isinstance(_[1], int):
            color = COLOR_LIST[str(_[1])]
        elif isinstance(_[1], str):
            color = _[1]
        else:
            raise TypeError

        if not os.path.exists(png):
            raise FileNotFoundError("文件不存在！：{}".format(png))
        ps_handler(True, png, color)
    print("点九图渲染完毕")


# 删除所有点九图副本
def remove_temp_dian9():
    print("删除点九图副本...")
    for _ in DIAN9:
        png = _[0]
        png = (PNG_ROOT + png).replace("\\", "/")
        temp_dian9 = png + "副本.png"
        if os.path.exists(temp_dian9):
            os.remove(temp_dian9)
        else:
            print("文件不存在！：{}".format(temp_dian9))
    print("删除点九图副本完毕")


# 渲染所有非点九图
def render_not_dian9():
    print("对非点九图进行颜色渲染...")
    for _ in NOT_DIAN9:
        png = (PNG_ROOT + _[0]).replace("\\", "/")
        if isinstance(_[1], int):
            color = COLOR_LIST[str(_[1])]
        elif isinstance(_[1], str):
            color = _[1]
        else:
            raise TypeError

        if not os.path.exists(png):
            raise FileNotFoundError("文件不存在！：{}".format(png))
        ps_handler(False, png, color)
    print("点九图渲染完毕")


# 删除所有非点九图副本
def remove_temp_not_dian9():
    print("删除点九图副本...")
    for _ in NOT_DIAN9:
        png = _[0]
        png = (PNG_ROOT + png).replace("\\", "/")
        temp_dian9 = png + "副本.png"
        if os.path.exists(temp_dian9):
            os.remove(temp_dian9)
        else:
            print("文件不存在！：{}".format(temp_dian9))
    print("删除点九图副本完毕")


# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上，防止pytest-html报告中文乱码
#     """
#     for item in items:
#         item.name = item.name
#         item._nodeid = item.nodeid


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

# ps_handler(True, "D:/color_tool_navigation_view_bg.9.png","#ff0000")
# ps_handler(False, "D:/status_bar_qs_tile_bg_active.png", "#666666")
