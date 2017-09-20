from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.maximize_window()

url = 'http://test.qifasilu.com/admin/reg'
dr.get(url)
time.sleep(3)
#dr.find_elements_by_css_selector('#drow-language > li:nth-child(2)').click()  # 切换俄语

# 登录信息
dr.find_element_by_id("admin-username").send_keys("test2903")  # 填写登录名
dr.find_element_by_id("admin-password").send_keys("test2903")  # 填写密码
dr.find_element_by_id("admin-passwordrepeat").send_keys("test2903")  # 确认密码
dr.find_element_by_css_selector("div.form-group.reg_foot > div > button").click()  # 点击下一步
time.sleep(3)
print(dr.current_url)

# 联系人信息
dr.find_element_by_css_selector("#admininfo-contact_name").send_keys("test person")  # 联系人名字
dr.find_element_by_css_selector("#admininfo-contact_mobile").send_keys("18813096248")  # 联系人手机号
dr.find_element_by_css_selector("#admininfo-contact_email").send_keys("11@qq.cn")  # 邮箱
dr.find_elements_by_css_selector("div > button:nth-child(2)")[0].click()  # 点击下一步
time.sleep(3)
print(dr.current_url)

# 经营资质
dr.find_element_by_id("admincompanycn-company_name").send_keys("沙漏2")  # 公司名称
dr.find_elements_by_css_selector("#admincompanycn-company_province > option")[5].click()  # 经营地址省
time.sleep(2)
dr.find_elements_by_css_selector("#admincompanycn-company_city > option")[2].click()  # 经营地址市
dr.find_element_by_id("admincompanycn-company_address").send_keys("测试详细地址")  # 填写详细地址
dr.find_elements_by_css_selector("div > button:nth-child(2)")[1].click()  # 点击下一步
time.sleep(3)
print(dr.current_url)

# 商标信息
dr.find_element_by_id("admintrademark-0-trademark_name").send_keys("测试商标名称")  # 商标名称
dr.find_element_by_id("admintrademark-0-trademark_owner").send_keys("测试商标人名")  # 商标人名
uploads = dr.find_elements_by_css_selector("span > input.file_buttom1")  # 上传图片
# uploads[0].send_keys("D:\Moive\83b1OOOPIC20.jpg")
uploads[1].send_keys("D:\Moive\wh1200.jpg")
dr.find_element_by_id("admintrademark-0-trademark_expire").send_keys("2018/11/4")  # 填写时间
time.sleep(7)
dr.find_element_by_css_selector("div > button.btn.btn-info").click()  # 提交注册
time.sleep(4)
dr.quit()