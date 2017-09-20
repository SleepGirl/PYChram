from selenium import webdriver
import time

browser = webdriver.Chrome()

first_page = 'http://www.baidu.com'
browser.get(first_page)
print('access to %s' %(first_page))
time.sleep(2)


second_page = 'http://news.baidu.com/'
browser.get(second_page)
print('access to %s' % second_page)
time.sleep(3)

browser.back()
print('back to %s' %(first_page))
time.sleep(3)

browser.forward()
print('forward to %s' % (second_page))
time.sleep(2)
browser.quit()




