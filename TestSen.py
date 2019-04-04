import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from matplotlib import pyplot as plt



header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
parser = 'html.parser'
url = 'https://www.bilibili.com/blackboard/BDF2019-xy.html'
browser = webdriver.Chrome()
browser.get(url)
schools = browser.find_elements_by_xpath('//*[@id="bdf19"]/div/div[2]/div[2]/div')
schools.extend(browser.find_elements_by_xpath('//*[@id="bdf19"]/div/div[2]/div[3]/div/div'))
for school in schools:
    print(school.text)
browser.close()

