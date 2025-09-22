# -*- coding: utf-8 -*-
# @Time    : 2021-09-24 17:09
# @Author  : 何忠意
# @FileName: 1.py
# @Software: PyCharm

COLOR_LIST = {
    "1": "#666666",
    "2": "#666666",
    "3": "#666666",
    "4": "#666666",
    "5": "#666666",
    "6": "#666666",
    "7": "#666666",
    "8": "#666666",
    "9": "#666666",
    "10": "#666666",
    "11": "#666666",
    "12": "#666666",
    "13": "#666666",
    "14": "#666666",
    "15": "#666666",
    "16": "#666666",
    "17": "#666666",
    "18": "#666666",
    "19": "#666666",
    "20": "#666666",
    "21": "#666666",
    "22": "#666666",
    "23": "#666666",
    "24": "#666666",
    "25": "#666666",
    "26": "#666666",
    "27": "#666666",
    "28": "#666666",
    "29": "#666666",
    "30": "#666666",
    "31": "#666666",
    "32": "#666666",
    "33": "#666666",
    "34": "#666666",
    "35": "#666666",
    "36": "#666666"
}

PNG_ROOT = r"D:/EVA驾驶员款主题切图包/"  # 资源包根目录
THEME_NAME = "XXXX"  # 自定义主题名称
BACKGROUND_STYLE = "深色背景"  # 深色背景/浅色背景，二选一
COLORFUL_BATTERY = "否"  # 使用多彩电池。若有提供彩虹电池资源，则改为“是”。
USE_CUT_VIEW = "否"  # 是否使用切图
CUT_VIEW = "否"  # 是否切图
ICON_USE_COLOR = "是"  # 控制中心通知中心-开关-选择-图标是否使用颜色
SWITCH_BACKGROUND_USE_COLOR = "是"  # 控制中心通知中心-开关-选择-开关背景是否使用颜色
CONTROL_CENTER_THEME = "Theme1"  # 控制中心通知中心-模块全局设置-主题色
COMMUNICATION_THEME = "Theme1"  # 通信-模块全局设置-主题色
SETTING_THEME = "Theme1"  # 设置-模块全局设置-主题色

# --------------------------------------------------------------------------------以下无需改动-------------------------------------------------------------------------------- #
if BACKGROUND_STYLE == "深色背景":
    FOREGGROUND_STYLE = "白色"
    FOREGROUND_COLOR = "#FFFFFF"  # 深色背景白 浅色背景黑
elif BACKGROUND_STYLE == "浅色背景":
    FOREGGROUND_STYLE = "黑色"
    FOREGROUND_COLOR = "#000000"  # 深色背景白 浅色背景黑
else:
    raise ValueError("BACKGROUND_STYLE 填写错误！")
if COLORFUL_BATTERY not in ["是", "否"]:
    raise ValueError("COLORFUL_BATTERY 填写错误！")
if USE_CUT_VIEW not in ["是", "否"]:
    raise ValueError("USE_CUT_VIEW 填写错误！")
if CUT_VIEW not in ["是", "否"]:
    raise ValueError("CUT_VIEW 填写错误！")
if CONTROL_CENTER_THEME not in ["Theme1", "Theme2", "Theme3", "Theme4", "Theme5", "Theme6"]:
    raise ValueError("CONTROL_CENTER_THEME 填写错误！")
if ICON_USE_COLOR not in ["是", "否"]:
    raise ValueError("ICON_USE_COLOR 填写错误！")
if SWITCH_BACKGROUND_USE_COLOR not in ["是", "否"]:
    raise ValueError("SWITCH_BACKGROUND_USE_COLOR 填写错误！")
if COMMUNICATION_THEME not in ["Theme1", "Theme2", "Theme3", "Theme4", "Theme5", "Theme6"]:
    raise ValueError("COMMUNICATION_THEME 填写错误！")
if SETTING_THEME not in ["Theme1", "Theme2", "Theme3", "Theme4", "Theme5", "Theme6"]:
    raise ValueError("SETTING_THEME 填写错误！")

ROOT = r"D:/projects/WinAppUITest/"  # 项目根目录
OPPO_THEME_EDITOR = r"C:/Program Files/HeyTapThemeEditor/HeyTapThemeEditor.exe"  # OPPO编辑器的执行路径
RESOURCE = ROOT + "resource"
REPORT = ROOT + "report"
UPLOAD_IMAGE_EXE = RESOURCE + "/upload_image.exe"  # 上传图片exe
UPLOAD_ZIP_EXE = RESOURCE + "/upload_zip.exe"  # 上传zipexe
SERVER_URL = "http://127.0.0.1:4723"
PHOTOSHOP_EXE = RESOURCE + "/Adobe Photoshop CS6 (64 Bit)/Photoshop.exe"
PS_DIAN9_JSX = RESOURCE + "/ps_dian9.jsx"
PS_NOT_DIAN9_JSX = RESOURCE + "/ps_not_dian9.jsx"

DIAN9 = [
    [r"01 全局设置\栏\搜索栏\color_searchview_corner_rect_bg.9.png", 9],
    [r"01 全局设置\栏\工具栏\color_tool_navigation_view_bg.9.png", 1],
    [r"01 全局设置\弹窗\底部弹窗\color_bottom_alert_dialog_bg_portrait.9.png", 21],
    [r"01 全局设置\弹窗\底部弹窗\color_bottom_alert_dialog_bg_landscape.9.png", 21],
    [r"01 全局设置\弹窗\底部弹窗\coui_bottom_alert_dialog_bg.9.png", 21],
    [r"01 全局设置\弹窗\居中弹窗\color_center_alert_dialog_bg_no_orientation.9.png", 21],
    [r"01 全局设置\弹窗\更多浮层\color_popup_list_window_bg.9.png", 21],
    [r"01 全局设置\控件组件\Tips\color_tool_tips_background.9.png", 15],
    [r"01 全局设置\控件组件\列表详情\color_detail_floating_background.9.png", 15],
    [r"01 全局设置\控件组件\面板\color_panel_bg_without_shadow.9.png", 21],
    [r"06 通信\来电&通话\陌生号码来电挂机\incall_bg_numbermark.9.png", 21],
    [r"06 通信\联系人&拨号\拨号-无联系人\pb_bg_unavaliable_contact.9.png", 15],
    [r"06 通信\联系人&拨号\新建联系人\pb_bg_window.9.png", 15],
    [r"06 通信\联系人&拨号\拨号\pb_bg_dial_btn_normal.9.png", 2],
    [r"06 通信\联系人&拨号\拨号\pb_bg_dial_btn_pressed.9.png", 2],
    [r"06 通信\联系人&拨号\拨号\pb_bg_dialer.9.png", 15],
    [r"06 通信\联系人&拨号\拨号-通话记录\pb_bg_dial_header_tips.9.png", 15],
    [r"06 通信\联系人&拨号\拨号-通话记录\pb_bg_cloud_header.9.png", 15],
    [r"06 通信\联系人&拨号\联系人列表\pb_bg_not_transparent.9.png", 15],
    [r"06 通信\联系人&拨号\联系人列表\pb_bg_another_search_view.9.png", 15],
    [r"06 通信\短信\短信对话-气泡界面\1.9.png", 34],
    [r"06 通信\短信\短信对话-气泡界面\2.9.png", 35],
    [r"06 通信\短信\新建\mms_bg_bottom_menu.9.png", 15],
    [r"06 通信\短信\新建\mms_bg_chip.9.png", 15],
    [r"06 通信\短信\新建\mms_bg_compose_edit_text.9.png", 15],
    [r"06 通信\短信\网络消息\mms_bg_im_audio_play_mode.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_push_message_default_shop_window_normal.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_push_message_default_shop_window_pressed.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_push_message_inner_shop_window_normal.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_push_message_inner_shop_window_pressed.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_push_message_normal.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_push_message_pressed.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_quick_button_container.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_common_card_normal.9.png", 21],
    [r"06 通信\短信\网络消息\mms_bg_common_card_pressed.9.png", 21],
    [r"07 设置\搜索历史\oplus_toolbar_bg.9.png", 9],
    [r"08 音量\systemui_icon_volume_bg.9.png", 21]
]

NOT_DIAN9 = [
    [r"02 桌面\桌面文件夹\ic_launcher_page_point_focused.png", FOREGROUND_COLOR],
    [r"02 桌面\桌面文件夹\ic_launcher_folder.png", FOREGROUND_COLOR],
    [r"04 控制中心_通知中心\控制中心\开关\status_bar_qs_tile_bg_active.png", 20],
    [r"04 控制中心_通知中心\控制中心\开关\status_bar_qs_tile_bg_inactive.png", 21],
    [r"06 通信\联系人&拨号\拨号-通话记录\pb_dr_floating_dial_btn_normal.png", 2],
    [r"06 通信\联系人&拨号\拨号-通话记录\pb_dr_floating_dial_btn_pressed.png", 2],
]

NORMAL = [

]
# --------------------------------------------------------------------------------以下无需改动-------------------------------------------------------------------------------- #
