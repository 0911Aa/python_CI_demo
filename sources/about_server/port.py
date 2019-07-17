# -*- coding: utf-8 -*-
'''
Created on 2018年10月24日

@author: uidq1501
'''
from sources.about_server.dos_cmd import DosCmd

class Port:
    def port_is_used(self,port):
        """
        判断端口是否被占用,注意端口号不是PID号
        :param port:
        :return: flog标识,被占用返回True，否则是False
        """
        flag = None
        self.dos = DosCmd()
        command = 'netstat -ano | findstr '+str(port)
        result = self.dos.excute_cmd_result(command)
        if len(result)>0:
            flag = True
        else:
            flag = False
        return flag
    
    def create_port_list(self,start_port,device_list):
        '''
        生成有用的端口，根据设备数量来生成对应个数
        参数：start_port
       参数: device_list
        '''
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port +1
            return port_list
        else:
            print ('生成可用端口失败')
            return None
              
if __name__ == '__main__':
    port = Port()
    print(port.port_is_used(8001))
    # li = [1,2,3]
    # print (port.create_port_list(4722,li))