from  selenium import  webdriver
import  unittest
import time

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("https://www.baidu.com/")
        cls.driver.maximize_window()

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('奥特曼')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)

    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('淘宝')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
