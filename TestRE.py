from matplotlib import pyplot as plt

x = [1,2,2,4]
y = [3,2,5,3]
# fig = plt.figure()
# for i in range(4):
#     plt.plot(x[i],y[i],'o')
#     plt.pause(1)
# plt.show()

with open('result.txt', 'w') as f:
    f.write(str(x))

with open('result.txt', 'r') as f:
    x = f.read()
    print(isinstance(eval(x),list))

'//*[@id="bdf19"]/div/div[2]/div[2]/div[1]/header/div/div[3]/div[1]/span'
'//*[@id="bdf19"]/div/div[2]/div[3]/div/div[6]/header/div[3]/div[1]/span'
'//*[@id="bdf19"]/div/div[2]/div[3]/div/div[3]/header/div[3]/div[1]/span'