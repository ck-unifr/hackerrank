#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

# Task
# You have a sample of 100 values from a population with mean 500 and with standard deviation 80.
# Compute the interval that covers the middle 95% of the distribution of the sample mean;
# in other words, compute A and B such that P(A < x < B) = 0.95.
# Use the value of z=1.96. Note that z is the z-score.

import math

sample_size = 100
sample_mean = 500
sample_std = 80
z = 1.96

interval = z * (sample_std / math.sqrt(sample_size))

A = round(sample_mean - interval, 2)
B = round(sample_mean + interval, 2)

# Gets the result and show on the screen
print(A)
print(B)


