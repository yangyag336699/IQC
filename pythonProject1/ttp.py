from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test1(self):
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
        time.sleep(1)

    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('钢铁侠')
        self.driver.find_element_by_id('su').click()
        time.sleep(10)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__=='__main__':
    unittest.main()