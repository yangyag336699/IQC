from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

dropo=webdriver.Chrome()
dropo.get('https://www.baidu.com')
dropo.maximize_window()
time.sleep(3)
dropo.find_element(By.ID,'kw').send_keys('蜘蛛侠')
time.sleep(3)
dropo.quit()

s=True
try:
    dropo.find_element(By.ID,'kw')
    s=True
except NoSuchElementException:
    s=False
except Exception:
    s=False
print(s)

