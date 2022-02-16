from selenium import webdriver
import unittest
import time


class YC:
    def __init__(self):
        self.driber = webdriver.Chrome()
# 进入网页ID
        self.driber.get('https://www.baidu.com/')
        self.driber.maximize_window()
        time.sleep(3)

    def Taba1(self):
# 搜索内容
        self.driber.find_element_by_id('kw').send_keys('QQ邮箱')
        time.sleep(3)
        self.driber.find_element_by_id('su').click()
        time.sleep(7)

# 网页定位
        self.driber.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/h3/a[1]').click()
        time.sleep(5)

# 定位页面
    def Taba2(self):
        self.driber.switch_to.window(self.driber.window_handles[-1])
        self.driber.get('https://mail.qq.com/')
        time.sleep(5)

# 定位账户框架
        self.driber.switch_to.frame('login_frame')
        time.sleep(2)
        self.driber.find_element_by_class_name('switch_btn').click()
        time.sleep(1)

# 输入账户密码
        self.driber.find_element_by_id('u').send_keys('1449162076')
        self.driber.find_element_by_id('p').send_keys('yangyang336699')

# 登录
        self.driber.find_element_by_class_name('btn').click()
        time.sleep(3)

# 写信
        self.driber.find_element_by_id('composebtn').click()
        time.sleep(5)
# 定位框架
        self.driber.switch_to.frame('mainFrame')
# 输入收件人
        self.driber.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input').send_keys('850589644@qq.com')
        self.driber.find_element_by_id('subject').send_keys('美女')
# 添加附件
        self.driber.find_element_by_name('UploadFile').send_keys('C:\\11\mein.jpg')
# 点击发送
        self.driber.find_element_by_name('sendbtn').click()
        time.sleep(10)
        self.driber.quit()

if __name__ == '__main__':
    unittest.main()