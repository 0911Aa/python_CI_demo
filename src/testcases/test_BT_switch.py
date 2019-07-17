# -*- coding: utf-8 -*-

import pytest,time,allure,sys
from sources.get_driver import DriverClient
from sources.read_config import ReadIni

read_ini = ReadIni()


class TestSetting:
    def setup_class(cls):
        print('初始化')
        cls.Action = DriverClient().Action

    # def teardown_class(cls):
    #     print('case结束')
    #     if cls.Action:
    #         cls.Action.clear()

    @allure.feature('BT_test')
    def test_BT(self):
        self.Action.home()
        self.Action.click(read_ini.get_value("setting"),'设置')
        self.Action.sleep(2)
        self.Action.click(read_ini.get_value("BT_home"),'蓝牙主界面')
        self.Action.click(read_ini.get_value("BT"),'蓝牙')
        self.Action.find_element(read_ini.get_value("BT_switch"),'蓝牙开关')
        self.Action.sleep(5)

    @allure.feature('BT_test')
    @allure.story('蓝牙开关测试')
    def test_BT_switch(self):
        for i in range(10):
            self.Action.click(read_ini.get_value("BT_switch"),'蓝牙开关')
            self.Action.sleep(10)
            self.Action.click(read_ini.get_value("BT_switch"), '蓝牙开关')
            i+=1

    @allure.feature('Power_test')
    def test_power(self):
            self.Action.home()
            self.Action.click(read_ini.get_value("setting"),'设置')
            self.Action.click(read_ini.get_value("power"),'电池')

    @allure.feature('WiFi_test')
    def test_wifi(self):
        self.Action.home()
        self.Action.click(read_ini.get_value("setting"),'设置')
        self.Action.click(read_ini.get_value("wifi_home"),'wifi')

