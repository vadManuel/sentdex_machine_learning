from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# print(plt.style.available)
style.use('fivethirtyeight')

# xx = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# yy = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def createDataset(hm, variance, step=2, correlation=False):
    val = 1
    yy = []
    for _ in range(hm):
        y = val + random.randrange(-variance, variance)
        yy.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xx = [i for i in range(len(yy))]
    return np.array(xx, dtype=np.float64), np.array(yy, dtype=np.float64)


def bestFitSlopeAndIntercept(xx, yy):
    m = ((mean(xx) * mean(yy) - mean(xx * yy)) /
         (mean(xx) ** 2 - mean(xx ** 2)))
    b = mean(yy) - m * mean(xx)
    return m, b


def squaredError(yyOrig, yyLine):
    return sum((yyLine-yyOrig)**2)


def coefficientOfDetermination(yyOrig, yyLine):
    yMeanLine = [mean(yyOrig) for y in yyOrig]
    squaredErrorRegr = squaredError(yyOrig, yyLine)
    squaredErrorMean = squaredError(yyOrig, yMeanLine)
    return 1 - squaredErrorRegr/squaredErrorMean


xx, yy = createDataset(40, 30, 2, correlation='pos')

m, b = bestFitSlopeAndIntercept(xx, yy)

regressionLine = [m * x + b for x in xx]

predictX = 8
predictY = m * predictX + b

rSquared = coefficientOfDetermination(yy, regressionLine)
print(rSquared)

plt.scatter(predictX, predictY)

plt.scatter(xx, yy)
plt.scatter(predictX, predictY, s=100)
plt.plot(xx, regressionLine)
plt.show()
