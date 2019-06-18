from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

# xx = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# yy = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)
xx = np.array([174,268,345,119,400,520,190,448,307,252], dtype=np.float64)
yy = np.array([8,10,15,7,22,31,15,20,11,9], dtype=np.float64)


def bestFitSlope(xx, yy):
    m = ((mean(xx) * mean(yy) - mean(xx * yy)) /
         (mean(xx)**2 - mean(xx**2)))
    return m


m = bestFitSlope(xx, yy)
print('m=',m)
b = mean(yy) - m * mean(xx)
print('b=',b)

x1 = (-1*b)/m
x2 = x1+600
y1 = 0
y2 = m*x2 + b

plt.plot([x1,x2],[y1,y2])
plt.scatter(xx, yy)
plt.show()
