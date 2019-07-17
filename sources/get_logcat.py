# -*- coding: utf-8 -*-
# 使用该方法后，手机端 logcat 缓存会清除归零，从新记录
# 建议每条用例执行完执行一边清理，遇到错误再保存减少陈余 log 输出
# Android
# logcat = self.driver.get_log('logcat')
#
# # iOS 需要安装 brew install libimobiledevice
# logcat = self.driver.get_log('syslog')
#
# # web 获取控制台日志
# logcat = self.driver.get_log('browser')
#
# c = '\n'.join([i['message'] for i in logcat])
# allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
#写入到 allure 测试报告中