#https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Task
# The interquartile range of an array is the difference between its first Q1 and third Q2 quartiles (i.e., ).
#
# Given an array, X, of n integers and an array F representing the respective frequencies of 's elements,
# construct a data set S where each x_i occurs at frequency f_i.
# Then calculate and print S's interquartile range,
# rounded to a scale of  decimal place (i.e.,  12.3 format).
#
# Tip: Be careful to not use integer division when averaging the middle two elements for a data set
# with an even number of elements, and be sure to not include the median in your upper and lower data sets.

# Input Format
#
# The first line contains an integer, n, denoting the number of elements in arrays X and F.
# The second line contains n space-separated integers describing the respective elements of array X.
# The third line contains n space-separated integers describing the respective elements of array F.

def median(X):
    sortedX = sorted(X)
    mid = len(sortedX) // 2
    if (len(sortedX) % 2 == 0):
        return (sortedX[mid - 1] + sortedX[mid]) / 2.0
    else:
        return sortedX[mid]

def quartiles(X):
    # https://en.wikipedia.org/wiki/Quartile
    # 1. Use the median to divide the ordered data set into two halves.


    # If there are an odd number of data points in the original ordered data set,
    # do not include the median (the central value in the ordered list) in either half.
    # If there are an even number of data points in the original ordered data set, split this data set exactly in half.

    # 2. The lower quartile value is the median of the lower half of the data.
    # The upper quartile value is the median of the upper half of the data.

    X.sort()

    mid = len(X) // 2

    if (len(X) % 2 != 0):
        Q1 = median(X[0:mid])
        Q3 = median(X[mid + 1:])
    else:
        Q1 = median(X[0:mid])
        Q3 = median(X[mid:])

    Q2 = median(X)

    return Q1, Q2, Q3



if __name__ == "__main__":
    N = input()
    X = input()
    F = input()
    N = int(N)
    X = X.split(' ')
    X = [int(x) for x in X]
    F = F.split(' ')
    F = [int(f) for f in F]

    S = []
    for x, f in zip(X, F):
        S += [x]*f

    Q1, Q2, Q3 = quartiles(S)

    print(round(Q3-Q1, 1))

    # import numpy as np
    # S.sort()
    # print(np.percentile(S, 25))
    # print(np.percentile(S, 50))
    # print(np.percentile(S, 75))
    #
    # print(round(np.percentile(S, 75)-np.percentile(S, 25), 1))