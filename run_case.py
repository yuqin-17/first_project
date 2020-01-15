"""
run_case.py
批量执行测试用例,并且生成HTML格式的测试报
将HTMLTestRunnerPlugins放在python安装目录的Lib目录中
"""
import unittest
import HTMLTestRunner
import os
import time

# 1.初始化当前路径
# current_dir = os.path.dirname(os.path.realpath(__file__))
# print(current_dir)
# 2.添加测试用例路径
# case_dir = os.path.join(current_dir,'script')
case_dir = "./script"
# print(case_dir)
# 3.添加测试报告存放路径
# report_dir = os.path.join(current_dir,"report")
report_dir = "./report"
# print(report_dir)
# 4.将测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py")
# 5.命名测试报告名称
# 以时间格式命名报告名称
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_file_name = report_dir+'\\'+now + "report.html"
with open(report_file_name,"wb") as fp:
    runner = HTMLTestRunner.HTMLTestRunner(title="自动化测试报告",
                                           description="报告描述",
                                           stream=fp)
    runner.run(discover)

