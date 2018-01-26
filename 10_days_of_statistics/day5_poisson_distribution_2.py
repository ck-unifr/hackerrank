#https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

# Task
# The manager of a industrial plant is planning to buy a machine of either type A or type B.
# For each day’s operation:
#
# 1. The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88.
# The daily cost of operating  A is C_A = 160 + 40*X^2.
#
# 2. The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55.
# The daily cost of operating  A is C_B = 128 + 40*Y^2.


# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure
# that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

# Input Format
#
# A single line comprised of  space-separated values denoting the respective means for A and B:
# 0.88 1.55

# Output format
# There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e.,  1234 format):
# 1. On the first line, print the expected daily cost of machine A.
# 2. On the second line, print the expected daily cost of machine B.


lam_A = 0.88
lam_B = 1.55


C_A = 160 + 40*(lam_A + lam_A**2)
C_B = 128 + 40*(lam_B + lam_B**2)

print(round(C_A, 3))
print(round(C_B, 3))