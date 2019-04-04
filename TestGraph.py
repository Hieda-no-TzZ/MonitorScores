from matplotlib import pyplot as plt
import numpy as np
d = {'哈尔滨工业大学': ['121197', '121197'], '深圳市宝安中学': ['116916', '116985'], '同济大学': ['60795', '60795'], '西北工业大学': ['451553', '451553'], '上海交通大学': ['540340', '540340'], '大连外国语大学': ['638136', '638136'], '中国传媒大学': ['735056', '735056'], '中南大学': ['816852', '816852'], '中国海洋大学': ['916794', '916794']}
time = ['17:49:59', '16:50:30']
fig = plt.figure()
plt.ion()

for t in range(len(time)):
    for sch in d:
        plt.legend(d[sch])
        print(time[t], int(d[sch][t]))
        plt.plot(time[t], int(d[sch][t]),'o', color='#FF00FF')
        plt.show()
        plt.pause(1)

plt.show()