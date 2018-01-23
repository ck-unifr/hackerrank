#https://www.hackerrank.com/challenges/s10-mcq-3/problem

import itertools

X = ['r']*4 + ['b']*3
Y = ['r']*5 + ['b']*4
Z = ['r']*4 + ['b']*4


nb = 0
nb_total = 0
for b1, b2, b3 in list(itertools.product(X, Y, Z)):
    nb_total += 1
    str = '{}{}{}'.format(b1, b2, b3)
    nb_red = str.count('r')
    nb_black = str.count('b')
    if nb_red == 2 and nb_black == 1:
        nb += 1

print('{}/{}'.format(nb, nb_total))


