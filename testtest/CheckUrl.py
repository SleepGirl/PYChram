# coding = utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome()
fo = open("articles.txt")

for i in range(60):
    try:
        line = next(fo)
        dr.get(line)
        print(dr.title)
        time.sleep(3)
    except StopIteration:
        print(i)

fo.close()
dr.quit()

