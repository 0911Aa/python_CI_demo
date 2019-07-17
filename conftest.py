# -*- coding: utf-8 -*-
"""
@ Description：Pytest hook Appium

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址
# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""
import os,sys,subprocess,pytest,datetime,allure
from sources.get_driver import DriverClient
sys.path.append('..')



# 当设置autouse为True时,
    # # 在一个session内的所有的test都会自动调用这个fixture
# 该函数需要放置在 conftest.py, pytest 运行时会自动拾取
# @pytest.fixture()
# def driver_setup(request):
#     request.instance.Action = DriverClient().init_driver()
#     print('driver初始化')
#     def driver_teardown():
#         request.instance.Action.clear()
#         print('退出')
#     request.addfinalizer(driver_teardown)

# def pytest_runtest_call(item):
#     # 每条用例代码执行之前，非用例执行之前
#     allure.dynamic.description('用例开始时间:{}'.format(datetime.datetime.now()))
#     Action = DriverClient().Action
    # if Action.get_app_pid() != Action.apppid:
    #     raise Exception('设备进程 ID 变化，可能发生崩溃')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 用例报错捕捉
    Action = DriverClient().Action
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        f = Action.driver.get_screenshot_as_png()
        allure.attach(f, '失败截图', allure.attachment_type.PNG)
        logcat = Action.driver.get_log('logcat')
        c = '\n'.join([i['message'] for i in logcat])
        allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
        # if Action.get_app_pid() != Action.apppid:
        #     raise Exception('设备进程 ID 变化，可能发生崩溃')
