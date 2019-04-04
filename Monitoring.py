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

result = {}
timeAxis = []
color = {}
colors = ['#FFB90F', '#FF4500', '#FF00FF', '#B2DFEE', '#A020F0', '#8B5A2B', '#7FFF00', '#0F0F0F', '#8B2323', '#98FB98', '#B03060', '#BC8F8F', '#9FB6CD']
colerindex = 0
times = 2
fig = plt.figure()
plt.ion()
while 1:
    browser.get(url)
    timeAxis.append(int(time.strftime("%d%H%M%S", time.localtime())))
    time.sleep(25)
    schools = browser.find_elements_by_xpath('//*[@id="bdf19"]/div/div[2]/div[2]/div')
    for school in schools:
        strings = school.text.split('\n')
        name = strings[0]
        score = int(re.sub('\D','',strings[1]))
        if name not in result:
            result[name] = []
            result[name].append(score)
            color[name] = colors[colerindex]
            colerindex += 1
        else:
            result[name].append(score)
        print(name, score)
        plt.plot(timeAxis[-1], score, 'o', color=color[name])

    schools = browser.find_elements_by_xpath('//*[@id="bdf19"]/div/div[2]/div[3]/div/div')
    for school in schools:
        strings = school.text.split('\n')
        name = strings[1]
        score = int(re.sub('\D', '', strings[2]))
        if name not in result:
            result[name] = []
            result[name].append(score)
            color[name] = colors[colerindex]
            colerindex += 1
        else:
            result[name].append(score)
        print(name, score)
        plt.plot(timeAxis[-1], score, 'o', color=color[name])

    plt.show()
    plt.pause(5)


    with open('result.txt', 'w') as f:
        f.write(str(result))

    with open('timeAxis.txt', 'w') as f:
        f.write(str(timeAxis))

