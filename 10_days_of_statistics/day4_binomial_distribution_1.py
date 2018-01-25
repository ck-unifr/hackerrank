#https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem


# Task
# The ratio of boys to girls for babies born in Russia is 1.09.
# If there is 1 child born per birth,
# what proportion of Russian families with exactly 6 children will have at least 3 boys?


# Input format
# A single line containing the following values:
# 1.09 1
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format
#
# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

import math

input = input()
input = input.split(' ')

ratio = float(input[0])
# ratio = 1.09
# nb_child = 1

p = ratio / (1+ratio)

b = [(math.factorial(6) / (math.factorial(n)*math.factorial(6-n)))*math.pow(p, n)*math.pow((1-p), (6-n))
     for n in [3, 4, 5, 6]]

print(round(sum(b), 3))

