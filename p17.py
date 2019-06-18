import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
newFeatures = [5,7]

def kNearestNeighbors(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('K is set to a value less than total voting groups!')

	distances = []
	for group in data:
		for features in data[group]:
			euclideanDistance = np.linalg.norm(np.array(features) - np.array(predict))
			distances.append([euclideanDistance, group])
	
	votes = [i[1] for i in sorted(distances)[:k]]
	print(Counter(votes).most_common(1))
	voteResult = Counter(votes).most_common(1)[0][0]

	return voteResult

result = kNearestNeighbors(dataset, newFeatures, k=3)
print(result)

[[plt.scatter(feature[0], feature[1], s=100, color=key) for feature in dataset[key]] for key in dataset]
plt.scatter(newFeatures[0],newFeatures[1])
plt.show()
