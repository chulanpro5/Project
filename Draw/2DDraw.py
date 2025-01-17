import json
import matplotlib.pyplot as plt
import numpy as np
import time
import math
f = open('Data2D.json',)
Data = json.load(f)


clor = ['blue' , 'green' , 'red']
plt.title("Chuyển động sau khi xử lí")
plt.xlabel("x axis")
plt.ylabel("z axis")

testID = [60, 61, 62]

for id in testID:
    data = Data[id]
    x_number_list = []
    y_number_list = []
    
    tempX = data[4]['hands'][0]['palmPosition'][0]
    tempY = data[4]['hands'][0]['palmPosition'][2]
    for curData in data:
        
        x_number_list.append(curData['hands'][0]['palmPosition'][0] - tempX - 230)
        y_number_list.append(-curData['hands'][0]['palmPosition'][2] + tempY - 46)
        #x_number_list.append(curData['hands'][0]['palmPosition'][0])
        #y_number_list.append(-curData['hands'][0]['palmPosition'][2])

    print(x_number_list)
    print(y_number_list)
    id = id % 3
    plt.scatter(x_number_list, y_number_list, s = 100 , color = clor[id])

    coor = [-230 , -138 , -46 , 46 , 138 , 230]

    xx = [-230 , 230]
    yyy = [-230 , 230]
    for i in coor:
        yy = []
        xxx = []
        yy.append(i)
        yy.append(i)
        xxx = yy
        plt.plot(xx , yy , color = 'black')
        plt.plot(xxx , yyy , color= 'black')


plt.show()