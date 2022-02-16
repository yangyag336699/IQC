from selenium import webdriver
import time
from  selenium.webdriver import  ActionChains

driber = webdriver.Chrome()
driber.window_handles
driber.get('https://www.baidu.com/')
driber.maximize_window()
time.sleep(2)
driber.find_element_by_id('kw').send_keys('淘宝')
driber.find_element_by_id('su').click()
time.sleep(2)
driber.find_element_by_id('content_left')
driber.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(2)
driber.switch_to.window(driber.window_handles[-1])
time.sleep(2)
mylist = driber.find_elements_by_css_selector('li.J_Cat.a-all')

acobj = ActionChains(driber)
for el in  mylist:
    acobj.move_to_element('el').perform()
    time.sleep(3)
