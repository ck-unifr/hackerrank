#https://www.hackerrank.com/challenges/s10-quartiles/problem


# Task
# Given an array of integers, calculate the respective first quartile (), second quartile (), and third quartile ().
# It is guaranteed that Q1, Q2, and Q3 are integers.

# Input format
# The first line contains an integer, n, denoting the number of elements in the array.
# The second line contains n space-separated integers describing the array's elements.

# Constraints
# n >= 5 and n <= 50
# x_i > 0 and x_i <= 100

# Output Format
#
# Print  lines of output in the following order:
#
# The first line should be the value of Q1.
# The second line should be the value of Q2.
# The third line should be the value of Q3.

def median(X):
    sortedX = sorted(X)
    mid = len(sortedX) // 2
    if (len(sortedX) % 2 == 0):
        return (sortedX[mid - 1] + sortedX[mid]) / 2.0
    else:
        return sortedX[mid]

N = input()
X = input()
N = int(N)
X = X.split(' ')
X = [int(x) for x in X]

X.sort()

#https://en.wikipedia.org/wiki/Quartile
# 1. Use the median to divide the ordered data set into two halves.
mid = len(X) // 2

# If there are an odd number of data points in the original ordered data set,
# do not include the median (the central value in the ordered list) in either half.
# If there are an even number of data points in the original ordered data set, split this data set exactly in half.


# 2. The lower quartile value is the median of the lower half of the data.
# The upper quartile value is the median of the upper half of the data.

if (len(X) % 2 != 0):
    Q1 = median(X[0:mid])
    Q3 = median(X[mid+1:])
else:
    Q1 = median(X[0:mid])
    Q3 = median(X[mid:])

Q2 = median(X)


print(int(Q1))
print(int(Q2))
print(int(Q3))







