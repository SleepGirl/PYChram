from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('test1.html')
dr.get(file_path)

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
ckboxs = dr.find_elements_by_css_selector('input[type=checkbox]')

for checkbox in ckboxs:
    checkbox.click()
time.sleep(2)

print(len(dr.find_elements_by_css_selector('input')))

time.sleep(2)
dr.quit()
