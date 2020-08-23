
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

#自动收集测试用例
testcase = unittest.defaultTestLoader.discover('case','test_*.py')

#自动运行case并生成报告
file_path = 'report/report.html'
title = '测谈网web自动化测试测试报告'
descr = '这是测谈网web自动化测试描述v1'

with open(file_path,'wb') as f:
    runner = HTMLTestRunner(stream=f,title=title,description=descr)
    runner.run(testcase)