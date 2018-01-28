#https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

# Task
# Given two n-element data sets X and Y,
# calculate the value of the Pearson correlation coefficient.

import math

N = input()
X = input()
Y = input()

def std(X, mean_X):
    X_new = [(x-mean_X)**2 for x in X]

    return math.sqrt(sum(X_new)/len(X))

def pearson_correlation(X, Y):
    p = 0

    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    std_X = std(X, mean_X)
    std_Y = std(Y, mean_Y)

    for i in range(0, len(X)):
        p += (X[i] - mean_X) * (Y[i] - mean_Y)

    p = p / (len(X) * std_X * std_Y)

    return p


N = int(N)
X = X.strip().split(' ')
X = [float(x) for x in X]
Y = Y.strip().split(' ')
Y = [float(y) for y in Y]

print(round(pearson_correlation(X, Y), 3))

