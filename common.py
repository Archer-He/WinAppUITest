# -*- coding: utf-8 -*-
# @Time    : 2021-09-24 17:09
# @Author  : 何忠意
# @FileName: 1.py
# @Software: PyCharm

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import os
import win32api
import win32con
from ctypes import *
from config import *
import allure


# # 转换参数
# def format_by(name):
#     by_dict = {"id": "id", "xpath": "xpath", "name": "name", "tagname": "tag name", "classname": "class name", "automationid": "accessibility id"}
#     by, value = "", ""
#     parameters = locals()
#     for key in parameters.keys():
#         by = by_dict[key]
#         value = parameters[key]
#     return (by, value)


@allure.step("查看元素是否可见：{name}")
def is_element_visible(driver, name, timeout=1):
    """
    查看元素是否可见，返回bool值
    name：元素的name
    timeout：超时时长
    """
    print("查看是否可见：{}".format(name))
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(("name", name)))
        print("元素可见")
        return True
    except TimeoutException:
        print("元素不可见")
        return False


# @allure.step("获取元素：{name}")
def get_element(driver, name, timeout=2):
    """
    通过name获取元素
    name：元素的name
    timeout：超时时长
    """
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(("name", name)))
    return element


@allure.step("获取元素：{xpath}")
def get_element_by_xpath(driver, xpath, timeout=2):
    """
    通过xpath获取元素
    xpath：元素的xpath
    timeout：超时时长
    """
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(("xpath", xpath)))
    return element


@allure.step("获取元素列表：{name}")
def get_elements(driver, name, timeout=2):
    """
    通过name获取元素列表
    name：元素的name
    timeout：超时时长
    """
    print("获取元素列表：{}".format(name))
    elements = WebDriverWait(driver, timeout).until(lambda driver: driver.find_elements("name", name))
    return elements


@allure.step("获取元素列表：{xpath}")
def get_elements_by_xpath(driver, xpath, timeout=2):
    """
    通过xpath获取元素列表
    xpath：元素的xpath
    timeout：超时时长
    """
    print("获取元素列表：{}".format(xpath))
    elements = WebDriverWait(driver, timeout).until(lambda driver: driver.find_elements("xpath", xpath))
    return elements


def get_attribute(driver, name, attribute):
    """
    获取元素的属性值
    name：通过元素的name定位元素
    attribute：元素属性
    """
    e = get_element(driver, name)
    return e.get_attribute(attribute)


# 不支持appium自带的坐标点击方法tap
# def tap(driver, x, y,press_time=100):
#     print("点击坐标：({},{})".format(x,y))
#     driver.tap([(x, y)], press_time)


@allure.step("点击element：{element}")
def click_element(element):
    """
    点击元素
    element：元素
    """
    print("点击元素{}".format(element))
    element.click()


@allure.step("点击元素：{name}")
def click(driver, name, timeout=2):
    """
    通过name点击元素
    name：元素的name
    timeout：超时时长
    """
    print("点击元素：{}".format(name))
    element = get_element(driver, name, timeout)
    element.click()
    print('已点中')
    time.sleep(0.5)


@allure.step("点击元素：{xpath}")
def click_by_xpath(driver, xpath, timeout=2):
    """
    通过xpath点击元素
    xpath：元素的xpath
    timeout：超时时长
    """
    print("点击元素：{}".format(xpath))
    element = get_element_by_xpath(driver, xpath, timeout)
    element.click()
    print('已点中')
    time.sleep(0.5)


@allure.step("在 {name} 输入框输入：{text}")
def send_text(driver, name, text):
    """
    在输入框输入
    name：元素的name
    text：待输入的文本
    """
    e1 = get_element(driver, name)
    e1.clear()
    print("输入：{}".format(text))
    e1.send_keys(text)


@allure.step("移动到 {name} 处并滑动")
def swip(driver, name, step=-2000):
    """
    移动到要滑动的元素上，再上/下滑动
    name：元素的name
    step：负数下滑，正数上滑
    """
    print("先移动到要滑动的地方")
    ActionChains(driver).move_to_element(
        get_element(driver, name)).perform()
    print("滑动")
    # dwFlags -> 鼠标指令；dx -> 水平位移；dy -> 垂直位移；dwData-> 只有滑轮操作时才生效，否则建议设为0
    win32api.mouse_event(dwFlags=win32con.MOUSEEVENTF_WHEEL, dx=0, dy=0, dwData=step)


@allure.step("获取元素中心坐标：{element}")
def get_center(element):
    """
    获取元素中心坐标
    element：元素
    """
    size = element.size
    print(size)
    width = size['width']
    height = size['height']
    ele_coordinate = element.location  # 左上角坐标
    left_top_x = ele_coordinate['x']
    left_top_y = ele_coordinate['y']
    x = round(left_top_x + width / 2)  # 元素中心点横坐标
    y = round(left_top_y + height / 2)  # 元素中心点纵坐标
    # center = {"x": x, "y": y}
    return (x, y)


# TODO
def touch_action(driver, start_x, start_y, end_x, end_y):
    """
    通过坐标滑动，还未写好...
    """
    action = TouchAction(driver)
    action.press(start_x, start_y).move_to(end_x, end_y).release().perform()


@allure.step("鼠标移动到元素：{element}")
def move_to_element(driver, element):
    """
    鼠标移动到元素
    """
    print("鼠标移动到元素：({})".format(element.location))
    ActionChains(driver).move_to_element(element).perform()


@allure.step("鼠标移动到坐标：{x},{y}")
def move_to_location(x, y):
    """
    鼠标移动到坐标
    x：横坐标
    y: 纵坐标
    """
    print("鼠标移动到坐标：({},{})".format(x, y))
    windll.user32.SetCursorPos(x, y)
    time.sleep(0.5)


@allure.step("鼠标移动到坐标并点击：{x},{y}")
def move_to_location_and_click(x, y, times=1):
    """
    鼠标移动到坐标并点击
    x：横坐标
    y: 纵坐标
    times：1:表示单击，2表示双击
    """
    print("鼠标移动到坐标并点击{}次：({},{})".format(times, x, y))
    windll.user32.SetCursorPos(x, y)
    time.sleep(0.5)
    if isinstance(times, int):
        for i in range(times):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    else:
        raise ValueError("点击次数错误！")
    time.sleep(0.5)


@allure.step("设置颜色：{name},{color}")
def set_color(driver, name, color, transparent=False):
    """
    更改颜色
    name：更改颜色的元素name属性
    color: 可以传数字，或者直接传rgb值如#FFFFFF
    transparent：True表示透明在rgb值尾部加26
    """
    if color == None:
        raise ValueError
    if isinstance(color, int):
        color = COLOR_LIST[str(color)]
    elif isinstance(color, str):
        pass
    else:
        raise TypeError
    if transparent == True:
        color += "26"
    # 先移动鼠标到空白处，以免干扰到定位元素
    windll.user32.SetCursorPos(0, 0)
    time.sleep(0.5)
    element = get_element(driver, name)
    location = element.location  # 获取左上角坐标
    move_to_location_and_click(location["x"] + 9, location["y"] - 33)
    send_text(driver, name="HEX", text=color)
    click(driver, "确认")


@allure.step("更改颜色：{element},{color}")
def set_color_by_element(driver, element, color, transparent=False):
    """
    更改颜色
    element：存在多个相似的元素时，先获取其中特定元素，再更改颜色
    color: 可以传数字，或者直接传rgb值如#FFFFFF
    transparent：True表示透明在rgb值尾部加26
    """
    if color == None:
        raise ValueError
    if isinstance(color, int):
        color = COLOR_LIST[str(color)]
    elif isinstance(color, str):
        pass
    else:
        raise TypeError
    if transparent == True:
        color += "26"
    # 获取左上角坐标
    location = element.location
    move_to_location_and_click(location["x"] + 9, location["y"] - 33)
    send_text(driver, name="HEX", text=color)
    click(driver, "确认")


@allure.step("清理exe执行缓存")
def init_debug():
    """
    清理exe执行缓存
    """
    temp = ROOT + "temp"
    if not os.path.exists(temp):
        os.makedirs(temp)
    temp_txt = temp + "/debug.txt"
    if os.path.exists(temp_txt):
        os.remove(temp_txt)


@allure.step("上传图片：{name},{png}")
def upload_pic(driver, name, png):
    """
    上传图片
    name: 上传元素的name属性
    png：图片路径
    """
    print("开始上传图片...")
    if png == None:
        raise TypeError("png can't be None!")
    # 对于经过渲染的点9图，上传的是渲染后的副本
    for item in DIAN9 + NOT_DIAN9 + NORMAL:
        if png == item[0]:
            png = png + "副本.png"
            break
    png = (PNG_ROOT + png).replace("\\", "/").replace("/", "\\")
    if not os.path.exists(png):
        raise FileNotFoundError("文件不存在")
    # 聚焦到要上传图片的元素上
    click(driver, name)
    element = get_element(driver, name)
    location = element.location
    init_debug()
    temp_txt = ROOT + "temp/debug.txt"
    exe_code = '"{}" "{}" "{}"'.format(UPLOAD_IMAGE_EXE, png, temp_txt)
    # 移动到元素上方会出现“上传图片”并点击
    move_to_location_and_click(location["x"] + 45, location["y"] - 30)
    print("执行【EXE】：{}".format(exe_code))
    with os.popen(exe_code) as p:
        p.close()
        if os.path.exists(temp_txt):
            print("上传成功")
        else:
            raise FileNotFoundError("上传失败！")
    time.sleep(1)


@allure.step("上传图片：{element},{png}")
def upload_pic_by_element(driver, element, png):
    """
    上传图片，存在多个相似的元素时，先获取其中特定元素，再上传图片
    element: 获取到的特定元素
    png：图片路径
    """
    print("开始上传图片...")
    if png == None:
        raise TypeError("png can't be None!")
    # 对于经过渲染的点9图，上传的是渲染后的副本
    for item in DIAN9 + NOT_DIAN9 + NORMAL:
        if png == item[0]:
            png = png + "副本.png"
            break
    png = (PNG_ROOT + png).replace("\\", "/").replace("/", "\\")
    if not os.path.exists(png):
        raise FileNotFoundError("文件不存在")
    # 聚焦到要上传图片的元素上
    click_element(element)
    location = element.location
    init_debug()
    temp_txt = ROOT + "temp/debug.txt"
    exe_code = '"{}" "{}" "{}"'.format(UPLOAD_IMAGE_EXE, png, temp_txt)
    # 移动到元素上方会出现“上传图片”并点击
    move_to_location_and_click(location["x"] + 45, location["y"] - 30)
    print("执行【EXE】：{}".format(exe_code))
    with os.popen(exe_code) as p:
        p.close()
        if os.path.exists(temp_txt):
            print("上传成功")
        else:
            raise FileNotFoundError("上传失败！")
    time.sleep(1)


@allure.step("上传图片：{size},{png}")
def upload_pic_by_size(driver, size, png):
    """
    上传图片，编辑器有些地方是上传图片到对应尺寸
    size: 编辑器里的尺寸名
    png：图片路径
    """
    print("开始上传图片...")
    if png == None:
        raise TypeError("png can't be None!")
    # 对于经过渲染的点9图，上传的是渲染后的副本
    for item in DIAN9 + NOT_DIAN9 + NORMAL:
        if png == item[0]:
            png = png + "副本.png"
            break
    png = (PNG_ROOT + png).replace("\\", "/").replace("/", "\\")
    if not os.path.exists(png):
        raise FileNotFoundError("文件不存在")
    # 聚焦到要上传图片的元素上
    click(driver, size)
    element = get_element(driver, size)
    location = element.location
    init_debug()
    temp_txt = ROOT + "temp/debug.txt"
    exe_code = '"{}" "{}" "{}"'.format(UPLOAD_IMAGE_EXE, png, temp_txt)
    # 移动到元素上方会出现“上传图片”并点击
    move_to_location_and_click(location["x"] + 45, location["y"] - 60)
    print("执行【EXE】：{}".format(exe_code))
    with os.popen(exe_code) as p:
        p.close()
        if os.path.exists(temp_txt):
            print("上传成功")
        else:
            raise FileNotFoundError("上传失败！")
    time.sleep(1)


@allure.step("批量上传图片：{zip}")
def multiple_upload(driver, zip):
    """
    上传ZIP
    zip: 要上传的zip路径
    """
    print("批量上传图片...")
    if zip == None:
        raise TypeError("zip can't be None!")
    zip = (PNG_ROOT + zip).replace("\\", "/").replace("/", "\\")
    if not os.path.exists(zip):
        raise FileNotFoundError("文件不存在")
    init_debug()
    temp_txt = ROOT + "temp/debug.txt"
    exe_code = '"{}" "{}" "{}"'.format(UPLOAD_ZIP_EXE, zip, temp_txt)
    click(driver, "批量上传 ")
    print("执行【EXE】：{}".format(exe_code))
    with os.popen(exe_code) as p:
        p.close()
        if os.path.exists(temp_txt):
            print("批量上传成功")
        else:
            raise FileNotFoundError("批量上传失败！")
    if is_element_visible(driver, "下载报告", timeout=3):
        # 按下ESC退出错误提示弹窗
        win32api.keybd_event(27, 0, 0, 0)  # 按下ESC
        win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放ESC
        time.sleep(2)
        raise TypeError("导入图片规格错误！请手工操作")


@allure.step("图片渲染：{color}")
def render(driver, color=None):
    """
    oppo编辑器里的图片渲染
    color: 要渲染成的颜色
    """
    if color == None:
        raise ValueError
    if isinstance(color, int):
        color = COLOR_LIST[str(color)]
    elif isinstance(color, str):
        pass
    else:
        raise TypeError
    click(driver, "图片渲染 ")
    e1 = get_element(driver, "全选")
    (x,y) = get_center(get_element(driver, "渲染"))
    # 勾选全选
    if e1.get_attribute("Toggle.ToggleState") == "0":
        move_to_location_and_click(x - 100, y)
    # 点击颜色控件
    move_to_location_and_click(x - 55, y - 8)
    send_text(driver, "HEX", text=color)
    click(driver, "确认")
    click(driver, "渲染")
    # 等待渲染完毕
    count = 0
    while True:
        print("渲染中...")
        count += 1
        if count > 15:
            raise TimeoutException
        time.sleep(2)
        e2 = get_element(driver, "渲染")
        if e2.get_attribute("IsEnabled") == "true":
            break
    click(driver, "提交")


@allure.step("收起菜单项：{name}")
def collapse(driver, name):
    """
    收起菜单项
    name: 控件name
    """
    if get_attribute(driver, name, "ExpandCollapse.ExpandCollapseState") == "Expanded":
        element = get_element(driver, name)
        location = element.location
        move_to_location_and_click(location["x"] + 20, location["y"] + 20)


@allure.step("展开菜单项：{name}")
def expand(driver, name):
    """
    展开菜单项
    name: 控件name
    """
    if get_attribute(driver, name, "ExpandCollapse.ExpandCollapseState") == "LeafNode":
        click(driver, name)


@allure.step("截图：{path}")
def shot(driver, path):
    """
    截图
    path: 截图保存路径
    """
    driver.get_screenshot_as_file(path)

