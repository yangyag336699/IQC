from selenium import webdriver
import time
import xlrd

dropk = webdriver.Chrome()  # 初始化游览器
dropk.maximize_window()  # 窗口最大化
deta = xlrd.open_workbook('C:\\Users/EDZ\\PycharmProjects\\pythonProject1\\shuju\\shujuqudong.xls')  # xls文件路径
aa = deta.sheet_by_name('Sheet1')  # 读取第一个工作表

list = []
for i in range(0,aa.nrows):  # 使用for循环输出所有数据
    list = aa.row_values(i)  # 读取工作表第一行
    break

print(list)
time.sleep(3)  # 强制暂停3秒

dropk.get(list[0])  #通过索引在excel表中获取百度URL
time.sleep(3)  # 强制暂停三秒

dropk.find_element_by_id(list[3]).send_keys(list[4])  #通过索引在excel表中获取百度输入框元素并输入要搜索的字段
time.sleep(3)  # 强制暂停三秒

dropk.find_element_by_id(list[7]).click()  #通过索引在excel表中获取百度点击“百度一下”元素并点击
time.sleep(3)  # 强制暂停3秒

list = []
for i in range(1,aa.nrows):  # 使用for循环输出所有数据
    list = aa.row_values(i)  # 读取excel第二行
    break
print(list)

dropk.find_element_by_css_selector(list[0]).click()  #跳转到“百度首页”
time.sleep(3)  # 强制暂停3秒
dropk.close()