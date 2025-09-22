# WinAppUITest
本项目实现自动化的技术选型：**Python+Appium+WinAppDriver+Pytest+Allure+autoit+photoshop** ，解决windows上使用oppo编辑器自动化制作主题，使用pytest或者allure生成报告。

***
## 项目说明
本项目结合业务采用自动化为主+人工为辅的方式，每次批量跑完一次即可制作出一个oppo主题，然后人工检查报告里失败步骤并对主题对应位置进行修改，来完成制作。 用户只需要将每次制作主题的可选项、颜色、资源目录等改成最新的即可。

***
## 项目部署
- python安装3.8.5版本，参考 https://blog.csdn.net/qq_43543789/article/details/107933636
- pycharm安装，参考 https://www.cnblogs.com/yrhiwx/p/14906335.html
- allure已在项目resource部署
- ps已在项目resource部署
- winAppDriver已在项目resource部署（需要开启windows系统开发中选项）
- 上传exe已在项目resource部署
- 在桌面按win+R出现输入框后，输入cmd点击回车，在命令行窗口里输入以下安装python依赖包：  
    pip install allure-pytest==2.8.40  
    pip install allure-python-commons==2.8.40  
    pip install Appium-Python-Client==1.2.0  
    pip install pytest==6.2.2  
    pip install pytest-html==3.1.1  
    pip install pytest-metadata==1.11.0  
    pip install pytest-rerunfailures==10.1  
    pip install python-dateutil==2.8.1  
    pip install pywin32==227  
    pip install pywin32-ctypes==0.2.0  
    pip install pywinauto==0.6.8  
    pip install selenium==3.141.0  
- 打开pycharm，选择打开已有项目（路径里选择本项目根目录）即可
- 配置python解释器，参考 https://www.cnblogs.com/yrhiwx/p/14906335.html

***
## 项目结构
- report ====>> 存放pytest报告和allure报告
- resource ====>> photoshop、winappdriver驱动、autoit写的上传图片exe、jsx为ps脚本
  - Adobe Photoshop CS6 (64 Bit) ====>> ps目录
  - allure-2.13.9 ====>> allure目录
  - Windows Application Driver ====>> winAppDriver目录
  - ps_dian9.jsx ====>> 处理点9图的ps脚本
  - ps_not_dian9.jsx ====>> 处理非点9图的ps脚本  
  - upload_image.exe ====>> 上传图片的执行程序
  - upload_zip.exe ====>> 上传压缩包的执行程序
- temp ====>> 执行过程中生成的临时文件夹 
- testcases ====>> 主题制作步骤，按照模块划分不同的py文件
- common====>> 封装的windows自动化的方法
- config ====>> 配置文件
- run ====>> 执行全量脚本入口

***
## case说明
- @allure.feature("全局设置-主题色")====>>标记模块
- class TestClass(object): 
    - @allure.title("全局设置-主题色") ====>>标记标题
    - def test_1(self, driver): ====>>方法参数里固定写法，引入driver，同时如果不写self会导致未知错误
        - common.click(driver, name="全局设置") ====>>点击元素
        - common.set_color(driver, name="主色调-正常", color_num=2) ====>>修改对应元素上面的颜色
        - common.set_color(driver, name="次色调-按下", color_num=2, transparent=True) ====>>transparent=True时颜色后面加26表示透明
        - common.upload_pic(driver, name="底部弹窗背景图片", png=r"01 全局设置\弹窗\底部弹窗\coui_bottom_alert_dialog_bg.9.png") ====>>上传图片