#https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# Task
# A random variable X, follows Poisson distribution with mean of 2.5.
# Find the probability with which the random variable X is equal to 5.

# Input Format
# The first line contains X's mean.
# The second line contains the value we want the probability for:
# 2.5
# 5

# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1234 format).

import math

def poisson_distribution(k, lam):
    p = math.pow(lam, k) * math.exp(-1*lam) / math.factorial(k)
    return p


lam = 2.5
k = 5

print(round(poisson_distribution(k, lam), 3))
