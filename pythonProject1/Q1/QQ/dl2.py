from selenium import webdriver
import time

class Fengzhuang():
    #选择Chrom驱动
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
    #隐式等待5秒
    def wait(self):
        self.driver.implicitly_wait(5)
    #打开网站
    def open(self,url):
        self.driver.get(url)
        self.wait()
        print("成功访问%s网站"%url)
    #搜索
    def ss(self,ssk,zhi):
        return self.driver.find_element(ssk,zhi)
    #定位标签页
    def dww(self):
        self.all = self.driver.window_handles
        self.driver.switch_to.window(self.all[-1])
    #定位框架
    def dwf(self,id):
        self.driver.switch_to.frame(id)
    #返回上一个框架
    def dwpf(self):
        self.driver.switch_to.parent_frame()
    #完成后关闭所有页面
    def __del__(self):
        time.sleep(4)
        self.driver.quit()
