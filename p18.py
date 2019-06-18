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

    return voteResult


df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)
fullData = df.astype(float).values.tolist()
random.shuffle(fullData) 

testSize = 0.2  # 20% of data
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

for group in testSet:
	for data in testSet[group]:
		vote = kNearestNeighbors(trainSet,data,k=5)
		if group is vote:
			correct+=1
		total += 1

print('Accuracy:',correct/total)