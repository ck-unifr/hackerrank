#https://www.hackerrank.com/challenges/s10-mcq-1/problem

import itertools

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

nb_at_most_9 = 0
nb_total = 0
for d1, d2 in list(itertools.product(dice1, dice2)):
    nb_total += 1
    if d1 + d2 <= 9:
        nb_at_most_9 += 1


print('{}/{}'.format(nb_at_most_9, nb_total))