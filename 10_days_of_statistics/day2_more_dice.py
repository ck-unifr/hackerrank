#https://www.hackerrank.com/challenges/s10-mcq-2/problem

import itertools

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

nb = 0
nb_total = 36
for d1, d2 in list(itertools.product(dice1, dice2)):
    if d1 + d2 == 6 and d1 != d2:
        nb += 1

print('{}/{}'.format(nb, nb_total))