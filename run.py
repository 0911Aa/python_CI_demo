"""
@ Description：
"""
import pytest,os,subprocess,time
from sources.about_server.server import Server


def init_env():
    if os.path.exists('data'):
        cmd1 = 'rd/s/q data'
        subprocess.call(cmd1, shell=True)
    cmd2 = "xcopy /D reports\history data\history\ /e"

    time.sleep(2)
    subprocess.call(cmd2, shell=True)
    server = Server()
    server.main()


#     cmd = "python -m uiautomator2 init"
#     subprocess.call(cmd, shell=True)
#     logger.info("初始化运行环境!")

def init_report():
    cmd1 = "allure generate data -o reports --clean"
    cmd2 = "allure open -h 192.168.2.102 -p 8083 reports"

    subprocess.call(cmd1, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    print("报告地址:{}".format(report_path))
    subprocess.call(cmd2,shell=True)



init_env()
pytest.main(["-s","--reruns=2", "src/testcases","--alluredir=data"])
init_report()

#pytest -v 说明：可以输出用例更加详细的执行信息，比如用例所在的文件及用例名称等
#pytest -s 说明：输入我们用例中的调式信息，比如print的打印信息等
#pytest -m ”标记“ 说明：执行特定的测试用例,如下：
# @pytest.mark.run_this_testcase
# def testOpenUrl():
#     pass
# pytest -m run_this_testcase,就是mark后面的参数

#pytest -k "关键字" 说明：执行用例包含“关键字”的用例，比如：
# pytest -k 'OpenUrl'




