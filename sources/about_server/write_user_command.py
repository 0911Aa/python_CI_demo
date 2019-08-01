# -*- coding: utf-8 -*-
'''
Created on 2018年10月25日

@author: uidq1501
'''
import yaml
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class WriteUserCommand:
    def read_data(self):
        """
        打开yaml文件
        :return: 文件内容data
        data是一个字典，里面又放了一个字典
        """
        with open(BASE_DIR+"/settings/userconfig.yaml") as fr:
            data = yaml.load(fr, Loader=yaml.FullLoader)
        return data
            
    def get_value(self,key,port):
        """

        :param key: 就是user_info_n
        :param port: 端口号
        :return:
        """
        data = self.read_data()
        if data and ('4' in data[key]['port']):
            value = data[key][port]
            return value
        
    def write_data(self,i, device, bp, port):
        """
        写入数据
        :param i: 设备的编号
        :param device:
        :param bp:
        :param port: 端口号
        :return:
        """
        data = self.join_data(i, device, bp, port)   #拼接数据
        # 例如：data = {"user_info_1":{"deviceName":"","bp":"","port":"4722"}}
        with open(BASE_DIR+"/settings/userconfig.yaml",'a') as fr:
            yaml.dump(data,fr)   #yaml序列化
        fr.close()
            
    def join_data(self,i,device,bp,port):
        '''
        拼接数据
        '''
        data = {
            "user_info_"+str(i):{
            "deviceName":device,
            "bp":bp,
            "port":port
            }
            }
        return data
    
    def clear_data(self):
        """
        清空数据
        :return:
        """
        with open(BASE_DIR+"/settings/userconfig.yaml",'w') as fr:
            fr.truncate()      #有点像sql里的truncate
        fr.close()

    def get_file_lines(self):
        """
        获取yaml文件的行数
        :return:
        """
        data = self.read_data()
        return len(data)

    def change_key(self,name):
        """
        修改yaml文件
        :param name:
        :return:
        """
        with open("../main_word/ROI.yaml",'r+') as fr:
            data = yaml.load(fr)
            y1 = data['key']['iy']
            x1 = data['key']['ix']
            y = data['key']['y']
            x = data['key']['x']
            data1 = {
                'key'+name:{
                    "ix":x1,
                    "iy":y1,
                    "x":x,
                    "y":y,
                    }  
                }
            yaml.dump(data1,fr)
            return data1
           

if __name__ == '__main__' :
    YQ = WriteUserCommand()
    # print (YQ.change_key('BT'))
    # print (YQ.get_value('user_info_'+str(0),'port'))
    # print (YQ.read_data()[key]['port'])
