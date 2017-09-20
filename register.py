#coding = utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
import time

dr = webdriver.Chrome()
dr.maximize_window()

url = 'http://test.qifasilu.com/admin/register'
dr.get(url)
time.sleep(2)
seleclang = dr.find_element_by_css_selector("button.btn.blue.cn")#ru class name 'btn default ru' 选择语言
seleclang.click()

#填写基本资料
dr.find_element_by_id("admin-username").send_keys("testCN12")#填写用户名
dr.find_element_by_id("admin-password").send_keys("testCN12")# 填写密码
dr.find_element_by_id("contact-name").send_keys("ContactName")#填写联系人姓名
Select(dr.find_element_by_id("contact-sex")).select_by_value("2")#选择性别
#Select(dr.find_element_by_id("contact-sex")).select_by_index(2)
dr.find_element_by_id("contact-mobile").send_keys("18813096248")#填写电话
upload1=dr.find_element_by_xpath("//*[@id='tab1']/div[9]/div/div/div[2]/div/div[1]/span/input[2]")#上传头像
upload1.send_keys("D:\Moive\83b1OOOPIC20.jpg")
time.sleep(2)

#填写经营资质
dr.find_element_by_css_selector("li:nth-child(2) > a").click()#切换到经营资质tab
dr.find_element_by_id("business-cname").send_keys("牡丹")
Select(dr.find_element_by_id("business-province")).select_by_value("3")#选择省
# Select(dr.find_element_by_id("departments-branches_branch_id")).select_by_value("36") #选择市
dr.find_element_by_id("business-addr").send_keys("这里是经营地址的详细地址")#详细地址
uploads = dr.find_elements_by_css_selector(" span > input.file_buttom1")#上传经营资质图片
uploads[1].send_keys("D:\Moive\83b1OOOPIC20.jpg")
dr.find_element_by_id("w0").send_keys("2017/11/4")#填写营业执照有效日期
time.sleep(2)

#填写注册商标
dr.find_element_by_css_selector(" li:nth-child(3) > a").click()
rds = dr.find_elements_by_css_selector("label:nth-child(4) > span ")#全部选择
rds[0].click()
rds[1].click()
rds[2].click()
rds[3].click()
time.sleep(2)

#填写商品信息
dr.find_element_by_css_selector("li:nth-child(4) > a").click()#选择商品信息
chexs = dr.find_elements_by_css_selector(" label:nth-child(3) > span")
chexs[5].click()
chexs[6].click()
chexs[7].click()
chexs[8].click()
time.sleep(2)

#提交
dr.find_element_by_css_selector("div.row.border-2 > button").click()
print(dr.current_url)



# time.sleep(2)
# dr.quit()