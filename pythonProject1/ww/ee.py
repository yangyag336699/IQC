from selenium import webdriver
import unittest
import time

class YY(unittest.TestCase):
    def setUp(self):
        self.derind = webdriver.Chrome()
        self.derind.get('https://www.baidu.com/')
        self.derind.maximize_window()
        time.sleep(5)

    def testQ1(self):
        self.derind.find_element_by_id('kw').send_keys('QQ邮箱')
        time.sleep(3)
        self.derind.find_element_by_id('su').click()
        self.driber.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/h3/a[1]').click()
        time.sleep(2)
        self.driber.switch_to.window(self.driber.window_handles[-1])
        self.driber.get('https://mail.qq.com/')
        time.sleep(5)
        self.derind.switch_to.frame('login_frame')
        time.sleep(3)
        self.derind.find_element_by_class_name('switch_btn').click()
        time.sleep(3)
        self.derind.find_element_by_id('u').send_keys('1449162076')
        self.derind.find_element_by_id('p').send_keys('yangyang336699')
        self.derind.find_element_by_class_name('btn').click()
        time.sleep(3)
        self.derind.find_element_by_id('composebtn').click()
        time.sleep(3)
        self.derind.switch_to.frame('mainFrame')
        self.derind.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input').send_keys('850589644@qq.com')
        self.derind.find_element_by_id('subject').send_keys('美女')
        self.derind.find_element_by_name('UploadFile').send_keys('C:\\11\mein.jpg')
        self.derind.find_element_by_name('sendbtn').click()
    def tearDown(self):
        time.sleep(3)
        self.derind.quit()

if __name__=='__main__':
    unittest.main()