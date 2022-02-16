from  selenium import webdriver

class BasePage:
    def __init__(self):
        self.zz= webdriver.Chrome
        self.zz.get('https://www.baidu.com')

    def find_ele(self,zz):
        ele=self.zz.find_element(*zz)
        return (ele)
