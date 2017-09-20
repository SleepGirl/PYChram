# coding = utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome();
dr.maximize_window()
# url = 'http://expo.qifa.ru/presale.html'
# dr.get(url)
#
# a = dr.find_elements_by_css_selector("div.goods-bt > div > a")
# # s = dr.find_elements_by_tag_name(a)
# for i in range(len(a)):
#     print(a[i].get_attribute("href"))
# time.sleep(3)
# dr.quit()

url = 'http://expo.qifa.ru/brands'
dr.get(url)
links = dr.find_elements_by_css_selector("a.btn.btn-sm.btn-primary.pull-right")
time.sleep(2)
fo = open("articles.txt","r+")
for i in range(len(links)):
    fo.write(links[i].get_attribute("href")+"\n")
    # print(links[i].get_attribute("href"))
print(fo.name)
time.sleep(3)
dr.quit()