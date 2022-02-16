from selenium import webdriver
import time

class Mylib():

    def __init__(self):
        self.driver = webdriver.Chrome()  # 初始化浏览器对象

    def pi(self):
        self.driver.implicitly_wait(5)  # 延迟等待时间

    def ou(self,url):
        self.driver.get(url)  #访问网页
        self.pi()
        print('访问:%s成功'%url)

    def lo(self,mo,ko):
        return self.driver.find_element(mo,ko)

    def __del__(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    web = Mylib()
    web.ou('https://www.baidu.com/')
    el = web.lo('id','kw')
    el.send_keys('奥特曼')
    el_sub = web.lo('id','su')
    el_sub.click()