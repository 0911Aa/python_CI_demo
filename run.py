"""
@ Description：
"""

import pytest,os,subprocess,time
from sources.about_server.server import Server
from settings import common_path
import sys
sys.path.append(common_path.project_path)


class Run:
    def __init__(self):
        self.project_path = common_path.project_path

    def init_env(self):
        if os.path.exists(self.project_path+'\data'):
            cmd1 = 'rd/s/q '+self.project_path+'\data'

            subprocess.call(cmd1, shell=True)
        cmd2 = "xcopy /D "+self.project_path+"\\reports\history "+self.project_path+"\data\history\ /e"
        time.sleep(2)
        subprocess.call(cmd2, shell=True)
        server = Server()
        server.main()


    #     cmd = "python -m uiautomator2 init"
    #     subprocess.call(cmd, shell=True)
    #     logger.info("初始化运行环境!")

    def init_report(self):
        cmd1 = "allure generate "+self.project_path+"\data -o "+self.project_path+"\\reports --clean"
        cmd2 = "allure open -h localhost -p 8083 "+self.project_path+"\\reports"

        subprocess.call(cmd1, shell=True)
        project_path = os.path.abspath(os.path.dirname(__file__))
        report_path = project_path + "/reports/" + "index.html"
        print("报告地址:{}".format(report_path))
        server = Server()
        server.kill_server()
        subprocess.call(cmd2,shell=True)


if __name__ == "__main__":
    run = Run()
    run.init_env()
    base_path = common_path.project_path
    pytest.main(["-s","--reruns=2", base_path+"/src/testcases","--alluredir="+base_path+"/data","-m=P1"])
    run.init_report()

#pytest -v 说明：可以输出用例更加详细的执行信息，比如用例所在的文件及用例名称等
#pytest -s 说明：输入我们用例中的调式信息，比如print的打印信息等
#pytest -m ”标记“ 说明：执行特定的测试用例,如下：
# @pytest.mark.run_this_testcase
# def testOpenUrl():
#     pass
# pytest -m run_this_testcase,就是mark后面的参数

#pytest -k "关键字" 说明：执行用例包含“关键字”的用例，比如：
# pytest -k 'OpenUrl'




