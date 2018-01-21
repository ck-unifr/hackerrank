# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Input Format
#The first line contains an integer, , denoting the number of elements in the array.
#The second line contains  space-separated integers describing the array's elements.

# Constraints
# N >= 10 and N <= 2500
# x_i >0 and x_i <= 10^5

# Output Format
# Print  lines of output in the following order:
# Print the mean on a new line, to a scale of  decimal place (i.e., , ).
# Print the median on a new line, to a scale of  decimal place (i.e., , ).
# Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

N = input()
X = input()
#N = 11
#X = [4978, 11735, 14216, 14470, 38120, 51135, 64630, 67060, 73429, 99233, 4978]
N = int(N)
X = X.split(' ')
X = [int(x) for x in X]

import numpy as np
from scipy import stats

mean = np.mean(X)
mean = round(mean, 1)
print(mean)

media = round(np.median(X), 1)
print(media)

m = stats.mode(X)
if len(m[0]) > 1:
    if m[0][0] > m[0][1]:
        mode = m[0][1]
    else:
        mode = m[0][0]
else:
    mode = m[0][0]
print(mode)

