def adb_shell(self, command, args, includeStderr=False):
    """
    appium --relaxed-security ��ʽ����
    adb_shell('ps',['|','grep','android'])

    :param command:����
    :param args:����
    :param includeStderr: Ϊ True �����쳣
    :return:
    """
    result = self.driver.execute_script('mobile: shell', {
        'command': command,
        'args': args,
        'includeStderr': includeStderr,
        'timeout': 5000
        })
    return result['stdout']