# -*- coding: utf-8 -*-

import pytest,time,allure
from sources.get_driver import DriverClient
from sources.read_config import ReadIni

read_ini = ReadIni()

class TestSetting:
    def setup_class(cls):
        print('播放器初始化')
        cls.Action = DriverClient().Action
        cls.Action.launchApp(read_ini.get_value('player_app'))

    def teardown_class(cls):
        print('case结束')
        if cls.Action:
            cls.Action.clear()

    def test_play_music(self):
        self.Action.find_element(read_ini.get_value('play/pause_btn'),'播放/暂停键').click()
        self.Action.sleep(10)
        self.Action.click(read_ini.get_value('play/pause_btn'),'播放/暂停键')