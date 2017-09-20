from selenium import webdriver

dr = webdriver.Firefox()
url = 'www.baidu.com'
dr.get("https://www.baidu.com/")