from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# print(plt.style.available)
style.use('fivethirtyeight')

xx = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
yy = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

def bestFitSlopeAndIntercept(xx, yy):
	m = ((mean(xx) * mean(yy) - mean(xx * yy)) /
		 (mean(xx)** 2 - mean(xx ** 2)))
	b = mean(yy) - m * mean(xx)
	return m, b
	
def squaredError(yyOrig, yyLine):
	return sum((yyLine-yyOrig)**2)

def coefficientOfDetermination(yyOrig, yyLine):
	yMeanLine = [mean(yyOrig) for y in yyOrig]
	squaredErrorRegr = squaredError(yyOrig, yyLine)
	squaredErrorMean = squaredError(yyOrig, yMeanLine)
	return 1 - squaredErrorRegr/squaredErrorMean

m,b = bestFitSlopeAndIntercept(xx, yy)

regressionLine = [m * x + b for x in xx]

predictX = 8
predictY = m * predictX + b

rSquared = coefficientOfDetermination(yy, regressionLine)
print(rSquared)

plt.scatter(predictX, predictY)

plt.scatter(xx, yy)
plt.plot(xx, regressionLine)
plt.show()
