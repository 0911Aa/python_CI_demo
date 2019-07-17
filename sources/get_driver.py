# -*- coding: utf-8 -*-

from appium import webdriver
import time
# from util.write_user_command import WriteUserCommand
from sources.action import ElementActions
# class DriverClient():
# #
# #     def init_driver(self):
# #         udid = 'RJCDU17529000254'
# #         desired_caps = {
# #             # udid adb devices
# #             "platformName": "Android",
# #             "platformVersion": "8.1.0",
# #             "deviceName": "android",
# #             "udid": udid,
# #             "noReset": 'true',  # 不重复安装APP
# #             "appActivity": ".HWSettings",
# #             "appPackage": "com.android.settings",
# #             'newCommandTimeout': '300',
# #         }
# #         host = "http://localhost:4723/wd/hub"
# #         driver = webdriver.Remote(host, desired_caps)
# #         Action = ElementActions(driver, desired_caps)
# #         return Action
# #
# # if __name__ == '__main__':
# #     driver = DriverClient()
# #     action = driver.init_driver()
# #     action.click("//android.widget.TextView[@text='设备连接']",'蓝牙')

class Singleton(object):
    """单例
    ElementActions 为自己封装操作类"""
    Action = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            udid = 'RJCDU17529000254'
            desired_caps = {
                # udid adb devices
                "platformName": "Android",
                "platformVersion": "8.1.0",
                "deviceName": "android",
                "udid": udid,
                "noReset": 'true',  # 不重复安装APP
                "appActivity": ".HWSettings",
                "appPackage": "com.android.settings",
                'newCommandTimeout': '300',
            }
            host = "http://localhost:4723/wd/hub"
            driver = webdriver.Remote(host, desired_caps)
            Action = ElementActions(driver, desired_caps)
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.Action = Action
        return cls._instance

class DriverClient(Singleton):
    pass

if __name__ == 'main__':
    Action = DriverClient().Action
    setting = "//android.widget.TextView[@content-desc='设置']"
    Action.click(setting, '设置')