import statistics, math
import numpy as np

# n = [13,13,13,13,14,14,16,18,21]
n = [14, 14, 14, 14, 18, 18, 23, 25]
mean = statistics.mean(n)
median = statistics.median(n)
mode = statistics.mode(n)
rang = np.max(n) - np.min(n)

print(mean, median, mode, rang)
