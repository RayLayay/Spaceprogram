from sklearn.datasets import load_sample_image
import cv2

flower = load_sample_image('flower.jpg')
cv2.imshow('flower',flower)
cv2.waitKey(0)


# 使用线性回归绘制预测曲线

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slop, intercept, r, p, std_err = stats.linregress(x,y)  #返回线性回归的重要键值
print(r)     #r-squared，表示两个值之间的关联，r=0表示没有关联，r=1表示100%

def myfun(x):
    return slop * x + intercept

mymodel = list(map(myfun,x))

plt.scatter(x,y)

plt.plot(x,mymodel)

plt.show()


# 如果关联参数r值偏低，不适合使用线性回归进行预测，numpy还有多项式回归提供
# numpy.poly1d(polyfit(x,y,n))  x,y为两组数据，n则为多项式的幂指数

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x,y,3))  #建立预测模型

myline = np.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))

plt.show()

#可以使用sklearn中的模块，计算出两组数据之间的拟合度r

from sklearn.metrics import r2_score

print(r2_score(y,mymodel(x)))     #r值越高，拟合度越好