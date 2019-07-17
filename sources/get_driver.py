# -*- coding: utf-8 -*-

from appium import webdriver
import time
from sources.about_server.write_user_command import WriteUserCommand
from sources.action import ElementActions
#
#
# class BaseDriver:
#     def desired_setting(self, i):
#         self.WF = WriteUserCommand()
#         udid = self.WF.get_value('user_info_' + str(i), 'deviceName')
#         port = self.WF.get_value('user_info_' + str(i), 'port')
#         desired_caps = {
#             "platformName": "Android",
#             "platformVersion": "8.1.0",
#             "deviceName": "android",
#             "udid": udid,
#             "noReset": 'true',  # 不重复安装APP
#             "appActivity": ".HWSettings",
#             "appPackage": "com.android.settings",
#             'newCommandTimeout': '300',
#             #       "automationName":"UIAutomator2"
#         }
#         driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", desired_caps)
#         Action = ElementActions(driver, desired_caps)
#         return Action
#
# if __name__ == '__main__':
#     Action = BaseDriver().desired_setting(0)
#     setting = "//android.widget.TextView[@text='设置']"
#     BT_home = "//*[@text='蓝牙、打印']"
#     Action.click(setting, '设置')
#     Action.click(BT_home, 'bt')
class Singleton(object):
    """单例
    ElementActions 为自己封装操作类"""
    Action = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls.WF = WriteUserCommand()
            udid = cls.WF.get_value('user_info_0','deviceName')
            port = cls.WF.get_value('user_info_0','port')
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
            host = "http://127.0.0.1:"+port+"/wd/hub"
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