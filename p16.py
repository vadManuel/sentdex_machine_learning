import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
newFeatures = [5,7]

# [[plt.scatter(feature[0], feature[1], s=100, color=key) for feature in dataset[key]] for key in dataset]
# plt.scatter(newFeatures[0],newFeatures[1])
# plt.show()

def kNearestNeighbors(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('K is set to a value less than total voting groups!')

	# knnalgos
	# return voteResults
	pass