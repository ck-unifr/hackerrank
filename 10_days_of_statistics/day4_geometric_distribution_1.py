#https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# Task
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the  1st defect is found during the 5th inspection?

# Input Format
#
# The first line contains the respective space-separated numerator and
# denominator for the probability of a defect, and the second line contains the inspection
# we want the probability of being the first defect for:
#
# 1 3
# 5
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).

import math

# def negative_bin_dist(x, n, p):
#     (math.factorial(n-1)/(math.factorial(x-1)*math.factorial(n-x)))*math.pow(p, x)*math.pow(1-p, n-x)

p = 1/3
n = 5

print(round(math.pow(1-p, n-1)*p, 3))