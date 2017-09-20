#coding = utf-8

from selenium import webdriver

import time


dr = webdriver.Chrome()
dr.maximize_window()
url = 'http://test.qifasilu.com/admin/register'
dr.get(url)

# seleclang = dr.find_element_by_css_selector("button.btn.blue.cn")#ru class name 'btn default ru' 选择语言
# seleclang.click()

dr.find_element_by_css_selector(" li:nth-child(2) > a").click()
# Select(dr.find_element_by_css_selector("#business-province")).click()#选择省
dr.find_elements_by_css_selector("#business-province > option")[5].click()
time.sleep(2)
dr.find_elements_by_css_selector("#departments-branches_branch_id > option")[4].click()
time.sleep(20)


dr.quit()

