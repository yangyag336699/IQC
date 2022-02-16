import unittest
import time
from ddt import ddt,data
from Q1.W1.oo import BaiduPage

@ddt
class BaiduTest(unittest.TestCase):

    @data('蜘蛛侠','钢铁侠')
    def test01(self,a):
        BaiduPage().search(a)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()