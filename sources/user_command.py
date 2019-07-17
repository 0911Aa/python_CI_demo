def adb_shell(self, command, args, includeStderr=False):
    """
    appium --relaxed-security 方式启动
    adb_shell('ps',['|','grep','android'])

    :param command:命令
    :param args:参数
    :param includeStderr: 为 True 则抛异常
    :return:
    """
    result = self.driver.execute_script('mobile: shell', {
        'command': command,
        'args': args,
        'includeStderr': includeStderr,
        'timeout': 5000
        })
    return result['stdout']