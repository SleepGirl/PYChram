from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.maximize_window()
url = "http://test3.qifa.ru/passport.html"
dr.get(url)
time.sleep(2)
dr.find_element_by_css_selector("#email").send_keys("458236511@qq.com")
a = dr.find_element_by_name("password").send_keys("111111")
dr.find_element_by_css_selector("#btn1").click()
time.sleep(3)
dr.quit()

