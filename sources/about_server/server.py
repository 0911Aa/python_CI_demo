# -*- coding: utf-8 -*-
'''
Created on 2018年10月24日

@author: uidq1501
'''
from sources.about_server.dos_cmd import DosCmd
from sources.about_server.port import Port
import threading
from sources.about_server.write_user_command import WriteUserCommand
import time

class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_device()
        # self.device_list = ['1234567','12345']
        self.wf = WriteUserCommand()
        
    def get_device(self):
        """
        获得设备的udid列表
        :return:
        """
        devices_list = []
        self.dos.excute_cmd('adb start-server')
        result_list = self.dos.excute_cmd_result('adb devices')
        # print (result_list)
        if len(result_list)>=2 and '\tdevice' in result_list[-1]:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                # print(devices_info)
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self,start_port):
        '''
        创建可用端口
        '''
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port,self.device_list)
        return port_list
    
    def create_command_list(self,i):
        """
        创建appium启动命令，比如#appium -p 4723 -bp 4724 -U 00001234
        :param i:
        :return:
        """
        command_list = []
        appium_port_list = self.create_port_list(4000)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        command = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override"
        #appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test01.log
        command_list.append(command)
        self.wf.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))

        return command_list

    
    def start_server(self,i):
        """
        启动appium服务
        :param i:
        :return:
        """
        self.start_list = self.create_command_list(i)
        print (self.start_list)
        self.dos.excute_cmd(self.start_list[0])
    def kill_server(self):
        """
        关闭appium服务
        :return:
        """
        command = 'tasklist | find "node.exe"'
        server_list = self.dos.excute_cmd_result(command)
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')
            
    def main(self):
        thread_list = []
        self.kill_server()
        self.wf.clear_data()
        for i  in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(25)
                   
if __name__ == '__main__':
    server = Server()
    print (server.get_device())
    # # print(server.create_command_list(0))
    # server.main()