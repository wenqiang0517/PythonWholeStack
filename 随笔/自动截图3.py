# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


def get_image(url, pic_name):
    # chromedriver的路径
    chromedriver = r"C:\Users\name\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # 设置chrome开启的模式，headless就是无界面模式
    # 一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    # 控制浏览器写入并转到链接
    driver.get(url)
    time.sleep(1)
    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width, height)
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    time.sleep(1)
    # 截图并关掉浏览器
    driver.save_screenshot(pic_name)
    driver.close()


# 你输入的参数
url = 'https://movie.douban.com/top250'
pic_name = r'./image.png'
get_image(url, pic_name)
