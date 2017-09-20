# coding = utf-8

from selenium import webdriver


def login():
    dr = webdriver.Chrome()
    dr.maximize_window()
    url = 'http://test.qifasilu.com/admin/login'
    dr.get(url)