# coding = utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("http://test.qifasilu.com/admin/login")
dr.find_element_by_css_selector("div:nth-child(3) > input").send_keys("shenhe")
dr.find_element_by_css_selector("div:nth-child(4) > input").send_keys("111111")
dr.find_element_by_id("login_btn").click()
time.sleep(3)
cookie = dr.get_cookies()
print(cookie)

time.sleep(2)
dr.quit()