from selenium import webdriver
import time

driber = webdriver.Chrome()
driber.window_handles

# 进入网页ID
driber.get('https://www.baidu.com/')
driber.maximize_window()
time.sleep(2)

# 搜索内容
driber.find_element_by_id('kw').send_keys('QQ邮箱')
time.sleep(3)
driber.find_element_by_id('su').click()
time.sleep(3)

# 网页定位
driber.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/h3/a[1]').click()
time.sleep(2)

# 定位页面
driber.switch_to.window(driber.window_handles[-1])
driber.get('https://mail.qq.com/')
time.sleep(2)

# 定位账户框架
driber.switch_to.frame('login_frame')
time.sleep(2)
driber.find_element_by_class_name('switch_btn').click()
time.sleep(1)

# 输入账户密码
driber.find_element_by_id('u').send_keys('1449162076')
driber.find_element_by_id('p').send_keys('')

# 登录
driber.find_element_by_class_name('btn').click()
time.sleep(3)

# 写信
driber.find_element_by_id('composebtn').click()
time.sleep(5)
# 定位框架
driber.switch_to.frame('mainFrame')
# 输入收件人
driber.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input').send_keys('452990633@qq.com')
driber.find_element_by_id('subject').send_keys('美女')
# 添加附件
driber.find_element_by_name('UploadFile').send_keys('C:\\11\mein.jpg')
# 点击发送
driber.find_element_by_name('sendbtn').click()