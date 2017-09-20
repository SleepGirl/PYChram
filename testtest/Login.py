# coding = utf-8

from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.maximize_window()
url = 'http://test.qifasilu.com/admin/login'
dr.get(url)
#登陆
dr.find_element_by_css_selector("div:nth-child(3) > input").send_keys("qifadmin")
dr.find_element_by_css_selector("div:nth-child(4) > input").send_keys("qifa1234")
dr.find_element_by_id("login_btn").click()

time.sleep(3)
url1 = 'http://test.qifasilu.com/admin/goods-view/index'
print(url1)
dr.get(url1)

time.sleep(3)

cookie = dr.get_cookies()
print(cookie)

time.sleep(3)
dr.quit()



