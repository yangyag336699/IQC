from  selenium import  webdriver

class BasePage:
    def __init__(self):
        self.aa = webdriver.Chrome()
        self.aa.get('https://www.baidu.com')

    def find_ele(self,*aa):
        ele = self.aa.find_element(*aa)
        return ele