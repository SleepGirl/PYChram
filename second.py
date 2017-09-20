# coding = utf-8

from selenium import webdriver
import time

browser = webdriver.Chrome()

url = 'http://test.qifasilu.com/admin/login'

browser.get(url)
browser.maximize_window()  # 浏览器窗口最大化
tk = browser.find_element_by_css_selector("button.btn.blue.cn")  # ru class name 'btn default ru'
time.sleep(2)
tk.click()  # 选择语言
time.sleep(2)
browser.find_element_by_name("info[username]").send_keys("tomtian")  # 输入用户名
browser.find_element_by_name("info[password]").send_keys("111111")  # 输入密码
time.sleep(2)
browser.find_element_by_id("login_btn").click()  # 点击登录按钮
print(browser.current_url)

# print ("now access %s" %(url))
# browser.get(url)
# time.sleep(2)
# browser.set_window_size(400,480)
# time.sleep(5)
# print(browser.title)
# browser.quit()


