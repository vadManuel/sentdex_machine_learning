import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd
import random


def kNearestNeighbors(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('K is set to a value less than total voting groups!')

	distances = []
	for group in data:
		for features in data[group]:
			euclideanDistance = np.linalg.norm(
				np.array(features) - np.array(predict))
			distances.append([euclideanDistance, group])

	votes = [i[1] for i in sorted(distances)[:k]]
	# print(Counter(votes).most_common(1))
	voteResult = Counter(votes).most_common(1)[0][0]
	confidence = Counter(votes).most_common(1)[0][1]/k

	# print(voteResult,confidence)

	return voteResult, confidence

accuracies = []
# for i in range(25):

import multiprocessing as mp

output = mp.Queue()

def foo():
	df = pd.read_csv('breast-cancer-wisconsin.data.txt')
	df.replace('?',-99999,inplace=True)
	df.drop(['id'],1,inplace=True)
	fullData = df.astype(float).values.tolist()
	random.shuffle(fullData)

	testSize = 0.4  # 20% of data
	# 2 is benign 4 is malignant
	trainSet = {2:[],4:[]}
	testSet = {2:[],4:[]}
	trainData = fullData[:-int(testSize*len(fullData))]	# up to 100% - 20% = 80%
	testData = fullData[-int(testSize*len(fullData)):]	# from 80% to 100%

	for i in trainData:
		trainSet[i[-1]].append(i[:-1])
	for i in testData:
		testSet[i[-1]].append(i[:-1])

	correct = 0
	total = 0
	totalConfidence = 0

	for group in testSet:
		for data in testSet[group]:
			vote, confidence = kNearestNeighbors(trainSet, data, k=5)
			if group is vote:
				correct += 1
			# else:
			# 	print(confidence)
			total+=1

	# print('My Accuracy:', correct / total)
	# accuracies.append(correct / total)

	output.put(correct/total)

# print('My Accuracy:', sum(accuracies) / len(accuracies))

processes = [mp.Process(target=foo) for _ in range(25)]
for p in processes:
	p.start()
for p in processes:
	p.join()
accuracies = [output.get() for p in processes]

print('My Accuracy:', sum(accuracies) / len(accuracies))
