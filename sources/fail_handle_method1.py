# -*- coding: utf-8 -*-
import allure
from functools import wraps
import datetime

def monitorapp(function):
    """
     用例装饰器，截图，日志，是否跳过等
     获取系统log，Android logcat、ios 使用syslog

     Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），
     为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
     写一个decorator的时候，最好在实现之前加上functools的wrap，
     它能保留原有函数的名称和docstring
    """

    @wraps(function)
    def wrapper(self, *args, **kwargs):
        try:
            allure.dynamic.description('用例开始时间:{}'.format(datetime.datetime.now()))
            function(self, *args, **kwargs)
            self.Action.driver.get_log('logcat')
        except Exception as E:
            f = self.Action.driver.get_screenshot_as_png()
            allure.attach(f, '失败截图', allure.attachment_type.PNG)
            logcat = self.Action.driver.get_log('logcat')
            c = '\n'.join([i['message'] for i in logcat])
            allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
            raise E
        finally:
            if self.Action.get_app_pid() != self.Action.Apppid:
                raise Exception('设备进程 ID 变化，可能发生崩溃')
    return wrapper