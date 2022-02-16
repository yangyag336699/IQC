from ww import HTMLTestRunnerCN
import unittest

#文件路径
Testcase_dir = 'C:\\Users\\EDZ\\PycharmProjects\\pythonProject1\\ww'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'ee.py')
# 定义报告存放路径
filename = "C:\\Users\\EDZ\\PycharmProjects\\pythonProject1\\rr\\result.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
    # 运行测试用例
runner.run(dis)

