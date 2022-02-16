from selenium.webdriver.common.by import By
from pp import BasePage
import time

class BaiduPage(BasePage):
    ww = (By.ID, 'kw')
    ee = (By.ID, 'su')

    def get_text_obj(self):
        ele = self.find_ele(*BaiduPage.ww)
        return ele

    def get_submit_obj(self):
        ele = self.find_ele(*BaiduPage.ee)
        return ele

    def search(self,search_string):
        self.get_text_obj().send_keys(search_string)
        self.get_submit_obj().click()
        time.sleep(3)
