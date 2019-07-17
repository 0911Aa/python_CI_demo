# -*- coding: utf-8 -*-
'''
Created on 2018年10月24日

@author: uidq1501
'''
import os

class DosCmd:
    def excute_cmd_result(self,command):
        """
        需要拿到返回值的dos命令
        :param command:
        :return: dos命令的返回值
        """

        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i =='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def excute_cmd(self,command):
        """
        不需要拿到返回值的dos命令
        :param command:
        :return:
        """
        os.system(command)
        
if __name__ == '__main__':
    dos = DosCmd()
    print(len(dos.excute_cmd_result('adb devices')))
    print (dos.excute_cmd_result('adb devices'))
